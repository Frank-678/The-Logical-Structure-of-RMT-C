# 29 · ChatGPT review 修复与三杠杆竞技场评估（2026-10-29）

来源：代码分支 review.md 的 C1–C5 与本文档对应条目 T1–T6（CG-C/T-20261029-01）；修复提交 `d795e16`、review 回复 `fa97cd3`（strategy/iterate-arena-2026-10-28）；日志勘误 `e92ed36`、归档补全 `f128812`（log 分支）。

结论先写：C1/C3/C4/C5 全部接受并修复；C2 接受注释修正、杠杆保持关闭。三个新杠杆经 train 场景评估后，**post_cap_combat_weight=0.02 晋升进正式配置**（heldout 一次性验证通过），stale_grace_ticks 与 worst_case_survival 保持默认关。

---

## 1. 三个新杠杆的设计与默认值

全部以"冠军逐位一致"为默认（0/false），晋升必须经过 train 评估与 heldout 一次性验证：

| 杠杆 | 类型 | 默认 | 修复对象 | 训练场景评估 |
| --- | --- | --- | --- | --- |
| stale_grace_ticks | int | 0 | 资源离开视野后前 N 个 Tick 不衰减（未观测≠消失），压单 Tick 视野缩小引起的目标震荡（C3 的 persistent_goal 失败根因） | **决策零变化**（1/2/3 与 0 在 24 场逐位一致） |
| worst_case_survival | bool | false | 生存判定按全敌攻击最坏情形，防御预测不再充当伤害上界的确定排除项（C1） | 保守代价大于收益（见 §3） |
| post_cap_combat_weight | double | 0.0→**0.02 晋升** | D≥500 封顶后增量 D 的平局估值权重；同分同任务同 R 按 D 决胜（C5，f728 战例 D556<1160 rank3） | objective 0.789→0.806（见 §4） |

实现位置：`strategy.cpp`（incoming_worst 双口径、grace 新鲜度、两处 post-cap 估值）、`strategy_parameters.hpp`（三字段+校验）、`match_config.hpp`（三 constexpr 条目+证据注释）、`tests/arena_main.cpp`（PARAMETER 注入与 --dump-competition）。

---

## 2. C3/C4 测试与评测修复

- **C3 测试注入**：`persistent_goal` 显式 `stale_grace_ticks=1`；`announced_fortress` 与 `announcement_benchmark` 显式 `prepare_fortress_value=12.0`；off-state 断言（grace=0 仍按衰减差换向；公告参数 0 时与无公告开局动作逐位一致）。
- **C4 评测口径**：arena 新增 `--dump-competition` 导出编译进二进制的 `competition()` 全部 46 字段；`run_arena.py` 非调参入口不再读过期 selected-parameters.json（4/4/0.1/0.25 与当前 5/8/0/0 不一致，曾静默冒充当前配置）；每份报告记录 `competition_parameters` 与 `binary_sha256`，自证"测的就是当前比赛程序"。
- **顺带修复**：`frontier_exploration` 的 stage1 断言在 HEAD 即红——explore_tour 晋升后本夹具左右对称（各 3 格新视野）平手取 left（reason=explore_tour），旧断言要求 right。断言改为避开只揭 2 格的 up，注释说明不变式。
- **验证**：`bash tests/run.sh` 退出码 0（startup → mock HTTP → 原版 practice 转发 → arena rules 18 maps 全过）；`announcement_benchmark` 退出码 0，delay 0/8/20 → 获得无双 tick 8/14/-1、攻击窗口 11/5/0（delay=20 公告到达时堡垒已结束，不追死堡垒）。

---

## 3. worst_case_survival：评估后保持关闭

train 场景（24 场/12 stage2），tests/eval_levers.py：

| 指标 | 默认 false | worst_case=true |
| --- | ---: | ---: |
| objective | 0.7891 | 0.7577 |
| stage2 score | 41.25 | 37.57 |
| stage2 R / D | 60.0 / 673.3 | 58.3 / 513.8 |
| deaths（全场） | 56 | 43 |
| blocked | 192 | 132 |

保守生存显著减少死亡与 blocked，但 stage2 得分与 objective 全面下滑：把防御预测当确定排除项的乐观口径，在陪练对手分布下反而更赚分。正式默认保持 false，机制与双口径计算保留（注释明确"是对陪练策略的推测，不是对方本Tick已提交的动作"），等待真实对局中低血量互杀的再评估窗口。

---

## 4. post_cap_combat_weight：晋升 0.02

