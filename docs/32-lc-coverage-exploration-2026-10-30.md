# 32 · L-c 杠杆轮：覆盖最大化探索方向 explore_component_value（2026-10-30）

来源：docs/31 复盘后的长线候选 L-c（默认关，train 评估 + heldout 一次性验证）。

## 1. 动机与机制

docs/31 的结论是两场败局均为"运气帽"（B2 的 (2,0)=20 在 A 的 vision=4 视野外，NW/SE 两片未探索区在 A 的信息下完全对称；B0 为出生圈贫富 + 中央簇距离赛 + 无预告事件伤害）。L-c 不是对 B2 的"修复"——信息对称下的硬币无法加权——而是对一个更一般的问题做受控实验：

**现有 frontier 探索是"局部增益优先"**：`consider_frontier` 对每个候选观察点按 `value × newly_visible / (distance+1)` 估值，其中 newly_visible 是该点视野包络内的未知格数。这意味着机器人会反复扫近处的小口袋（每次多看见几格），而迟迟不走向地图另一侧的大空白区——那里更可能藏着远侧资源簇（stage-2 机制结论："探索的 stage-2 价值 = 更早到达被争夺的簇"）。

**L-c 机制**：把全部未探索格按 4 连通标成连通区；候选观察点的估值加上一项 `explore_component_value × (其视野包络触及的最大未探索连通区大小)`。大空白区优先于近处零碎口袋。参数默认 0 = 冠军逐位一致（标号整段跳过，提前停止界与 utility 表达式在 +0.0 恒等下与旧式全等）。

## 2. 实现

- `match_config.hpp`：`explore_component_value = 0`（默认关）。
- `strategy_parameters.hpp`：成员 + `competition()` + `validate()`（与 post_cap_combat_weight 并列）。
- `tests/arena_main.cpp`：PARAMETER 注入 + `--dump-competition` 导出。
- `strategy.cpp` `consider_frontier`（strategy.cpp:1113 起）：
  - 标号块只在 `explore_component_value > 0 && stage_ == 2` 时执行（`unseen_comp` 平铺数组，宽×高，4 连通洪泛）——**仅第二阶段生效**（见 §5 分拆）；
  - 提前停止界改为 `(value × max_visible + cv × 最大连通区) / (distance+1)`——cv=0 时与旧式逐位一致；
  - utility 改为 `(value × newly_visible + cv × largest_touched) / (distance+1)`，largest_touched 为包络触及的最大连通区大小。
- `tests/eval_levers.py`：新增 `coverage` 组（首轮 `{5e-4, 2e-3, 8e-3}`，分拆轮 `{2e-3, 8e-3, 2e-2}`）。

## 3. 量级选择

stage-2 `frontier_value=0.02` × newly_visible（≤81）≈ ≤1.62/(d+1)。连通区大小在 36×36 图上可达数百：cv ∈ {5e-4, 2e-3, 8e-3} 对应 cv×300 ≈ {0.15, 0.6, 2.4}——从"仅在巨空白区时微弱生效"到"与局部增益相当"。三者覆盖决策改变率从 0 到显著的整段。

## 4. 预注册判据

沿用 docs/30 §4 与历轮杠杆协议：train 评估按 `[train[:6], train[:16], train]` 赛程（保 6→2，baseline+collision_only 恒在），selection_guard（invalid=0、stage1 ≥ baseline_stage1−1）；heldout 只在选定后评一次；不迭代 heldout。若 train 无正收益或决策改变率 ≈0 → 杠杆关闭（保留 0，如 stale_grace_ticks 先例）。若出现"stage-2 受益/stage-1 受害"的混合信号 → 按 frontier 分拆先例把参数改为仅 stage-2 生效再评，不在本轮直接晋升。

## 5. 首轮结果（levers-coverage-2026-10-30.json）：混合信号 → 分拆

