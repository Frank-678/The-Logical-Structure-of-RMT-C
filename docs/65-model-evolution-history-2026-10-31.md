# 模型变化历程总览（从始至终）

> 2026-10-31 16:29（Asia/Shanghai）· Claude Code（Frank 侧）
> 归档范围：10-20 源码起步 → 10-31 终版裁决与 Fix 1。依据：match_config.hpp 提交史（f157afe→acc91b6）、review.md 全时间线、docs/01-64、official_baseline_6179f56b_analysis.md / official_exp_round1.md（cst 仓根目录，已追踪）。
> 判读约定：本仓所有行为类改动默认关闭（=冠军行为位一致），离线竞技场 train+heldout 双验证 → 裁判复验 → 组合正和 → 晋升写回 match_config 注释。分数口径：stage1=40×R1/200；stage2=30×min(R2/120,1)+15×min(D/500,1)+5×M，满分条件 R2≥120 且 D≥500 且 M=3（D 封顶实测 500，非 rules.txt §10.2 的 300，docs/58 破解）。

## 一、起点与基线（10-20 ~ 10-27）

- 规则研读与架构（docs/01-20）：状态机、对手预测、消息设计；参数集中到单一头文件（f157afe "refactor(config): put explicit match settings in one header"），成为此后一切调参的唯一入口。
- 搜索基线定值（训练选定）：resource_plan_depth=4、resource_beam_width=5、resource_candidate_limit=8、resource_plan_budget_ms=10、frontier_value=0.02（stage2）、战术三 tick 搜索默认关（tactical_search=false）。
- 行为基线定值：stale_resource_decay=0.01、resource_mission_bonus=5.0、reach_mission_value=8.0、healing_below_hp=40、fortress_hold_value=20、fortress_capture_value=12、hazard_lead_ticks=2。
- 练习链路：10-25 起 mock 模式（6 会话 200 条，非真实调用）；10-28 21:21 起 real 模式，至 10-29 21:51 共 **90 个会话 HTTP 200 计 5912 次**（四席 A/B/C/D 均有成功记录，含 EVENT_USE 两局 dfcef97=45 分第一 / 178b15=55 分第一）——LLM 精化路径真实生效的直接证据；10-30 链路终验 request_ok（deepseek-flash / max_tokens 512 / proxy configured，1163ms）。

## 二、战役三连（10-28）

- **v1 全废重建**：批量改参脚本三连 sed 事故，全体变体作废，确立「入队前对 validate() 查表」铁律。
- **v2 备份污染**（05:2x）：备份拷贝混入工作树污染对照，重建隔离。
- **v3 24/24 建成**：24 变体战役全部落成。变体命名族谱：race_on/racex（竞速闸门）、tour（巡回）、frt（frontier）、ring（近出生覆盖）、decay/etr/grb/grace（衰减/入塔/格布/宽限）、flood（洪泛）、pbs/rbw/rmb/rmv/rpd/rpb（各类旋钮剂量）、mexp/mve（探索系）、fish（渔翁）、reachu、base-s2、c_*（战役复合）。

## 三、逐轴调参时代（10-28 ~ 10-30，竞技场家族轮）

每家族一轴、默认关、heldout 一次性验证。家族结论（注释留档）：

| 家族 / 参数 | 裁决 | 依据 |
|---|---|---|
| post_cap_combat_weight | **晋升 0.02** | heldout 0.771→0.830、stage2 40.8→43.9、win_share 0.375→0.458（d795e16，首笔晋升） |
| low_hp_attack_discount | 杠杆落地 1.0（后晋升 0.4） | docs/33 T5 死亡预测（c7fe48e） |
| race_reach_holdoff | 默认 0 待评估 | docs/36（eb321df） |
| fortress 轮（prepare_fortress_value） | 全负关闭 | pf03/06/12/24 objective 0.7971→0.7889 |
| survival 轮（worst_case_survival） | 全负关闭 | 0.7971→0.7597，过度求存变龟缩 |
| coverage 轮（explore_component_value） | 永久关闭 | heldout −0.039（arena 崩 vs 裁判口径冲突的第一次教训） |
| stage1_ring_value | 全负 | 两变体 −2.5 / −5.0 |
| stage1_flood_value | 未过晋升线 | 0.1/0.05/0.02 均未过 |
| assassin 轮（stage2_assassin_value） | 家族证伪 | 单一负翻转 |
| pie-window 攻击折扣 | 否决 | c7a4172 |
| stage2_shadow_value | 否决 | R 位不动、D +25..30 但饼份额未变 |
| defend_stall_break_ticks | 否决 | 49-tick 验证但 post-pie score-inert |
| frontier 拆分（stage1_frontier_value） | 未晋升 | f2.08 赢 train 但 heldout 大败（869621b） |
| stage2 hunger pull（mission_pull_stale_ticks） | 模块落地 0（后晋升 6） | 6fbf5ea |
| explore probe 任务加成缩放 | 默认 1.0 待评估 | 3a37703 |
| 防循环三件套 | 基线开启 | loop_recovery + loop_window/recovery/stalled_goal（27d1a75 等） |

