# 46. R2 候选对照：7 变体 × 6 短现场第一轮 + M3 候选收口（2026-10-29）

> 状态：**完成**。I4.2 任务（review.md:358，"保存首处分叉前后自身输入与 last_action，导出短现场再比较候选，别继续只调全局权重"）的候选对比步。第一轮 42/42 全部跑完（7 变体 × 6 现场，new 保真 6/6 位元级）；第二~八轮收口 **M3 候选 = old7_no_etr0（6 参数集，探针开启）**。
> 证据：WSL `~/cst/build/league/r2_compare/summary_42.json`（第一轮 42 行）+ `summary_r2.json`（第二轮 24 行）+ `summary_r3.json`（第三轮 21 行）+ `summary_r4.json`（第四轮 12 行）+ `summary_r5.json`（第五轮 10 行）+ `summary_r6.json`（第六轮 6 行）+ `summary_r7.json`（第七轮 3 行）+ `summary_r8.json`（第八轮 2 行）+ 每变体独立场景报告 `scenes/<case>-<variant>.json`；驱动脚本 `build/league/r2_compare.py` / `r2_compare5.py` ~ `r2_compare8.py`（第六~八轮 summary 由报告重放重建，带 `reconstructed=true` 标记）。
> 口径：离线竞技场 stage2 记分（`30*min(R/120,1)+15*min(D/500,1)+5*M`）；与联赛同 seed 短现场，非联赛对局，**不构成联赛证据**，只用于候选筛选。

## §1 结论（前置）

1. **方法成立**：new 变体（全默认参数）6/6 现场 500 Tick 决策与冻结 new tape 位元全等、终局 R/D/deaths/completed/hp 与 result.json 全等 → "strategy 代理 ≡ 冻结 new" 成立，参数变体对比有因果意义。
2. **sparse 家族（ref 40.0 vs 当前 22.5，-17.5）已定位且可完整恢复**：根因 = 新版把旧版"无门槛 2.0 到点任务拉拽"清零（T9 首分叉）。old 参数组（含 `mission_explore_value=2.0`）两格均恢复 **40.0**（= 旧版，Δ=0）且 **0 非法、0 副作用**；pull8（`stage2_mission_pull_stale_ticks=8`）economy 格恢复 40.0、archive 格因脚本回放对手在分歧世界中的非法动作触发 always 断言（**夹具伪影**，见 §5）。
3. **snake 家族（ref 60.0 vs 当前 27.5，-32.5）部分定位**：T22 分叉根因 = 新代码的资源探针以 +5.0 采集任务加成被选中（旧版无此代码），**参数不可复现**（old 参数组在 T22 仍走新路，仅靠晚局参数获得 +20 → 47.5）。probe0（探针加成缩放=0）换路 +5 → 32.5 且 0 副作用。残差 12.5–27.5 属探针代码差异本身，非参数可及。
4. **wide_lanes 家族（ref 47.5/57.5/47.5 vs 当前 32.5/47.5/32.5）根因不在 T2**：T2 动作（reach 8.0 vs 4.0 加成失效算术）可被 old/rrh 翻转且 match_old_at_T=True，但**翻动作不翻分**——old 参数组也只跟踪冻结 old 到 tick 10 即分叉、终局分数无恢复。分差根因在 tick 10 之后的决策（首嫌：旧版无门槛拉拽，第二轮 oldpull 验证）。
5. **否决 rrh**：rrh05/rrh10 在所有干净格 Δ=0；wide_lanes-archive 中止席位经第五轮复核 = **A（脚本回放，非 focal）**——夹具伪影（§5 原稿"focal 自身非法"已修正），但 rrh 仍因零收益被否决。
6. **M3 候选 = old7_no_etr0（6 参数集，探针开启）**：八轮收口（见 §6 冻结结论）：snake 47.5（+20）、sparse 40/40（= ref_old 精确）、wide_lanes 三格不变、0 中止、0 非法；行为类改动按巡逻规则默认关闭，冻结后仍待竞技场（144 场 M3）评估。

