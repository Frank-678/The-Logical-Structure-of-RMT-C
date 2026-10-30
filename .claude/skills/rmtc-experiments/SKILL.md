---
name: rmtc-experiments
description: RMTC 实验操作手册——网关验证、秒级场景批量（2万组方法论）、正式尺寸实跑、联赛批次、LLM 限额纪律、WSL 陷阱
---

# RMTC 实验操作手册

环境：本会话项目 D:\code\The-Logical-Structure-of-RMT-C（doc 仓）+ WSL ~/cst（代码仓 vrb）。目标：stage1 满分（40=200 资源）、stage2 高分（30R+15D+5M）、每局 LLM 调用限额内、低风险进步。

## 0. 铁律（任何操作前必查）

- 密钥形态 `sk-cbc[0-9a-f]{8,}` 永不入库；只许在 WSL 工作区 match_config.hpp 与临时文件；提交文本必须含「密钥扫描通过」；提交前全仓扫描 0 真实 key
- 永不 push main/master（doc main 例外：仅 README 进度矩阵扩充）
- 行为类改动默认关闭 → 竞技场评估 → 有证据才晋升；诊断/工具/配置类可直接采纳
- `~/.rmtc-practice/llm.env` 内容禁读——只由启动器运行时读取
- 比赛可写死就写死（match_config.hpp 编译期常量），不用环境变量猜测
- 实验室成果→ANALYSIS docs 编号递增；比赛→提交映射入 docs/56 台账；review.md 两仓同文回执（CRLF 保留、追加式）

## 1. 网关验证（check_ai 链路）

- 配置唯一来源：WSL `~/cst/src/rmtc_bot/include/rmtc_bot/match_config.hpp`，**编译期注入**。改完必须 `bash build.sh` 重建——0.5s 结束说明 colcon 没检测到变化、未重建
- `bash check_ai.sh`：启动器注入环境变量 → scripts/check_ai.py → requests 继承环境代理
- 判读：`request_ok/200`=链路通；`proxy_error`/`ProxySchemeUnknown: Proxy URL had no scheme`=**启动器二进制停在无 scheme 中间态，重建即可**（不一定是代码 bug）；`http_error 401`=key 空或失效；2ms 无网络动作=requests 解析阶段就失败
- 练习代理端口 8080（practice_port）；占用排查 `ss -tlnp | grep 8080`——占用时用 `RMTC_FORMAL_PORT=8082` 等换端口，**勿杀他人进程**

## 2. 秒级场景批量（2 万组主力路径）

- `bash scenarios.sh` = tests/run_scenarios.py：摆第 200 Tick 局面只跑验证段，**不启 ROS、不调模型**——单次秒级，规模化扫描首选
- 地图族：`python3 tools/formal_size_suite.py` 生成 20×20/24×24 可复现合成图（STYLES=uniform/cluster/edge/center/spread，seed 固定）；practice1/2/config.json 是官方形状基线
- **参数扫描架构**：match_config.hpp 是编译期常量 → 用 build_seat_variants 式**一次构建 K 个变体**（每变体=一组参数组合，并行编译），再短场景批量对打；绝不每组合单独 colcon build（15s×N 不可行）
- 判据纪律（docs/02 + COMPARISON report 02）：同图同席同对手配对、留出图、一机制一改动、记录 AI 资格与异常/失败回放；train 增益≠真实增益（docs/34 实证第二次）

## 3. 正式尺寸实跑（分钟级）

- `bash practice1/run.sh`（stage1 单席 20×20）、`bash practice2/run.sh`（stage2 24×24）：原版裁判+校验器；`RMTC_FORMAL_CONFIG/RMTC_FORMAL_PORT/RMTC_FORMAL_DATA_DIR` 环境可覆盖
- stage1 无 LLM（launcher：real = `--check-ai` || `--batch` || stage==2）；stage2 强制 real 模式
- 量化口径：会话目录 ai.jsonl 字段 seat/session_id/mode/status/success/success_count/attempt_count；success==(status==200) 恒等

## 4. 联赛批次（小时级）

- `tools/league.sh freeze old/current --ref SHA → suite --versions → run --limit`；冻结钉=tools/versions.json（二进制 sha256 + params_digest）
- 混合口径（docs/48 §5）：M1 基线（champion vs 原版陪练）、M2 自战（vs old_champion）、M5 同池对照；计分 30·min(R/120,1)+15·min(D/500,1)+5·len(completed)
- 勘误口径（引用前必读）：docs/44/45 死亡列=终局存活态误读（用 docs/55：16 局实际 122 死）；M3=五参数（tdc 死参数，docs/48）；40/50 目标以离线竞技场为准、league 原版裁判分为另一口径

## 5. LLM 每局限额（stage2 命门）

- 每场每席 ≥1 次真实统一 AI 成功，否则任务分=0；每局调用次数有限额 → 只对高价值事件调用、公告批次包含去重、连续 3 坏回复暂停重试（生命周期 Idle→Queued→Requesting→Validate→Backoff/Stopped）
- max_tokens=512（2026-10-30 手册）；截断=finish_reason "length" → 压缩 prompt/减少重复上下文（REAL_TEST 5977ms 教训）；不靠关键词/正则/时间表替代 LLM 语义理解

## 6. WSL 陷阱（实测踩过）

- wsl.exe 命令中禁 `$()`；PowerShell 外层双引号会吞 `$N`/`$?`——外层用单引号最稳
- bash -lc 内层用单引号写 bash 语法；避免 awk print $6 这类组合

## 7. 收尾清单

- 结论入 ANALYSIS docs（编号递增）并推送；doc main 只碰 README 矩阵
- 两仓 review.md 同文回执块（CG-R- 编号、DeepSeek 身份、Asia/Shanghai 时间戳、完整 SHA、验证命令+正反结果）
