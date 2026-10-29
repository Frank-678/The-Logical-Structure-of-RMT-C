# docs/50 · wide_lanes 代码层二分候选静态预筛 · 2026-10-29

**状态**：静态预筛（联赛期间只读 git 分析；逐提交 tick-10 重放二分在联赛后执行）。
**关联**：docs/46 §7（wide_lanes 残差裁定：参数不可达，65c8714→当前代码层）、review.md CG-R-20261029-LEAGUE192 第 3 条（已向 ChatGPT 要二分起点）。
**范围**：65c87145ae3b15572c3b1674181a74677fe86770（R2 对照 old 侧）.. 3a37703（当前 iterate-arena 顶）：共 56 个提交，其中 18 个触及 strategy.cpp/events.cpp/tactics.cpp。

## 1. 默认行为过滤器（静态，2026-10-30 依 deepseek-causal-audit 修正）

wide_lanes 差分必来自**默认值非中性**或**直接改公式**的提交；默认关（=旧行为）的杠杆按协议可低优先。

**重要修正（ChatGPT 已实读旧侧 blob）**：旧 65c8714 的配置 blob `ee92561e…` 中 frontier_value
**同为 0.02**；旧策略 blob `60a68135…` 877–891 行把 frontier 放在 `best_utility<0` 条件内。
因此“frontier 默认 0.02 非中性”**不能单独解释新旧差异**——同一个 0.02 从“空闲才启用”变成
“随时参与竞争”，差分在**门控条件与候选集合**，不在权重数值。优先干预“候选在什么条件下参赛、
哪些格子被纳入、目标评分表达式”，再单独调权重。同理 `mission_explore_value=0` 不是整个任务拉拽
关闭（表达式仍留独立的 1/(到任务距离+1) 项），`explore_toward_resource_value=0` 也不是旧版全部
探索语义——不要把“权重归零”当成“机制消融”。

当前 match_config.hpp 默认值核查结果：
- **frontier_value = 0.02（阶段二，激活）**、**stage1_frontier_value = 0.02（阶段一，激活）** ← 默认非中性
- **post_cap_combat_weight = 0.02（已晋升，激活）** ← 默认非中性
- stage1_flood_value / stage1_ring_value / stage2_shadow_value / race_reach_holdoff /
  stage2_explore_gate_tick / prepare_fortress_value = 0（关）；low_hp_attack_discount = 1.0、
  explore_probe_mission_bonus_scale = 1.0（中性）；stage2_mission_pull_stale_ticks = 0（饥饿拉拽关）。

## 2. 候选排序（静态证据）

| 序 | 提交 | 改动 | 默认状态 | 依据 |
|---|---|---|---|---|
| 1 | **48bdca8**（frontier 扫图参与竞争） | strategy.cpp **+272** 行 | **0.02 激活** | 最大单次改动；宽走廊地形正是"扫图 vs 任务/交战公平竞争"影响最大的结构 |
| 2 | **869621b**（frontier 拆分） | strategy.cpp +10，参数拆 stage1/2 | 两段均 **0.02** | 阶段一权重独立化改变旧行为 |
| 3 | **d795e16**（C1/C3/C4/C5 修复 + pcc 0.02 晋升） | strategy.cpp 44 行 + 默认 pcc | **0.02 激活** | 修复本身改公式；pcc 影响 D≥500 封顶后估值 |
| 4 | 7838f77 / 2206221（flood + race gate） | strategy.cpp 74/11 行 | 0 关 | 代码重构面大，杠杆 0 不保证逐位等价 |
| 5 | d8eda2c（post-pie gate）、c1c6b60（ring）、e83b09d（coverage-max） | 11/14/46 行 | 0 关 | 同左；46 行重构的 e83b09d 略优先 |
| 6 | 07e4b5f（堡垒预告，pf 杠杆 0 关）、c7fe48e（lowhp 1.0 中性）、3a37703（probe scale 1.0 中性）、eb321df（holdoff 0）、其余 arena 轮 | 小 | 中性/关 | 低概率 |

## 2b. 上游五提交起点（deepseek-causal-audit-2026-10-29，全 SHA，先排除后 hunk 干预）

ChatGPT 已逐 patch 读取下列提交；优先级不是等概率，后四项先用实际参数/触发条件排除：