## §2 方法

- **场景**：R2 原版计划 6 短现场（`build/league/r2_plan.json` 子集；snake/sparse/wide_lanes × pressure/economy/archive），真实 NPC 对手、同 seed、温重放已证明与联赛逐位一致（docs/42）。
- **变换**：focal 席位 external → 离线 runner 内进程 strategy 代理（参数编译自 match_config.hpp）；archive 局其余 external 席位（$anchor=new）按 new 侧 tape 脚本化（= 原局对手真实行为回放）；run 覆写为 `until_tick=500`（去掉 expect/break_when/save_at/warm_until）保证完整 500 Tick 可比。
- **对比**：T = 冻结 new/old tape 首分叉 tick（snake 22 / sparse 9 / wide_lanes 2）；测变体在 T 的动作是否与冻结 old 一致（match_old_at_T）、与两条 tape 的首分叉 tick、终局 R/D/deaths/completed/hp；变体间只改参数（sed 换 match_config.hpp → 独立构建缓存 → 跑局 → 还原），参数表见 §3 注。
- **旧侧身份（权威）**：r2_run/versions/old/manifest.json = 源提交 **65c8714**（前杠杆时代策略代码：无资源探针、无 stage2 杠杆参数、任务拉拽为硬编码 2.0），参数覆盖表 rmb 4.0 / rmv 4.0 / grb 0.1 / tdc 0.25 / frontier 0.02 / fortress_capture 12.0 等；**不是** 9bc72a7。9bc72a7 源码配置与 27c3bcd 冠军树仅注释级差异 + 6 个默认中性新参数（唯一行为增量 = post_cap_combat_weight 0.02 取代旧硬编码 0）。故"old 变体"= 当前代码 + {rmb 4.0, rmv 4.0, mev 2.0, etr 0.0, pcc 0.0, grb 0.1, tdc 0.25}，其中 mev=2.0 近似旧硬编码拉拽、etr=0.0 近似旧代码无探针、pcc=0.0 = 旧硬编码——近似性已在 sparse 双格 40.0（= ref_old 精确）验证。
- **已知局限**（诚实声明）：archive 格对手为"冻结 new 的脚本回放"，在 focal 路径分歧后不重新决策，可能把原世界合法的动作变成分歧世界的非法动作（§5 伪影）；故 archive 格只作辅助证据，economy/pressure 格（真实 NPC 决策）为主证据。

## §3 第一轮全表（竞技场 stage2 分）

| 现场（ref_old→ref_new） | new | old | rrh05 | rrh10 | pull8 | probe0 | combo |
|---|---|---|---|---|---|---|---|
| snake-A-pressure（60.0→27.5） | 27.5 | 47.5 | 27.5 | 27.5 | 27.5 | **32.5** | 32.5 |
| sparse-A-economy（40.0→22.5） | 22.5 | **40.0** | 22.5 | 22.5 | **40.0** | 22.5 | **40.0** |
| sparse-A-archive（40.0→22.5） | 22.5 | **40.0** | 22.5 | 22.5 | 40.0† | 22.5 | 40.0† |
| wide_lanes-C-economy（47.5→32.5） | 32.5 | 32.5 | 32.5 | 32.5 | 32.5 | 32.5 | 32.5 |
| wide_lanes-C-pressure（57.5→47.5） | 47.5 | 47.5 | 47.5 | 47.5 | 47.5 | 47.5 | 47.5 |
| wide_lanes-C-archive（47.5→32.5） | 32.5 | 32.5 | 32.5† | 32.5† | 32.5 | 32.5 | 32.5† |