| 组 | objective | stage1 score | stage1 R | stage2 score | stage2 R | stage2 D | stage2 M | deaths | blocked | win_share |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| base_off | 0.7971 | 33.33 | 166.7 | 41.25 | 60.0 | 1026.7 | 2.58 | 83 | 93 | 0.333 |
| cov0005 | 0.7512 | 30.33 | 151.7 | 41.25 | 60.0 | 1007.5 | 2.58 | 86 | 105 | 0.250 |
| cov002 | 0.7653 | 31.00 | 155.0 | 41.875 | 60.8 | 1000.4 | 2.75 | 98 | 86 | 0.250 |
| cov008 | 0.7813 | 31.17 | 155.8 | 42.50 | 61.7 | 844.6 | 2.83 | 86 | 212 | 0.333 |

读法：

1. **第一阶段全负**（三个 cv 一致）：score 33.33 → 30.3~31.2，R −10~15。覆盖排序把扫图拉向大空白区、脱离收集相关口袋——与 stage1_ring_value 轮同型失败（巡回重排扰动收集链），再次确认"第一阶段贪心最近扫图是局部最优"。
2. **第二阶段分数随 cv 单调微升**：41.25 → 42.5（12 局，R +1.7、M +0.25，方向与机制预测一致——更早到达远侧簇），但 win_share 持平 0.333，且增益出现的 cov008 处 D −182（1027→845）、blocked +119（93→212）：覆盖最大化把机器人拖过整张图的争夺区，路上碰撞/交火代价显著。
3. **总体 objective 全负**（0.751/0.765/0.781 vs 0.797）——首轮无晋升，触发 §4 预注册的混合信号分支：改为仅 stage-2 生效（`explore_component_value > 0 && stage_ == 2`，对齐 frontier_value 惯例），量级 {2e-3, 8e-3, 2e-2}，重评 train（levers-coverage-split-2026-10-30.json，结果见 §6）。

## 6. 分拆轮结果（levers-coverage-split-2026-10-30.json）与 heldout 判据（预注册）

（本节先写判据，再填数据——判据在 heldout 运行前已定，不做事后改口。）

| 组 | objective | stage1 score | stage2 score | stage2 R | stage2 D | stage2 M | deaths | blocked | win_share |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| base_off | 0.7971 | 33.33 | 41.25 | 60.0 | 1026.7 | 2.58 | 83 | 93 | 0.333 |
| cov002 | 0.7945 | 33.33 | 41.875 | 60.8 | 1000.4 | 2.75 | 98 | 86 | 0.250 |
| cov008 | **0.8084** | 33.33 | 42.50 | 61.7 | 844.6 | 2.83 | 86 | 212 | 0.333 |
| cov02 | 0.7660 | 33.33 | 39.64 | 50.8 | 737.3 | 2.75 | 85 | 125 | 0.167 |

读法：

1. **门控生效**：stage-1 四组全部 33.33/166.7——与 base 逐位一致，分拆干净。
2. **cov008 为唯一 train 正收益**（objective +0.0113；stage2 score +1.25、R +1.7、M +0.25，全部与机制方向一致），且通过 selection_guard（invalid=0、stage1=基线）。但增益量级弱：win_share 持平（无排名翻转，与 postcap 的 0.25→0.417 决定性信号不同）、blocked 93→212、D −182、按 objective 分解 margin 项平均 −11（赢得更窄）。n=12 局 stage-2，+1.25 分 < 1 SEM。
3. **cov002 持平**（objective −0.0026，win 0.333→0.25）；**cov02 崩**（R 50.8、win 0.167——cv 过大致覆盖项霸占估值，机器人弃饼横穿地图）。量级窗口窄。
4. **与 explore_tour_value 的交互问题由门控消解**：tour 是 stage-1 门控（strategy.cpp:1085），覆盖项是 stage-2 门控——两杠杆跨阶段，无交互可能。heldout 中仍保留 tour/frontier 两个消融作对照完整性。

