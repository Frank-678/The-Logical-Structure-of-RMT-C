# docs/54 策略·算法·参数总清单（技术报告设计/实现底稿）

- 目的：按 2026-10-30 要求，一次性回答三问——①吃东西（资源收集）有哪些策略；②打仗按什么情境分叉（单挑 / 多打一 / 被夹心），各自用什么参数；③每一步用什么算法（是 beam 还是什么）。同时作为语雀技术报告"设计/实现"章节的事实底稿。
- 依据：冠军构建 **eb321df** 源码逐行核对（`src/rmtc_bot/{strategy.cpp,tactics.cpp,bot.cpp,ai_worker.cpp,events.cpp,session.cpp}` + `include/rmtc_bot/match_config.hpp`）。所有参数值以 `match_config.hpp` 编译期配置为准；标注"关"的行为杠杆在代码中完整实现但比赛配置默认关闭（行为类改动待竞技场评估后才开）。
- 架构一句话：**单机器人、三层决策**——导航/规划层（BFS、beam、DP）、选择层（贪心 utility argmax + 情境折扣）、理解层（后台 LLM 异步理解公告事件，不阻塞每 Tick 决策）。

---

## 1. 每 Tick 决策管道（strategy.cpp `decide()` 实际顺序）

| 步骤 | 内容 | 算法 |
|---|---|---|
| 0 感知 | 解析本队感知 JSON、校验坐标/实体、验证上一 Tick 回执（moved/failed_moves） | 解析+校验 |
| 1 状态重建 | `history_` 快照、`update_effects()` 从历史重算幻术/无双/治疗/易伤/堡垒连续驻留进度 | 全量重建（防重复累计） |
| 2 移动前危险 | 本 Tick 先结算的爆炸 `pre_damage`、分裂墙激活 `split_forced_wait`、致命判定 | 事件检查 |
| 3 危险守卫 | `safe_first_steps`（8 Tick 倒推 DP，≤145 格，只查分裂墙/爆炸）、碰撞改道 `collision_replan`、辣椒可能火线 `possible_fire`、`avoid_possible_chili_fire`、公告危险撤离 `escape_announced_hazard`（提前 `hazard_lead_ticks=2`） | **倒推 DP** + BFS |
| 4 全图 BFS | 已知格上 BFS，每格只存{首步方向,距离}，每帧重算；首层按火线风险升序；不规划超过 `remaining_ticks` 的路线 | **BFS** |
| 5 收益候选 | 采集/任务/回血/堡垒/辣椒/接近敌方/前沿探索等全部 reason 分支算 utility，统一 `consider()` 比较 | **贪心 argmax**（资源串是 **beam**，见 §2） |
| 6 ATTACK 搜索 | 四个方向逐向算攻击估值（最近目标/无双 5×5），情境折扣见 §3 | **贪心 argmax** |
| 7 终选 | 脱困 `unstuck_relocate` → 战术层 `tactical_choice`（**关**）→ `attack_opportunity`（攻击可压过 hold_fortress）→ 最优 MOVE → `probe_unknown_cell`（未知邻格试探）→ 防御兜底 | 见 §6 算法命名表 |
| 8 发动作 | 发 MOVE 时补偿幻术方向反转 `(step+2)%4`；ATTACK 方向不变 | — |
| 旁路 AI | 后台线程：公告去重 → Chat Completions 请求 → 结果校验；**从不等待**，不阻塞动作 | LLM |

---

## 2. 吃资源策略（采集）