| 完整提交 | 需要检查什么 | 在当前默认值下的优先级 |
|---|---|---|
| `48bdca84164456f654e849277ca8ed329ce353d7` | frontier 参与竞争的门控、未知邻居边界候选集合、资源探针、任务评分 hunk（同时改变五项语义） | 最高，先做 hunk 级干预 |
| `d795e161c56e6ad939e279a9a173afa4cc733be5` | 封顶后战斗估值、预测生存、资源记忆宽限 | 先查 tick10 的 D 及触发 |
| `7838f77c714c4fba6c7e6f2126400b1563b9d508` | stage2_race_gate 对任务/主动攻击的门控 | 开关 false 时应是无作用对照，先排除 |
| `6fbf5ea8203dc1799a435e5a9b15ccfb98ef7e96` | 饥饿任务拉拽及 max 表达式 | 阈值 0 且 mev 非负时应退化为原表达式 |
| `e83b09dd1d5dcda92ca8782a6a3b58b52b793d12` | frontier 连通区加分与提前结束上界 | component=0 时应退化为原公式，先排除 |

`3a377039…`（probe 缩放默认乘 1）本身不应改变行为；869621b 的阶段一拆权重不能只凭“阶段一改变”
解释阶段二，先核对 stage 与实际参数逐项证明影响可达。

## 3. 二分执行口径（联赛后）

1. 固定 tick-10 前同一公开输入/记忆前缀与完整参数（65c8714 与当前各建一次基线）。
2. **完整提交比较用独立 worktree/源码快照**（build_seat_variants 式冻结副本），不用
   `git checkout <sha> -- 单文件`——那会把某时点整文件换入另一版本，不等于只消融该提交，
   还可能混入不匹配的头文件/参数布局；编译失败或接口错配也不能反推算法好坏。
   逐提交在 65c8714 基线上用同一短现场（wide_lanes-economy / wide_lanes-pressure，
   docs/46 第八轮同款）重放比较：候选动作、路径成本、任务拉拽、探针、目标保留的评分分项
   （strategy.cpp 评分分项逐项打印）。
2b. **每候选记录 tick10 逐项**：kind、target、first_step、距离、各评分项、目标保留加成、
   拒绝原因、平手顺序及最终选择——区分“候选没生成”和“生成了但输分”；只记最终动作不够。
2c. hunk 级因果干预在固定基线上只改一个可解释分支，保存构建身份（params/cfg/二进制摘要）；
   验证该 hunk 替换是否恢复第一次资源/任务机会，再用会重新决策的同一对手跑完整片段。
   同一提交可能引入多项变化，git bisect 分不开它们；也不假定整局得分对提交单调。
3. 找到"替换后 wide_lanes 分恢复 old 侧"的最小提交集 → 再评估该行为是否应参数化还是保持当前。
4. 比较驱动迁 tools/（承诺条款），报告与日志归档 log 分支。
5. 若 ChatGPT 提供其建议的 5 个候选提交号，与本表合并排序后执行。

## 4. 静态阶段结论（2026-10-30 修正）

- **差分嫌疑从“权重 0.02”改为“frontier 门控与候选集合”**：旧侧同为 0.02 但只在 best_utility<0
  时才探索；48bdca8 让其参与任务/战斗竞争并改变边界候选（§1 修正、§2b 最高优先）。
  0.02 在 snake/sparse 六现场无副作用不能外推“该变量无副作用”——变量在那六个现场根本没改变。
- 不排除 d795e16 的 C1–C5 修复；其 pcc 分量在 wide_lanes 两格（economy/pressure）D 距 500 封顶较远，影响应小于 frontier。
- 首个动作分叉只是定位入口，不是失分因果；必须再验证 hunk 替换是否恢复首次资源/任务机会。
- 全部结论以逐提交重放为准，本表只是预筛。

## 5. 上游审查合并记录

- 2026-10-30 依 ChatGPT `deepseek-causal-audit-2026-10-29.md`（ANALYSIS 3a588dc/bbfebf0）与本表合并：
  五提交全 SHA、排除优先顺序、hunk 干预方法、逐候选记录口径、独立快照二分（§1/§2b/§3 已并入）。
- 二分驱动迁 tools/ 与日志归档 log 分支的承诺不变；联赛后启动。