### 4.1 train 评估（0.02/0.05/0.1 三档）

| 指标 | 0（旧行为） | 0.02 | 0.05 | 0.1 |
| --- | ---: | ---: | ---: | ---: |
| objective | 0.7891 | **0.8056** | 0.8055 | 0.8055 |
| stage2 D_mean | 673.3 | 985.8 | 1011.7 | 1011.7 |
| stage2 win_share | 0.250 | **0.417** | 0.417 | 0.417 |
| deaths（全场） | 56 | 72 | 74 | 74 |
| stage1 score | 33.33 | 33.33 | 33.33 | 33.33 |
| invalid | 0 | 0 | 0 | 0 |

逐局明细（stage2 train，base → pc002，w=win_share、D、d=deaths、rk=rank）：

| scene | base | pc002 | pc005 |
| --- | --- | --- | --- |
| open s101 | w0 D 625 rk3 | w0 D 845 rk3 | w0 D 845 rk3 |
| open s307 | w1 D 720 rk1 | w1 D1130 rk1 | w1 D1130 rk1 |
| maze s148 | w0 D 500 rk3 | w0 D 500 rk3 | w0 D 500 rk3 |
| maze s354 | w1 D 540 rk1 | w1 D 640 rk1 | w1 D 640 rk1 |
| rooms s195 | w0 D 600 rk3 | w0 D1555 rk3 | w0 D1555 rk3 |
| **rooms s401** | **w0 D 600 rk2** | **w1 D 810 rk1** | w1 D 810 rk1 |
| lanes s242 | w0 D 600 rk3 | w0 D 650 rk2 | w0 D 960 rk2 |
| lanes s448 | w0 D 790 rk2 | w0 D1310 rk2 | w0 D1310 rk2 |
| clusters s289 | w1 D 630 rk1 | w1 D1100 rk1 | w1 D1100 rk1 |
| clusters s495 | w0 D 800 rk3 | w0 D 940 rk3 | w0 D 940 rk3 |
| crossroads s336 | w0 D 520 rk2 | w0 D 960 rk2 | w0 D 960 rk2 |
| **crossroads s542** | **w0 D1155 rk2** | **w1 D1390 rk1** | w1 D1390 rk1 |

增益来源清晰：rooms-s401 与 crossroads-s542 两场由 rk2 翻 rk1，正是 win_share 0.25→0.417 的全部来源；0.05/0.1 与 0.02 翻盘一致但战斗更多（deaths 74 vs 72），故取最小生效点 0.02。代价：deaths 4.67→6.0 场（train stage2），已知代价记录在 match_config 注释。

### 4.2 heldout 一次性验证（选择后唯一一次，vs 冻结 baseline）

`arena-postcap-heldout-2026-10-29.json`，30 场：

| 指标 | baseline（冻结） | selected（含 0.02） |
| --- | ---: | ---: |
| objective | 0.7710 | **0.8299** |
| stage2 score | 40.78 | 43.88 |
| stage2 R / D | 61.3 / 737.0 | 69.6 / 887.4 |
| stage2 win_share | 0.375 | 0.458 |
| stage1 score | 32.33 | 32.67 |
| invalid | 0 | 0 |

消融同轮确认：explore_tour 对 stage1 正贡献（无 tour 时 stage1 32.0）；collision_replan 正贡献（0.8291 vs 0.8299）；tactical_search/resource_refinement 在本轮场景中性。结论：晋升成立，post_cap_combat_weight=0.02 进入正式配置。

### 4.3 真实对局风险标注

train/heldout 对手是竞技场风格模型；真实对局中多打一枪的收益与多死一次（重生位移）的代价分布不同。下一轮批量实战将把 A 席位 deaths、D 与平局次数作为对照指标，若真实局 deaths 显著上升而无平局翻盘，回退 0。

---

## 5. 归档与后续

- 实验报告（代码仓 tests/results/，gitignore 不提交）：`levers-grace/survival/postcap-2026-10-29.json`、`arena-postcap-heldout-2026-10-29.json`；评估入口 `tests/eval_levers.py` 随代码提交。
- 批量实战变体 4-7 重跑已归档 log 分支（f128812）：A 4/4 胜、0 invalid（50.0/47.5/47.5/47.5；变体 5 与 D 同 47.5 靠 D 1070>945 决胜）。
- 下一轮：新二进制（含 post-cap 0.02）跑多图多对手批量，轮换检测；低血量预测失败、资源争抢时间线、公告窗口按 T5 排序排查。