### 2.1 单目标采集 `collect_resource`（贪心）
- 触发：记忆图 `tiles_` 中任何 `value>0` 的可达资源。
- 估值：`utility = benefit × freshness / (distance+1)`，distance 是 BFS 绕障距离。
- **新鲜度衰减**：`freshness = 1/(1 + max(0, tick−last_seen−stale_grace_ticks) × 0.01)`——资源离开视野后每 Tick 衰减 1%（`stale_resource_decay=0.01`；`stale_grace_ticks=0` 关：离视野当 Tick 即衰减，未观测≠消失）。
- **第二阶段 benefit 换口径**（R 封顶公式）：`benefit = score_delta(R, v, 120, 30) + min(v,20)×0.001`——R=119 再拿 20 只有 1 点进入封顶计分，不按 20 全额估值。
- **任务加成**：未完成的 normal/high 采集任务给 `resource_mission_bonus=5.0`（每类计一次）；`resource_value` 任务给 `0.1×v`。
- **先到先得折扣**：可见敌车到该格的直线距离 ≤ 我方绕障距离时 `benefit ×= opponent_claim_discount=0.5`——避开会被先拿走的格子。

### 2.2 资源串规划 `collect_resource_chain`（**beam search，开**）
- 触发：≥2 个已知资源；先按单目标 utility 取前 `resource_candidate_limit=8` 个。
- 算法：**beam search**——深度 `resource_plan_depth=4`（最多 4 个连续目标）、束宽 `resource_beam_width=5`（两轮筛选：先保证每首方向一个，再补满 5 条；按 (first, position, collected, elapsed) 去重）、预算 `resource_plan_budget_ms=10`（软预算，耗尽交回已算好的合法基线）。
- 串内拾取：每格重算 `score_delta(virtual_r, v, 120, 30)` + 任务加成（每类一次）+ 门槛机会 `0.1×min(v, value_target−virtual_r)`，乘 freshness 累加；`utility=benefit/(elapsed+1)`。
- 局部改进 `resource_refinement=true`：从当前最好串出发 `resource_refinement_trials=12` 次 反转/插入/删除 目标，每次都完整重评（不交换距离数字）。
- 路线：同帧 BFS + `(起点,终点,elapsed)` 路由缓存复用。
- 上帧计划 `previous_plan` 先重评（目标仍有效则续用）。

### 2.3 巡回 `collect_resource_tour` / `explore_tour`（stage1）
- 算法：**BFS all-pairs**（资源两两距离）→ 近邻构造访问顺序 → **有界 2-opt**（6 pass，只翻转顺序不改距离）→ 剩余窗口内兑现前缀收益。
- 锚点防抖：上一帧首停点仍在边界上就固定为本周起点，防止对称边界每帧来回翻转原地抖动。
- `explore_tour_value=0.03`：stage1 空档期把散布边界观察点（≤8 个、两两距离>2）排成小巡回。

### 2.4 试探采集 `explore_toward_resource`（`0.5`，开）
- 已知资源绕路过远（BFS 距离 > 3×直线+6）或未连通时，只沿已探明边界向它试探：`benefit × 0.5 / (best_cost+1)`，best_cost = 边界格 BFS 距离 + 曼哈顿下界。**不把未知格当空地**。
- `explore_probe_mission_bonus_scale=1.0`（旧行为）：探针与采集同额计入任务加成；0 则只按封顶分差估值（竞技场评估后再定值）。

### 2.5 争抢与竞速
- **争格防护**（stage2）：对方轨迹预测（两次连续相同位移的一步猜测 `forecast`）——预计争同格 `opponent_contest_cost=1.0` 加一份等待成本；下一 Tick 可能入射线的 `opponent_pressure_cost=0.25` 软成本；两者都只影响收益排序，不封路。
- **竞速闸门 `stage2_race_gate=false`（关）**：两轮实验均显示早期主动交火有压制对手扫资源的价值——R 未封顶时禁止主动开战反而亏。
- **到点任务暂缓 `race_reach_holdoff=0`（关）**：docs/35 损失路径=首分钟资源争抢（V1 t62 弃 20R、V4 t14 弃 10R 被 reach_mission 压过）；>0 时已知可达资源未清空前 reach_mission 按 (1−holdoff) 打折。

---

## 3. 打仗策略（战斗情境分支）

