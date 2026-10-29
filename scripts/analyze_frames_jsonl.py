#!/usr/bin/env python3
"""frames.jsonl 回放分析工具：逐 tick 统计各队死亡/受击/资源里程碑（只读归档）。

口径（已用 2026-10-29 变体 4 原始帧逐帧验证）：
  - 死亡 = alive true→false 边沿；死亡窗口 3 tick（hp=0），重生后 hp 回 100。
  - 每次死亡 effective_damage −40（V4 t47→48：D 120→80）。
  - damage_events = hp 下降但未阵亡的 tick 数（受击近似）。
  - R 里程碑 = resource_value 首次到达 60/70/80/120 的 tick。

用法: python3 -I analyze_frames_jsonl.py <frames.jsonl> [frames2.jsonl ...]
"""
import json
import sys


def analyze(path):
    rows = [json.loads(line) for line in open(path, encoding="utf-8") if line.strip()]
    team_traj = {}
    for row in rows:
        for t in row["teams"]:
            team_traj.setdefault(t["team"], []).append(
                (row["tick"], t["hp"], t["alive"], t["resource_value"]))
    last = rows[-1]["teams"]
    print(path)
    for team, traj in team_traj.items():
        deaths, dead_since, prev_alive, prev_hp = [], None, True, 100
        damage_events = first_hit = 0
        milestones = {t: None for t in (60, 70, 80, 120)}
        for tick, hp, alive, rv in traj:
            if alive and prev_hp > hp > 0:
                damage_events += 1
                if not first_hit:
                    first_hit = tick
            if not alive and prev_alive:
                dead_since = tick
            elif alive and not prev_alive:
                deaths.append((dead_since, tick - 1))
            prev_alive, prev_hp = alive, hp
            for target in milestones:
                if milestones[target] is None and rv >= target:
                    milestones[target] = tick
        final = next(t for t in last if t["team"] == team)
        print(f"  {team}: score={final['score']} R={final['resource_value']} "
              f"D={final['effective_damage']} M={final['mission_completed']} "
              f"invalid={final['invalid_actions']} hp={final['hp']}")
        print(f"     deaths={len(deaths)} {deaths} hits={damage_events} first_hit={first_hit} "
              f"R60/70/80/120={milestones}")


if __name__ == "__main__":
    for p in sys.argv[1:]:
        analyze(p)