## 四、联赛与同池对照（10-29）

- **league-192**：M4 candidate vs champion-B Δ+2.76（48/48 全胜方向，review 21:54 块口径）。
- **M5 同池 32 局（docs/53）**：candidate vs champion **Δ+1.20 分 / R+3.4 / D−409.8**（5/8 seed 正）；前 24 局均分 45.35、13 次第一、R65.0/D726.8。M1-M4 均分不连成趋势（对手池不同）。
- **AI 口径勘误**：RUN_INDEX 的 222 局（M1-M4 192 + M5 30）全落空 key 时代，AI 全 502 口径成立；「练习从未真实调用 AI」类表述作废（见 §一）。

## 五、d28 全败与 d29 重跑

- **d28：12 变体全收、无一晋升**（ring 退化 w12u23 −30 为代表）。
- **rpb40 旋钮超校验范围**（validate 1..30，入队前未查表）——非法值事故，铁律入库。
- **d29 重跑**：rpb5 / frt04 / frt06 / frt01 四变体（bjk6ybzql），frt 家族由此进入冲刺视野。

## 六、官方图冲刺（10-31 11:5x ~ 13:3x）

- **基线深析**（official_baseline_6179f56b_analysis.md）：A=40 第二 vs D=45 第一；采集 t8 停在 R=40 后 490 tick 白打，11 死逐条复盘（8 次对称换血站桩）；「渔翁」假设提出。
- **计分破解**（official_exp_round1.md）：D 封顶 500；满分条件 R2≥120+D≥500+M=3；「B=36.15 之谜」解开。
- **fish（渔翁门）否决**：29 vs 40 净亏 11——「少打无谓仗」方向对、「完全禁战」执行错（500 tick 仅出手 9 次、15 死全被动）。
- **race_on（race gate）晋升**：A=45 全场第一 ×2 局（R 40→60、死 11→7）；frames.jsonl 证实全图 200 资源 t20 前被四席瓜分完毕，A 几何上限即 R=60。
- **racex（explore 放宽）否决**：41.1/43.75 两局分叉非确定，D 885→370、死 7→11——t20 后无资源可探，探索注定空转。
- **stage1 满分达成 🎯**：s1_g1 **40.0/40**（t76 收满 200R、余量 24 tick，近似最优 TSP 零回头）。
- **24×24 判不可达**：stage1 最优 TSP ≥105 tick > 100，上限≈190，数学上不可达；s2 A=39.5 第二（A 带 50+破序修正≈60 上限）。18×18 官方图为唯一满分目标。

## 七、冲刺三件套晋升（10-31，cb28ee7 / docs/60）+ 配套（0f4fd3f / 08876bb）

| 晋升 | 值 | 依据 |
|---|---|---|
| low_hp_attack_discount | 1.0→**0.4** | 10-29 train +0.014 / heldout +0.0576；10-31 heldout 单独 −0.0012 但组合贡献 +0.0018、裁判 500-tick 复验零副作用 → 组合正和终裁晋升 |
| stage2_mission_pull_stale_ticks | 0→**6** | b2 批内 +0.0194（42.5 分）、heldout 30 场景 +0.0042；剂量窗窄（s2pull3 −0.018 负） |
| stage1_frontier_value | 0.02→**0.06** | 裁判曲线 d29 同图集 13 图 +140 顶点（base 2170/frt06 2310、5 增益图 ×3 稳定、代价仅 w12-uniform-23 −10×3）；arena train −0.023 全部来自自造 maze/rooms 风格图，按 docs/60 裁决「正式赛图以裁判为准」不否决 |
| explore_tour_value | 0.03→**0.06** | relaxed 31 图 w12u23 170→200 且 ×3 复验、其余 30 图零损失（0f4fd3f） |
| stage2_race_gate | →**true** | 官方图两局全胜逐 tick 确定（08876bb，§六） |

