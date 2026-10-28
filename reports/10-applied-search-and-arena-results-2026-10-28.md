# 2026-10-28 外部建议的实际迁移与反例反馈

代码固定`4c7676159be4b35dded9f41a473ca5a2e8530ad6`，无需新增外部仓库搜索。本轮将此前已研读的原则转为独立RMTC实现，不搬原游戏规则或直接粘贴许可证不明代码。此前9仓库/云盘AHC/Gemini的逐项借鉴、拒绝和阅读范围继续见08/09报告，不把本轮扩写成所有上游逐行审计。

| 思路 | 本轮适配 | 未照搬/限制 |
| --- | --- | --- |
| AHC小束宽与多样性 | 资源4目标/束宽5/候选8；可选3Tick攻防束搜索 | 不用AHC分数推RMTC分数，战术默认关闭是训练结果 |
| AHC未执行序列局部改进 | 资源目标反转、插入、删除，12次且完整重算合法性 | 已执行Tick不回滚，不做置换群共轭；本批消融同分，无收益证据 |
| Orienteering可行插入/删除 | 先已知BFS可行和期限，再估值；保持单目标退路 | 不允许不可达高收益目标使搜索直接退出；未知图非静态完整图 |
| CodeCraft距离缓存 | 仅一帧内同起点/目标/时间的BFS缓存 | 不假设地图永久不变，不为对手预约路线或约定让路 |
| Pacman多对手情景 | 直追/防御/轨迹/资源/侧向，可能无双另情景 | 不是已校准概率或精确Nash；不能从父模拟中读隐藏真值 |
| 前沿探索 | 沿用实际视野新增格/距离 | 不搬SLAM/Nav2坐标或全图路线前提 |
| harness/消融建议 | 六地图六陪练、训练/留出、910局含重复训练与消融 | 自建裁判共享规则不能替代原版；延迟oracle不证明LLM理解 |

首轮训练优胜者留出平均32.09→30.87，未采纳。补连续受阻改道后换新种子，最终对抗33.54→34.72、获胜份额29.2%→37.5%，死亡81→89。关闭受阻改道为33.06/41.7%，保留指标取舍。不是每个模块都提高成绩，非官方标准车结果。

[实现/方法](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/4c7676159be4b35dded9f41a473ca5a2e8530ad6/ARENA.md) · [最终结果](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/4c7676159be4b35dded9f41a473ca5a2e8530ad6/tests/results/arena-2026-10-28.json) · [状态机](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/4c7676159be4b35dded9f41a473ca5a2e8530ad6/STATE_MACHINE.md)。研究说明见同仓ANALYSIS的docs/24；不从代码PR或main暴露准备区入口。正式工程主分支未改，代码PR保持开放。
