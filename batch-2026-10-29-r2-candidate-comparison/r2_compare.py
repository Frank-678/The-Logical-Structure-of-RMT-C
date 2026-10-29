#!/usr/bin/env python3
"""R2 候选对照（I4.2 "导出短现场再比较候选" 的对比步）。

方法：取 R2 原版计划场景（真实 NPC 对手、同 seed——温重放已证明与联赛逐位一致），
把 focal 席位 external 换成 strategy 代理（离线 runner 内进程运行，参数编译自 match_config.hpp）：
- 保真（new 变体，全默认参数）：strategy 从 t0 冷启动，500 Tick 决策须与冻结 new tape 全等、
  终局 R/D/deaths/completed 须与 result.json new 行相等 → 证明"strategy 代理 ≡ 冻结 new"，
  参数变体才有对照意义。
- 变体：sed 换 match_config.hpp → 独立 build 缓存 → 跑完整对局 → 比较分歧 Tick 动作与终局。

变体（全部默认关，1.0/0=旧行为；行为类改动待竞技场评估）：
  第一轮（42 行证据见 summary_42.json）：old / rrh05 / rrh10 / pull8 / probe0 / combo
  第二轮（24 行证据见 summary_r2.json）：pull8probe0 / oldpull / oldpullprobe0 / oldprobe0
  第三轮（单参数消融，summary_r3.json）：mev2 / rmb4 / rmv4 / grb01 / tdc025 / etr0 / pcc0 × 3 现场
  第四轮（mev2 两参交互，本运行）：mev2rmb4 / mev2rmv4 / mev2etr0 / mev2pcc0 × 3 现场
"""
import copy, gzip, json, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path("/home/frank/cst")
PLAN = json.load(open(ROOT / "build/league/r2_plan.json"))
RUN = ROOT / "build/league/r2_run"
OUT = ROOT / "build/league/r2_compare"
OUT.mkdir(parents=True, exist_ok=True)
CFG = ROOT / "src/rmtc_bot/include/rmtc_bot/match_config.hpp"

CASES = [
    ("snake-A-pressure", "A"),
    ("sparse-A-economy", "A"),
    ("sparse-A-archive", "A"),
    ("wide_lanes-C-economy", "C"),
    ("wide_lanes-C-pressure", "C"),
    ("wide_lanes-C-archive", "C"),
]
VARIANTS = [
    # 第四轮：与 mev2（已证 sparse 修复项）的两参交互拆解，定位 snake +20 的最小组合。
    ("mev2rmb4", {"mission_explore_value": "2.0", "resource_mission_bonus": "4.0"}),
    ("mev2rmv4", {"mission_explore_value": "2.0", "reach_mission_value": "4.0"}),
    ("mev2etr0", {"mission_explore_value": "2.0", "explore_toward_resource_value": "0.0"}),
    ("mev2pcc0", {"mission_explore_value": "2.0", "post_cap_combat_weight": "0.0"}),
]
CASES = [
    ("snake-A-pressure", "A"),
    ("sparse-A-economy", "A"),
    ("sparse-A-archive", "A"),
]
WORKERS = 6


def plan_case(case_id):
    for c in PLAN["cases"]:
        if c["id"] == case_id:
            return c
    raise KeyError(case_id)


def load_tape(case_id, side):
    rows = []
    with gzip.open(RUN / case_id / side / "tape.jsonl.gz", "rt", encoding="utf-8") as fh:
        for line in fh:
            rows.append(json.loads(line))
    return rows


def action_key(reply):
    a = reply.get("action") or {}
    kind = a.get("action")
    if kind == "attack":
        return ("attack", a.get("target"))
    if kind == "move":
        return ("move", a.get("direction"))
    return (kind,)


def tape_actions(case_id, side, focal):
    out = {}
    for r in load_tape(case_id, side):
        rep = r["replies"].get(focal)
        if rep is not None:
            out[r["tick"]] = action_key(rep)
    return out