† = 断言中止（stop=assertion_failed，always 条件 `/world/cars/X/invalid == 0` 被打破，即出现非法动作）：sparse-archive × pull8/combo；wide_lanes-archive × rrh05/rrh10/combo。中止局终局分数为中止时刻值，仅参考不计数。
**保真**：new 6/6 fidelity_ok=True、fidelity_ticks_mismatch=[]、final_matches_ref_new=True。

变体参数（其余参数全部保持当前默认；当前默认 = 赛后迭代值）：

| 变体 | 参数改动 |
|---|---|
| old | resource_mission_bonus 4.0、reach_mission_value 4.0、goal_retention_bonus 0.1、tactical_death_cost 0.25、mission_explore_value 2.0、explore_toward_resource_value 0.0、post_cap_combat_weight 0.0 |
| rrh05 / rrh10 | race_reach_holdoff 0.5 / 1.0 |
| pull8 | stage2_mission_pull_stale_ticks 8 |
| probe0 | explore_probe_mission_bonus_scale 0.0 |
| combo | rrh10 + pull8 + probe0 |

**分叉结构**（首分叉 tick，与冻结 old tape / 冻结 new tape 比较）：

| 现场（T） | old | pull8 | probe0 | rrh（代表） |
|---|---|---|---|---|
| snake（22） | match_old@T22=否；跟 new 至 36 | 全程=new | 跟 new 至 33 | 全程=new |
| sparse（9） | **match_old@T9=是**；跟 old 至 95（eco）/24（arch） | 跟 new 至 11，与 old 从 T9 即不同 | 全程=new | 全程=new |
| wide_lanes（2） | match_old@T2=是；**跟 old 仅至 10** | 全程=new | 全程=new | match_old@T2=是；跟 old 仅至 10 |

## §4 机制解读

- **sparse**：T9 分叉根因 = 新版把旧版无门槛拉拽清零（docs/42 结论）。old 参数组恢复 `mission_explore_value=2.0` 后 T9 立即走旧路、跟踪冻结 old 至 95 tick，两格均 40.0 干净——**该家族差距完全由该参数解释**。pull8 从另一条路径（资源 8 tick 未现身才拉拽）也到达 40.0，但路径与冻结 old 不同（T9 起即分歧），archive 格撞出脚本伪影。
- **snake**：T22 分叉根因 = 新代码资源探针（explore_toward_resource 的边界格试探）以 `resource_mission_bonus × scale`（5.0）计入采集任务加成而被选中，沿资源走廊拖走行动力（与 docs/42 一致）。old 参数组把加成降为 4.0，**仍在 T22 选探针**（=新路），故 T22 行为不可由参数复现——这是代码差异，不是参数差异；其 47.5 的 +20 全部来自晚局任务/死亡参数。probe0 把加成归零后 T33 换路，多完成 reach 任务 +5。
- **wide_lanes**：T2 分叉根因 = reach 8.0 vs 4.0 的加成失效算术（docs/42 结论）。old/rrh 均能翻转 T2 动作且与冻结 old 一致，但**跟到 tick 10 就分叉、终局分数不恢复**——说明 T2 动作本身不具分因果性；frozen-old 的 R=70（vs 当前 30）来自 tick 10 之后的决策。old 参数组不覆盖该决策（首嫌：无门槛拉拽在 wide_lanes 的形态 ≠ `mission_explore_value` 的作用域），由第二轮 oldpull（mission_explore_value=2.0 + pull8）直接验证。

## §5 INVALID-ABORT 分析（中止格席位归属）

中止格 = 出现非法动作（竞技场 always 断言 `/world/cars/X/invalid == 0`）。席位归属证据链（per-variant 报告 + 组件隔离逻辑）：

