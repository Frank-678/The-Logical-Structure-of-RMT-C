#!/usr/bin/env python3
"""R2 候选对照第九轮：grb×tdc 四格消融（回应 ChatGPT CG-C-20261029-HANDOFF-FINAL 第 2 条）。

背景：代码核查发现 tactical_search=false（match_config.hpp:78），tactical_choice 仅在
strategy.cpp:1411 的 parameters_.tactical_search 门内被调用（唯一调用点 strategy.cpp:1438），
故 tactical_death_cost 在全部候选变体里是死参数。本轮用四格消融实证：
  grb0_tdc0    = M3 冻结五参数去掉 grb（mev2/pcc0/rmb4/rmv4）
  grb0_tdc025  = 同上 + tdc0.25（若 tdc 死，应与 grb0_tdc0 逐位一致）
  grb01_tdc0   = M3 冻结五参数（grb0.1）——与第 6~8 轮 old7_no_etr0 的预期结果应逐位一致
  grb01_tdc025 = 原 old7_no_etr0 六参数——若 tdc 死，应与 grb01_tdc0 逐位一致
预期：tdc 两列逐位相同（死参实证）；grb 0.0 vs 0.1 两行显示 grb 单独贡献。
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
BASE = {"resource_mission_bonus": "4.0", "reach_mission_value": "4.0",
        "mission_explore_value": "2.0", "post_cap_combat_weight": "0.0"}
VARIANTS = [
    ("grb0_tdc0", dict(BASE, goal_retention_bonus="0.0", tactical_death_cost="0.0")),
    ("grb0_tdc025", dict(BASE, goal_retention_bonus="0.0", tactical_death_cost="0.25")),
    ("grb01_tdc0", dict(BASE, goal_retention_bonus="0.1", tactical_death_cost="0.0")),
    ("grb01_tdc025", dict(BASE, goal_retention_bonus="0.1", tactical_death_cost="0.25")),
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
    (OUT / "summary_ablate9.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=1))
    print(f"[summary] {len(summary)} rows -> {OUT / 'summary_ablate9.json'}", flush=True)


if __name__ == "__main__":
    sys.exit(main())
