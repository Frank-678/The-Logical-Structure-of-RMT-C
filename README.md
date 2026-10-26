# RMTC · ANALYSIS

[同批新增三张群聊截图](docs/17-map-uncertainty-2026-10-27.md)：堡垒不能硬编码，地图对称性占比说法冲突，中心迷宫仍仅猜测。

2026-10-27当前规则为RULES-03 v1.2：[迁移与行动](docs/16-v1.2-rule-migration.md)。堡垒范围以当场公告为准；复活选点已写入正式规则；语言不限，镜像不再必交。旧版本记录保留作历史依据。

[新增地图编辑器与现场通知](docs/15-map-editor-and-onsite-addendum.md)：原件、导出兼容性、13项逻辑检查和配置验证；现场替补与切换仍按封存规则执行。

[战术与消息处理详解](docs/14-tactical-and-message-design.md)：汇总攻击/移动、辣椒、堡垒、计分及暂停恢复；验收用例均待执行。

2026-10-25更新：已读取QA-02副本（7问6答），补充世界分裂复活保护、堡垒坐标和提交要求；此前Q&A未读描述为历史状态。组队信息.xlsx仍未取得。[最新澄清](docs/13-qa-and-fortress-2026-10-25.md)。

**上一版v1.1归档：** [规则迁移与策略重算](docs/11-v1.1-rule-migration.md) · [新包冲突核对](docs/12-v1.1-package-audit.md) · [原件/53页全文](materials/releases/v1.1/README.md) · [三截图转录](materials/addenda/2026-10-23/chat-transcript.md)。首批6 PDF72页及v1.1三PDF53页保留历史，新增v1.2规则24页，共10 PDF149页。当前规则v1.2；配套最新已取得协议/教程仍v1.1。旧“D/300、死亡不扣伤害”不再适用。

本分支保存我们对本次比赛的材料核读、规则理解、设计取舍与验证计划。前三次任务是学习准备，比赛以正式规则、通信协议和有效书面公告为准。

**从这里开始：** [总索引](INDEX.md) → [来源与引用](REFERENCES.md) → [全部附件核读](docs/01-source-review.md) → [设计取舍](docs/03-tradeoffs.md) → [架构](docs/04-architecture.md) → [验证](docs/05-validation.md)。

| 内容 | 入口 |
|---|---|
| 原始 8 个附件、6 PDF 共 72 页 | [材料目录](materials/README.md)、[机器索引](materials/catalog.json) |
| 正式规则与练习配置差异 | [规则基线](docs/02-rulebook.md)、[原始核读](docs/01-source-review.md) |
| 新增群内答疑：复活选点、席位顺序、有线联调 | [澄清与实现影响](docs/10-rule-clarifications-2026-10-21.md)、[截图转录](materials/addenda/2026-10-21/chat-transcript.md) |
| 已采纳、否决与待验证方案 | [决策记录](docs/07-decisions-and-open-questions.md) |
| 对话中形成的结论与修正 | [讨论记录](docs/08-discussion-record.md) |
| 联调、封存和提交 | [交付清单](docs/06-delivery-and-schedule.md) |
| 原件和程序完整性 | [校验说明](checks/README.md)、scripts/verify_materials.py |
| 外部六集研究和摘录 | [COMPARISON 分支](https://github.com/Frank-678/The-Logical-Structure-of-RMT-C/tree/COMPARISON) |

当前阶段：完成材料整理、静态核对与方案设计；**尚未完成 ROS 2 Humble 对局联调和新策略胜率验证。** 不把设计文档当作已实现参赛程序。

分支边界：本次只维护 ANALYSIS、COMPARISON，不改 main。[原协作规范](governance/original-collaboration-guidelines.md)保留。引用和第三方材料权利见 [NOTICE](NOTICE.md)。

**私密预备资料：** 本分支不进入其他分支或公开导航；未来公开使用干净历史导出，见 [私密预备约定](governance/private-preparation.md)。
