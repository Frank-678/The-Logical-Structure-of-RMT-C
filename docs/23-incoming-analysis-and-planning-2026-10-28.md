# 新增分析、云盘源码、9仓库建议与小步实施

2026-10-28。本轮已完成材料核对、三个小功能提交与一个文档结果提交；尚未完成完整裁判比赛、标准对手胜率、全事件联合推演或自动调参。详见[结构化证据](../checks/incoming-analysis-and-planning-2026-10-28.json)。本文记录可核查的依据、决定与结果，不是隐藏推理或逐字聊天导出。

## 用户新增输入与授权

1. 追问旧指令是否完成，并交来两份分析。已逐段读取298/164段正文，SHA256与[归档正文](../materials/addenda/2026-10-28-analysis/README.md)保留；不是只看标题或片段。
2. 指明云盘AHC #77562268。已取得MHTML中完整2195行源码，重点核对Beam、Retro、OperationLocalSearch和verify；没有运行原解法，也没有独立证实实时冠军排名。
3. 指明Gemini的Rmtc Bot Node仅供参考。已取得888行源码、全文阅读并用真实Humble头文件做语法检查通过；未运行节点，未替换比赛工程。
4. 要求分析Gemini精准指出的外部仓库。9份README和22代码文件固定到HEAD/blob，阅读范围与三函数反例见[9仓库研究](https://github.com/Frank-678/The-Logical-Structure-of-RMT-C/blob/COMPARISON/reports/08-gemini-repository-suggestions-2026-10-28.md)。
5. **明确授权扩充main README矩阵和勾号**。此前AGENTS的禁止main约定据本次用户指令作有限例外，只改README；不合并研究历史，不将两支名称/入口写入main或代码PR。已从25行扩至37行，提交`beb91a8`。

云盘两源码的[重点审查](https://github.com/Frank-678/The-Logical-Structure-of-RMT-C/blob/COMPARISON/reports/09-drive-ahc-and-gemini-node-review-2026-10-28.md)指出：Gemini节点缺请求model、1.8秒超时、无异步场次所有权、同Tick再处理、幻术延期、后两段曼哈顿距离和边界风险。它能过语法，不代表这些运行语义已对。这里只借主线，独立改善现有实现。

## 对旧建议的实际推进

| 提交 | 变更 | 证明范围 |
| --- | --- | --- |
| `361541e` | 有效目标迟滞；100/500最终状态和剩余动作窗 | 原实现目标振荡回归失败，新实现通过；危险/复活/断帧/失败MOVE可打断 |
| `405023a` | 已知BFS资源串，最多3目标/5束宽/8候选/10ms软预算 | 路过拾取去重，虚拟R正确跨越计分上限；是资源目标深度，不是3Tick攻防树 |
| `a23edad` | 信息增益观察点与7个采集夹具 | 靠边界旧版选重复视野，新版观察格从9到12；危险仍优先 |
| `a7d2318` | [详细说明](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/a7d2318fcce432878277686cbb2da65c87ca30fe/PLANNING.md)、函数变量导读、6张图及完整结果 | 文档、哈希、真实输出可核查，不替代实战 |

原先两步诊断在完整500Tick场景不能证明“向右必优”；本轮把短程比较明确放在剩2次动作的Tick498，第一阶段另核对Tick98。完整时域也可能先取另一目标更好，所以没有为了固定测试方向扭曲策略。末步不能再追结束后才到的资源。

搜索分支保存预计坐标、步数、虚拟R、已拾取集合与一次任务机会。每段BFS只用已知可走格，按预计时间检查爆炸/分裂，当前首步仍需经过原安全守卫。结果只交首步，下一帧读裁判位置和回执；没有预先改写真实状态。任务机会仍是启发式，不是完整进度/AI资格模拟；未来敌人动作未当作真值。

## 配对结果与运行范围

同一个`tests/planning_benchmark.cpp`分别链接`90af985`与`a23edad`，保持地图、起点、剩余Tick、视野一致。两步新增R20→30，四步40→50；初始R110都仅增加2.5资源分；密集资源200都收完但40步→36步；迷宫均18步；全部7例无受阻MOVE。[完整轨迹](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/a7d2318fcce432878277686cbb2da65c87ca30fe/tests/results/planning-2026-10-28.json)保留旧新SHA与计时。

新版单次决策最大观测约2.28ms，每例一轮，不是可靠分布或整个ROS回调。夹具不包含敌车、随机事件、任务、AI；没有留出场景，不能外推整场收益、胜率、部署参数最优或多人安全。

核心Werror、固定HTTP、原版Handler转发、启动守卫、ASan/UBSan均通过；LeakSanitizer关闭。真实ROS源码再次以Humble头文件/库手动链接成功，仍非完整colcon/WSL验收。6张Mermaid解析通过，未宣称本轮图像渲染审校。

当前`getifaddrs`复核仍为-1/errno1（EPERM），完整裁判继续受DDS环境阻塞；本轮没有新增真实模型调用或实际比赛。既有两次DeepSeek HTTP200是此前固定提交测试：4.652秒/5.977秒，第二次超过2.5秒预告；不能当成本轮节点成功、短预告及时率或正式资格。practice所有18文件与原树保持一致。

## 本轮分支快照与未完成事项

截至读取快照仍为4支。两个研究支HEAD未被他人推进；log新增提交`2dac70f`只添13字符/2行的`ros-logs/log.txt`，无Tick或移动/调用数据，不能解读为新一轮失败，更不能绑定当前代码。其他旧log保留历史属性。

main的R19/R20/R21/R23只标部分完成；R35守卫只验收具体回归；R29/R30只验收外部函数反例。P0完整对局/AI时效仍阻塞；P2完整攻防模型、多情景、通用未来计划局部优化、对手池消融、自动调参、正式封存均未完成。用户授权网络不改变当前平台实际拒绝的系统调用，没有绕过权限限制。

后续在正常Ubuntu22.04/Humble环境按原PDF流程先仅接A再接B/C/D，固定地图/席位/种子、记录R/D/M/死亡/无效动作/AI及时率。只修改集中配置再编译，原practice不动。代码仍在开放PR中，多次小提交可独立评审，未合并代码main。
