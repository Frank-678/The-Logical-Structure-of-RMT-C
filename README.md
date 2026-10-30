# RMTC 图灵对决赛 · 项目总览与可审计进度表

本仓库用于**比赛规则整理、算法方案论证、实施和测试证据跟踪**；实际参赛 C++/ROS 2 工程另存放在 [RoboMaster-Turing-Competition-BeyondControl](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl)。这里的勾号只代表**已有对应证据的阶段**，不表示该方案已经提高胜率。

**状态基线：2026-10-29。** 矩阵扩至R49；代码固定`b27397f788b9ce0c950eece0b8ef296e7e716af8`。规则v1.2、通信协议/教程v1.1；新增自建对手池与两轮参数搜索，失败结果保留。原版practice18文件未改；当前补丁仍无本工具执行的完整原版裁判对标准车验收；用户新增整场日志另按R46核对，真实HTTP与模拟资格分开。

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
| R02 | 本队 ROS 2 感知与动作、QoS、场次/Tick 缓存 | ✅ | ✅ | ✅ | ◐ | [用户本机运行](https://github.com/Frank-678/The-Logical-Structure-of-RMT-C/blob/ANALYSIS/docs/implementation/REAL_TEST.md)：截图场已见26个不同Tick成功移动、执行Tick29；源码SHA未提供，完整对局未验收。当前工具环境DDS仍阻塞 |
| R03 | 地图局部感知、历史记忆、未知格与真实坐标区分 | ✅ | ✅ | ✅ | ◐ | [策略源码](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/strategy/visible-resource-bfs/src/rmtc_bot/src/strategy.cpp)；有局部回归，未证实实战最优 |
| R04 | 已知地图 BFS 资源寻路与合法未知格试探 | ✅ | ✅ | ✅ | ◐ | 同上；尚需真实陪练的收集效率/撞墙率数据 |
| R05 | 未来 8 Tick 安全接续动态规划 | ✅ | ✅ | ✅ | ◐ | [状态机](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/strategy/visible-resource-bfs/STATE_MACHINE.md)；仅对有限已知格有效 |
| R06 | 攻击/防御/事件时序与八类事件状态 | ✅ | ◐ | ✅ | ◐ | [自建规则边界](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/4c7676159be4b35dded9f41a473ca5a2e8530ad6/ARENA.md)通过，含八事件与同时分奖；共享部分规则、未原版差分，不能扩为全部组合/实战验收 |
| R07 | 官方计分边际函数、R/D 封顶与死亡扣 D | ✅ | ✅ | ✅ | ◐ | [scoring.hpp](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/strategy/visible-resource-bfs/src/rmtc_bot/include/rmtc_bot/scoring.hpp)；多人情景待整局核对 |
| R08 | 堡垒动态区域、驻留、增益兑现 | ✅ | ◐ | ✅ | ◐ | [本地裁判边界](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/4c7676159be4b35dded9f41a473ca5a2e8530ad6/tests/arena_test.cpp)覆盖授予时序和跨死亡保留；隐藏敌方进度及原版对局仍待 |
| R09 | 辣椒入点、爆炸/分裂提前避险 | ✅ | ◐ | ✅ | ◐ | [规则模型与局限](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/4c7676159be4b35dded9f41a473ca5a2e8530ad6/ARENA.md)：本地八事件/火线批次与激活顺序通过；罕见组合和独立裁判差分未验收 |
| R10 | 对手连续轨迹的一步预测（只作软惩罚） | ✅ | ✅ | ✅ | ◐ | [状态机和回归记录](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/strategy/visible-resource-bfs/STATE_MACHINE.md)；没有经对手池校准准确率 |
| R11 | LLM 公告理解与本地每 Tick 动作决策分离 | ✅ | ✅ | ✅ | ◐ | [真实链路记录](https://github.com/Frank-678/The-Logical-Structure-of-RMT-C/blob/ANALYSIS/docs/implementation/REAL_TEST.md)；HTTP 成功不等于正式资格 |
| R12 | 真实 DeepSeek 上游及事件结构化解析 | ✅ | ✅ | ✅ | ◐ | [最新真实复测](https://github.com/Frank-678/The-Logical-Structure-of-RMT-C/blob/ANALYSIS/docs/implementation/REAL_TEST.md)：当前C++经原Handler两项200且契约通过，4169/3772ms，上游走工具环境代理；另两次最小探测200但最终JSON未通过。用户本机direct仍读超时，不能跨环境判成功；短预告及时率待测 |
| R13 | 累积公告重复膨胀修复 | ✅ | ✅ | ✅ | ✅ | [REAL_TEST.md](https://github.com/Frank-678/The-Logical-Structure-of-RMT-C/blob/ANALYSIS/docs/implementation/REAL_TEST.md)：该具体回归复现后修复并复测通过 |
| R14 | 正常 Humble/DDS 环境下的原版参考车验证 | ✅ | — | ❌ | ⛔ | [真实测试记录](https://github.com/Frank-678/The-Logical-Structure-of-RMT-C/blob/ANALYSIS/docs/implementation/REAL_TEST.md)：启动失败，原因是接口权限；须在目标环境重跑 |
| R15 | A 对标准 B/C/D 的完整对局与真实得分 | ✅ | ◐ | ◐ | ⛔ | [最新用户记录](https://github.com/Frank-678/The-Logical-Structure-of-RMT-C/blob/ANALYSIS/checks/code-results/user-ai-502-2026-10-28.json)：本机已运行至暂停Tick30，但未完赛且LLM为0；工具环境启动失败另存，仍无有效整局胜率 |
| R16 | 每 Tick 动作真实回执、不同场次和同 Tick 幂等验证 | ✅ | ✅ | ◐ | ◐ | [代码导读](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/strategy/visible-resource-bfs/CODE_GUIDE.md)；还需目标环境回执串联 |
| R17 | AHC068 自身提交的势函数 + BFS 逆层剥离分析 | ✅ | — | — | — | [用户提交 #77563950](https://atcoder.jp/contests/ahc068/submissions/77563950)；仅外部算法研究 |
| R18 | AHC068 高分提交的 Beam/历史插入/序列局部优化比较 | ✅ | — | — | — | [提交 #77562268](https://atcoder.jp/contests/ahc068/submissions/77562268)的网页备份已取得2195行源码，核对Beam、Retro、局部优化与最终合法性检查；未运行原程序，未独立核实实时冠军排名 |
| R19 | 多目标、跨Tick的边际收益估值 | ✅ | ◐ | ✅ | ◐ | [规划](https://github.com/Frank-678/The-Logical-Structure-of-RMT-C/blob/ANALYSIS/docs/implementation/PLANNING.md)：资源虚拟R与可选3Tick R/D/任务/死亡估值；模型有隐藏状态误差，三Tick模块当前关闭 |
| R20 | 目标迟滞与未执行计划的局部重排 | ✅ | ◐ | ✅ | ◐ | [资源重排](https://github.com/Frank-678/The-Logical-Structure-of-RMT-C/blob/ANALYSIS/docs/implementation/PLANNING.md)：旧串重评，12次反转/插入/删除，共享10ms；只资源目标，本批消融同分，不称成绩增益 |
| R21 | 小束宽Beam Search与滚动规划 | ✅ | ◐ | ✅ | ◐ | [规划](https://github.com/Frank-678/The-Logical-Structure-of-RMT-C/blob/ANALYSIS/docs/implementation/PLANNING.md)：比赛资源深度4、束5、候选8；可选三Tick战斗已实现并测试但训练选择关闭；不是完整整场搜索 |
| R22 | 多对手情景预测与收益评估 | ✅ | ◐ | ✅ | ◐ | [tactics](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/4c7676159be4b35dded9f41a473ca5a2e8530ad6/src/rmtc_bot/src/tactics.cpp)：五种情景与可能无双情景，公共续步只发首步；非校准概率/纳什解，当前关闭 |
| R23 | R/D/M、死亡、争格与风险配对消融 | ✅ | ◐ | ✅ | ◐ | [结果](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/4c7676159be4b35dded9f41a473ca5a2e8530ad6/ARENA.md)：910局含训练/消融，首轮失败保留；新留出24对抗+6采集/组，具完整指标，仍是自建裁判与延迟oracle |
| R24 | AHC 置换群共轭和已执行历史操作插入照搬 RMTC | ✅ | — | — | — | **明确拒绝**：RMTC 已结算 Tick 不能回滚 |
| R25 | 赛前封存Prompt、参数与构建一致性 | ✅ | ◐ | ✅ | ◐ | [固定选项](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/4c7676159be4b35dded9f41a473ca5a2e8530ad6/src/rmtc_bot/include/rmtc_bot/match_config.hpp)与[选择记录](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/4c7676159be4b35dded9f41a473ca5a2e8530ad6/tests/results/selected-parameters.json)；训练固定参数、无在线调参；正式赛封存/现场复核仍待 |
| R26 | 20×20 / 24×24 双阶段正式尺寸练习夹具 | ✅ | ✅ | ⬜ | ⬜ | [配置与校验代码](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/tree/strategy/iterate-arena-2026-10-28/practice2)；已经提交独立 practice1/2、原版校验入口；**原版二进制是否接受尚待实测** |
| R27 | 双阶段非官方训练目标 98/100 | ✅ | ◐ | ⬜ | ⬜ | Stage1≥38（R1≥190）+ Stage2=60（R2≥120,D≥500,M=3）是训练目标，**赛事两阶段不合并排名**；需正式尺寸多图配对及 AI 资格证明 |
| R26 | PacmanAI：手写收益/风险特征与模式切换选读 | ✅ | — | — | — | [README与heuristicTeam.py](https://github.com/jhammarstedt/PacmanAI/blob/2611a267b99c274516f889bba32852df083ad721/src/heuristicTeam.py)；实际获胜后备队是启发式，CNN/DQL训练不足。借鉴风险/记忆，不部署本地训练模型；未运行原游戏 |
| R27 | pacman-mcts-agent-v2：有选择地分配搜索预算 | ✅ | — | — | — | [实际文件myTeam(1).py](https://github.com/neeilnandal/pacman-mcts-agent-v2/blob/4b48e73977bf5313a486acd39b4bccd22c8f1856/myTeam(1).py)；核对UCT与模式切换。默认0.82秒不适合直接放进100/500ms动作窗口；未运行原游戏 |
| R28 | Pacman-Capture-the-Flag：设计与后续改进建议 | ✅ | — | — | — | [README](https://github.com/DXJ3X1/Pacman-Capture-the-Flag/blob/f2ed02de687e63ab4e2fd634fef5526dbb8314e1/README.md)；该仓库提供演示/设计材料，没有选手源码；提高单位步食物收益部分属于Further Improvements，不能当作已实现算法。PPT未读 |
| R29 | Orienteering-Problem：贪心可行性反例 | ✅ | — | ✅ | ✅ | [原函数](https://github.com/MiladNooraei/Orienteering-Problem/blob/d41a5d7e1a9a561b7b3d94b27c683cb8c7bfb51d/Orienteering%20Problem.py)；已固定源码执行函数级反例：预算2时先选不可达高比值点后退出，实得0，另有距离1/得分10的可行路径。仅验收此反例，非完整项目或比赛 |
| R30 | Algorithm-OP-Heuristic-Approaches：8种示例逐项核对 | ✅ | — | ✅ | ✅ | [仓库](https://github.com/aliiimaher/Algorithm-OP-Heuristic-Approaches/blob/44dec64428580615bd50da40a443258180e0b906/README.md)；已读8个脚本。函数级反例确认DP仅按递增编号，预算3时得10而可行重排得20；标为未完成的DFS拒绝了正收益邻点。不能称通用精确DP；未运行整个项目 |
| R31 | op-solver：可行插入、删除与预算恢复选读 | ✅ | — | — | — | [add.c](https://github.com/gkobeaga/op-solver/blob/992a2443dd845c7a6f4952e1f28c51a4297e887b/src/cp/heur/add.c)、[drop.c](https://github.com/gkobeaga/op-solver/blob/992a2443dd845c7a6f4952e1f28c51a4297e887b/src/cp/heur/drop.c)、EA优化及可行性示例；适合作离线参考，静态全图与闭合路线前提不同；尚未集成或运行求解器 |
| R32 | mrtsp_exploration_ros2：未知边界、信息量/路程选读 | ✅ | — | — | — | [README](https://github.com/mertgulerx/mrtsp_exploration_ros2/blob/d9bc18085f49f6aa4396b4009d22ad5255096bf9/README.md)及WFD/成本/排序代码；实际为Python/Jazzy、贪心排序，不能直接称精确TSP或Humble C++包。信息增益已独立适配见R36 |
| R33 | AutoFrontierSearch：Humble边界检测选读 | ✅ | — | — | — | [algolism.py](https://github.com/Nyanziba/AutoFrontierSearch_ros2-humble/blob/8e72eeebddceff5addfde1e3111de203bf917311/src/frontier_exploration/frontier_exploration/algolism.py)；未知邻接空地、近墙过滤与随机选点。RMTC使用自身格图/视野，未搬SLAM、Nav2坐标与随机目标 |
| R34 | CodeCraft_2024：距离缓存、方向持续与预约选读 | ✅ | — | — | — | [quick_view_version](https://github.com/PinkEx/CodeCraft_2024/blob/98d53b453302d2ee33e433fc859f1ab3f8c64818/quick_view_version/functions.h)及main/robot；可参考反向BFS、收益场和队内让行。RMTC对手不承诺让路，未知地图也不等于物流全图；未运行原赛事 |
| R35 | 阶段结束与剩余动作数守卫 | ✅ | ✅ | ✅ | ✅ | [规划说明](https://github.com/Frank-678/The-Logical-Structure-of-RMT-C/blob/ANALYSIS/docs/implementation/PLANNING.md)：明确100/500动作Tick，最终状态不发布；末步/两阶段窗口核心回归通过。此勾仅验收守卫，不代表实战获胜 |
| R36 | 已知可达观察点的信息增益探索 | ✅ | ✅ | ✅ | ◐ | [规划说明](https://github.com/Frank-678/The-Logical-Structure-of-RMT-C/blob/ANALYSIS/docs/implementation/PLANNING.md)：按实际视野计算新增未知格/路程，只走已知路径；边界与危险回归通过，局部下一帧覆盖9→12，未有整局覆盖率统计 |
| R37 | 新旧采集策略的同条件夹具 | ✅ | ✅ | ✅ | ◐ | [7例配对轨迹](https://github.com/Frank-678/The-Logical-Structure-of-RMT-C/blob/ANALYSIS/checks/code-results/planning-2026-10-28.json)：7例无受阻MOVE，两步新增R20→30、四步40→50、密集资源200的耗时40→36；迷宫均18步。单次决策最大观测2.28ms，仅一轮样本；不是标准车胜率或完整回调延迟 |
| R38 | 练习代理的上游出网诊断 | ✅ | ✅ | ✅ | ◐ | [诊断与实测](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/7e5af551da20a1c17e40e0e14d1ce1ff072d7903/README.md)：8本机HTTP+6注入异常、旧启动器拦截通过；用户已运行并报direct/read_timeout/10065ms。TLS握手亦可能被标read_timeout，需继续区分DNS/TCP/TLS/响应，不计比赛资格 |
| R39 | 六地图、六陪练的独立规则测试裁判 | ✅ | ✅ | ✅ | ◐ | [ARENA](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/4c7676159be4b35dded9f41a473ca5a2e8530ad6/ARENA.md)：公开局部观测/公告后延迟oracle；18地图边界、八事件测试；未原版差分或真实AI验收 |
| R40 | 训练筛选、失败留存与新留出调参 | ✅ | ✅ | ✅ | ◐ | [910局记录](https://github.com/Frank-678/The-Logical-Structure-of-RMT-C/blob/ANALYSIS/docs/implementation/ARENA_RESULTS.md)：首轮退步未采纳，第二轮对抗均分33.54→34.72、获胜29.2%→37.5%；小样本非官方结果，死亡增加及对照胜率更高均保留 |
| R41 | 新公告模型/顶层关闭思考与JSON透传 | ✅ | ✅ | ✅ | ◐ | [字段说明](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/4c7676159be4b35dded9f41a473ca5a2e8530ad6/README.md)：deepseek-flash、thinking disabled、json_object；实际C++与原Handler固定上游回归通过，未正式网关验收；512是示例 |
| R42 | 连续两次移动失败后的安全改道 | ✅ | ✅ | ✅ | ◐ | [源码与回归](https://github.com/Frank-678/The-Logical-Structure-of-RMT-C/blob/ANALYSIS/docs/implementation/PLANNING.md)：只按真实回执，两次失败且有安全替代时重算首步；新留出受阻1178→282，原版实战仍待 |
| R43 | 成功往返/争格的无进展检测与脱困 | ✅ | ✅ | ✅ | ◐ | [复现与日志](https://github.com/Frank-678/The-Logical-Structure-of-RMT-C/blob/ANALYSIS/docs/implementation/NAVIGATION.md)：12可信帧窗口、目标暂缓/脱困期限；压力往返500→16Tick，正常绕路保留；另60局新地图均分37.37→38.16。未取得用户地图、未原版DDS验收，致命守卫仍可能停留 |
| R44 | 假设火线保留唯一已知爆炸逃路 | ✅ | ✅ | ✅ | ◐ | [七份字幕的取舍与反例](https://github.com/Frank-678/The-Logical-Structure-of-RMT-C/blob/ANALYSIS/docs/implementation/LESSONS.md)：每版32个席位/方向/敌动作变换，不踩点旧16死→新0死，实际踩点仍16死；另60局新地图分数未变，参数未重调。不是32独立地图或原版实战，保留风险 |
| R45 | 自建裁判四席位观测隔离契约 | ✅ | ✅ | ✅ | ✅ | [规则回归](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/826c4da5afa74d038b7ffad032da570e682d31a1/tests/arena_test.cpp)：逐席位身份、坐标、R/D和自他区分断言通过ASan/UBSan；仅验收该观测契约，不代表完整裁判差分一致 |
| R46 | 用户新增练习日志的场次与重复数据核验 | ✅ | — | ✅ | ◐ | [A审计](https://github.com/Frank-678/The-Logical-Structure-of-RMT-C/blob/7fb18759dc16d08b4947f88570a2997f59232166/practice-2a4edb203071443189635dfbc1b2037b/ai.jsonl)：25次real/200；同场500Tick原始分45。1000帧有500份完全重复，去重后才统计；7fb归档中27835目录score却属于2a4ed，拒绝串场归因。是用户上传证据，未精确绑定每场二进制，不冒充本工具新补丁实战 |
| R47 | 分析文档和历史报告迁入独立仓库 | ✅ | ✅ | ✅ | ✅ | [归档入口](https://github.com/Frank-678/The-Logical-Structure-of-RMT-C/blob/ANALYSIS/docs/implementation/README.md)：迁移点名五篇、拆出ARENA历史结论、14份JSON保留原字节；运行/源码/规则接口、测试用法及仍使用的选定参数留代码仓库。跨仓引用已修复，practice不变 |
| R48 | 未来堡垒前置规划及公告采纳追踪 | ✅ | ✅ | ✅ | ◐ | [实现与失败/结果](https://github.com/Frank-678/The-Logical-Structure-of-RMT-C/blob/ANALYSIS/docs/implementation/EVENT_USE.md)：同夹具及时解释时无双窗口5→11；迟到不补时。首版59011退步保留，恢复active策略后69013对抗36.21→36.44、胜率持平；核心/HTTP/ASan/UBSan/ROS链接通过，非原版新补丁实战 |
| R49 | 第一阶段38/40回跳30的同场取证 | ✅ | — | ✅ | ◐ | [计分流复核](https://github.com/Frank-678/The-Logical-Structure-of-RMT-C/blob/ANALYSIS/docs/implementation/SCOREBOARD.md)：三场每Tick各有stage1与stage2计分；R190对应38/30，R200对应40/30，score.json及scoring.log为40。未改原裁判，冲突消息进程身份仍待维护方溯源 |

> 本表“验收”必须对应具体范围：例如 R13 的 ✅ 仅表示重复公告回归通过，不表示 AI 模型在所有事件上正确；R14/R15 的 ❌ 是**测试执行失败**而非“算法已输给标准车”。R17/R18/R24及R26–R34的实现栏破折号表示外部研究或拒绝项；具体迁移单列R19–R21、R36。R29/R30的执行/验收只指上述函数反例。

## 下一轮执行优先级

1. **P0：完成完整对局和 AI 时效数据。** 在正常 Ubuntu 22.04 / ROS 2 Humble/DDS 环境获取 A 与标准 B/C/D 的真实回执、R/D/M、得分、死亡、无效动作、模型调用与事件可用时间；不要动裁判原件。
2. **P1：实测新增目标规划。** 迟滞、资源串和信息增益已有代码及局部配对结果；自建留出和模块对照已运行；下一步在正常DDS原版裁判与标准对手下复核。
3. **P2：补齐搜索模型，再决定是否扩展。** 已有可选三Tick局部多情景；隐藏状态与模型误差仍在，训练选中关闭，完整整场模型未完成。继续只执行首步，下一Tick依据裁判回执重算。
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
