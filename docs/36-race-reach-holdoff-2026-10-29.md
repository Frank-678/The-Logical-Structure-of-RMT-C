# 36 · race_reach_holdoff：已知资源未清空时压后到点任务（早期资源争抢杠杆）

> review.md T5 处方："先找一条明确损失路径，再写一个小改进与一组配对反例。" 损失路径 = docs/35（首分钟资源争抢：地图 200 R 一次性、t28–t83 耗尽、A 全程只拿 30–80 R、失利集中在耗尽时份额 ≤50 且对手 ≥60 的对局；docs/30 §5 因果修正——缠斗循环是耗尽后的现象，不是原因）。本档案 = 那个小改进（杠杆）的设计、train 证据与预注册 heldout 判据；heldout 结果与裁决在判据之后补写。

## 1. 损失路径（docs/35 摘要，配对反例）

- 15 局（7 新 + 8 postcap 归档）机制一致：A 在任务链完成后弃已知资源赶 [9,9]；reach_mission 估值 8/(d+1) 压过采集 0.3–0.4。
  - V1 t62 弃 [7,4]+[6,2] 20 R（已知、可达、无人抢）；
  - V4 t14 弃 10 R 同类；
  - V0/V2/V4 冻结时已知未收集资源为 0（发现力问题，本杠杆 no-op——如实记录）；
- t30 零浪费 UP 0.908（对手 0.827/0.787）：移动效率无损，缺陷在选择（目标排序）。
- D≥500 与失利均发生在耗尽之后：胜负在采集竞速里决定，postcap 杠杆无介入窗口。

## 2. 杠杆设计

`race_reach_holdoff`（double，[0,1]，默认 0.0 = 冠军逐位一致）：
- 条件：stage_==2 && holdoff>0 && resource_value<120 && ∃ 已知可达资源（tile.value>0 && !tile.wall && paths 有解）；
- 作用：reach_mission 估值 × (1−holdoff)；资源清空后恢复原权重（"M 点晚拿不丢"——到点任务无截止时间）；
- 与已关闭 stage2_race_gate 的机械区别：**不动交火轴**（gate 两轮实验已证早期交火有压制对手扫资源的价值）；gate 关闭的是"采集 vs 交火"，本杠杆只调"采集 vs 到点"。
- 诚实边界：V0/V2 型发现力损失（冻结时已知资源为 0）不在本杠杆射程内。

扫 {1.0, 0.8, 0.5} + base_off（冠军基线）；train 全量 24 场景（12 stage-1 + 12 stage-2），协议同前（selection_guards：invalid==0、stage1 ≥ baseline_stage1−1；heldout 仅对选中者评估一次）。

代码五处：match_config.hpp 常量、strategy_parameters.hpp（成员+competition 列表+validate 0-1）、strategy.cpp（known_resource_race + reach_scale）、arena_main.cpp（PARAMETER + dump）、eval_levers.py（race 家族）。默认 0.0 时 known_resource_race 恒 false、reach_scale 恒 1.0（IEEE x*1.0 逐位不变），冠军逐位一致由 train base_off 复现钉证明。

## 3. 预注册判据（写于 heldout 运行前）

1. **train 选择**：满足 selection_guards 的候选中取 train objective 最高者；train 全胜零差异 → 不选（家族关闭，默认 0.0 保持）。
2. **heldout 晋升判据**：选中者的 heldout objective ≥ **冠军封存 0.8298625**（arena-postcap-heldout-2026-10-29，同 30 场景；docs/32 §7.3 参考系）。冻结 baseline 行必须逐位复现 **0.7710073**（确定性钉），否则本次 heldout 作废重跑。
3. 不达标 → 家族关闭，保持 0.0，不作第二次 heldout。
4. **本杠杆的 train 场景盲区（如实预期）**：损失路径在 train 上不可见——不是"竞技场无争抢"（生成器确有 6 种手写对手共享资源表、按资源收益寻路；U7 勘误采纳），而是当前 train 对手组合、地形与争抢强度没有有效暴露这条真实失误（docs/35 §6 已同口径）。heldout 同分布，只裁噪声；真实检验是下一轮真实对局批次（docs/35 §5 预注册判据：耗尽时 A 份额回升、拾取数回升、t30 完成率 ≥0.356；deaths/damage_events 沿用均值≥9 且中位≥8）。

## 4. train 结果

`python3 tests/eval_levers.py --levers race --report race-2026-10-29`（24 场景，结果封存 tests/results/levers-race-2026-10-29.json）：

| 组 | objective | invalid | deaths | blocked | stage1 | stage2 | D2 | R2 | M2 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| base_off（冠军） | **0.7970931712962963** | 0 | 83 | 93 | 33.333 | 41.25 | 1026.67 | 60.0 | 2.583 |
| rrh10 (1.0) | 0.7782442 | 0 | 83 | 81 | 33.333 | 41.04 | 902.08 | 57.5 | 2.667 |
| rrh08 (0.8) | 0.7959502 | 0 | 85 | 73 | 33.333 | 42.08 | 926.25 | 61.67 | 2.667 |
| rrh05 (0.5) | 0.7970931712962963 | 0 | 83 | 93 | 33.333 | 41.25 | 1026.67 | 60.0 | 2.583 |

1. **确定性钉 ✓**：base_off 与 lowhp/coverage 两轮冠军逐位相同（objective 0.7970931712962963 / deaths 83 / blocked 93 / stage2 41.25 / D2 1026.67）——默认 0.0 时杠杆零改动、冠军逐位一致，bit-identity 成立。
2. **rrh05 = 全部场景决策零差异**（与 base_off 五项统计逐位相同）：0.5 折扣后 reach 4/(d+1) 仍压过采集 0.3–0.4，在这些场景里从未翻盘一次排序。杠杆在 train 场景中要到 ≥0.8 才生效。
3. rrh08：stage2 分 +0.83、R2 +1.67（多采的直观方向），但 deaths +2、D2 −100.4，objective −0.0011；rrh10：objective −0.0189。**无候选在 train 上超过冠军。**

## 5. 裁决：train 关闭，不做 heldout；真实检验转实战批次

按 §3 预注册判据：候选最高 train objective = 0.7970931（rrh05，与冠军逐位零差异）→ "train 全胜零差异 → 不选"。**家族在 train 关闭：race_reach_holdoff 保持 0.0（冠军配置不变），不作 heldout。** train 场景的对手组合与地形未有效暴露资源争抢型失误（措辞按 U7 勘误：竞技场生成器确有 6 种手写对手共享资源表，不是"无争抢"，而是当前组合/地形/强度没有触发这条真实损失路径），heldout 同分布只会裁噪声。

杠杆代码保留在库中（默认关，含注释与证据链），供下一轮实战批次经 config 显式开启对照。触发条件只依据**本队感知**（known-reachable tiles_：tile.value>0 && !tile.wall && paths 有解），不读取 config、观赛 map_view 或地图真值——符合 U7 的"参赛程序只能依据本队感知估计"要求。

真实检验 = docs/35 §5 预注册批次判据（耗尽时 A 份额回升、拾取数回升、t30 完成率 ≥0.356；deaths/damage_events 沿用均值≥9 且中位≥8），按 batch_practice 惯例以 config 参数覆盖 A=rrh10/rrh08 对照冠军，赛后按真值指标离线核算。
