# 2026-10-28 上沿往返、争格与无进展脱困

用户报告队友改地图后，500Tick里约200Tick在上沿上下移动，而且其他情形/顽固对手也可能造成卡住。本轮尚未取得那张具体地图或同场日志；复现同类问题，不冒充原场复盘。代码功能提交27d1a75，方法/结果提交`4ba9dcdaf2056248505ebd2479077b77cf68a7ef`，仍在现有PR #1，未合并；practice18原件不变。

## 确认的缺口

此前仅有两次失败MOVE后的改道。两个格子来回走且moved=true，完全不会触发。固定旧生产核心3ecc01f后，确实在自建上沿用例中复现整500Tick往返、R=0。根因之一：反伤有效且敌方持续防御时，攻击估值已拒绝，接近同一敌人的估值却仍为正，反复调整站位。另复现两车争同一到点任务500Tick不完成。

反伤下预测只能自损时不奖励接近；连续12份可信观测缺少R/D/任务/新地图/回血/驻留增长且周期重复或局限四格时，暂缓旧目标24Tick，选循环区外安全目的地最多坚持12Tick。每帧重读实际位置和占位，只发首步。正常长廊/绕路、真实得分、堡垒进度、断帧/缺回执等有独立回归。公开席位打破同分对称，未知图不补成空地。

当前无安全出口则DEFEND并每帧重查，保留原循环区防止暂停后又空跑。当前致命防御/已知危险仍优先，不能把所有停留都定义为算法失败，也没有保证物理封死或致命射线下仍强行逃离。原本正常移动默认不改成WAIT。四个新增导航参数集中原头文件，旧权重不重调，新阈值不称优化到最优。

## 实际验证

同一C++测试裁判/六场景分别链接旧生产核心与新核心，共12局、每局500Tick：上沿持续反伤最长无收益往返500→16Tick且R0→20；30Tick反伤30→0；争格任务未完成→Tick43完成，受阻252→35且R0→20；正常墙后任务两版都Tick28/R20；闭合两格空跑500→12，之后488Tick明确无出口防御；长廊回头采集两版R30。无效动作均0。持续500Tick反伤是放大错误的压力用例，不当作正式标准事件时长；其他车的停用计数仅测试端，不改正式复活规则。

另外新种子39007起、六地图四对抗席位、每版6采集+24对抗，手写NPC固定且不用Strategy作对照车，以保持陪练不随版本变化。没有重新调权重。采集均分31.67不变；对抗37.37→38.16、获胜份额41.7%→50.0%、死亡85→81、受阻91→79、无效0。小样本、地图席位相关、自建规则及延迟oracle均限制结论，不宣传正式胜率。

核心/HTTP/原Handler/裁判边界ASan/UBSan通过（本环境关闭LSan），实际ROS源码Humble手工链接通过，8个Mermaid块解析通过。没有原版DDS整局，没有新增真实模型调用，没有用户WSL执行。

[方法与日志](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/4ba9dcdaf2056248505ebd2479077b77cf68a7ef/NAVIGATION.md) · [六例全部轨迹](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/4ba9dcdaf2056248505ebd2479077b77cf68a7ef/tests/results/unstuck-2026-10-28.json) · [新地图逐局](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/4ba9dcdaf2056248505ebd2479077b77cf68a7ef/tests/results/unstuck-maps-2026-10-28.json) · [验证范围](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/4ba9dcdaf2056248505ebd2479077b77cf68a7ef/tests/results/unstuck-verification-2026-10-28.json)。新日志navigation含无进展时长、脱困次数/目标、暂缓数和no_safe_exit，便于用户回传同场具体原因。

## 上一轮网关超时问答的记录

用户询问超时及模型能否给N Tick后的决策。已核对代码：总HTTP上限35秒，建连5秒包含其中；后台等待不阻塞本地Tick。当前LLM输出绝对生效时间的事件解释，下一新Tick验场次/证据并按当前状态选动作；尚未输出带条件的未来动作队列，也没有按事件截止动态调整HTTP超时。35秒只是网络兜底，提前5Tick且500ms/Tick时仅约2.5秒，还需扣撤离时间。本轮未借导航修复冒称完成这一时效调度设想。

main只更新用户授权的README矩阵至R43；研究材料不进入代码PR或其他公开导航。