### 3.0 总原则：两条伤害口径
- **机会口径** `incoming`：预测会防御的敌车不计入（`enemy_will_defend` 按公开信息推测）；用于攻击估值。
- **生存口径** `incoming_worst`：全敌攻击最坏情形；用于致命判定。`worst_case_survival=false`（survival 轮全负：objective 0.7971→0.7597、D 1026.7→677.1，过度求存龟缩）。
- **还手豁免**：本 Tick 已被火力波及（`incoming>0`）时，所有攻击折扣（竞速闸门、饼窗、低血）一律不适用——不白挨打。

### 3.1 单挑（1v1）——§6 攻击方向贪心 + 接近估值
- 每个方向取最近目标（普通攻击只命中同射线最近一辆；障碍不挡攻击）：
  - 伤害预估：`damage = 预测防御 ? defended_damage_(10) : attack_damage_(20)`；反伤事件中预测防御的目标只计入反伤不伤血。
  - `contribution = min(damage, hp) + (hp ≤ damage ? 60 : 0)`——**补刀 60 击杀奖励**只按一击必杀估值。
  - `utility = combat_value(contribution) + (need_damage && contribution>0 ? 0.5 : 0) − reflected×0.05`，其中 `combat_value(c) = score_delta(D, c, 500, 15) + min(c,60)×0.001`。
  - 若 `reflected + pre_damage ≥ hp` 整个方向跳过。
- **补刀过滤**：`protected_spawn || hp > attack_damage_` 的目标跳过——不为一击打不死的对手放弃近处采集（assassin 杠杆的保留条件，杠杆本身关）。
- **接近估值** `approach_enemy`：`(combat_value(contribution) + (need_damage?0.5:0)) / (distance+2)`；反伤期反复接近同一防御目标不给分。
- **战术层 beam（已实现，比赛关）**：`tactical_search=false`——宽 5、深 `min(3, remaining_ticks)`，对手情景 5-6 个（0 直追/1 驻守/2 轨迹延续 forecast/3 抢资源/4 侧向接近/5 潜在无双 area-attack），每情景 `advance()` 模拟完整 Tick（事件激活→同时战斗→存活者移动→环境/回血/堡垒→拾取→任务），`value = score_delta(R,Δ,120,30) + score_delta(D,Δ,500,15) + task_reward(5×model_reply_seen) + tactical_hp_value×Δhp − tactical_death_cost×deaths`，`aggregate = (1−0.6)×mean + 0.6×worst`，深度折扣 `0.65^depth`，尾值 = 目标 BFS 距离改善 + 堡垒驻留。深度 0 攻击分支吃低血折扣（同口径）。**"本轮训练选中关闭，不假定更复杂必然更强"**——1v1 最优动作实际由 §6 贪心 + 情境折扣承担。

### 3.2 多打一（我方被集火 / 我方打一个目标附近多个敌）
- 被集火：`incoming` 对所有方向的最近射线敌车求和（`enemy_will_defend` 预测不计）；致命判定 `survival_incoming ≥ hp − pre_damage` 且防御能活 → `defend_lethal_threat` 防御保命；连续致命防御驻守计数 `lethal_defend_streak_`，`defend_stall_break_ticks=0`（关，crossroads-542 曾连续 49 Tick 站防 R 仅 50 的教训对应的杠杆未开）。
- 非致命多向压力：`fire_cost[dir] = 1 + possible_fire(next)/max(1, hp−pre_damage)` 折扣首步；contest/pressure 折扣路线（§2.5）。
- 我方打群：攻击只取最近目标（无双时 5×5 全体）；`stage2_assassin_value=0.0`（关）——派窗口刺杀扫资源簇对手的归属收益，只补刀一击必杀目标、按脚边 5×5 未收集资源估值。

