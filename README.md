# RMTC 图灵对决赛 · 项目总览与可审计进度表

本仓库用于**比赛规则整理、算法方案论证、实施和测试证据跟踪**；实际参赛 C++/ROS 2 工程另存放在 [RoboMaster-Turing-Competition-BeyondControl](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl)。这里的勾号只代表**已有对应证据的阶段**，不表示该方案已经提高胜率。

**状态基线：2026-10-28。** 当前正式规则 v1.2，配套最新已取得的通信协议/裁判教程 v1.1。当前选手策略已有代码与部分离线测试，但**完整原版裁判/标准车对战尚未完成**；不能把 HTTP 请求成功等同于本场官方 AI 资格。

## 如何打勾：四道独立检查

| 图例 | 含义 | 何时可以使用 |
| --- | --- | --- |
| ✅ | 已完成且可核查 | 对应阶段有规则/源码定位、提交 SHA、测试输出或裁判结果 |
| ◐ | 部分完成/只验证了较小范围 | 例如仅固定 HTTP 联调、仅实现一步预测 |
| ⬜ | 尚未完成或没有证据 | 不能因“已有想法/代码似乎存在”自动打勾 |
| ⛔ | 被外部条件阻塞 | 写清阻塞日志、环境和下一步 |
| ❌ | 确认执行失败 | 有可复现的错误，而不是尚未测试 |
| — | 明确拒绝/不适用 | 比如不合法或不符合赛制的移植方法 |

**审查**：已核对规则/外部研究/代码，并写明适用边界。**实现**：在可定位的参赛代码中完成。**执行**：实际运行了相应测试，保留日志。**验收**：运行结果证实**该行声称的具体目标**（例如离线回归通过或完整比赛获胜），不得跨范围扩大结论。每行四列分别更新；一个 ✅ 不能覆盖其他三列。

## 核心研究、开发和验证矩阵