- **heldout 组合 lhp+s2pull+frt = 0.8358 全场最优**；三件套组合正和 +0.0076。
- 教训：**编译窗口污染闸门**（评估须在干净构建上跑）；GET/POST 链路分裂排查；arena 与裁判曲线方向冲突时以裁判为准（docs/60 裁决规则）。

## 八、终版裁决（10-31 14:05，docs/62 633c9e6）

晋升 header 即历史最优；**不再试验**；crons 全删、裁判进程停；材料三项用户侧 10-31 20:00 提交。

## 九、R3 联赛与 Fix 1（docs/64 + acc91b6）

- R3 联赛 7/27 中止（frt04/frt06/race_on/racex/tour12/rcl6/rcl10，seed 20261029-35）：A 池 10-29 旧构建模型 finished 停车被蹲出生点收割（旧 bug，当前 header 无此路径）；候选 B 成绩由「死不死」决定。
- **E_BLOCKED 根因**：同 tick 战斗先于移动、争格回执 moved:false——四处路径规划未把「回执确认失败」当信息用。
- **Fix 1**：receipt_block_ticks（回执确认 MOVE 失败 → 目标格堵格 N tick 记忆，主 BFS/资源路由/巡回 TSP/生存 DP 按到达时刻绕行）。默认 0=关、比赛行为不变；arena fix1_block_ab（block0/8/12/16 heldout 对照）被收尾指令打断，待恢复后补跑裁决。

## 十、当前 header 参数总表（2026-10-31 终版）

**已晋升生效**：stage1_frontier_value=0.06、explore_tour_value=0.06、stage2_race_gate=true、stage2_mission_pull_stale_ticks=6、low_hp_attack_discount=0.4、post_cap_combat_weight=0.02、explore_toward_resource_value=0.5、opponent_claim_discount=0.5、opponent_pressure_cost=0.25、opponent_contest_cost=1.0、stale_resource_decay=0.01、loop_recovery=true（window/recovery=12、stalled_cooldown=24）、collision_replan=true、resource_refinement=true（trials=12）、hazard_lead_ticks=2、healing_below_hp=40、fortress 20/12、mission 5.0/8.0、ai_max_tokens=512（官方网关口径）、ai_max_calls_per_match=0。

**默认关待评估**：receipt_block_ticks=0（Fix 1）、race_reach_holdoff=0、stage2_reach_urgency_tick/value=0（reach 完成率 100%，保险）、explore_probe_mission_bonus_scale=1.0、stale_grace_ticks=0、prepare_fortress_value=0、stage2_race_explore_gate=false、stage2_fisherman_gate=false。

**否决永久关闭**：worst_case_survival、explore_component_value、stage1_ring_value、stage1_flood_value、stage2_assassin_value、stage2_pie_attack_discount、stage2_shadow_value、defend_stall_break_ticks、mission_explore_value、stage2_explore_gate_tick、goal_retention_bonus、tactical_death_cost、tactical_search（训练未选中）。

## 十一、未决与待办

1. arena fix1_block_ab 对照补跑与晋升裁决（恢复迭代第一项）。
2. 正式尺寸冒烟：20×20 stage1 / 24×24 stage2（stage2 重标定清单见 review.md 21:54 块第 5 点；stage1 全参数需先修 arena MAP-04）。
3. R3 联赛剩余 20 局续跑（rcl12 起，需先按 r3_driver.sh 重建 27 变体）。
4. stage2 满分差距：官方图 A 几何上限 R=60 → 30×60/120+15+15=45 分；满分 60 需跨带抢资源（R≥120 数学上需对手漏采或换图）。stage1 已 40/40。
5. 停赛挂起项（docs/64 待办三条）+ 10-31 20:00 材料用户侧三项。