### 3.3 被夹心（两向及以上同时射线）
- **没有独立"被夹心"分支**——由三层机制自然覆盖：①`incoming` 多向求和 + 致命判定 → 防御/重生换位；②`fire_cost`/contest/pressure 压高风险首步；③战术层 beam（若开）在同帧模拟全部敌车同时移动，多敌夹击在推演里自动体现。
- 具体行为：被夹且致命 → `defend_lethal_threat`；被夹不致命 → 正常收益排序，还手攻击方向仍取最高 utility（还手不受折扣）；`break_defend_stall` 若开则连续驻守后选**距最近敌车最远**的安全邻格脱离（接受死亡代价的主动重生换位）。
- 无双夹心：我方 `empowered_`（堡垒驻留达标）→ 攻击改为 5×5 全体 + `attack=event.amount`（50 档）、防御伤害 `defended_damage`；敌方潜在无双 → 不确定情景 `possible_enemy_area`（战术层情景 5）/策略层不把未知无双当确定伤害。

### 3.4 战斗情境折扣（参数）
| 杠杆 | 当前值 | 状态 | 依据 |
|---|---|---|---|
| `stage2_pie_attack_discount` 饼窗攻击折扣 | 0.0 | 关 | clusters-495：t20-26 攻击致死、错过中簇 70R；竞速期攻击把我们从抢饼线路吸走。还手不折扣。与 race gate 不同：只压攻击估值，不动任务/接近 |
| `low_hp_attack_discount` 低血攻击折扣 | 1.0 | 关(1.0=旧) | docs/33 T5：53 死亡中 40 例最后动作为攻击且 hp<60、12 例死亡 tick 存在安全方向、8 例可撤退。hp<60 且未被火力波及时乘此值（策略层 §6 + 战术层深度 0 同口径） |
| `post_cap_combat_weight` 封顶后平局权重 | 0.02 | **开** | D≥500 后增量 D 的平局估值（同分同任务同 R 按 D 决胜）。train 晋升 objective 0.7891→0.8056（win_share 0.25→0.417，rooms-s401/crossroads-s542 rk2→rk1）；heldout 一次性验证 0.771→0.830、stage2 40.8→43.9、invalid 0。0.05/0.1 无更多增益 |
| `tactical_risk` | 0.6 | 随战术层关 | 最差情景权重；不是经训练的概率 |
| `tactical_hp_value` | 0.015 | 同上 | 每 HP 的未来机会估值，不写入官方分数 |
| `tactical_death_cost` | 0.0 | 同上 | 调参未发现正向作用 |
| `tactical_future_discount` | 0.65 | 同上 | 第二 Tick 相对第一 Tick 的收益权重 |
| `tactical_goal_weight` | 0.65 | 同上 | 原目标评价在战术比较中的尾部价值 |

### 3.5 环境战斗
- **辣椒**：`trigger_chili`——敌车在火线上且 `hp ≤ amount` 时按补刀 `combat_value(60)` 估值，否则 0.02；`possible_fire` 自伤规避（对方下一步可能踩辣椒的保守估计）。
- **出生保护**：保护车不能被攻击/被计入伤害；我方保护中不发攻击（战术层 `protected_spawn` 攻击动作置空）。
- **堡垒/无双**：见 §4。

---

## 4. 探索·导航·事件·脱困

### 4.1 导航（BFS）
- 每帧全图已知格 BFS，每格存 `{first_step, distance}`；首层按火线风险升序探索；split_wall/dangerous 时空检查；`remaining_ticks` 上限。
- `collision_replan=true`：同一起点同一落点连续 2 次 MOVE 失败，存在合法替代时避开该首步一 Tick。

### 4.2 安全首步（倒推 DP）
- `safe_first_steps`：8 Tick 视界、≤145 格（|dx|+|dy|≤8），从第 8 回合倒推 `good[k][i]`（第 tick+k 站格 i 之后还有避开已知危险的路）；爆炸先于移动结算可进入、下一 Tick 必须安全；找不到认证路线就交回原策略（不判"必死"）。

