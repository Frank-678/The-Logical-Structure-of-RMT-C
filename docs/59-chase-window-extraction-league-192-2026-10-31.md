# docs/59 · 追击窗口真实提取（docs/49 Q3 第一步）· 2026-10-31

**任务 #20（CHASE 真实墙角失败提取，docs/49 Q1-Q6）第一步产出**：从 league-192 冠军模型（M1-M3 共 144 场，A 席）真实对局中提取"追击窗口"——连续 ≥5 tick 与敌曼哈顿距离 ≤2、全程零 ATTACK 的片段——并对每个窗口计算攻击机会与漏打判定。工具：/tmp/chase_extract.py（botA.log × communication.jsonl 双源对齐），结果 /tmp/chase_windows.jsonl。

## 1. 窗口总览

| 指标 | 值 |
|---|---|
| 对局数 | 144（M1/M2/M3，冠军=A 席） |
| 追击窗口 | 191 个，共 2078 tick |
| 长度 | 最小 5 / 中位 10 / 最大 42 |
| 起始于地图边缘（≤1 格） | 85/191（45%） |
| 真墙角（两边 ≤1 格） | 8/191 |
| 窗口内死亡 | **0/191** |
| 掉血窗口 | 45/191（中位 Δhp=0） |
| 停滞（stagnant>0） | 0/191 |

## 2. 动作原因分布

| reason | 窗口数 |
|---|---|
| approach_enemy | 125 |
| defend_lethal_threat | 99 |
| unstuck_relocate | 76 |
| explore_frontier | 34 |
| reach_mission / collect_resource(_chain) | 17+12+10 |
| explore / finished | 5+11 |

## 3. 「漏攻击」判定与解释

攻击规则（strategy.cpp:59-67）：普通攻击=同直线 1–2 格、墙不挡；无双=5×5。窗口内"可攻击"tick = 同轴曼哈顿 1-2 ∧ 敌非保护 ∧ 己非保护 ∧ 存活。共 766 个可攻击 tick，全部未出手（窗口定义即零 ATTACK），按门控解释分层：

| 分类 | 窗口数 | 依据 |
|---|---|---|
| lethal_defense（致命防御位移） | 99 | reason 含 defend_lethal_threat；保命优先 |
| race_gate（竞速禁战） | 18 | reason 含 collect_resource(_chain)/reach_mission |
| low_hp（hp≤20 保命） | 17 | hp0≤20 |
| D 封顶（post_cap） | ~57 | 窗口起点 effective_damage **全部 ≥500**（505-620）——strategy.cpp:1343 D≥500 且无伤害任务时攻击价值 ×0.02，属设计行为 |
| **无法解释的真实漏打** | **0** | 无 |

## 4. 结论

1. **冠军模型在 league-192 中不存在无法解释的墙角/逼边 MOVE-only 失败**：191 个近敌零攻击窗口全部由四类设计门控解释（致命防御 99、竞速门 18、低血保命 17、D 封顶 57），窗口内死亡 0、停滞 0。
2. 用户 Frank 报告的"墙角一直 MOVE"现象在冠军模型联赛数据中不重现；若其在现场复现，输入侧差异（地图/对手/事件）优先排查（docs/49 Q3 步骤 2 短场景比对仍为后续手段）。
3. 附带结论：D≥500 后冠军对近身敌完全停火（post_cap 0.02 只保平局价值）——联赛窗口里 57 个窗口约 44 tick 的"可打不打"是封顶设计使然；若正式赛 D 封顶口径仍为 500，此为预期行为。
4. 遗留：M4 冠军在 B 席，无 B 席感知（communication.jsonl 仅 A 席），未纳入；如需要可另行重放。

*密钥扫描通过（本文件不含密钥）。*