def first_divergence(case_id, focal):
    tn = load_tape(case_id, "new")
    to = load_tape(case_id, "old")
    for rn, ro in zip(tn, to):
        if action_key(rn["replies"][focal]) != action_key(ro["replies"][focal]):
            return rn["tick"]
    return None


def result_row(case_id, side, focal):
    orig = json.load(open(RUN / case_id / side / "result.json"))
    row = [x for x in orig["result"] if x["seat"] == focal][0]
    row["completed"] = orig["world"]["cars"][focal]["completed"]
    return row


def set_params(spec):
    """sed 风格换参；返回原文本用于还原。"""
    orig = CFG.read_text(encoding="utf-8")
    text = orig
    for key, value in spec.items():
        pattern = re.compile(r"(inline constexpr (?:double|int|bool) " + key + r"\s*=\s*)[^;]*;")
        text, n = pattern.subn(lambda m: m.group(1) + value + ";", text)
        assert n == 1, (key, n)
    CFG.write_text(text, encoding="utf-8")
    return orig


def build_scene(case_id, focal):
    case = plan_case(case_id)
    scene = copy.deepcopy(case["scene"])
    scene["name"] += "-strategy-focal"
    scene["agents"][focal] = {"type": "strategy", "event_delivery": "oracle"}
    # archive 局其余席位是 external($anchor=new)：按 new 侧 tape 脚本化（= 原局对手真实行为）。
    tape = load_tape(case_id, "new")
    for seat, agent in list(scene["agents"].items()):
        if seat == focal or agent.get("type") != "external":
            continue
        actions = {}
        for r in tape:
            reply = r["replies"].get(seat)
            assert reply is not None, f"{case_id} tape lacks seat {seat}"
            actions[str(r["tick"])] = reply.get("action")  # 死 Tick 为 null，脚本合法
        scene["agents"][seat] = {"type": "script", "event_delivery": "oracle",
                                 "actions": actions, "otherwise": {"action": "defend"}}
    # 与 r2_export 的温重放一致：跑满 500 tick，去掉原计划 expect/break_when/save_at/warm_until，
    # 避免 always 失败或断点让 trace 提前截断（保真对比要求完整 500 tick）。
    scene["run"] = {"until_tick": 500, "always": list(case["scene"]["run"]["always"]),
                    "expect": []}
    return scene


def run_scene(scene_path, out_prefix):
    proc = subprocess.run([sys.executable, str(ROOT / "tests/run_scenarios.py"),
                           str(scene_path), "--out", str(out_prefix)],
                          capture_output=True, text=True, timeout=600)
    if proc.returncode not in (0, 1):
        raise RuntimeError(proc.stderr.strip() or "runner failed")
    return json.loads(Path(str(out_prefix) + ".json").read_text())


def evaluate(case_id, focal, variant, scenes_dir):
    scene_path = scenes_dir / f"{case_id}-strategy.scene.json"
    out_prefix = scenes_dir / f"{case_id}-{variant}"
    report = run_scene(scene_path, out_prefix)
    run = report["runs"][0]
    actions = {}
    for row in run["trace"]:
        d = row["decisions"][focal]
        actions[int(row["tick"])] = action_key({"action": d["chosen"]})
    final = run["trace"][-1]["after"]["cars"][focal]
    return {"case_id": case_id, "variant": variant, "passed": report["passed"],
            "stop": run.get("stop"), "end_tick": run.get("end_tick"),
            "failed_conditions": run.get("failed_conditions"), "actions": actions,
            "final": {"R": final["R"], "D": final["D"], "deaths": final["deaths"],
                      "completed": final["completed"], "hp": final["hp"]},
            "report": str(out_prefix) + ".json"}