### 4.3 探索（扫图）
| 杠杆 | 值 | 状态 | 说明 |
|---|---|---|---|
| `frontier_value` | 0.02 | 开(stage2) | 每份潜在新视野 `value×newly_visible/(d+1)`；stage2 与任务/交战公平竞争，只评有未知邻格的边界格；BFS 距离不降提前停止 |
| `stage1_frontier_value` | 0.02 | 开(stage1) | 与 stage2 分离（arena-frontier 轮证实探索权重两阶段影响相反） |
| `explore_tour_value` | 0.03 | 开(stage1) | 边界观察点小巡回（§2.3） |
| `stage1_flood_value` | 0.0 | 关 | 最近边界洪泛（距离优先、同距离取更大新视野；maze-148 +20R 的候选，未通过竞技场） |
| `stage1_ring_value` | 0.0 | 关 | 近出生点完成覆盖加成（rooms-195 左侧 30R 口袋滞留 t91-99 的修复轴，未通过） |
| `explore_component_value` | 0 | 关 | 覆盖最大化：按视野触及最大未探索连通区（4 连通洪泛标号）加权。第一阶段全负；第二阶段 train 略正但 heldout **−0.039**，永久关闭 |
| `stage2_explore_gate_tick` | 0 | 关 | Tick 过闸且 60 Tick 无资源现身时关闭扫图让位交火 |
| `stage2_mission_pull_stale_ticks` | 0 | 关 | 前沿长期无资源发现时向到点任务方向拉拽（rooms 基线教训的候选） |
| `stage2_shadow_value` | 0.0 | 关 | 影子跟踪：对手朝未知区连续同向移动时向其投影前端（k=2..6 已知可走格）探路合流 |
| `mission_explore_value` | 0.0 | 关 | 沿到点任务方向探路——到点任务无截止时间，拉拽会在资源比赛早期拖离采集线 |

### 4.4 事件理解（LLM + 本地校验）
- **LLM**：后台 `AiWorker` 线程。公告原文去重（新批次包含旧批次时移除旧副本，纯字节比较）→ 累计 ≤128KiB → 首帧必发一次请求（即使公告为空，`understood_` 置位前持续）→ Chat Completions：`{session_id, tick, map, announcements, known_events}` + 系统提示要求 JSON 事件解释。
- **传输**：`ai_url`（练习 127.0.0.1:8080，正式赛官方网关）、`ai_token`（练习 practice-A，正式赛**席位令牌 Bearer**）、`ai_model=deepseek-flash`、`max_tokens=2200`（公告示例 512 是否硬上限待 docs/02 定稿）、`thinking=disabled`（2026-10-28 公告要求顶层明确）、`response_format=json_object`、超时 35s/5s、响应 ≤256KiB、请求 ≤2MiB。
- **健壮性**：失败指数退避 1/2/4/8s（最多 4 连败）、3 次 invalid 暂停重试、401/403/400/404/quota 停止、mock 网关识别、跨场代数取消在途请求。
- **本地校验**：`events.cpp` 对 LLM 解释做证据核对（迟到/拒绝/已校验状态机）；`update_effects()` 从历史重建效果（幻术 `reversed_`、无双 `empowered_`、治疗、易伤、堡垒进度 `capture_progress_`）。
- **手册硬性**：stage2 每场须 ≥1 次真实 AI 成功调用，否则该场任务分=0——`model_reply_seen` 才给战术层任务奖励 5 分的前提也与此一致。

### 4.5 脱困
- `loop_recovery=true`：连续 12 份可信回执、周期 1-6 重复或 4 格内徘徊且无实际进展（R/D/hp/已知格/任务/驻留六指标）→ 触发；坏目标冷却 `stalled_goal_cooldown_ticks=24`；脱困目标最多 `recovery_ticks=12`，每帧重查道路与危险。
- 脱困选点：元组字典序 `(有新视野, 新视野/((d+1)×fire_cost), 未访问, −访问数, 距离/fire_cost, 席位去对称)`，只选 `loop_cells_` 外且 ≤6 步的格。
- 兜底：`defend_while_holding`（被火力波及原地防御）、`defend_for_safe_route`（无可走安全路线）、`no_path`、幻术未知 `uncertain_illusion`（禁用定向行为）。