| ID | 关键想法/技术点 | 审查 | 实现 | 执行 | 验收 | 证据及下一步 |
| --- | --- | :---: | :---: | :---: | :---: | --- |
| R01 | 正式规则 v1.2、攻击先于移动、任务和评分边界 | ✅ | ◐ | ◐ | ◐ | [规则状态/实现说明](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/strategy/visible-resource-bfs/STATE_MACHINE.md)；已有条款映射和核心回归，仍需原版对局 |
| R02 | 本队 ROS 2 感知与动作、QoS、场次/Tick 缓存 | ✅ | ✅ | ◐ | ⛔ | [bot.cpp](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/strategy/visible-resource-bfs/src/rmtc_bot/src/bot.cpp)；真实 DDS 开局受网卡枚举权限阻塞 |
| R03 | 地图局部感知、历史记忆、未知格与真实坐标区分 | ✅ | ✅ | ✅ | ◐ | [策略源码](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/strategy/visible-resource-bfs/src/rmtc_bot/src/strategy.cpp)；有局部回归，未证实实战最优 |
| R04 | 已知地图 BFS 资源寻路与合法未知格试探 | ✅ | ✅ | ✅ | ◐ | 同上；尚需真实陪练的收集效率/撞墙率数据 |
| R05 | 未来 8 Tick 安全接续动态规划 | ✅ | ✅ | ✅ | ◐ | [状态机](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/strategy/visible-resource-bfs/STATE_MACHINE.md)；仅对有限已知格有效 |
| R06 | 攻击/防御/事件时序与八类事件状态 | ✅ | ◐ | ◐ | ⛔ | [既有测试说明](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/strategy/visible-resource-bfs/DEV.md)；无法把部分回归扩展为全事件对局验收 |
| R07 | 官方计分边际函数、R/D 封顶与死亡扣 D | ✅ | ✅ | ✅ | ◐ | [scoring.hpp](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/strategy/visible-resource-bfs/src/rmtc_bot/include/rmtc_bot/scoring.hpp)；多人情景待整局核对 |
| R08 | 堡垒动态区域、驻留、增益兑现 | ✅ | ◐ | ◐ | ⛔ | 规则 v1.2 说明及代码；需同场不同公告区域和占点回执 |
| R09 | 辣椒入点、爆炸/分裂提前避险 | ✅ | ◐ | ◐ | ⛔ | 已有对应处理与测试设计；完整多车/多事件结算未验收 |
| R10 | 对手连续轨迹的一步预测（只作软惩罚） | ✅ | ✅ | ✅ | ◐ | [状态机和回归记录](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/strategy/visible-resource-bfs/STATE_MACHINE.md)；没有经对手池校准准确率 |
| R11 | LLM 公告理解与本地每 Tick 动作决策分离 | ✅ | ✅ | ✅ | ◐ | [真实链路记录](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/strategy/visible-resource-bfs/REAL_TEST.md)；HTTP 成功不等于正式资格 |
| R12 | 真实 DeepSeek 上游及事件结构化解析 | ✅ | ✅ | ✅ | ◐ | 同上：两次 HTTP 200，4652ms/5977ms，解释正确但短预告有时效问题 |
| R13 | 累积公告重复膨胀修复 | ✅ | ✅ | ✅ | ✅ | [REAL_TEST.md](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/strategy/visible-resource-bfs/REAL_TEST.md)：该具体回归复现后修复并复测通过 |
| R14 | 正常 Humble/DDS 环境下的原版参考车验证 | ✅ | — | ❌ | ⛔ | [真实测试记录](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/strategy/visible-resource-bfs/REAL_TEST.md)：启动失败，原因是接口权限；须在目标环境重跑 |
| R15 | A 对标准 B/C/D 的完整对局与真实得分 | ✅ | ◐ | ❌ | ⛔ | 同上：未成功开局；**暂无当前策略胜率或得分** |
| R16 | 每 Tick 动作真实回执、不同场次和同 Tick 幂等验证 | ✅ | ✅ | ◐ | ◐ | [代码导读](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/strategy/visible-resource-bfs/CODE_GUIDE.md)；还需目标环境回执串联 |
| R17 | AHC068 自身提交的势函数 + BFS 逆层剥离分析 | ✅ | — | — | — | [用户提交 #77563950](https://atcoder.jp/contests/ahc068/submissions/77563950)；仅外部算法研究 |
| R18 | AHC068 高分提交的 Beam/历史插入/序列局部优化比较 | ✅ | — | — | — | [外部提交 #77562268](https://atcoder.jp/contests/ahc068/submissions/77562268)；此前源码审阅，不能当 RMTC 已实现 |
| R19 | 将全局势函数改为多目标、跨 Tick 的边际收益估值 | ✅ | ⬜ | ⬜ | ⬜ | 研究结论已形成；优先 P1，在受控测试中评价后续目标 |
| R20 | 目标迟滞与未执行计划的局部重排 | ✅ | ⬜ | ⬜ | ⬜ | 只改变未来路线，危险发生必须可立即打断 |
| R21 | 小束宽 Beam Search / 滚动规划 | ✅ | ⬜ | ⬜ | ⬜ | 待测：深度 H=3、束宽 B=5 为实验起点，不是结论 |
| R22 | 多对手情景预测与收益评估 | ✅ | ◐ | ◐ | ⬜ | 目前仅一步轨迹软惩罚，尚无多情景前瞻 |
| R23 | 完整计分、死亡/争格/风险的配对消融实验 | ✅ | ⬜ | ⬜ | ⬜ | 保持地图、对手池、席位、随机条件可比，不只看平均总分 |
| R24 | AHC 置换群共轭和已执行历史操作插入照搬 RMTC | ✅ | — | — | — | **明确拒绝**：RMTC 已结算 Tick 不能回滚 |
| R25 | 赛前封存 Prompt、策略参数、构建 SHA 与现场一致性 | ✅ | ◐ | ◐ | ⬜ | [配置和构建说明](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/strategy/visible-resource-bfs/README.md)；正式赛上场仍待核验 |

> 本表“验收”必须对应具体范围：例如 R13 的 ✅ 仅表示重复公告回归通过，不表示 AI 模型在所有事件上正确；R14/R15 的 ❌ 是**测试执行失败**而非“算法已输给标准车”。R17/R18/R24 的破折号表示研究或拒绝项，不应安排实现。

## 下一轮执行优先级

1. **P0：完成完整对局和 AI 时效数据。** 在正常 Ubuntu 22.04 / ROS 2 Humble/DDS 环境获取 A 与标准 B/C/D 的真实回执、R/D/M、得分、死亡、无效动作、模型调用与事件可用时间；不要动裁判原件。
2. **P1：优化已经存在的目标评价。** 在保留当前安全守卫和行动回退前提下，加入目标迟滞及后续位置/资源的可兑现价值。
3. **P2：再做小规模滚动 Beam Search。** 每个 Tick 只执行首动作，下一 Tick 依据真实感知重算；预测值不得当作裁判真值。
4. **P3：多情景与消融。** 测试改动是否真实提升、什么地图/对手下失效；失败可回退基线。
5. **P4：赛前封存与验收。** 确认版本、配置、协议、运行入口和规则权限，保持可追溯。

## AI / 人工协作：怎样更新这张表

每次处理一个稳定 ID（例如 R21），先核对当前仓库/选手工程的实际 HEAD、规则版本和已有测试证据。只有在**对应阶段确实完成**时改成 ✅；尚未做就保留 ⬜，部分完成写 ◐，出错写 ❌ + 可重现信息，受环境阻碍写 ⛔ + 具体环境/错误。任何改动应记录日期、提交 SHA、测试命令、输入场景、预期与实际结果。**不许基于文档、旧回放或别人的 mock 记录填“实战通过”。**

把研究与参赛代码分开。赛中遵守正式的封存、统一 AI 接口及公开感知权限，不允许读取观赛全图、内部 ROS 或未经许可模型。本 README 仅含适合总览的状态，不包含内部准备材料的入口和私密记录。

---

## 原有协作约定（保留）

协作规范

使用 AI 辅助开发

使用 AI 生成或修改的代码，应先提交到非 "main" 分支，再通过 Pull Request（PR）合并到 "main"。

根据改动规模选择合并方式：

- 较大的功能改动：使用 Create a merge commit，保留完整的提交历史。
- 较小的功能改动：优先使用 Rebase and merge；若无法使用，再考虑 Squash and merge。

独立开发

自行编写代码时，按改动的确定程度处理：

- 方案尚未确定或效果有待验证：无论改动大小，都应先提交到非 "main" 分支，验证后再通过 PR 合并。
- 内容明确且已验证的补丁：可以直接提交到 "main"。

edit:

我的想法是代码提交到另一个仓库里。这个仓库就可以方便我们的交流。

怎么讨论？对ai的，让他们新建branch分析把结果记录到新建的branch，不提交pr；对人，可以用discussion讨论，交流，或者对ai的内容评论。QQ也可以。

毕竟还是不把这个提交给学长，所以就畅所欲言。最后提交的是只有代码的那个仓库，或者你学一学docker提交容器。