1. **sparse-A-archive × pull8/combo → 席位 B（脚本回放）**：直接证据 = combo 落盘报告 cars/B/invalid（tick 316，第一轮幸存）、oldpull 报告 cars/B/invalid（tick 429，第二轮）、mev2 报告 cars/B/invalid（tick 429，第三轮）——三份报告一致指向席位 B。组件隔离：pull8 单独即中止、rrh10/probe0 单独不中止（summary_42 中止行）→ 归属 pull8 路径。机制：B 是冻结 new 的脚本回放，focal 在分歧路径下产生新世界状态后，B 在**原世界合法**的脚本动作在新世界非法（如撞占位）——**夹具伪影，不代表真实对局中 B 会非法**（真实 B 会重新决策）。佐证：old 参数组同样恢复 sparse 40.0 但走冻结 old 原路，B 脚本全程合法，两格零非法；第四轮 mev2pcc0 三格全干净（pcc0 改晚局交战路径后伪影不触发）——中止与否是分歧路径依赖，非参数固有属性。
2. **wide_lanes-C-archive × rrh05/rrh10/combo**：组件隔离成立——rrh 单独即中止、pull8/probe0 单独不中止（summary_42 中止行）→ 归属 rrh 路径。但第一轮 per-variant 报告因共享 out_prefix 缺陷被覆盖，**中止席位无幸存直接证据**，且该场 focal = 席位 C（A/B/D 均为脚本回放）——若席位非 C 则同样属夹具伪影。第五轮复跑 rrh10 直接取证（见 §6 结论）。无论席位归属，rrh 均因"翻动作不翻分、零收益"被否决，席位结论只影响风险定性（focal 自身非法 = 真实风险 / 脚本非法 = 伪影）。

**对候选的判定含义**：INVALID-ABORT 是筛选的硬否决项之一；夹具伪影类（席位=脚本回放对手）不否决候选但降低 archive 格证据力，以 economy/pressure 格为主证据；focal 自身非法类直接否决该变体。

## §6 第二轮收口 + 第三轮单参数消融（M3 候选冻结）

**第二轮全表**（pull8probe0 / oldpull / oldpullprobe0 / oldprobe0 × 6 现场）：

| 现场（ref_old→ref_new） | pull8probe0 | oldpull | oldpullprobe0 | oldprobe0 |
|---|---|---|---|---|
| snake-A-pressure（60.0→27.5） | 32.5 | 27.5 | 27.5 | **47.5** |
| sparse-A-economy（40.0→22.5） | 40.0 | 40.0 | 40.0 | 40.0 |
| sparse-A-archive（40.0→22.5） | 40.0† | 40.0† | 40.0† | **40.0** |
| wide_lanes-C-economy（47.5→32.5） | 32.5 | 32.5 | 32.5 | 32.5 |
| wide_lanes-C-pressure（57.5→47.5） | 47.5 | 47.5 | 47.5 | 47.5 |
| wide_lanes-C-archive（47.5→32.5） | 32.5 | 32.5 | 32.5 | 32.5 |

第二轮结论：
1. **wide_lanes 参数不可达**：oldpull（mission_explore_value=2.0 + pull8）在 snake 上全程 ≡ new（first_diff_vs_new=None）、wide_lanes 三格分毫未动——"旧版无门槛拉拽"假设对 snake 残差与 wide_lanes 分差**同时证伪**。wide_lanes 的 tick-10 分叉属于 9bc72a7→当前代码的代码层差异，参数不可及（§7.3 转代码层排查）。
2. **snake +20 与 mev2/pull8 无关**：oldpull 在 snake 上 ≡ new；snake 的 47.5 来自 old 参数组的其余参数（第三轮拆解）。
3. **pull8 的 archive 中止非"唯一元凶"修正**：第二轮 5/5 含 pull8 中止、2/2 不含通过；但第三轮 mev2 单独也中止（见下）——中止是"轨迹分歧后脚本回放对手非法"的伪影，取决于分歧后的具体路径，不是单一参数的固有属性。
4. **oldprobe0 ≡ old**：probe0 在 explore_toward_resource_value=0.0 下无作用（探针动作整体被关）。