### 4.6 堡垒与治疗
- 堡垒：驻留进度保持 `hold_fortress = fortress_hold_value(20)/(wait+1)`；前往占领 `capture_fortress = 12/(distance+capture_ticks)`（已激活事件按剩余可驻留判断）；提前占点 `prepare_fortress_value=0`（关：fortress 轮 pf03/06/12/24 全负，objective 0.7971→0.7889、deaths 83→87-92）。
- 治疗：`hp < healing_below_hp(40)` 且治疗效果未覆盖 → `min(100−hp, amount×effect_ticks)×0.2/(distance+1)`。

---

## 5. 完整参数表（match_config.hpp，冠军构建 eb321df）

### 5.1 采集与竞速
| 参数 | 值 | 状态 |
|---|---|---|
| stale_resource_decay | 0.01 | 开 |
| stale_grace_ticks | 0 | 关 |
| resource_mission_bonus | 5.0 | 开 |
| reach_mission_value | 8.0 | 开（8/(d+1)） |
| opponent_contest_cost | 1.0 | 开 |
| opponent_pressure_cost | 0.25 | 开 |
| opponent_claim_discount | 0.5 | 开 |
| explore_toward_resource_value | 0.5 | 开 |
| explore_probe_mission_bonus_scale | 1.0 | 旧行为 |
| stage2_race_gate | false | 关 |
| race_reach_holdoff | 0.0 | 关 |
| resource_plan_depth | 4 | 开 |
| resource_beam_width | 5 | 开 |
| resource_candidate_limit | 8 | 开 |
| resource_plan_budget_ms | 10 | 开 |
| resource_refinement | true | 开 |
| resource_refinement_trials | 12 | 开 |

### 5.2 战斗
| 参数 | 值 | 状态 |
|---|---|---|
| post_cap_combat_weight | 0.02 | **开**（train+heldout 晋升） |
| stage2_pie_attack_discount | 0.0 | 关 |
| stage2_assassin_value | 0.0 | 关 |
| low_hp_attack_discount | 1.0 | 关（1.0=旧） |
| worst_case_survival | false | 关 |
| defend_stall_break_ticks | 0 | 关 |
| tactical_search | false | 关（beam 层在代码中完整实现） |
| tactical_risk | 0.6 | 随战术层关 |
| tactical_hp_value | 0.015 | 同上 |
| tactical_death_cost | 0.0 | 同上 |
| tactical_future_discount | 0.65 | 同上 |
| tactical_goal_weight | 0.65 | 同上 |

### 5.3 探索
| 参数 | 值 | 状态 |
|---|---|---|
| frontier_value | 0.02 | 开(stage2) |
| stage1_frontier_value | 0.02 | 开(stage1) |
| explore_tour_value | 0.03 | 开(stage1) |
| stage1_flood_value | 0.0 | 关 |
| stage1_ring_value | 0.0 | 关 |
| mission_explore_value | 0.0 | 关 |
| explore_component_value | 0 | 关（永久） |
| stage2_explore_gate_tick | 0 | 关 |
| stage2_mission_pull_stale_ticks | 0 | 关 |
| stage2_shadow_value | 0.0 | 关 |

### 5.4 导航·脱困·堡垒
| 参数 | 值 | 状态 |
|---|---|---|
| hazard_lead_ticks | 2 | 开 |
| loop_recovery | true | 开 |
| loop_window_ticks | 12 | 开 |
| recovery_ticks | 12 | 开 |
| stalled_goal_cooldown_ticks | 24 | 开 |
| collision_replan | true | 开 |
| healing_below_hp | 40.0 | 开 |
| fortress_hold_value | 20.0 | 开 |
| fortress_capture_value | 12.0 | 开 |
| prepare_fortress_value | 0.0 | 关 |
| goal_retention_bonus | 0.0 | 关 |