**heldout 判据（预注册，heldout 运行前定）**：cov008 通过全部 selection_guard 且 train objective 为正 → 按协议触发 heldout 一次性验证（arena-coverage-heldout-2026-10-30.json，30 场景）。晋升条件：`heldout objective(selected) ≥ objective(baseline) + 0.01` 且 invalid=0（postcap 先例为 +0.059 决定性差距；train 信号弱，故要求 heldout 明确为正）。任一不满足 → 家族关闭，`explore_component_value` 保持 0。

## 7. heldout 结果（arena-coverage-heldout-2026-10-30.json）：家族关闭

| 组 | objective | stage1 score | stage2 score | stage2 R | stage2 D | stage2 M | deaths(30局) | win_share |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| baseline（冻结） | 0.7710 | 32.33 | 40.78 | 61.25 | 737.0 | 2.58 | 140 | 0.375 |
| selected（cov008） | 0.7906 | 32.67 | 42.06 | 61.25 | 830.8 | 2.83 | 151 | 0.375 |
| selected_without_tour | 0.7873 | 32.00 | 42.06 | 61.25 | 830.8 | 2.83 | 151 | 0.375 |
| selected_without_frontier | 0.7358 | 32.67 | 38.63 | 51.67 | 979.1 | 2.46 | 159 | 0.333 |
| 冠军封存（postcap heldout，同30场景） | **0.8299** | 32.67 | 43.88 | 69.6 | — | 2.83 | — | 0.458 |

裁决：**家族关闭，explore_component_value 保持 0**。

1. **可比性钉死**：冻结基线在两次 heldout 中逐位复现（0.7710073 vs 0.7710073，同 30 场景、同 arena 规则；冠军路径在 cv=0 时逐位一致，stage-1 恒等已佐证）。
2. **杠杆边际 = −0.039**：selected(cov008) 0.7906 vs 冠军自身封存 0.8299（arena-postcap-heldout-2026-10-29，同 30 场景）。train 的 +0.0113 是噪声偏正向：stage2 R +1.7 未复现（61.25 = 61.25）、score 42.06 < 冠军 43.88、win_share 0.375 < 冠军 0.458。
3. **参考系修正（透明记录）**：§6 预注册的判据写成"objective(selected) ≥ objective(冻结基线) + 0.01"——机械套用会得出 0.7906 ≥ 0.7810"通过"，但那把"冠军既有提升"与"本杠杆增量"混在一起。正确参考系是冠军自身封存 heldout（postcap 轮同一场景的 0.8299）。修正方向与晋升相反（从严），非结果挑选；该教训并入协议：**杠杆 heldout 的晋升基准是冠军封存 heldout，冻结基线只作可比性校验**。
4. **消融**：without_tour → stage-2 恒等、仅 stage-1 掉 0.67（tour 与覆盖跨阶段无交互，与门控设计一致）；without_frontier → 0.7358、R 51.7（frontier_value 是承重项，覆盖项不能独立成立）。
5. **机制诚实结论**：覆盖最大化在 stage-2 的"更早到达远侧簇"收益未超过"横穿争夺区的路径代价"（blocked/deaths 上升、win 持平）。L-c 家族与 assassin、ring、shadow 等并列关闭；`explore_component_value=0` 永久保留（代码保留、默认关、冠军逐位一致，供后人对照）。

## 8. 归档

- 代码：strategy/iterate-arena-2026-10-28 e83b09d（杠杆实现 + 3 份封存报告 + eval_levers coverage 组）。
- 数据：tests/results/levers-coverage-2026-10-30.json、levers-coverage-split-2026-10-30.json、arena-coverage-heldout-2026-10-30.json、selected-parameters-coverage-heldout-2026-10-30.json。
- 下一轮队列：T5 剩余项（低血量预测失败、可用公告窗口）；批量实战轮换多图多对手。
