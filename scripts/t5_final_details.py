#!/usr/bin/env python3
# 细节：每局首次公告 tick；非战斗 30 伤害 tick 的事件归属；死亡时易伤。
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
precise = None  # 不用
for session in sorted(TRUE.keys()):
    label = TRUE[session]
    comms = [json.loads(l) for l in (ROOT / session / "communication.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    first = None
    for row in comms:
        if row["kind"] == "perception" and row["seat"] == "A":
            t = (row["data"].get("event_text") or "").strip()
            if t and first is None:
                first = row["data"]["tick"]
    print(label, "firstAnnouncement=", first)

# B2/B4 非战斗 30 伤害 tick：重扫
import sys

for session, label in (("practice-bd40e9be8ce74c388d43f6912f28d66c", "B2"),
                       ("practice-701cfb8ac2fe49529a3dd9e52ddb682c", "B4")):
    comms = [json.loads(l) for l in (ROOT / session / "communication.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    pos = {t: {} for t in "ABCD"}
    evtext = {}
    for row in comms:
        if row["kind"] == "perception":
            d = row["data"]
            pos[row["seat"]][d["tick"]] = tuple(d["self"]["position"])
            if row["seat"] == "A":
                evtext[d["tick"]] = d.get("event_text") or ""
    frames = [json.loads(l) for l in (ROOT / session / "frames.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    a_hp = {}
    for f in frames:
        for t in f["teams"]:
            if t["team"] == "A":
                a_hp[f["tick"]] = t["hp"]

    def cheb(a, b):
        return max(abs(a[0] - b[0]), abs(a[1] - b[1]))

    for tick in range(0, 499):
        if a_hp.get(tick + 1, 100) < a_hp.get(tick, 100):
            ap = pos["A"].get(tick)
            near = 0
            if ap:
                near = sum(1 for e in "BCD" if pos[e].get(tick) and cheb(ap, pos[e].get(tick)) <= 2)
            if near == 0:
                drop = a_hp[tick] - a_hp[tick + 1]
                lines = [ln for ln in (evtext.get(tick, "").splitlines()) if ln.strip()]
                recent = [ln[:90] for ln in lines if re.search(r"爆炸|辣椒|分裂|易伤", ln)]
                print(f"{label} t{tick} drop={drop} pos={ap} textLinesWithEvents={recent}")
