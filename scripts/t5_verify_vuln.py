#!/usr/bin/env python3
# 核实：(1) 所有“移动后获得负面效果”行（哪个座位、何时）；
# (2) B0 t7/8/9/20 伤害来源（敌人距离、掉落值、事件配置）。
import json
import re
from pathlib import Path

ROOT = Path("/mnt/d/code/The-Logical-RMT-C-log/batch-2026-10-30-seed-20261030")
TRUE = {
    "practice-6668d1207f774ac0b5a51376ea389722": "B0",
    "practice-d2993b9189ae45ff998dd2b3b8b569c3": "B1",
    "practice-bd40e9be8ce74c388d43f6912f28d66c": "B2",
    "practice-d23fc7a6b58a438285f3c00e0b389ceb": "B3",
    "practice-701cfb8ac2fe49529a3dd9e52ddb682c": "B4",
    "practice-f4a4057422d443e69cd96b832ea04726": "B5",
    "practice-81b18bb91fac4b69b9e8fec4d5462248": "B6",
    "practice-50d3db38495e43da8de39556d0c2b828": "B7",
}
RE_DEBUFF = re.compile(r"第 (\d+) Tick：([A-D]) 号战车移动后获得负面效果")
found = {}
for session in sorted(TRUE.keys()):
    comms = [json.loads(l) for l in (ROOT / session / "communication.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    for row in comms:
        if row["kind"] == "perception" and row["seat"] == "A":
            t = (row["data"].get("event_text") or "").strip()
            for ln in t.splitlines():
                m = RE_DEBUFF.search(ln)
                if m:
                    key = (TRUE[session], m.group(2))
                    found.setdefault(key, set()).add(int(m.group(1)))
for k in sorted(found):
    print(k, sorted(found[k]))

# B0 伤害来源
s0 = ROOT / "practice-6668d1207f774ac0b5a51376ea389722"
cfg = json.loads((s0 / "config.json").read_text(encoding="utf-8"))
print("\nB0 events config:")
for e in cfg.get("events", []):
    print("  ", json.dumps(e, ensure_ascii=False)[:200])
comms = [json.loads(l) for l in (s0 / "communication.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
pos = {t: {} for t in "ABCD"}
for row in comms:
    if row["kind"] == "perception":
        d = row["data"]
        pos[row["seat"]][d["tick"]] = tuple(d["self"]["position"])
frames = [json.loads(l) for l in (s0 / "frames.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
a_hp = {}
for f in frames:
    for t in f["teams"]:
        if t["team"] == "A":
            a_hp[f["tick"]] = t["hp"]
print("\nB0 A hp t0-25:", {t: a_hp.get(t) for t in range(0, 26)})
print("B0 positions t5-21:")
for t in range(5, 22):
    row = {s: pos[s].get(t) for s in "ABCD"}
    print(f"  t{t} {row}")


def cheb(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))


for t in (6, 7, 8, 9, 19, 20):
    ap = pos["A"].get(t)
    if not ap:
        continue
    near = [(s, pos[s].get(t), cheb(ap, pos[s].get(t))) for s in "BCD" if pos[s].get(t)]
    print(f"t{t} A={ap} near={near}")