**第三轮单参数消融**（× snake / sparse-economy / sparse-archive；grb01/tdc025 为 no-op——当前默认已等于旧值，属规格冗余）：

| 现场 | mev2 | rmb4 | rmv4 | grb01 | tdc025 | etr0 | pcc0 |
|---|---|---|---|---|---|---|---|
| snake-A-pressure | 27.5 | 27.5 | 27.5 | 27.5 | 27.5 | 32.5 | 31.3 |
| sparse-A-economy | **40.0** | 22.5 | 22.5 | 22.5 | 22.5 | 22.5 | 22.5 |
| sparse-A-archive | 40.0† | 22.5 | 22.5 | 22.5 | 22.5 | 22.5 | 22.5 |

消融结论：
1. **sparse 恢复 = mev2 单独贡献**（40.0，= ref_old 精确）；rmb4/rmv4 单参对两家族均无效；pcc0 只改晚局交战（snake D 800→460、sparse D 820→660），无分。
2. **snake 的 +20 = 参数交互**：没有任何单参单独给出 +20；etr0（关探针）单参 +5（=probe0 的效果——关探针与探针无加成殊途同归，都完成 reach 任务），pcc0 +3.8。old 变体的 47.5 来自组合效应（第四轮两参拆解）。
3. **mev2 单独在 archive 格中止**（脚本回放伪影），old 全参数组在 archive 格干净——中止与否取决于分歧后的具体路径，非单参固有属性。
4. **勘误（原稿误称 grb01/tdc025 为 no-op）**：当前默认 `goal_retention_bonus=0.0`、`tactical_death_cost=0.0`（并非旧值 0.1/0.25）——grb01/tdc025 是真实改动，只是**单独无效应**；第五/六轮差分证明它们在组合中参与 snake route-B（见下）。

**第四轮两参交互**（mev2 与各 old 参配对 × snake / sparse-economy / sparse-archive）：

| 现场 | mev2rmb4 | mev2rmv4 | mev2etr0 | mev2pcc0 |
|---|---|---|---|---|
| snake-A-pressure | 27.5（≡new） | 27.5（≡new） | 27.5 | **31.3** |
| sparse-A-economy | 40.0 | 40.0 | 40.0 | **40.0** |
| sparse-A-archive | 40.0† | 40.0† | 40.0† | **40.0** |

第四轮结论：
1. **snake +20 不是任何两参组合**：mev2rmb4/mev2rmv4 在 snake 上全程 ≡ new（first_diff_vs_new=None）；mev2etr0 = 27.5——**mev2 抵消 etr0 单独的 +5**（etr0 单独 32.5，轨迹交互：mev2 改早期拉拽轨迹后 etr0 关探针的效果不再产生 reach 任务完成）；mev2pcc0 = 31.3——pcc0 的 +3.8 幸存。old7 的 snake 47.5 是 ≥3 参交互（第五轮 leave-one-out 定位）。
2. **mev2pcc0 三格全干净（40/40/40）+ snake 31.3**：mev2 单独在 archive 格中止，加 pcc0 后中止消失——pcc0 改晚局交战路径，避开脚本回放非法动作的触发路径；中止与否是分歧路径依赖的又一证据（§5）。
3. mev2 与 etr0 在 snake 上互斥（轨迹交互），二者不可叠加使用。

**第五轮收口**（snake leave-one-out + rrh 席位复核；six_no_mev2 / etr0pcc0 / mev2etr0pcc0 / old7_no_etr0 × snake、wide_lanes-C-archive；rrh10 × 同两场）：

| 现场 | six_no_mev2 | etr0pcc0 | mev2etr0pcc0 | old7_no_etr0 | rrh10 |
|---|---|---|---|---|---|
| snake-A-pressure | **47.5** | **47.5** | 31.3 | **47.5** | 27.5（≡new） |
| wide_lanes-C-archive | 32.5 | 32.5 | 32.5 | 32.5 | 32.5†（tick 196） |

