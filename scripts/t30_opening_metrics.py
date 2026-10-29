#!/usr/bin/env python3
# t30 开局收集指标：收集完成率（R@t30/200）与零浪费率（相邻拾取间隔 vs 无障碍 BFS 最短下界）。
# 输入：批量目录（含 practice-*/frames.jsonl），或单个对局目录。
# 用法：python3 -I t30_opening_metrics.py <batch_dir> [more_dirs...]
# 输出：每局 t30 指标 + 批量汇总；随 docs/35 分析提交（docs/30 §4 对照指标 + 新增 t30 指标）。
import json
import sys
from collections import deque
from pathlib import Path

MAP_TOTAL_R = 200  # make_variant 恒 16 资源 = 12×10 + 4×20


def bfs_dist(start, goal, obstacles):
    """18×18 网格无障碍 BFS 最短移动数（障碍=variant 墙）。"""
    if start == goal:
        return 0
    seen = {start}
    q = deque([(start[0], start[1], 0)])
    while q:
        x, y, d = q.popleft()
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = x + dx, y + dy
            if not (0 <= nx < 18 and 0 <= ny < 18):
                continue
            if (nx, ny) in obstacles or (nx, ny) in seen:
                continue
            if (nx, ny) == goal:
                return d + 1
            seen.add((nx, ny))
            q.append((nx, ny, d + 1))
    return None  # 不可达（理论不出现；调用方按 ∞ 计）


def analyze(battle_dir: Path):
    frames = []
    with open(battle_dir / "frames.jsonl", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                frames.append(json.loads(line))
    # 每 tick：A 的 R、位置、存活；障碍取第一帧 map_view.obstacles
    r_by_tick, pos_by_tick, alive_by_tick = {}, {}, {}
    obstacles = set()
    for fr in frames:
        t = fr["tick"]
        mv = fr.get("map_view") or {}
        for o in mv.get("obstacles", []):
            obstacles.add(tuple(o))
        robots = mv.get("robots", [])
        for rb in robots:
            if rb.get("team") == "A":
                pos_by_tick[t] = tuple(rb["position"])
                alive_by_tick[t] = rb.get("alive", True)
        for tm in fr.get("teams", []):
            if tm.get("team") == "A":
                r_by_tick[t] = tm.get("resource_value", 0.0)
    ticks = sorted(r_by_tick)
    r_at = lambda t: r_by_tick.get(t, None)
    # 拾取事件：R 增量的 tick 与当时位置
    pickups = []  # (tick, pos, r_after)
    prev_r = 0.0
    for t in ticks:
        r = r_by_tick[t]
        if r > prev_r:
            pickups.append((t, pos_by_tick.get(t), r))
        prev_r = r
    # t30 窗口指标
    t30 = [p for p in pickups if p[0] <= 30]
    r30 = r_at(30)
    if r30 is None:
        # 帧不足 30 tick（异常对局），用最后一帧
        r30 = r_by_tick[ticks[-1]]
    # 零浪费率：相邻拾取间隔 vs BFS 下界；起点=出生格
    spawn = pos_by_tick.get(ticks[0])
    segs = []
    prev_t, prev_c = 0, spawn
    for t, c, _r in t30:
        d = bfs_dist(prev_c, c, obstacles) if (prev_c and c) else None
        actual = t - prev_t
        if d is None:
            segs.append((prev_t, t, actual, None, None))
        else:
            wasted = actual - d
            segs.append((prev_t, t, actual, d, max(wasted, 0)))
        prev_t, prev_c = t, c
    ok_segs = [s for s in segs if s[3] is not None]
    sum_actual = sum(s[2] for s in ok_segs)
    sum_min = sum(s[3] for s in ok_segs)
    zero_waste_rate = (sum_min / sum_actual) if sum_actual else None
    n_zero = sum(1 for s in ok_segs if s[4] == 0)
    return {
        "battle": battle_dir.name,
        "spawn": spawn,
        "ticks": len(ticks),
        "r30": r30,
        "completion_rate_t30": round((r30 or 0) / MAP_TOTAL_R, 4),
        "pickups_t30": len(t30),
        "zero_waste_rate_t30": round(zero_waste_rate, 4) if zero_waste_rate is not None else None,
        "zero_waste_pickups": f"{n_zero}/{len(ok_segs)}",
        "first_pickup_tick": pickups[0][0] if pickups else None,
        "t50_tick": next((t for t in ticks if r_by_tick[t] >= 50), None),
        "dead_by_30": not alive_by_tick.get(30, True) if 30 in alive_by_tick else None,
        "segs_t30": segs,
    }


def main():
    args = [Path(a) for a in sys.argv[1:]]
    if not args:
        print("usage: t30_opening_metrics.py <batch_dir_or_battle_dir> ...")
        return 2
    rows = []
    for a in args:
        dirs = [a] if (a / "frames.jsonl").exists() else sorted(a.glob("practice-*"))
        for d in dirs:
            if not (d / "frames.jsonl").exists():
                print(f"skip {d}: no frames.jsonl")
                continue
            try:
                rows.append(analyze(d))
            except Exception as e:  # noqa
                print(f"FAIL {d}: {e}")
    for r in rows:
        print(
            f"{r['battle']}: R30={r['r30']:5.1f} 完成率={r['completion_rate_t30']:.3f} "
            f"拾取={r['pickups_t30']} 零浪费率={r['zero_waste_rate_t30']} "
            f"零浪费段={r['zero_waste_pickups']} 首拾t={r['first_pickup_tick']} "
            f"R50t={r['t50_tick']} 30前死亡={r['dead_by_30']}"
        )
    if rows:
        print("\n--- 批量汇总 ---")
        n = len(rows)
        print(f"局数={n}")
        print(f"R@t30 均值={sum(r['r30'] for r in rows) / n:.2f}")
        print(f"完成率均值={sum(r['completion_rate_t30'] for r in rows) / n:.3f}")
        zr = [r["zero_waste_rate_t30"] for r in rows if r["zero_waste_rate_t30"] is not None]
        print(f"零浪费率均值={sum(zr) / len(zr):.3f}（{len(zr)}/{n} 局有≥2次拾取）")
        t50 = [r["t50_tick"] for r in rows if r["t50_tick"] is not None]
        print(f"R50 达成 tick 均值={sum(t50) / len(t50):.1f}（{len(t50)}/{n} 局达成）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