### 5.5 AI 与通信（赛前固定配置）
| 参数 | 值 |
|---|---|
| ai_url | 练习 `http://127.0.0.1:8080/v1/chat/completions`；正式赛官方网关（必须完整 /chat/completions 端点） |
| ai_token | 练习 `practice-A`；正式赛**席位令牌**（Bearer，绝不提交） |
| ai_model | deepseek-flash |
| ai_max_tokens | 2200（公告示例 512 待 docs/02 定稿） |
| ai_thinking | disabled（顶层明确） |
| ai_json_output | true |
| ai_timeout_ms / ai_connect_timeout_ms | 35000 / 5000 |
| ros_domain_id | 27 |
| stage1_ticks / stage2_ticks | 100 / 500 |
| team / team_name | A / Frank（正式赛按裁判分配改） |

---

## 6. 算法命名表（直接回答"每一步是 beam 还是什么"）

| 步骤 | 算法 | 比赛状态 |
|---|---|---|
| 寻路/可达性（strategy.cpp §4、resource_plans 路线、tactics 尾值距离） | **BFS**（每帧重算，只存首步+距离） | 开 |
| 安全首步避险（safe_first_steps） | **倒推 DP**（8 Tick 视界、≤145 格） | 开 |
| 单资源选择（collect_resource 等） | **贪心 argmax**（utility=收益×新鲜度/(距离+1)） | 开 |
| 资源串规划（collect_resource_chain） | **beam search**（宽 5 深 4 + 局部改进 12 次，10ms 预算） | **开** |
| 巡回（collect_resource_tour / explore_tour） | BFS all-pairs + 近邻构造 + **有界 2-opt**（6 pass）+ 锚点防抖 | 开(stage1) |
| 战斗（§6 ATTACK 搜索） | **贪心 argmax**（四方向×最近目标 + 情境折扣：补刀 60/还手豁免/封顶平局 0.02） | 开 |
| 战斗（tactical_choice 战术层） | **beam search**（宽 5 深 ≤3、5-6 对手情景、均值/最差混合、深度折扣、BFS 尾值） | 已实现，**比赛关** |
| 探索（frontier） | 贪心 argmax（newly_visible/(d+1)，BFS 距离早停） | 开 |
| 探索（explore_component 连通区） | 4 连通**洪泛标号**（flood fill） | 关（永久） |
| 脱困（unstuck） | 元组**字典序 argmax**（视野/风险/访问数/距离/席位去对称） | 开 |
| 事件理解 | **LLM**（deepseek-flash，JSON 模式，后台异步）+ 本地证据校验（效果全量重建） | 开 |
| 对手预测 | 两次连续相同位移的一步猜测（`forecast`），不外推长路线 | 开 |
| 未见任何 | 裁判状态注入/作弊路径/伪随机预测 | 无 |

---

## 7. 与正式赛对接的待办（见 docs/02 与材料清单）
- 材料提交 **2026-10-31 20:00** 截止；正式赛 **2026-11-01**；10 分钟调整窗口（turn_mode 状态机）；decision_type 不登记（与 ChatGPT 一致确认）。
- stage2 每场须 ≥1 次真实 AI 成功调用（本清单 §4.4 的 `model_reply_seen`/HTTP 成功统计即证据口径）。
- `ai_max_tokens` 2200 vs 手册公告示例 512：docs/02 定稿；`team`/`team_name`/`ai_url`/`ai_token` 正式赛前改官方值。
- 候选五参数（38b5d09 构建记录为准，M5 同池对照收批后 docs/53 定稿）与冠军（eb321df）唯一差异在采集/战斗五个杠杆，本清单为冠军口径。