第五轮结论：
1. **snake +20 最小集 = etr0+pcc0 两参（47.5）**——route A（关探针）。six_no_mev2 = 47.5 证明 **mev2 不参与 snake 增益**；etr0 单独 +5、pcc0 单独 +3.8，两参组合非线性叠加到 +20。
2. **route B（探针保持开启）= pcc0 + rmb4 + rmv4 + grb01 + tdc025**：old7_no_etr0 = 47.5；第四/六轮差分证明该组合缺 grb01/tdc025 即回落（mev2pcc0rmb4rmv4 = 31.3）。
3. **mev2 与 snake 增益互斥**：mev2etr0pcc0 = 31.3——mev2 改变早期任务拉拽轨迹后，etr0+pcc0 的 synergy 消失；但 mev2 不干扰 route B（old7_no_etr0 含 mev2 仍 47.5）。
4. **rrh10 中止席位 = A（脚本回放，非 focal C）**——§5 席位复核完成：夹具伪影，非真实风险；rrh 否决改由"翻动作不翻分、零收益"单独支撑（§5 原稿"focal 自身非法"表述已修正）。

**第六轮**（mev2pcc0rmb4rmv4 / mev2pcc0rmv4 × snake/sparse-economy/sparse-archive）：sparse 三格全 40.0 干净（mev2+pcc0 组合不破坏恢复）；snake 均 31.3——确认 route B 缺 grb01/tdc025 不可达 +20（与第五轮 old7_no_etr0=47.5 差分对照）。

**第七轮**（old7_no_etr0 × snake/sparse-economy/sparse-archive）：**47.5 / 40.0 / 40.0 全过、0 中止、0 非法**——route B 候选在 sparse 双格同样精确恢复 ref_old 40.0。

**第八轮**（old7_no_etr0 × wide_lanes-economy/pressure）：32.5 / 47.5，= new 不变、全过——候选对 wide_lanes 零扰动（三格齐，archive 格见第五轮）。

**冻结结论：M3 候选 = old7_no_etr0**（6 参数集，探针保持开启）：

```
mission_explore_value = 2.0   （恢复旧版无门槛任务拉拽 → sparse +17.5）
post_cap_combat_weight = 0.0  （恢复旧版硬编码 0 → 与 grb/tdc 组合出 snake +20）
resource_mission_bonus = 4.0  （旧版值）
reach_mission_value = 4.0     （旧版值）
goal_retention_bonus = 0.1    （旧版值，组合必需）
tactical_death_cost = 0.25    （旧版值，组合必需）
```

6/6 现场全覆盖证据：snake 47.5（+20）、sparse 40/40（+17.5，= ref_old 精确）、wide_lanes 三格不变、**0 中止、0 非法、0 副作用**。route A（etr0+pcc0，2 参）同效但需关探针，风险面更大，不选。行为类改动按巡逻规则默认关闭：该参数集**不进入默认配置**，只在 M3 席位以参数集形态上场，待 144 场竞技场评估。

## §7 裁决与下一步

1. **候选冻结（已定）**：M3 候选参数集 = old7_no_etr0（§6 冻结结论），写入 144 场计划（M3 缺席时跳过机制不变）。
2. **行为类改动默认关闭**：候选参数不进入默认配置；只在 M3 席位以参数集形态上场（与 old_champion-B 同机制），待 144 场竞技场评估后再决定是否进入默认。
3. **wide_lanes 残差（已裁定）**：第二轮 oldpull 在 snake/wide_lanes 上 ≡ new（"旧版无门槛拉拽"假设对 wide_lanes 证伪），wide_lanes 分差根因在代码层（65c8714→当前 513 行差），需回到冻结 old 的 tick-10 决策现场排查，不再调全局权重（I4.2 原话）。
4. 证据归档 log 分支（summary_42.json / summary.json / 驱动脚本 / 场景报告）随本报告提交后执行。