def compare(ev, case_id, focal, tapes_new, tapes_old, T, row_new, row_old):
    acts = ev["actions"]
    # tape 对死亡 Tick 无 replies 行；只对比双方 tape 都覆盖的存活 Tick，避免死亡段产生幻影差异。
    seq_new = {t: a for t, a in acts.items() if t in tapes_new}
    diff_old = next((t for t in sorted(seq_new) if t >= T and seq_new[t] != tapes_old.get(t)), None)
    diff_new = next((t for t in sorted(seq_new) if seq_new[t] != tapes_new.get(t)), None)
    final = ev["final"]
    row = {"case_id": case_id, "variant": ev["variant"], "T": T,
           "action_at_T": seq_new.get(T), "old_tape_at_T": tapes_old.get(T),
           "match_old_at_T": seq_new.get(T) == tapes_old.get(T),
           "first_diff_vs_old": diff_old, "first_diff_vs_new": diff_new,
           "final": final,
           "ref_new": {"R": row_new["R"], "D": row_new["D"], "deaths": row_new["deaths"]},
           "ref_old": {"R": row_old["R"], "D": row_old["D"], "deaths": row_old["deaths"]},
           "passed": ev["passed"], "stop": ev["stop"], "report": ev["report"]}
    if ev["variant"] == "new":
        # 保真：全 500 Tick 决策 == 冻结 new tape；终局 == result.json new 行
        mism = [t for t in sorted(seq_new) if seq_new[t] != tapes_new.get(t)]
        row["fidelity_ticks_mismatch"] = mism[:5]
        row["fidelity_ok"] = not mism
        row["final_matches_ref_new"] = (final["R"] == row_new["R"] and final["D"] == row_new["D"]
                                        and final["deaths"] == row_new["deaths"]
                                        and final["completed"] == row_new["completed"]
                                        and abs(final["hp"] - row_new["hp"]) < 0.01)
    return row


def main():
    summary = []
    scenes_dir = OUT / "scenes"
    scenes_dir.mkdir(parents=True, exist_ok=True)
    tapes_new, tapes_old, Ts, rows = {}, {}, {}, {}
    for case_id, focal in CASES:
        tapes_new[case_id] = tape_actions(case_id, "new", focal)
        tapes_old[case_id] = tape_actions(case_id, "old", focal)
        Ts[case_id] = first_divergence(case_id, focal)
        rows[case_id] = (result_row(case_id, "new", focal), result_row(case_id, "old", focal))
        (scenes_dir / f"{case_id}-strategy.scene.json").write_text(
            json.dumps(build_scene(case_id, focal), ensure_ascii=False, indent=1))
        print(f"[plan] {case_id} focal={focal} T={Ts[case_id]}", flush=True)

    for variant, spec in VARIANTS:
        print(f"[variant] {variant} spec={spec}", flush=True)
        backup = set_params(spec) if spec else None
        try:
            evals = {}
            with ThreadPoolExecutor(max_workers=WORKERS) as pool:
                futs = {pool.submit(evaluate, cid, foc, variant, scenes_dir): cid for cid, foc in CASES}
                for fut in as_completed(futs):
                    cid = futs[fut]
                    try:
                        evals[cid] = fut.result()
                    except Exception as e:  # noqa: BLE001
                        print(f"[error] {variant}/{cid}: {e}", flush=True)
                        raise
            for cid, foc in CASES:
                ev = evals[cid]
                row_new, row_old = rows[cid]
                row = compare(ev, cid, foc, tapes_new[cid], tapes_old[cid], Ts[cid], row_new, row_old)
                summary.append(row)
                print(f"[done] {variant}/{cid}: T={row['T']} act={row['action_at_T']} "
                      f"old={row['old_tape_at_T']} match_old={row['match_old_at_T']} "
                      f"first_diff_vs_old={row['first_diff_vs_old']} "
                      f"final R/D/deaths={row['final']['R']}/{row['final']['D']}/{row['final']['deaths']} "
                      f"ref new {row['ref_new']} old {row['ref_old']} passed={row['passed']}", flush=True)
        finally:
            if backup is not None:
                CFG.write_text(backup, encoding="utf-8")
    (OUT / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=1))
    print("summary ->", OUT / "summary.json")


if __name__ == "__main__":
    main()
