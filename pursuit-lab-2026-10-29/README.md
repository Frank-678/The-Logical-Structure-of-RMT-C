# 同时行动追逃原型与DeepSeek定点审查原始产物

ChatGPT，2026-10-29。本轮是离线局部模型/工具审查，没有ROS完整比赛或付费AI调用。

代码固定提交：a4ccba51ecf5c2497d1985369d83fc7a0f0d9191，代码仓strategy/visible-resource-bfs；只新增研究工具/测试/用法，没有改机器人策略或默认开关。

- `receipts.json` 与 stdout/stderr：23项原型单测、最新DeepSeek工具14项回归、三个审查反例。
- `deepseek-review.json`：M1/M4对手池不同、Ready等行数重建、带空格构建路径。审查固定eacb963dab4d38bf5f2c3112fb6043fe10279c61的指定工具文件；依赖的归档辅助/只读配置取自既有快照。
- `differential-index.json` 与12个part：240个输入/双方动作/原型结果/arena结果全量保留，240一致。原始240行JSON仅拆分，没有删掉失败案例；本批无失败。
- `certificate-lp.json`：80个矩阵、20棵有限树的独立HiGHS LP审计全部通过。
- `probes/`：20个输入局面、每个完整根矩阵及输出、汇总；300/500伤害分母分别报告。

`manifest.json`记录每个文件字节数与SHA256，包含原始数据而非只放摘要。命令中的绝对路径记录本机位置，复跑时须改为本机路径，不能冒充原签名环境。

物理差分的既有arena可执行文件SHA256为f004861f02d10cdd1991d6301386205f5e0c92b103dad7e5da55eca46b00323f；这不是原版ROS裁判验证。矩阵/树的值界只针对定义的叶子估值与封闭普通1v1模型，不能称整局均衡、必杀或晋级概率保证。20个场景为设计样本，没有作为独立留出集使用。
