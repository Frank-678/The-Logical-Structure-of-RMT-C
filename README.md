# RMTC · ANALYSIS

[七份字幕与假设风险逃路修复](docs/26-subtitle-counterexamples-and-risk-ordering-2026-10-28.md)：确认可能火线硬过滤缺陷并修复；32例对称变换/版与新地图验证，保留不可照搬规则和未解决项。

[上沿往返与无进展脱困](docs/25-motion-loops-and-recovery-2026-10-28.md)：补足成功MOVE往返漏检；同类压力用例500→16Tick，争格任务Tick43完成，正常绕路保留。另60局新地图验证，不冒充用户原地图或原版裁判。

[2026-10-28多风格对战与参数封存](docs/24-multistyle-arena-tuning-and-gateway-2026-10-28.md)：910局包含训练和消融，首轮失败保留；新留出对抗平均33.54→34.72，非官方标准车。三Tick搜索保留但训练选择关闭；practice18原件不变，新公告字段回归通过。

[用户本机502排查与独立出网检查](docs/18-conversation-and-implementation.md#22-用户本机已执行移动最新失败是http502)：本机ROS已实际执行移动，3次完成请求均HTTP502而非35秒客户端超时。新增诊断入口，旧启动器拒绝执行，原practice不变；上游根因仍待本机检查。

[2026-10-28新增分析与实际规划](docs/23-incoming-analysis-and-planning-2026-10-28.md)：两份DOCX、云盘AHC/Gemini源、9仓库关键代码；3次功能提交+1次文档结果提交，7例采集配对。资源目标Beam/迟滞/信息探索已实现，完整攻防及标准车对局仍未验收。用户明确授权的main README矩阵已扩至R37。以下历史“Beam未实现”以本条为最新。

[2026-10-28新增内容复核](docs/22-latest-branches-and-ahc-review-2026-10-28.md)：4分支、9次新提交；两步采集反例与R封顶检查，区分已有首步闭环和未实现Beam。

[2026-10-28 AHC068→RMTC 策略迁移分析](docs/21-ahc068-to-rmtc-decision-study-2026-10-28.md)：记录 AHC 与本赛差异、已实现基线、短时域搜索设计、审查/执行边界与 P0–P4 验收；新算法尚未实战。

[2026-10-28规则状态机与对手预测](docs/20-state-machines-and-opponent-prediction.md)：45个编号范围、5张图；实际加入权限状态和短轨迹预测，完成后重试参考车及标准陪练。两项因DDS权限未开局，无有效胜率。

[2026-10-28原件逐项复读与实测](docs/19-original-materials-full-review.md)：8原件、72页全文、42页原页核对；真实DeepSeek两次成功，累积公告膨胀已修复。原版裁判与标准陪练因当前环境DDS权限未能开局，尚无胜率。

[2026-10-27对话与实施全程记录](docs/18-conversation-and-implementation.md)：需求、依据、取舍、修正、21个代码提交及验证边界。选手主流程已有PR实现；完整Humble/DDS与真实模型联调仍未验收。原件复读和2026-10-28新增实测见上方入口；历史文档保留当时含义。

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

当前阶段：已有选手PR实现、核心回归与两次真实模型调用证据；**尚未完成 ROS 2 Humble 对局联调和新策略胜率验证。** 不把设计文档当作已实现参赛程序。

分支边界：本次只维护 ANALYSIS、COMPARISON，不改 main。[原协作规范](governance/original-collaboration-guidelines.md)保留。引用和第三方材料权利见 [NOTICE](NOTICE.md)。

**私密预备资料：** 本分支不进入其他分支或公开导航；未来公开使用干净历史导出，见 [私密预备约定](governance/private-preparation.md)。

