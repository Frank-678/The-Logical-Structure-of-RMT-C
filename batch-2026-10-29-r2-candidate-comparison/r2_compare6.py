#!/usr/bin/env python3
"""R2 候选对照（I4.2）第六轮：M3 冻结候选验证（最小全恢复集，probe 开）。

背景（summary_r4/r5.json）：
- 第四轮两参交互证明 snake +20（old7 的 47.5）不是 mev2 与任一单参的两参组合
  （mev2rmb4/mev2rmv4 ≡ new；mev2etr0 = 27.5 —— mev2 抵消 etr0 单独 +5；
   mev2pcc0 = 31.3 —— pcc0 的 +3.8 幸存）；mev2pcc0 三格全干净 40/40/40。
- 故本轮：leave-one-out 定位 old7 中 snake +20 的最小贡献集（≥3 参交互）。
- 另：第一轮 rrh 在 wide_lanes-C-archive 的 focal 非法（cars/A/invalid）声称
  只有 round-1 被覆盖的报告，本轮直接复跑 rrh10 取证席位。

变体（默认关，行为类待竞技场评估）：
  six_no_mev2  = old7 去掉 mev2（测 mev2 是否参与 snake +20）
  etr0pcc0     = 两个单独增益参配对（+5 与 +3.8 是否叠加）
  mev2etr0pcc0 = mev2 + 两个增益参（若 =47.5 则 snake 最小集 ≤3 参）
  old7_no_etr0 = old7 去掉 etr0（snake +20 是否依赖关探针）
  rrh10        = 复核 wide_lanes-C-archive 中止席位
"""
import copy, json, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path("/home/frank/cst")
PLAN = json.load(open(ROOT / "build/league/r2_plan.json"))
RUN = ROOT / "build/league/r2_run"
OUT = ROOT / "build/league/r2_compare"
CFG = ROOT / "src/rmtc_bot/include/rmtc_bot/match_config.hpp"

CASES = [
    ("snake-A-pressure", "A"),
    ("sparse-A-economy", "A"),
    ("sparse-A-archive", "A"),
]
VARIANTS = [
    ("mev2pcc0rmb4rmv4", {"mission_explore_value": "2.0", "post_cap_combat_weight": "0.0",
                          "resource_mission_bonus": "4.0", "reach_mission_value": "4.0"}),
    ("mev2pcc0rmv4", {"mission_explore_value": "2.0", "post_cap_combat_weight": "0.0",
                      "reach_mission_value": "4.0"}),
]
WORKERS = 6


def plan_case(case_id):
    for c in PLAN["cases"]:
        if c["id"] == case_id:
            return c
    raise KeyError(case_id)


def load_tape(case_id, side):
    rows = []
    import gzip
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
    tape = load_tape(case_id, "new")
    for seat, agent in list(scene["agents"].items()):
        if seat == focal or agent.get("type") != "external":
            continue
        actions = {}
        for r in tape:
            reply = r["replies"].get(seat)
            assert reply is not None, f"{case_id} tape lacks seat {seat}"
            actions[str(r["tick"])] = reply.get("action")
        scene["agents"][seat] = {"type": "script", "event_delivery": "oracle",
                                 "actions": actions, "otherwise": {"action": "defend"}}
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
    abort_seats = []
    for fc in (run.get("failed_conditions") or []):
        p = fc.get("path", "")
        if "/cars/" in p:
            abort_seats.append(p.split("/cars/")[1].split("/")[0])
    return {"case_id": case_id, "variant": variant, "passed": report["passed"],
            "stop": run.get("stop"), "end_tick": run.get("end_tick"),
            "failed_conditions": run.get("failed_conditions"), "actions": actions,
            "abort_seats": sorted(set(abort_seats)),
            "final": {"R": final["R"], "D": final["D"], "deaths": final["deaths"],
                      "completed": final["completed"], "hp": final["hp"]},
            "report": str(out_prefix) + ".json"}


def compare(ev, case_id, focal, tapes_new, tapes_old, T, row_new, row_old):
    acts = ev["actions"]
    seq_new = {t: a for t, a in acts.items() if t in tapes_new}
    diff_old = next((t for t in sorted(seq_new) if t >= T and seq_new[t] != tapes_old.get(t)), None)
    diff_new = next((t for t in sorted(seq_new) if seq_new[t] != tapes_new.get(t)), None)
    final = ev["final"]
    return {"case_id": case_id, "variant": ev["variant"], "T": T,
            "action_at_T": seq_new.get(T), "old_tape_at_T": tapes_old.get(T),
            "match_old_at_T": seq_new.get(T) == tapes_old.get(T),
            "first_diff_vs_old": diff_old, "first_diff_vs_new": diff_new,
            "final": final, "passed": ev["passed"], "stop": ev["stop"],
            "abort_seats": ev["abort_seats"], "end_tick": ev["end_tick"],
            "failed_conditions": ev["failed_conditions"],
            "ref_new": {"R": row_new["R"], "D": row_new["D"], "deaths": row_new["deaths"]},
            "ref_old": {"R": row_old["R"], "D": row_old["D"], "deaths": row_old["deaths"]},
            "report": ev["report"]}


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
        backup = set_params(spec)
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
                row = compare(ev, cid, foc, tapes_new[cid], tapes_old[cid], Ts[cid],
                              rows[cid][0], rows[cid][1])
                summary.append(row)
                print(f"[done] {variant}/{cid}: T={row['T']} match_old={row['match_old_at_T']} "
                      f"first_diff_vs_old={row['first_diff_vs_old']} "
                      f"first_diff_vs_new={row['first_diff_vs_new']} "
                      f"final R/D/deaths={row['final']['R']}/{row['final']['D']}/{row['final']['deaths']} "
                      f"passed={row['passed']} stop={row['stop']} abort_seats={row['abort_seats']}",
                      flush=True)
        finally:
            if backup is not None:
                CFG.write_text(backup, encoding="utf-8")
    (OUT / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=1))
    print("summary ->", OUT / "summary.json")


if __name__ == "__main__":
    main()
