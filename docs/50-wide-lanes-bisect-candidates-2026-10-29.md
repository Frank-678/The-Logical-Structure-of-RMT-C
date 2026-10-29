# docs/50 · wide_lanes 代码层二分候选静态预筛 · 2026-10-29

**状态**：静态预筛（联赛期间只读 git 分析；逐提交 tick-10 重放二分在联赛后执行）。
**关联**：docs/46 §7（wide_lanes 残差裁定：参数不可达，65c8714→当前代码层）、review.md CG-R-20261029-LEAGUE192 第 3 条（已向 ChatGPT 要二分起点）。
**范围**：65c87145ae3b15572c3b1674181a74677fe86770（R2 对照 old 侧）.. 3a37703（当前 iterate-arena 顶）：共 56 个提交，其中 18 个触及 strategy.cpp/events.cpp/tactics.cpp。

## 1. 默认行为过滤器（静态）

wide_lanes 差分必来自**默认值非中性**或**直接改公式**的提交；默认关（=旧行为）的杠杆按协议可低优先。

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

## 3. 二分执行口径（联赛后）

1. 固定 tick-10 前同一公开输入/记忆前缀与完整参数（65c8714 与当前各建一次基线）。
2. 逐提交在 65c8714 基线上 `git checkout <sha> -- src/rmtc_bot/...` 替换候选分支（或反向：当前树上 revert 该提交），
   用同一短现场（wide_lanes-economy / wide_lanes-pressure，docs/46 第八轮同款）重放比较：
   候选动作、路径成本、任务拉拽、探针、目标保留的评分分项（strategy.cpp 评分分项逐项打印）。
3. 找到"替换后 wide_lanes 分恢复 old 侧"的最小提交集 → 再评估该行为是否应参数化还是保持当前。
4. 比较驱动迁 tools/（承诺条款），报告与日志归档 log 分支。
5. 若 ChatGPT 提供其建议的 5 个候选提交号，与本表合并排序后执行。

## 4. 静态阶段结论

- frontier 家族（48bdca8 + 869621b）默认 0.02 为 wide_lanes 分差**最可疑根因**；
  但 0.02 在 snake/sparse 上已证实无副作用（docs/46 第七/八轮 6/6 现场不变），故嫌疑集中在"宽走廊"这一特定结构。
- 不排除 d795e16 的 C1–C5 修复；其 pcc 分量在 wide_lanes 两格（economy/pressure）D 距 500 封顶较远，影响应小于 frontier。
- 全部结论以逐提交重放为准，本表只是预筛。
