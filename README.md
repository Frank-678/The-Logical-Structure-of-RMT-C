# RMTC 图灵对决赛 · 项目总览与可审计进度表

本仓库用于**比赛规则整理、算法方案论证、实施和测试证据跟踪**；实际参赛 C++/ROS 2 工程另存放在 [RoboMaster-Turing-Competition-BeyondControl](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl)。这里的勾号只代表**已有对应证据的阶段**，不表示该方案已经提高胜率。

**状态基线：2026-10-28。** 本轮将矩阵扩至R37；新增实现与结果固定于代码提交`a7d2318`（功能头`a23edad`），原版practice未改。 当前正式规则 v1.2，配套最新已取得的通信协议/裁判教程 v1.1。当前选手策略已有代码与部分离线测试，但**完整原版裁判/标准车对战尚未完成**；不能把 HTTP 请求成功等同于本场官方 AI 资格。

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
| R18 | AHC068 高分提交的 Beam/历史插入/序列局部优化比较 | ✅ | — | — | — | [提交 #77562268](https://atcoder.jp/contests/ahc068/submissions/77562268)的网页备份已取得2195行源码，核对Beam、Retro、局部优化与最终合法性检查；未运行原程序，未独立核实实时冠军排名 |
| R19 | 多目标、跨 Tick 的边际收益估值 | ✅ | ◐ | ✅ | ◐ | [规划说明](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/a7d2318fcce432878277686cbb2da65c87ca30fe/PLANNING.md)：资源串用更新后的虚拟R逐次计算封顶收益；任务、死亡和多车联合推演仍未完成 |
| R20 | 目标迟滞与未执行计划的局部重排 | ✅ | ◐ | ✅ | ◐ | [规划说明](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/a7d2318fcce432878277686cbb2da65c87ca30fe/PLANNING.md)：连续Tick的有效目标有10%排序余量；断帧、复活、失败MOVE与危险可打断。已有振荡回归；未实现通用2-opt/计划局部优化 |
| R21 | 小束宽 Beam Search / 滚动规划 | ✅ | ◐ | ✅ | ◐ | [规划说明](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/a7d2318fcce432878277686cbb2da65c87ca30fe/PLANNING.md)：已实现最多3个资源目标、束宽5、候选8、10ms软预算，只执行首步；深度是目标数，不是3Tick；尚非完整攻防动作Beam |
| R22 | 多对手情景预测与收益评估 | ✅ | ◐ | ◐ | ⬜ | 目前仅一步轨迹软惩罚，尚无多情景前瞻 |
| R23 | 完整计分、死亡/争格/风险的配对消融实验 | ✅ | ◐ | ◐ | ◐ | [7例配对轨迹](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/a7d2318fcce432878277686cbb2da65c87ca30fe/tests/results/planning-2026-10-28.json)：同夹具分别链接旧/新版的采集比较已运行；无敌车、事件或AI，完整R/D/M与对手池消融仍未建立 |
| R24 | AHC 置换群共轭和已执行历史操作插入照搬 RMTC | ✅ | — | — | — | **明确拒绝**：RMTC 已结算 Tick 不能回滚 |
| R25 | 赛前封存 Prompt、策略参数、构建 SHA 与现场一致性 | ✅ | ◐ | ◐ | ⬜ | [配置和构建说明](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/strategy/visible-resource-bfs/README.md)；正式赛上场仍待核验 |

| R26 | PacmanAI：手写收益/风险特征与模式切换选读 | ✅ | — | — | — | [README与heuristicTeam.py](https://github.com/jhammarstedt/PacmanAI/blob/2611a267b99c274516f889bba32852df083ad721/src/heuristicTeam.py)；实际获胜后备队是启发式，CNN/DQL训练不足。借鉴风险/记忆，不部署本地训练模型；未运行原游戏 |
| R27 | pacman-mcts-agent-v2：有选择地分配搜索预算 | ✅ | — | — | — | [实际文件myTeam(1).py](https://github.com/neeilnandal/pacman-mcts-agent-v2/blob/4b48e73977bf5313a486acd39b4bccd22c8f1856/myTeam(1).py)；核对UCT与模式切换。默认0.82秒不适合直接放进100/500ms动作窗口；未运行原游戏 |
| R28 | Pacman-Capture-the-Flag：设计与后续改进建议 | ✅ | — | — | — | [README](https://github.com/DXJ3X1/Pacman-Capture-the-Flag/blob/f2ed02de687e63ab4e2fd634fef5526dbb8314e1/README.md)；该仓库提供演示/设计材料，没有选手源码；提高单位步食物收益部分属于Further Improvements，不能当作已实现算法。PPT未读 |
| R29 | Orienteering-Problem：贪心可行性反例 | ✅ | — | ✅ | ✅ | [原函数](https://github.com/MiladNooraei/Orienteering-Problem/blob/d41a5d7e1a9a561b7b3d94b27c683cb8c7bfb51d/Orienteering%20Problem.py)；已固定源码执行函数级反例：预算2时先选不可达高比值点后退出，实得0，另有距离1/得分10的可行路径。仅验收此反例，非完整项目或比赛 |
| R30 | Algorithm-OP-Heuristic-Approaches：8种示例逐项核对 | ✅ | — | ✅ | ✅ | [仓库](https://github.com/aliiimaher/Algorithm-OP-Heuristic-Approaches/blob/44dec64428580615bd50da40a443258180e0b906/README.md)；已读8个脚本。函数级反例确认DP仅按递增编号，预算3时得10而可行重排得20；标为未完成的DFS拒绝了正收益邻点。不能称通用精确DP；未运行整个项目 |
| R31 | op-solver：可行插入、删除与预算恢复选读 | ✅ | — | — | — | [add.c](https://github.com/gkobeaga/op-solver/blob/992a2443dd845c7a6f4952e1f28c51a4297e887b/src/cp/heur/add.c)、[drop.c](https://github.com/gkobeaga/op-solver/blob/992a2443dd845c7a6f4952e1f28c51a4297e887b/src/cp/heur/drop.c)、EA优化及可行性示例；适合作离线参考，静态全图与闭合路线前提不同；尚未集成或运行求解器 |
| R32 | mrtsp_exploration_ros2：未知边界、信息量/路程选读 | ✅ | — | — | — | [README](https://github.com/mertgulerx/mrtsp_exploration_ros2/blob/d9bc18085f49f6aa4396b4009d22ad5255096bf9/README.md)及WFD/成本/排序代码；实际为Python/Jazzy、贪心排序，不能直接称精确TSP或Humble C++包。信息增益已独立适配见R36 |
| R33 | AutoFrontierSearch：Humble边界检测选读 | ✅ | — | — | — | [algolism.py](https://github.com/Nyanziba/AutoFrontierSearch_ros2-humble/blob/8e72eeebddceff5addfde1e3111de203bf917311/src/frontier_exploration/frontier_exploration/algolism.py)；未知邻接空地、近墙过滤与随机选点。RMTC使用自身格图/视野，未搬SLAM、Nav2坐标与随机目标 |
| R34 | CodeCraft_2024：距离缓存、方向持续与预约选读 | ✅ | — | — | — | [quick_view_version](https://github.com/PinkEx/CodeCraft_2024/blob/98d53b453302d2ee33e433fc859f1ab3f8c64818/quick_view_version/functions.h)及main/robot；可参考反向BFS、收益场和队内让行。RMTC对手不承诺让路，未知地图也不等于物流全图；未运行原赛事 |
| R35 | 阶段结束与剩余动作数守卫 | ✅ | ✅ | ✅ | ✅ | [规划说明](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/a7d2318fcce432878277686cbb2da65c87ca30fe/PLANNING.md)：明确100/500动作Tick，最终状态不发布；末步/两阶段窗口核心回归通过。此勾仅验收守卫，不代表实战获胜 |
| R36 | 已知可达观察点的信息增益探索 | ✅ | ✅ | ✅ | ◐ | [规划说明](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/a7d2318fcce432878277686cbb2da65c87ca30fe/PLANNING.md)：按实际视野计算新增未知格/路程，只走已知路径；边界与危险回归通过，局部下一帧覆盖9→12，未有整局覆盖率统计 |
| R37 | 新旧采集策略的同条件夹具 | ✅ | ✅ | ✅ | ◐ | [7例配对轨迹](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/a7d2318fcce432878277686cbb2da65c87ca30fe/tests/results/planning-2026-10-28.json)：7例无受阻MOVE，两步新增R20→30、四步40→50、密集资源200的耗时40→36；迷宫均18步。单次决策最大观测2.28ms，仅一轮样本；不是标准车胜率或完整回调延迟 |

> 本表“验收”必须对应具体范围：例如 R13 的 ✅ 仅表示重复公告回归通过，不表示 AI 模型在所有事件上正确；R14/R15 的 ❌ 是**测试执行失败**而非“算法已输给标准车”。R17/R18/R24及R26–R34的实现栏破折号表示外部研究或拒绝项；具体迁移单列R19–R21、R36。R29/R30的执行/验收只指上述函数反例。

## 下一轮执行优先级

1. **P0：完成完整对局和 AI 时效数据。** 在正常 Ubuntu 22.04 / ROS 2 Humble/DDS 环境获取 A 与标准 B/C/D 的真实回执、R/D/M、得分、死亡、无效动作、模型调用与事件可用时间；不要动裁判原件。
2. **P1：实测新增目标规划。** 迟滞、资源串和信息增益已有代码及局部配对结果；在留出地图、不同席位和标准对手下检查收益与失效条件。
3. **P2：补齐搜索模型，再决定是否扩展。** 现有束搜索只比较资源目标；完整多车攻防、任务、事件情景仍未完成。继续只执行首步，下一Tick依据裁判回执重算。
4. **P3：多情景与消融。** 测试改动是否真实提升、什么地图/对手下失效；失败可回退基线。
5. **P4：赛前封存与验收。** 确认版本、配置、协议、运行入口和规则权限，保持可追溯。

## AI / 人工协作：怎样更新这张表

每次处理一个稳定 ID（例如 R21），先核对当前仓库/选手工程的实际 HEAD、规则版本和已有测试证据。**当前这套研究/追踪工作仅使用已经存在的目标分支，不擅自创建分支。**只有在**对应阶段确实完成**时改成 ✅；尚未做就保留 ⬜，部分完成写 ◐，出错写 ❌ + 可重现信息，受环境阻碍写 ⛔ + 具体环境/错误。任何改动应记录日期、提交 SHA、测试命令、输入场景、预期与实际结果。**不许基于文档、旧回放或别人的 mock 记录填“实战通过”。**

把研究与参赛代码分开。赛中遵守正式的封存、统一 AI 接口及公开感知权限，不允许读取观赛全图、内部 ROS 或未经许可模型。本 README 仅含适合总览的状态，不包含内部准备材料的入口和私密记录。

---

## 原有协作约定（历史保留；新任务以当前明确授权和上面的追踪规范为准）

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
