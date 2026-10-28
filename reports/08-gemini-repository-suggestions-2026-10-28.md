# Gemini推荐的9仓库：实际代码、反例与迁移边界

日期2026-10-28。本次固定9个HEAD，完整读取9份README，取得并核对22个代码文件的Git blob，再阅读关键函数/范围。不是对全部仓库逐行审计，也没有运行原比赛。文件、行段、哈希与链接见[31文件清单](../checks/external-source-inventory-2026-10-28.json)。原建议来自用户提供的《Gemini的分析》，其正文已在ANALYSIS归档。

## 1 手写Pacman：奖励必须换成RMTC语义

[jhammarstedt/PacmanAI](https://github.com/jhammarstedt/PacmanAI/blob/2611a267b99c274516f889bba32852df083ad721/README.md)的README明确区分未充分训练的CNN/DQL和实际获胜的后备启发式队。核心阅读[heuristicTeam.py](https://github.com/jhammarstedt/PacmanAI/blob/2611a267b99c274516f889bba32852df083ad721/src/heuristicTeam.py)的`chooseAction`、特征/权重和食物变化处理（150–285、325–450）。可借鉴低风险/进攻模式切换、依据连续观测更新目标。原游戏的食物带回本方和旗区机制不属于RMTC；原权重不直接抄，也不带本地训练模型上场。当前未重跑其获胜叙述。

[neeilnandal/pacman-mcts-agent-v2](https://github.com/neeilnandal/pacman-mcts-agent-v2/blob/4b48e73977bf5313a486acd39b4bccd22c8f1856/README.md)真正文件叫[myTeam(1).py](https://github.com/neeilnandal/pacman-mcts-agent-v2/blob/4b48e73977bf5313a486acd39b4bccd22c8f1856/myTeam(1).py)，不是README所写的myTeam.py。208–320、346–415能看到UCT选择、MCTS式局部搜索和模式切换。默认搜索0.82秒，对100ms/500ms动作窗口过长；代码也不能仅凭README就当作完整多对手随机模拟器。可采纳“只在分歧有价值时分配有限预算”；不把回家距离奖励、原时间预算当RMTC常量。

[DXJ3X1/Pacman-Capture-the-Flag](https://github.com/DXJ3X1/Pacman-Capture-the-Flag/blob/f2ed02de687e63ab4e2fd634fef5526dbb8314e1/README.md)树中8件主要是README、PPT、图片/GIF，**没有选手源码**。本次读README，没读PPT/图片。其陷阱搜索、绕路BFS和模式设计可作概念参考，但“每步吃更多食物”等部分列在Further Improvements，不能替它声明已实现高性能组合规划。

## 2 定向问题：先检验可行性，再借算法名称

[MiladNooraei/Orienteering-Problem](https://github.com/MiladNooraei/Orienteering-Problem/blob/d41a5d7e1a9a561b7b3d94b27c683cb8c7bfb51d/Orienteering%20Problem.py)实际主要函数是收益/欧氏距离贪心，不是通用动态规划或Floyd求解。每轮挑最高比例，再发现超预算就退出，未先筛掉不合格点。函数级反例：预算2，起点(0,0)，远点(10,0)值1000，近点(1,0)值10；实得0，但近点可行且得10。因此借鉴预算/收益表达，不直接搬实现。

[aliiimaher/Algorithm-OP-Heuristic-Approaches](https://github.com/aliiimaher/Algorithm-OP-Heuristic-Approaches/blob/44dec64428580615bd50da40a443258180e0b906/README.md)的8个小脚本均已读：最近点、最高收益、收益减成本、收益/距离、DP、Kruskal、Prim、未完成DFS。

| 脚本 | 实际范围或问题 | 本次执行 |
| --- | --- | --- |
| App1–4 | 各种贪心基线；App2排序收益后与原位置索引存在错配；App4从初始点计比值且有固定阈值2 | 静态阅读，未运行 |
| App5_DP | `dp[node][time]`只从小编号转到大编号，距离浮点转整数；不是一般访问集合DP | 预算3的反例实得10，允许重排可得20 |
| App6_Kruskal | 选树边本身不等于可执行的单条行走路线 | 静态阅读，未运行 |
| App7_Prim | 节点/父指针与路线输出有前提，不能默认树长就是合法行程 | 静态阅读，未运行 |
| App8_DFS_Modifed | 文件自己标为未完成；起点就把累计距离增加整个Tmax，后续正距离不能入选 | 相邻值10的可行点也输出No valid path |

三个例子的[真实输出](../checks/op-counterexamples-2026-10-28.json)与[脚本](../tools/check_op_examples.py)已保存。脚本校验固定Git blob，只用AST取已审查函数，不执行外部模块顶层、绘图或整个框架。复现：按清单取3个固定源文件并保留`owner/repo/path`目录，运行`python3 tools/check_op_examples.py /path/to/source-root`。这三例验证具体函数缺陷，不构成整个项目的性能排名。

[gkobeaga/op-solver](https://github.com/gkobeaga/op-solver/blob/992a2443dd845c7a6f4952e1f28c51a4297e887b/README.md)值得更认真参考：实际启发式核心在`src/cp/heur/`。本次读`add.c`前90行、`drop.c`前155行、`ea/opt.c`前155行及完整可行性示例。重点是最小成本插入、必要时删点恢复预算和独立检查约束；不是把静态全图闭合路线求解器塞进每Tick。精确模式的CPLEX等依赖、离线性能和上界尚未运行；其论文/仓库介绍不能替代RMTC在线可用性证据。

## 3 Frontier：新视野有价值，但不是SLAM照搬

[mertgulerx/mrtsp_exploration_ros2](https://github.com/mertgulerx/mrtsp_exploration_ros2/blob/d9bc18085f49f6aa4396b4009d22ad5255096bf9/README.md)是Python/Jazzy工程，README另链接C++仓库。本次读WFD 45–155、成本45–135和整个小型排序器：未知与已知空地相邻的边界、两层BFS聚类、信息/成本排序、只取下一目标。实际排序器是贪心，不能称精确TSP；起点代价与论文目标也有实现近似。可用其信息增益想法，不带入Nav2膨胀、世界坐标、激光建图和未经验证参数。

[Nyanziba/AutoFrontierSearch_ros2-humble](https://github.com/Nyanziba/AutoFrontierSearch_ros2-humble/blob/8e72eeebddceff5addfde1e3111de203bf917311/README.md)的`algolism.py`是简单ROS示例：-1未知格邻接0空地、过滤近墙点、随机选目标，再经SLAM/里程计坐标发布。RMTC已有离散格和裁判坐标，应独立计算真实视野能新看到几格，不能把未知当空、不能直接用米制缩放/随机目标。

已独立实现的RMTC适配见[PLANNING](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/a7d2318fcce432878277686cbb2da65c87ca30fe/PLANNING.md)：在已知可达观察点比较`新增可见格/(距离+1)`；当前危险与合法性守卫仍先执行。边界夹具下一帧累计可见格从9到12；不是整局探索率或胜率。

## 4 CodeCraft：缓存/方向持续可借，队内礼让不能套给对手

[PinkEx/CodeCraft_2024](https://github.com/PinkEx/CodeCraft_2024/blob/98d53b453302d2ee33e433fc859f1ab3f8c64818/README.md)已归档。阅读`quick_view_version`的`functions.h` 80–165（货物/港口收益场和移动）、`main.cpp` 198–270及303–350（货物反向BFS、目标分配、调度）和robot声明。可以参考少量目标距离缓存、收益场、方向持续和失效重算；原机器人ID优先级/预约是队内协作规则，不保证RMTC敌人让行。也不能用全图货物真值、港口/船舶或原权重。

README自己提到固定种子/地图的过拟合限制。Gemini提出“下一Tick失败回执排堵”是合理RMTC设计，但这次未定位到足够证据，不能归成此仓库已经精确实现的同一机制。

## 5 这次真正落地的内容

| 借鉴点 | 参赛改动 | 验证范围 |
| --- | --- | --- |
| 少量未来目标一同估值 | 最多3个资源目标、束宽5、候选8、10ms软预算；已知BFS每段、虚拟R、沿途拾取去重 | 核心回归、7采集夹具；无完整多人推演 |
| 方向/目标持续 | 近似同分的有效旧目标10%排序余量；失败MOVE、断帧、复活或危险打断 | 振荡回归，非参数最优证明 |
| Frontier信息价值 | 实际视野下新增未知格/距离，仍只走已知路线 | 边界与危险回归，非SLAM集成 |
| OP预算可行性 | 明确100/500动作窗，路径不超剩余动作数 | 最终状态、末步及两阶段回归 |

[7例同条件结果](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/a7d2318fcce432878277686cbb2da65c87ca30fe/tests/results/planning-2026-10-28.json)：两步R20→30，四步40→50，密集200资源40步→36步；迷宫均18步，全部无受阻MOVE。新版单次决策最大观测2.28ms，一轮样本，不含网络/ROS，不是延迟分布。没有将其他游戏的成绩或反例当作RMTC强度验收。

完整对标准车仍被当前DDS接口权限阻塞；留出地图、对手池、死亡/任务/争格和AI时效配对实验仍待测试。原practice未改，未直接复制外部完整节点或部署训练模型。
