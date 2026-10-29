#!/usr/bin/env python3
# T5 精确版 v2：修正则（行内有逗号）+ 爆炸行去重 + 非战斗无归属伤害统计。
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
DIRS4 = [(0, -1), (0, 1), (-1, 0), (1, 0)]
RE_A_VULN = re.compile(r"第 (\d+) Tick：A 号战车移动后获得负面效果「易伤」.*?持续至 Tick (\d+)")
RE_VULN_END = re.compile(r"易伤统一在 Tick (\d+) 结束")
RE_EXPLODE_ON = re.compile(r"第 (\d+) Tick：爆炸发生")
RE_EXPLODE_OFF = re.compile(r"第 (\d+) Tick：爆炸已结束")


def cheb(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))


results = {}
for session in sorted(TRUE.keys()):
    label = TRUE[session]
    sroot = ROOT / session
    cfg = json.loads((sroot / "config.json").read_text(encoding="utf-8"))
    m = cfg["map"]
    W, H = m["width"], m["height"]
    walls = {tuple(o) for o in m["obstacles"]}

    comms = [json.loads(l) for l in (sroot / "communication.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    pos = {t: {} for t in "ABCD"}
    evtext = {}
    acts = {}
    for row in comms:
        if row["kind"] == "perception":
            d = row["data"]
            pos[row["seat"]][d["tick"]] = tuple(d["self"]["position"])
            if row["seat"] == "A":
                evtext[d["tick"]] = d.get("event_text") or ""
        elif row["kind"] == "action" and row["seat"] == "A":
            d = row["data"]
            acts[d["tick"]] = (d.get("action"), d.get("direction"))

    frames = [json.loads(l) for l in (sroot / "frames.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    a_hp, a_alive = {}, {}
    for f in frames:
        for t in f["teams"]:
            if t["team"] == "A":
                a_hp[f["tick"]] = t["hp"]
                a_alive[f["tick"]] = t["alive"]

    # 去重扫描全部公告行 → A 易伤区间 [T,E)、爆炸区间、易伤统一结束
    seen = set()
    a_vuln, explode_raw, vuln_end = [], [], None
    for tick in range(0, 501):
        txt = evtext.get(tick, "")
        for ln in txt.splitlines():
            if ln in seen:
                continue
            seen.add(ln)
            m = RE_A_VULN.search(ln)
            if m:
                a_vuln.append((int(m.group(1)), int(m.group(2))))
            m = RE_VULN_END.search(ln)
            if m and vuln_end is None:
                vuln_end = int(m.group(1))
            m = RE_EXPLODE_ON.search(ln)
            if m:
                explode_raw.append((int(m.group(1)), None))
            m = RE_EXPLODE_OFF.search(ln)
            if m:
                for i in range(len(explode_raw) - 1, -1, -1):
                    if explode_raw[i][1] is None and explode_raw[i][0] <= int(m.group(1)):
                        explode_raw[i] = (explode_raw[i][0], int(m.group(1)))
                        break
    a_vuln.sort()
    merged = []
    for s, e in a_vuln:
        if merged and s <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], e))
        else:
            merged.append((s, e))
    a_vuln = merged

    def vuln_active(t):
        return any(s <= t < e for s, e in a_vuln)

    def explode_active(t):
        return any(s <= t <= (e or 500) for s, e in explode_raw)

    damage_ticks = []
    for tick in range(0, 499):
        if a_hp.get(tick + 1, 100) < a_hp.get(tick, 100):
            drop = a_hp[tick] - a_hp[tick + 1]
            ap = pos["A"].get(tick)
            enemies_near = 0
            if ap:
                enemies_near = sum(1 for e in "BCD" if pos[e].get(tick) and cheb(ap, pos[e].get(tick)) <= 2)
            txt = evtext.get(tick, "")
            damage_ticks.append(dict(tick=tick, drop=drop, near=enemies_near,
                                     announced=bool(txt.strip()),
                                     vuln=vuln_active(tick), explode=explode_active(tick),
                                     act=acts.get(tick)))

    unannounced = [d for d in damage_ticks if not d["announced"]]
    vuln_combat = [d for d in damage_ticks if d["vuln"] and d["near"] > 0]
    vuln_attack = [d for d in damage_ticks if d["vuln"] and d["act"] and d["act"][0] == "attack"]
    explode_ticks = [d for d in damage_ticks if d["explode"] and d["near"] == 0]
    other_noncombat = [d for d in damage_ticks if d["near"] == 0 and not d["explode"]]
    vuln_attack_all = [t for t in range(0, 500) if vuln_active(t) and t in acts and acts[t][0] == "attack"]
    vuln_move_all = [t for t in range(0, 500) if vuln_active(t) and t in acts and acts[t][0] == "move"]
    vuln_defend_all = [t for t in range(0, 500) if vuln_active(t) and t in acts and acts[t][0] == "defend"]

    deaths = []
    for tick in range(0, 499):
        if a_alive.get(tick, True) and not a_alive.get(tick + 1, True):
            dmg = [d for d in damage_ticks if tick - 10 <= d["tick"] <= tick]
            ap = pos["A"].get(tick)
            last_act = None
            for t2 in range(tick, tick - 6, -1):
                if t2 in acts:
                    last_act = acts[t2]
                    break
            safe_dir_at_death = False
            if ap:
                for dx, dy in DIRS4:
                    np_ = (ap[0] + dx, ap[1] + dy)
                    if not (0 <= np_[0] < W and 0 <= np_[1] < H) or np_ in walls:
                        continue
                    if all(cheb(np_, pos[e].get(tick, (-99, -99))) > 2 for e in "BCD"):
                        safe_dir_at_death = True
                        break
            hp_before = a_hp.get(tick, 0)
            n_dmg_ticks = len(dmg)
            cls = "burst" if n_dmg_ticks <= 2 else "sustained"
            if n_dmg_ticks >= 4 and safe_dir_at_death and hp_before < 80:
                cls = "retreatable"
            deaths.append(dict(tick=tick, hp=hp_before, dmg_ticks=n_dmg_ticks,
                               act=last_act, safe=safe_dir_at_death, cls=cls,
                               vuln=vuln_active(tick)))

    results[label] = dict(
        spawn=cfg["robots"][0]["spawn"],
        damage_ticks=len(damage_ticks),
        total_dmg=sum(d["drop"] for d in damage_ticks),
        unannounced=len(unannounced),
        unannounced_dmg=sum(d["drop"] for d in unannounced),
        unannounced_ticks=[d["tick"] for d in unannounced],
        vuln_combat=len(vuln_combat),
        vuln_combat_dmg=sum(d["drop"] for d in vuln_combat),
        vuln_attack=len(vuln_attack),
        vuln_attack_dmg=sum(d["drop"] for d in vuln_attack),
        explode_ticks=len(explode_ticks),
        explode_dmg=sum(d["drop"] for d in explode_ticks),
        other_noncombat=len(other_noncombat),
        other_noncombat_dmg=sum(d["drop"] for d in other_noncombat),
        vuln_windows=a_vuln,
        vuln_unified_end=vuln_end,
        vuln_attack_actions=len(vuln_attack_all),
        vuln_move_actions=len(vuln_move_all),
        vuln_defend_actions=len(vuln_defend_all),
        deaths=deaths,
    )

tot = dict(deaths=0, retreatable=0, sustained=0, burst=0, safe=0, attack_low_hp=0,
           unannounced=0, unannounced_dmg=0, total_dmg=0,
           vuln_combat=0, vuln_combat_dmg=0, vuln_attack=0, vuln_attack_dmg=0,
           explode=0, explode_dmg=0, other_noncombat=0, other_noncombat_dmg=0,
           vuln_attack_actions=0, vuln_move_actions=0, vuln_defend_actions=0)
for label, r in sorted(results.items()):
    print(f"=== {label} spawn={r['spawn']} dmgTicks={r['damage_ticks']} totalDmg={r['total_dmg']} "
          f"unannounced={r['unannounced']} dmg={r['unannounced_dmg']} {r['unannounced_ticks']}")
    print(f"    vulnWin={r['vuln_windows']} end={r['vuln_unified_end']} "
          f"vulnCombat={r['vuln_combat']} dmg={r['vuln_combat_dmg']} "
          f"vulnAttackDmgTicks={r['vuln_attack']} dmg={r['vuln_attack_dmg']} "
          f"acts: atk={r['vuln_attack_actions']} mv={r['vuln_move_actions']} def={r['vuln_defend_actions']} "
          f"explode={r['explode_ticks']} dmg={r['explode_dmg']} "
          f"otherNonCombat={r['other_noncombat']} dmg={r['other_noncombat_dmg']}")
    for dth in r["deaths"]:
        print(f"    DEATH t{dth['tick']} hp={dth['hp']:.0f} dmgTicks={dth['dmg_ticks']} "
              f"act={dth['act']} safe={dth['safe']} cls={dth['cls']} vuln={dth['vuln']}")
    for k in tot:
        if k == "deaths":
            tot[k] += len(r["deaths"])
        elif k in ("retreatable", "sustained", "burst"):
            tot[k] += sum(1 for dth in r["deaths"] if dth["cls"] == k)
        elif k == "safe":
            tot[k] += sum(1 for dth in r["deaths"] if dth["safe"])
        elif k == "attack_low_hp":
            tot[k] += sum(1 for dth in r["deaths"] if dth["act"] and dth["act"][0] == "attack" and dth["hp"] < 60)
        else:
            tot[k] += r["explode_ticks" if k == "explode" else k]
print("\nTOTALS:", tot)
with open("/tmp/t5_precise_v2.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=1)
