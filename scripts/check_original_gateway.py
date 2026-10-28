#!/usr/bin/env python3
"""只读测试原版 practice.py 的 HTTP 处理器；不启动 ROS，不访问真实模型。

运行：python3 scripts/check_original_gateway.py /绝对路径/practice.py
可加 --output result.json 保存证据。只用标准库，不向原目录写字节码。
固定上游负责控制完成时机；本脚本验证转发行为，不能证明模型理解或裁判结算。
"""
import argparse
import hashlib
import http.client
import importlib.util
import json
import os
from pathlib import Path
import sys
import tempfile
import threading
import time
import types


def load_original(path, upstream):
    """临时提供 ROS 名称占位和固定上游；导入原文件，不创建其 Practice/节点。"""
    sys.dont_write_bytecode = True
    modules = {
        'requests': {'post': upstream.post, 'RequestException': RuntimeError},
        'rclpy': {}, 'rclpy.executors': {'MultiThreadedExecutor': object},
        'rclpy.node': {'Node': object},
        'rclpy.qos': {'QoSProfile': object, 'DurabilityPolicy': object},
        'std_msgs': {}, 'std_msgs.msg': {'String': object},
        'internal_ros': {'internal_context': lambda: None},
    }
    for name, members in modules.items():
        module = types.ModuleType(name)
        module.__dict__.update(members)
        sys.modules[name] = module
    spec = importlib.util.spec_from_file_location('original_practice_fixture', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Upstream:
    """固定响应和可控阻塞；entered 表示已进入上游，release 表示允许其完成。"""
    def __init__(self):
        self.entered = threading.Event()
        self.release = threading.Event()
        self.release.set()
        self.calls = []

    def block(self):
        self.entered.clear()
        self.release.clear()

    def post(self, url, **kwargs):
        self.calls.append({'url': url, **kwargs})
        self.entered.set()
        if not self.release.wait(5):
            raise RuntimeError('fixture release timed out')
        # choices 非空，但 content 故意不是事件 JSON，用于区分调用成功和语义通过。
        reply = {'choices': [{'message': {'content': 'not an event JSON'}}]}
        return FixedResponse(reply)


class FixedResponse:
    """实现原 forward_ai 实际使用的 requests 响应接口。"""
    status_code = 200

    def __init__(self, reply):
        self.reply = reply

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def json(self):
        return self.reply


def wait_until(predicate):
    """等待后台 HTTP 收尾；只用于测试同步，不推进或模拟比赛 Tick。"""
    deadline = time.monotonic() + 3
    while not predicate():
        if time.monotonic() >= deadline:
            raise AssertionError('HTTP handler did not finish')
        time.sleep(0.01)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('practice_py', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    original = args.practice_py.resolve()
    before = original.read_bytes()
    # 本结果只对应已核对的原版，遇到不同版本拒绝套用结论。
    expected = 'a72f6be6915a75c142298ff1b8f3d1ff2adbe3d763eaa35915747459c0b0d82a'
    assert hashlib.sha256(before).hexdigest() == expected, 'different practice.py version'
    upstream = Upstream()
    module = load_original(original, upstream)
    cases = []
    # 都是本脚本进程内的夹具值；不读取用户密钥，不访问该上游网址。
    os.environ.update(PRACTICE_LLM_URL='https://fixture.invalid/chat/completions',
                      PRACTICE_LLM_KEY='fixture-upstream-key', PRACTICE_MODEL='')
    with tempfile.TemporaryDirectory(prefix='rmtc-gateway-audit-') as directory:
        app = types.SimpleNamespace(args=types.SimpleNamespace(ai_mode='real'),
            lock=threading.RLock(), session='fixture-first', stopped=False,
            ai_slots={seat: threading.BoundedSemaphore(1) for seat in 'ABCD'},
            ai={}, run=Path(directory))
        server = module.Server(('127.0.0.1', 0), module.Handler)
        server.app = app
        serving = threading.Thread(target=server.serve_forever, daemon=True)
        serving.start()

        def request(payload=None, path='/v1/chat/completions'):
            connection = http.client.HTTPConnection(*server.server_address, timeout=3)
            try:
                headers = {'Content-Type': 'application/json',
                           'Authorization': 'Bearer practice-A'}
                connection.request('GET' if payload is None else 'POST', path,
                                   None if payload is None else json.dumps(payload), headers)
                response = connection.getresponse()
                return response.status, json.loads(response.read())
            finally:
                connection.close()

        def audit_rows():
            path = app.run / 'ai.jsonl'
            return [json.loads(line) for line in path.read_text().splitlines()] if path.exists() else []

        body = {'messages': [{'role': 'user', 'content': 'fixture'}], 'model': 'request-model'}
        try:
            assert request(path='/healthz')[0] == 404
            assert request({'messages': body['messages']})[0] == 400
            assert audit_rows() == []
            cases.append({'case': 'healthz_absent_and_missing_model_not_audited', 'passed': True})

            os.environ['PRACTICE_MODEL'] = 'fallback-model'
            status, reply = request(body)
            call = upstream.calls[-1]
            assert status == 200 and call['json']['model'] == 'request-model'
            assert call['headers']['Authorization'] == 'Bearer fixture-upstream-key'
            assert call['timeout'] == (5, 25) and call['allow_redirects'] is False
            cases.append({'case': 'request_model_wins_and_upstream_credentials_replace_seat_token', 'passed': True})

            assert reply['choices'][0]['message']['content'] == 'not an event JSON'
            assert audit_rows()[-1]['success'] is True
            cases.append({'case': 'success_count_does_not_validate_event_json', 'passed': True})
            assert request({'messages': body['messages']})[0] == 200
            assert upstream.calls[-1]['json']['model'] == 'fallback-model'
            cases.append({'case': 'omitted_model_uses_practice_fallback', 'passed': True})

            upstream.block()
            disconnected = http.client.HTTPConnection(*server.server_address, timeout=3)
            disconnected.request('POST', '/v1/chat/completions', json.dumps(body),
                {'Content-Type': 'application/json', 'Authorization': 'Bearer practice-A'})
            assert upstream.entered.wait(3)
            disconnected.close()  # 客户端先断开，原处理器仍在等待上游。
            before_count = len(audit_rows())
            assert request(body)[0] == 429
            assert len(audit_rows()) == before_count
            upstream.release.set()
            wait_until(lambda: len(audit_rows()) == before_count + 1)
            # 审计先于 finally 释放槽位；单独等槽位释放，避免测试竞态。
            def slot_available():
                if not app.ai_slots['A'].acquire(blocking=False):
                    return False
                app.ai_slots['A'].release()
                return True
            wait_until(slot_available)
            assert request(body)[0] == 200
            cases.append({'case': 'client_disconnect_keeps_seat_busy_until_upstream_finishes', 'passed': True})

            upstream.block()
            completed = []
            worker = threading.Thread(target=lambda: completed.append(request(body)))
            worker.start()
            assert upstream.entered.wait(3)
            before_count = len(audit_rows())
            with app.lock:
                app.session = 'fixture-second'
                app.ai = {}
            upstream.release.set()
            worker.join(3)
            assert not worker.is_alive() and completed[0][0] == 200
            assert len(audit_rows()) == before_count and app.ai == {}
            cases.append({'case': 'old_session_response_can_be_200_without_new_session_audit', 'passed': True})
        finally:
            upstream.release.set()
            server.shutdown()
            server.server_close()
            serving.join(3)
    assert original.read_bytes() == before
    result = {'practice_py_sha256': expected, 'original_unchanged': True,
              'transport': 'real loopback HTTP to unmodified original Handler',
              'upstream': 'controlled in-process requests fixture; no real model',
              'ros': 'import names stubbed; no ROS or judge binary executed', 'cases': cases}
    text = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
    if args.output:
        args.output.write_text(text)
    print(text, end='')


if __name__ == '__main__':
    main()
