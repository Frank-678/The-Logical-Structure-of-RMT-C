# audit distill
summary: Extract every requirement from all branches of doc+code repos, verify compliance against current state
agents: 11, tokens: 1182956, toolcalls: 454

## result 0: scope=doc-analysis-a
- checks: [{"req_id": "GL-01", "status": "partial", "evidence": "D:/code/The-Logical-Structure-of-RMT-C/docs/01-source-review.md:76 记录「满分40」；当前状态：冠军 heldout 阶段一 32.67/40（docs/implementation/LESSONS.md:156）", "gap": "stage1 ≥40 目标未达成（32.67）；LESSONS.md:76 已按不可达口径如实记载（TSP 下界天花板≈37）", "action": "保持锚点口径；若冲 40 需突破 TSP 下界，否则按目标锚点如实记载"}, {"req_id": "GL-02", "status": "partial", "evidence": "docs/01-source-review.md:77 记录「500 Tick、满分60」；stage2 锚点 41.25（docs/37-race-batches-real-battles-2026-10-29.md:60）、heldout 43.89（LESSONS.md:156）", "gap": "stage2 ≥50 未达成；rrh10 最终裁决（docs/37 §7，HEAD ec9bb4e）race 家族关闭于 0.0，最高 51.7 均值来自 n=3 部分批次不能作为达标", "action": "执行 docs/38 版本联赛（先 24 场试点）补 stage-2 证据；继续新杠杆（如 prepare_fortress_value 实验）"}, {"req_id": "GL-03", "status": "partial", "evidence": "docs/38-version-league-spec-2026-10-29.md:50 完整记录（已核对该行原文）", "gap": "联赛尚未执行——原版/自战维度真实名次与分数分布证据缺失", "action": "内存允许后按 docs/38 先跑 24 场试点再放量"}, {"req_id": "GL-04", "status": "partial", "evidence": "docs/37-race-batches-real-battles-2026-10-29.md:60 记录证据缺口（已核对）；docs/38 §1 联赛规格已冻结（d49a5f8/cbd9fb7 之前）", "gap": "证据缺口未补齐：唯一 stage2 锚点仍是训练集 41.25", "action": "执行联赛试点（与 GL-03 同一动作）"}, {"req_id": "GL-05", "status": "partial", "evidence": "docs/38-version-league-spec-2026-10-29.md:3 记录目的与 U6 判定（多 profile 自战档案不能代表旧版本/原版）；已有一批 vs 原版陪练证据（log 分支 f971206 8局6W/2L、58ed0ca rrh10 8局）", "gap": "原版对局维度已有证据；self-play 冻结二进制联赛（M3 混合）未执行", "action": "按 docs/38 §1 M1/M2/M3 混合先 24 场试点"}, {"req_id": "GL-06", "status": "met", "evidence": "docs/implementation/LESSONS.md:76 记录不可达口径（阶段一 TSP 天花板≈37、阶段二需 R≈90+M3+D500）", "gap": "", "action": ""}, {"req_id": "MT-01", "status": "met", "evidence": "docs/01-source-review.md:108 记录 S1 = 40 × R1 / 200（FULL 匹配）", "gap": "", "action": ""}, {"req_id": "MT-02", "status": "met", "evidence": "docs/01-source-review.md:110 记录旧公式 S2 = 30×min(R/120,1)+15×min(D/300,1)+5M（FULL 匹配）", "gap": "", "action": ""}, {"req_id": "MT-03", "status": "met", "evidence": "docs/03-tradeoffs.md:13 记录现行公式与斜率（FULL 匹配）", "gap": "", "action
- requirements: 112
  - GL-01 [goal] 第一阶段：每队1–2人独立采集，100 Tick，100 ms/Tick，共10秒，满分40（RMTC目标：stage1 40分）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/01-source-review.md:76
      ev: 每队 1–2 人；第一阶段独立采集 100 Tick，100 ms/Tick，共 10 秒，满分 40
  - GL-02 [goal] 第二阶段：最多四队同场 500 Tick，500 ms/Tick，共250秒，满分60。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/01-source-review.md:77
      ev: 第二阶段最多四队同场 500 Tick，500 ms/Tick，共 250 秒，满分 60
  - GL-03 [goal] stage2 目标 50 分；当前锚点是训练集 41.25，联赛数据将给出原版/自战维度真实名次与分数分布作为 50 分验收的第一手证据。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/38-version-league-spec-2026-10-29.md:50
      ev: stage2 目标 50 的当前锚点：训练集 41.25；联赛数据将给出原版/自战维度的真实名次与分数分布，作为 50 分验收的第一手证据。
  - GL-04 [goal] 必须补齐 stage-2 证据缺口（原版对局 + 自战联赛）；当前唯一 stage2 锚点仍是训练集 41.25，距离 50 目标尚远。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/37-race-batches-real-battles-2026-10-29.md:60
      ev: stage-2 证据缺口（原版对局 + 自战联赛）仍待 C7/U6 版本联赛实施 —— 当前唯一 stage2 锚点仍是训练集 41.25，距离 50 目标尚远
  - GL-05 [goal] 版本联赛目的：补齐 stage-2 证据缺口——与原版的一局 + 自己打自己不同模型（冻结二进制的自战版本联赛；多 profile 自战档案不能代表旧版本或原版 robot_node）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/38-version-league-spec-2026-10-29.md:3
      ev: 目的：补齐 stage-2 证据缺口 —— 与原版的一局 + 自己打自己不同模型……U6 判定：多 profile 自战档案不能代表旧版本或原版 robot_node。
  - GL-06 [metric] 阶段一40分受TSP下界约束不可达（天花板≈37）；阶段二50分需要R≈90+M3+D500——两目标在当前规则与视野4下均不可达（目标是锚点，按不可达口径如实记载）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/implementation/LESSONS.md:76
      ev: 阶段一40分受TSP下界约束不可达（天花板≈37）；阶段二50分需要R≈90+M3+D500……两目标在当前规则与视野4下均不可达
  - MT-01 [metric] 第一阶段计分公式：S1 = 40 × R1 / 200。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/01-source-review.md:108
      ev: 第一阶段：S1 = 40 × R1 / 200。
  - MT-02 [metric] 第二阶段计分公式（v1.0）：S2 = 30 × min(R/120, 1) + 15 × min(D/300, 1) + 5 × M。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/01-source-review.md:110
      ev: 第二阶段：S2 = 30 × min(R/120, 1) + 15 × min(D/300, 1) + 5 × M。
  - MT-03 [metric] 第二阶段计分公式（现行）：S2 = 30 min(R/120,1) + 15 min(D/500,1) + 5M；未封顶时资源斜率0.25分/价值，有效伤害0.03分/点；普通资源2.5分、高级5分、任务每项5分。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/03-tradeoffs.md:13
      ev: S2=30 min(R/120,1)+15 min(D/500,1)+5M。未封顶时资源斜率0.25分/价值，调整后有效伤害0.03分/点；普通资源直接2.5分、高级5分，任务每项5分。
  - MT-04 [metric] 对抗分 = 15×min(D/500,1)，最高仍15分，替代旧 D/300（RULES-02 §10.2 第18页）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/11-v1.1-rule-migration.md:13
      ev: 对抗分 | 15×min(D/500,1)，最高仍15分；替代旧D/300 | RULES-02 §10.2，第18页
  - MT-05 [metric] 死亡结算：本Tick所有伤害/奖励先入账，再每次死亡扣60，最低0；分裂立即复活也扣。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/11-v1.1-rule-migration.md:15
      ev: 本Tick所有伤害/奖励先入账，再每次死亡扣60，最低0；分裂立即复活也扣 | RULES-02 §5.2第13页、§7第14页
  - MT-06 [metric] 击杀奖励：每名死者一份60，致死批次造成正伤害的队伍去重后均分。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/11-v1.1-rule-migration.md:16
      ev: 每名死者一份60，致死批次造成正伤害的队伍去重后均分 | §10.2，第18页
  - MT-07 [metric] 有效伤害递推：D_t = max(0, D_(t-1) + 本Tick实际攻击贡献 + 击杀奖励 − 60×本Tick死亡次数)；D可超500并随死亡下降，超额是缓冲不可截断。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/11-v1.1-rule-migration.md:29
      ev: D_t = max(0, D_(t-1) + 本Tick实际攻击贡献 + 击杀奖励 - 60*本Tick死亡次数)
  - MT-08 [metric] 杠杆 heldout 晋升基准 = 冠军封存 heldout objective 0.8298625（arena-postcap-heldout-2026-10-29）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/34-lowhp-attack-discount-2026-10-29.md:22
      ev: ≥ 冠军封存 0.8299…冻结 baseline 行必须逐位复现 0.7710073（确定性钉），否则本次 heldout 作废重跑
  - MT-09 [metric] 冻结 baseline 行必须逐位复现 0.7710073（确定性钉），否则本次 heldout 作废重跑；冻结基线只作可比性校验，不是晋升基准。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/34-lowhp-attack-discount-2026-10-29.md:22
      ev: 冻结 baseline 行必须逐位复现 0.7710073（确定性钉），否则本次 heldout 作废重跑
  - MT-10 [metric] 真实对局护栏：若 deaths 显著上升（均值 ≥9 且中位数 ≥8）且平局翻盘 0 次 → 回退 post_cap_combat_weight=0.02。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/30-real-battle-baseline-and-postcap-batch-2026-10-29.md:39
      ev: 若 deaths 显著上升（均值 ≥9 且中位数 ≥8）且平局翻盘 0 次 → 回退 0.02
  - MT-11 [metric] 真实批量预注册判据：t30 完成率 ≥0.356；耗尽时A份额回升、拾取数回升；deaths/damage_events 沿用"均值 ≥9 且中位 ≥8"防线。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/35-t30-opening-metrics-batch-2026-10-29.md:86
      ev: 下轮真实批量预注册判据（同口径）：耗尽时 A 份额均值回升、拾取数回升、t30 完成率 ≥0.356；deaths/damage_events 沿用"均值 ≥9 且中位 ≥8"防线。
  - MT-12 [metric] 版本联赛规模：144 场/版本起步 = 12 图 × 4 席位 × 3 对手混合。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/38-version-league-spec-2026-10-29.md:22
      ev: 144 场/版本起步 = 12 图 × 4 席位 × 3 对手混合
  - MT-13 [metric] 冠军 search_04 锚点：留出阶段一 32.67/40、阶段二 43.89/60；14 个杠杆家族关闭，冠军在每轴均为经验局部最优。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/implementation/LESSONS.md:156
      ev: 冠军search_04不变：留出阶段一32.67/40、阶段二43.89/60
  - MT-14 [metric] 旧冠军 heldout objective 0.8437 须连同源码 SHA、参数与对手版本封存并逐局复现，不能只凭参数名未变就自动延续到新源码。
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:34
      ev: 旧冠军的 0.8437 应连同其源码 SHA、参数与对手版本保存，不能只凭参数名未变就自动延续到新源码。
  - CN-01 [constraint] 堡垒区域：多数地图 [11,11] 至 [13,13]，特殊地图按当场公告；不能写死坐标，堡垒范围以当场公告为准。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/02-rulebook.md:19
      ev: 堡垒区域 多数[11,11]至[13,13]，特殊地图按当场公告；不能写死坐标
  - CN-02 [constraint] 模型调用必须走官方网关；禁止本地模型。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/02-rulebook.md:21
      ev: 模型：官方网关；禁止本地模型
  - CN-03 [constraint] 正式运行除官方统一调用外不允许其他 AI 调用，包括本地模型；提交与现场运行版本须一致。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/13-qa-and-fortress-2026-10-25.md:26
      ev: 正式运行除官方统一调用外不允许其他AI调用，包括本地模型；提交与现场运行版本须一致
  - CN-04 [constraint] 现场启动哪个版本就提交哪个，不能提交与运行两套代码。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/13-qa-and-fortress-2026-10-25.md:29
      ev: 现场启动哪个版本，就提交哪个，不能提交与运行两套代码
  - CN-05 [constraint] 封存后不能随意修改源代码、Prompt 或策略参数。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/01-source-review.md:184
      ev: 封存后不能随意修改源代码、Prompt 或策略参数
  - CN-06 [constraint] 人工重启每阶段原则上最多两次，不补时。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/01-source-review.md:185
      ev: 人工重启每阶段原则上最多两次，不补时
  - CN-07 [constraint] 2026-10-31 20:00 前提交代码、镜像、技术报告与自有程序联调截图/录屏；2026-11-01 正式比赛。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/01-source-review.md:186
      ev: 2026-10-31 20:00前提交代码、镜像、技术报告与自有程序联调截图/录屏；2026-11-01正式比赛
  - CN-08 [constraint] 材料截止仍 2026-10-31 20:00，正式比赛仍 11 月 1 日；删镜像不代表取消前置检录截图/录屏。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/16-v1.2-rule-migration.md:26
      ev: 材料截止仍2026-10-31 20:00（§1第5页、§2.2第7页），正式比赛仍11月1日。删镜像不代表取消前置检录截图/录屏。
  - CN-09 [constraint] 现场替补/切换仍按封存规则执行。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/15-map-editor-and-onsite-addendum.md:74
      ev: 现场替补/切换仍按封存规则
  - CN-10 [constraint] 令牌不提交仓库、不录入公开截图。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/15-map-editor-and-onsite-addendum.md:76
      ev: 令牌不提交仓库、不录入公开截图
  - CN-11 [constraint] 不写死练习目标与示例坐标；正式任务内容不固定，读取本场 missions（每场从对局数据读取）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/04-architecture.md:22
      ev: 任务规划 | missions+资源/伤害进度→目标候选 | 不写死练习目标；考虑封顶与任务资格
  - CN-12 [constraint] 比赛中不存在 JSON/ROS 调参入口；伤害距离/结算常量不可交给优化器搜索；生产配置集中 match_config.hpp（编译期）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/24-multistyle-arena-tuning-and-gateway-2026-10-28.md:13
      ev: 不存在赛中JSON/ROS调参入口，伤害距离/结算常量不搜索
  - CN-13 [constraint] 不得以关键词匹配替代 LLM 事件理解（不得以"天下无双"关键词触发固定区域并用无关模型请求冒充事件理解）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/17-map-uncertainty-2026-10-27.md:18
      ev: 随机事件入口仍是公开event_text，经官方LLM理解位置、触发、生效与失效；本地代码校验并执行。不得以"天下无双"关键词触发固定区域并用其他无关模型请求冒充事件理解。
  - CN-14 [constraint] 赛前自备网线、有线环境实测；SSH 或网页可达不能替代 ROS/DDS 通信证据（有线联调纳入验收）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/10-rule-clarifications-2026-10-21.md:67
      ev: 赛前自备网线，用有线环境实测能否运行……SSH或网页可达不能替代ROS/DDS通信证据。
  - CN-15 [constraint] 表述纪律：不把"移动可能改善下一回合站位"写成"能躲掉本回合的攻击"。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/02-rulebook.md:28
      ev: 不要把"移动可能改善下一回合站位"写成"能躲掉本回合的攻击"
  - CN-16 [constraint] 封存要求：源代码、Prompt、策略参数一起版本化。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/06-delivery-and-schedule.md:26
      ev: 封存：源代码、Prompt、策略参数一起版本化
  - CN-17 [constraint] 不修改原裁判，不让机器人发布或覆盖成绩。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/implementation/SCOREBOARD.md:21
      ev: 不修改原裁判，不让机器人发布或覆盖成绩
  - CN-18 [constraint] 练习配置（事件参数与正式标准不同）仅人工练习，不能作为决策输入。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/12-v1.1-package-audit.md:15
      ev: 两阶段JSON配置 | 与旧包相同，事件参数仍与正式标准不同 | 仅人工练习；不能作为决策输入
  - CN-19 [constraint] 任务得分须满足本场、本席位真实统一 AI 成功调用资格（真实统一 AI 成功调用资格是计分前提）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/01-source-review.md:116
      ev: 真实统一 AI 成功调用资格
  - CN-20 [metric] 总分构成：资源30 + 对抗15 + 三任务15 = 60；正式任务内容不固定，读取本场 missions。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/11-v1.1-rule-migration.md:24
      ev: 总分仍为资源30＋对抗15＋三任务15＝60；正式任务内容不固定，读取本场missions。
  - CN-21 [constraint] 参赛决策输入边界：运行裁判或真实 AI 前读取接入说明；不得把观赛真值、内部 ROS、管理端或练习配置作为参赛决策输入。
      src: D:/code/The-Logical-Structure-of-RMT-C/AGENTS.md:8
      ev: 运行裁判或真实 AI 前读取接入说明；不得把观赛真值、内部 ROS、管理端或练习配置作为参赛决策输入
  - CN-22 [constraint] 杠杆触发条件只依据本队感知（known-reachable tiles_：value>0、非墙、paths 有解），不读取 config、观赛 map_view 或地图真值；资源总量真值只用于赛后指标。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/36-race-reach-holdoff-2026-10-29.md:52
      ev: 触发条件只依据本队感知……不读取 config、观赛 map_view 或地图真值——符合 U7 的"参赛程序只能依据本队感知估计"要求。
  - CN-23 [constraint] 参赛程序只能依据本队感知、回执、可用公开公告与合法记忆估计，不能读取 config、观赛 map_view 或别车感知来准确获知全图耗尽；试验时资源总量真值用于赛后指标，策略触发条件另写清楚。
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:227
      ev: 参赛程序只能依据本队感知、回执、可用公开公告与合法记忆估计，不能读取 config、观赛 map_view 或别车感知来准确获知全图耗尽。
  - CN-24 [constraint] 不能猜地图或事件参数；不引入地图真值、关键词事件解析或模型直接动作（本地按真实坐标持续行动，模型异步解释、校验后更新）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/implementation/MATERIALS_CHECK.md:14
      ev: 不能猜地图或事件参数……这次修复调用链和可观察性，不引入地图真值、关键词事件解析或模型直接动作
  - CN-25 [constraint] 用户贴入的真实上游密钥不得抄入文档、代码或提交；提示其撤销轮换；测试仅使用 fixture 凭据。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/18-conversation-and-implementation.md:115
      ev: 用户贴入的真实上游密钥没有抄入本文、代码或提交；提示其撤销轮换。测试仅使用fixture凭据
  - CN-26 [constraint] 临时 Key 只用于测试，没有写入代码、日志或结果文件（测试后删除临时副本）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/implementation/REAL_TEST.md:7
      ev: 临时Key只用于测试，没有写入代码、日志或结果文件
  - CN-27 [constraint] 凭据未写入仓库或结果，临时副本测试后已删除。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/18-conversation-and-implementation.md:196
      ev: 凭据未写入仓库或结果，临时副本测试后已删除
  - CN-28 [process] 推送/归档前 API key 扫描必须干净（sk-cbc 扫描通过）；网关核验 ai.jsonl 行数==seat 调用数，A 0 失败。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/37-race-batches-real-battles-2026-10-29.md:53
      ev: 网关核验：ai.jsonl 行数==seat 调用数，A 0 失败；全部文件 sk-cbc 扫描通过。
  - CN-29 [constraint] 归档记录哈希/validated/rejected/partial/去重/token/费用，但不存凭据。
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:245
      ev: A 独立 event_update 日志随批归档，哈希/validated/rejected/partial/去重/token/费用记录（不存凭据）
  - CN-30 [constraint] 通常禁止修改、合并或推送 main；2026-10-28 用户明确新增授权：可直接扩充 main/README.md 的进度矩阵与勾号状态，本次例外仅限该文件；不要自动创建指向 main 的合并操作。
      src: D:/code/The-Logical-Structure-of-RMT-C/AGENTS.md:4
      ev: 通常禁止修改、合并或推送 main。2026-10-28 用户明确新增授权：可直接扩充 main/README.md 的进度矩阵……本次例外仅限该文件……不要自动创建指向 main 的合并操作
  - CN-31 [constraint] main 授权边界：只改 README 矩阵与勾号；不合并研究历史，不将两支名称/入口写入 main 或代码 PR。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/23-incoming-analysis-and-planning-2026-10-28.md:11
      ev: 明确授权扩充main README矩阵和勾号……只改README；不合并研究历史，不将两支名称/入口写入main或代码PR
  - CN-32 [constraint] ANALYSIS/COMPARISON 为保密预备分支：不得向其他分支、PR、Issue、标签、公开工作流、发布说明或网站添加这些分支的名称、入口或曾存在的线索；不得把本研究历史合并到正式开发分支；未来公开采用干净历史导出。
      src: D:/code/The-Logical-Structure-of-RMT-C/governance/private-preparation.md:3
      ev: 不得向其他分支、PR、Issue、标签、公开工作流、发布说明或网站添加这些分支的名称、入口或曾存在的线索；不得把本研究历史合并到正式开发分支
  - CN-33 [constraint] 只在现有研究分支提交，不创建新分支、不动 main 或参赛 PR；旧原件、practice、上游快照及其哈希不改。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/22-latest-branches-and-ahc-review-2026-10-28.md:88
      ev: 旧原件、practice、上游快照及其哈希不改；只在现有研究分支提交，不创建新分支、不动 main 或参赛 PR。
  - CN-34 [constraint] 用户最终指定分支：ANALYSIS 归档本比赛，COMPARISON 归档外部比较与代码摘录；禁止操作 main，不创建向 main 的合并操作。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/08-discussion-record.md:23
      ev: 用户最终指定分支：ANALYSIS归档本比赛，COMPARISON归档外部比较与代码摘录；禁止操作main……不创建向main的合并操作
  - CN-35 [process] AI 生成或修改的代码，应先提交到非 main 分支，再通过 PR 合并到 main。
      src: D:/code/The-Logical-Structure-of-RMT-C/governance/original-collaboration-guidelines.md:5
      ev: 使用 AI 生成或修改的代码，应先提交到非 "main" 分支，再通过 Pull Request（PR）合并到 "main"。
  - CN-36 [process] 方案尚未确定或效果有待验证：无论改动大小都应先提交到非 main 分支，验证后再 PR；内容明确且已验证的补丁可以直接提交到 main。
      src: D:/code/The-Logical-Structure-of-RMT-C/governance/original-collaboration-guidelines.md:16
      ev: 方案尚未确定或效果有待验证：无论改动大小，都应先提交到非 "main" 分支，验证后再通过 PR 合并。/ 内容明确且已验证的补丁：可以直接提交到 "main"。
  - PR-01 [process] 2026-10-29 用户补充：分析类文件放本仓库（ANALYSIS），与代码强相关的除外；代码仓库保留构建运行、源码/规则接口与测试用法。
      src: D:/code/The-Logical-Structure-of-RMT-C/AGENTS.md:15
      ev: 2026-10-29用户补充：分析类文件放本仓库，与代码强相关的除外……构建运行、源码/规则接口与测试用法保留代码仓库
  - PR-02 [process] 文档归属：新分析/实验档案写入本仓库 docs/ 与 checks/code-results/；代码仓库保留构建/运行/源码接口/测试用法与部署所需参数（match_config.hpp、run.sh、run_arena.py、eval_levers.py）；旧来源 SHA 与文件哈希随档案保存；不迁入整段研究分支历史
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:90
      ev: 本轮新分析/实验档案写入本仓库 docs/29-*（2026-10-29 轮）与 checks/code-results/；代码仓库保留构建/运行/源码接口/测试用法与部署所需参数……旧来源 SHA 与文件哈希随档案保存
  - PR-03 [process] 迁移说明：LESSONS/MATERIALS_CHECK/NAVIGATION/PLANNING/REAL_TEST 等按 2026-10-28 用户要求移入分析仓库 docs/implementation/，进一步编辑在此维护，保留原代码基线 826c4da 出处。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/implementation/README.md:17
      ev: 迁移说明：本文于2026-10-28按用户要求从代码仓库移入分析仓库；原代码基线826c4da，原有测试结论按当时范围理解。
  - PR-04 [protocol] Review 回复协议：双方只 append 本 review.md，按实际写入时间顺序，不改写、删除、重排历史；每条注明北京时间、身份、回应 ID、接受/异议/待验证、相关提交 SHA，以及证据和下一步。
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:7
      ev: 你的回复也必须直接追加在本 review.md 末尾。双方只 append，按实际写入时间顺序，不改写、删除、重排历史。每条注明北京时间、身份、回应 ID、接受/异议/待验证、相关提交 SHA，以及证据和下一步。
  - PR-05 [protocol] Review 勘误与分卷：旧记录有错时新增勘误，保留原记录；代码条目回代码分支同名 review.md，理论与日志条目回本文件；并发更新先重新读取再追加，保留双方内容，不强推。
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:7
      ev: 旧记录有错时新增勘误，保留原记录。代码条目请回代码分支的同名文件；理论与日志条目回本文件。并发更新先重新读取再追加，保留双方内容，不强推。
  - PR-06 [process] 远程分支监控：追踪全部分支的新提交，固定 HEAD 快照（ANALYSIS 457d99a…、main bee5397… 等）随表冻结。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/22-latest-branches-and-ahc-review-2026-10-28.md:11
      ev: ANALYSIS | 457d99a286338d41fe278781d727c5d37424e135 | 79bf098403accd9f412ab8ba0cd1b44622df9ce9 | 3 | docs/21 新研究，以及 README、INDEX 导航
  - PR-07 [process] 每小时自动检查状态（如实）：5/5 定时任务已满，未创建成功、未停用现有任务；本文件不代表已启用实时监控；后续若启用按远端实质变更追加，跳过纯 ChatGPT review 提交避免自我触发。
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:62
      ev: 服务返回 too_many_active_automations，当前 5/5 定时任务已满，没有创建成功，也没有停用现有任务。本文件不代表已启用实时监控。
  - PR-08 [protocol] 杠杆晋升总则：全部以"冠军逐位一致"为默认（0/false），晋升必须经过 train 评估与 heldout 一次性验证。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/29-review-fixes-and-postcap-lever-2026-10-29.md:11
      ev: 全部以'冠军逐位一致'为默认（0/false），晋升必须经过 train 评估与 heldout 一次性验证
  - PR-09 [protocol] train 协议：全量 24 场景（12 stage-1 + 12 stage-2）；selection_guards：invalid==0、stage1 ≥ baseline_stage1−1；heldout 仅对选中者评估一次。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/36-race-reach-holdoff-2026-10-29.md:22
      ev: train 全量 24 场景（12 stage-1 + 12 stage-2），协议同前（selection_guards：invalid==0、stage1 ≥ baseline_stage1−1；heldout 仅对选中者评估一次）。
  - PR-10 [protocol] 预注册要求：批量对照判据写于批量运行中、结果未读（预注册判据须先于结果确立）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/35-t30-opening-metrics-batch-2026-10-29.md:19
      ev: 预注册对照判据（写于批量运行中，结果未读）
  - PR-11 [protocol] 杠杆 heldout 的晋升基准是冠军封存 heldout；冻结基线只作可比性校验（协议修正后口径）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/32-lc-coverage-exploration-2026-10-30.md:81
      ev: 杠杆 heldout 的晋升基准是冠军封存 heldout，冻结基线只作可比性校验
  - PR-12 [protocol] heldout 不达标 → 家族关闭，保持默认值，不作第二次 heldout。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/34-lowhp-attack-discount-2026-10-29.md:23
      ev: 不达标 → 家族关闭，保持 1.0，不作第二次 heldout
  - PR-13 [protocol] 留出集合纪律：反复使用同一留出结果的集合只能称"反复使用的验证成绩"，不能称"完全未参与选择的最终测试集"；最终检查用一次未看过的地图族/种子，无需为每个小改动消耗新最终测试。
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:32
      ev: 即使每个候选只跑它一次，只要看完结果决定是否保留参数、是否继续该策略族，这个集合已经参与开发决策，不能继续称作完全未参与选择的最终测试集。
  - PR-14 [process] 评测方法学：固定对照版本、候选版本和最佳已验证版本；测试种子/对手池/机器/并行数/规则版本都记录；调参集和验收集分开；统计单位按地图配对，不把同图换边结果当完全独立样本。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/05-validation.md:29
      ev: 固定对照版本、候选版本和最佳已验证版本；测试种子/对手池/机器/并行数/规则版本都记录。调参集和验收集分开。统计单位按地图配对，不把同图换边结果当完全独立样本
  - PR-15 [process] 没有显著改善时保留旧版。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/05-validation.md:33
      ev: 没有显著改善时保留旧版
  - PR-16 [process] 墙钟负载控制：对照评估轮换 A→B/B→A 顺序、重复场景、报告成对差值范围与超预算次数；小于一次拾取的均值差不作结论；机器负载问题先控制再决定细小调参差是否可信。
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:82
      ev: 后续对照评估将轮换 A→B/B→A 顺序、重复场景并报告成对差值范围与超预算次数。……小于一次拾取的均值差，不宜直接下"逐位同一/局部最优/家族闭合"的结论。
  - PR-17 [process] 被校验器拒绝的配置计为生成/校验失败单独报告，不能当作机器人输赢，也不应静默减少样本量。
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:227
      ev: 配置被拒绝的一场应计为生成/校验失败并单独报告，不能当作机器人输赢，也不应静默减少样本量。
  - PR-18 [protocol] 版本冻结清单：tools/versions.json 冻结 champion/old_champion/candidate 的 commit SHA、params_digest（match_config.hpp sha256）、binary_sha256、独立构建目录；选手参数只在 match_config.hpp（编
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/38-version-league-spec-2026-10-29.md:18
      ev: 每个版本一个独立构建目录……二进制 sha256 冻结；同一版本在全部对局中位元不变。选手参数只在 match_config.hpp（编译期），无运行时参数注入
  - PR-19 [protocol] 自战第二席位 = 同源码换席位重建（team="A"→"B"，"能写死就写死"合规）；每版本构建 4 个席位变体（A/B/C/D），构建脚本临时改头文件→build→还原。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/38-version-league-spec-2026-10-29.md:18
      ev: 席位/令牌也是 constexpr（team="A"、ai_token="practice-A"），故自战第二席位 = 同源码换席位重建（team="B"、practice-B；"能写死就写死"合规）。每版本构建 4 个席位变体（A/B/C/D）
  - PR-20 [process] 版本联赛先 24 场试点（2 图 × 4 席位 × 3 混合）验证调度器与双选手同场后再放量（144×3 版本）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/38-version-league-spec-2026-10-29.md:33
      ev: 先 24 场试点（2 图 × 4 席位 × 3 混合）验证调度器与双选手同场……后再放量。
  - PR-21 [protocol] 联赛每局归档字段：代码 SHA、完整参数（params_digest）、AI 模式、session_id、最终名次、score/R/D/M/hp/invalid；版本级报告按初始地图成组，保留最差样本。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/38-version-league-spec-2026-10-29.md:37
      ev: 每局归档：代码 SHA、完整参数（params_digest）、AI 模式、session_id、最终名次、score/R/D/M/hp/invalid。版本级报告：……按初始地图成组，保留最差样本。
  - PR-22 [protocol] 短序列差分验收：向原版 practice 与自建引擎输入相同合法动作序列，核对攻击/死亡/重生/增益时序与分数；差分只作一致性证据，不替代原版对局（共享 rules.hpp 可能共享同一错误）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/38-version-league-spec-2026-10-29.md:41
      ev: 向原版 practice 与自建引擎输入相同合法动作序列，核对攻击/死亡/重生/增益时序与分数。风险：……差分只作一致性证据，不替代原版对局。
  - PR-23 [constraint] practice 原文件保持只读；测试驱动、临时配置和结果放外部（沿用 18 号文档先例）；原版 practice robot_node 只读。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/38-version-league-spec-2026-10-29.md:41
      ev: practice 原文件保持只读，测试驱动/临时配置/结果放外部（沿用 18 号文档先例）。
  - PR-24 [process] 不要把旋转/镜像后的同一张图或四席位计作独立新地图。
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:215
      ev: 不要把旋转/镜像后的同一张图或四席位计作独立新地图。
  - PR-25 [process] batch 驱动器、归档与筛选/验证脚本迁入代码仓 tools/ 并随批提交（可重跑脚本、版本清单与归档检查入库）。
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:261
      ev: batch 驱动器、归档与筛选/验证脚本下轮迁入代码仓 tools/ 并随批提交。
  - PR-26 [protocol] log 分支归档：每批全量 10 件套 + batch_summary.json + README 上传 log 分支；中断批次 README 必须注明中断。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/37-race-batches-real-battles-2026-10-29.md:51
      ev: rrh08 7 局全量 10 件套 + batch_summary.json + README……rrh10 3 局 + batch_summary_reconstructed.json + README 注明中断
  - PR-27 [process] 归档自洽校验：文件内所有 session 匹配目录、起止 Tick 完整、客户端/网关次数同一场、构建 SHA 和配置哈希对应；归档失败就标"不配套"，不要自动拼接；原日志不删除，追加勘误/对应说明。
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:17
      ev: 建议你在本地归档时检查：文件内所有 session 是否匹配目录、起止 Tick 是否完整、客户端/网关次数是否同一场，构建 SHA 和配置哈希是否对应。归档失败就标"不配套"，不要自动拼接。原日志不删除，追加一份勘误/对应说明即可。
  - PR-28 [process] bot_A.log 必须当局结束后立即从该局路径拷贝，禁止从共享路径统一拷贝（T1 后固化进 copy_batch_artifacts.sh）。
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:70
      ev: bot_A.log 必须当局结束后立即从该局路径拷贝，禁止从共享路径统一拷贝。
  - PR-29 [process] run.sh 保存机器人输出到项目 log/bot_时间_进程号.log；不要只上传裁判 run_dir 而漏掉外部启动的 A 端日志；日志只供赛后诊断，不反馈到比赛决策输入。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/implementation/EVENT_USE.md:43
      ev: run.sh……保存机器人输出到项目log/bot_时间_进程号.log……不要只上传裁判 run_dir 而漏掉外部启动的 A 端日志。日志只供赛后诊断，不反馈到比赛决策输入
  - PR-30 [protocol] 运行完整原版 practice 时，把本场的代码 SHA、参数、AI 模式、session 与最终名次一起归档；改善自己原始分与改善最终名次须分开报，直接读取裁判 rank 并保留平局判定键。
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:58
      ev: 运行完整原版 practice 时，把本场的代码 SHA、参数、AI 模式、session 与最终名次一起归档。……后续评测直接读取裁判 rank，并保留平局判定键。改善自己原始分与改善最终名次须分开报。
  - EV-01 [constraint] 证据纪律：不要把读取/解析通过说成运行通过，也不要把全仓扫描说成所有源文件逐行审查。
      src: D:/code/The-Logical-Structure-of-RMT-C/AGENTS.md:9
      ev: 不要把读取/解析通过说成运行通过，也不要把全仓扫描说成所有源文件逐行审查
  - EV-02 [constraint] 所有机制结论标来源，所有策略假设标"待测试"；保留原件哈希、版本和许可说明。
      src: D:/code/The-Logical-Structure-of-RMT-C/AGENTS.md:6
      ev: 所有机制结论标来源，所有策略假设标'待测试'。保留原件哈希、版本和许可说明
  - EV-03 [constraint] 不得把未完成事项（材料递交/ROS 联调等）写成已完成。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/06-delivery-and-schedule.md:29
      ev: 不得把这些写成已完成
  - EV-04 [constraint] 不得假称已获胜率；不能把环境启动失败写成策略战败，也不能把 HTTP 200 写成赛事 AI 资格已达成。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/21-ahc068-to-rmtc-decision-study-2026-10-28.md:75
      ev: 不得假称已获胜率……不能把环境启动失败写成策略战败，也不能把 HTTP 200 写成赛事 AI 资格已达成。
  - EV-05 [constraint] 实施清单是任务队列，不是已经实现的功能；每项应关联验证日志和规则来源；不把参考 repo 高分作为完成证明。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/09-implementation-checklist.md:23
      ev: 以上是任务队列，不是已经实现的功能。每项应关联验证日志和规则来源；不把参考repo高分作为完成证明。
  - EV-06 [constraint] 用户实机记录不冒充本工具亲测（日志 session/分数不匹配时如实标注，不拼凑因果链）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/27-late-practice-log-integrity-2026-10-28.md:3
      ev: 用户实机记录不冒充本工具亲测
  - EV-07 [constraint] 不把文件清单、静态阅读或模拟测试称为真实比赛通过；原版 practice/ 继续只读。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/implementation/MATERIALS_CHECK.md:3
      ev: 本页解释采用了什么，不把文件清单、静态阅读或模拟测试称为真实比赛通过。原版practice/继续只读。
  - EV-08 [constraint] 没有把建议的 144 场说成已运行；未修改 practice/（审查记录如实）。
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:229
      ev: 没有把建议的 144 场说成已运行，也未修改 practice/。
  - EV-09 [constraint] 复现同类问题时不冒充原场复盘（尚未取得用户具体地图与同场日志时必须如实说明）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/25-motion-loops-and-recovery-2026-10-28.md:3
      ev: 本轮尚未取得那张具体地图或同场日志；复现同类问题，不冒充原场复盘。……practice18原件不变。
  - EV-10 [constraint] 每版 32 例是 4 席位×4 旋转×2 固定敌方动作，不是 32 独立地图；未伪造无风险保证。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/26-subtitle-counterexamples-and-risk-ordering-2026-10-28.md:7
      ev: 每版32例是4席位×4旋转×2固定敌方动作，不是32独立地图。……未伪造无风险保证。
  - EV-11 [constraint] 夹具没有敌车、随机事件、任务或 AI，不得当作真实比赛成绩；未完成完整 colcon/WSL 和原版裁判对标准车验收、无有效胜率时必须如实声明。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/implementation/PLANNING.md:49
      ev: 上述夹具没有敌车、随机事件、任务或AI，不得当作真实比赛成绩。……未完成完整colcon/WSL和原版裁判对标准车验收……无有效胜率。
  - EV-12 [constraint] 修复候选全部标"待测试"，批量验证前不改集中参数默认值。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/28-first-real-llm-dds-battle-2026-10-29.md:111
      ev: 回放驱动修复候选（全部标"待测试"，批量验证前不改集中参数默认值）
  - EV-13 [constraint] 原始材料保持原样不修改，保留哈希与许可说明（NOTICE）。
      src: D:/code/The-Logical-Structure-of-RMT-C/NOTICE.md:1
      ev: 原始材料未修改、保留哈希（NOTICE 材料/许可说明）
  - TC-01 [technical] QoS 契约：感知、动作 = RELIABLE VOLATILE depth 1；注册、任务、队伍名录 = RELIABLE TRANSIENT_LOCAL depth 1；事件公告 = RELIABLE TRANSIENT_LOCAL depth 128；发布/订阅 QoS 须匹配正式契约，不能把事件也统一设成深度 
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/14-tactical-and-message-design.md:76
      ev: 感知、动作 | RELIABLE | VOLATILE | 1 …… 事件公告 | RELIABLE | TRANSIENT_LOCAL | 128 ……发布/订阅QoS须匹配正式契约，不能把事件也统一设成深度1。
  - TC-02 [technical] 动作 JSON 每 Tick 由本地生成；LLM 异步生成事件 JSON 可跨 Tick，校验后才更新后续状态；不要求逐 Tick 由 AI 生成动作；模型超时不延长动作窗口。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/implementation/MATERIALS_CHECK.md:11
      ev: 不要求逐Tick由AI生成动作；模型超时不延长动作窗口 | 动作JSON每Tick由本地生成；LLM异步生成事件JSON，可以跨Tick，校验后才更新后续状态
  - TC-03 [technical] 动作窗口：正式规则 §3 规定第一阶段动作 Tick 为 0–99、第二阶段 0–499；stage1_ticks=100、stage2_ticks=500 集中在配置中；最终状态不发布动作；改变练习长度时明确修改这一处配置并重新编译，practice/ 不改。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/implementation/PLANNING.md:31
      ev: 正式规则§3规定第一阶段动作Tick为0–99、第二阶段0–499。stage1_ticks=100、stage2_ticks=500集中在配置中；最终状态不发布动作。……改变练习长度时明确修改这一处配置并重新编译，practice/不改。
  - TC-04 [technical] 复活选点：使用曼哈顿距离；从初始出生点按"上、右、下、左"邻接顺序 FIFO 逐层枚举；静态墙、分裂墙和车辆占据不能阻止候选向更远层展开；A→D 依次占位。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/10-rule-clarifications-2026-10-21.md:18
      ev: 使用曼哈顿距离，不使用欧氏距离或避障最短路长度 …… 从初始出生点出发，按"上、右、下、左"邻接顺序作FIFO逐层枚举……静态墙、分裂墙和车辆占据不能阻止候选向更远层展开。
  - TC-05 [constraint] 复活选点实现解释待与裁判对照，不能写成读到了引擎实现。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/10-rule-clarifications-2026-10-21.md:30
      ev: 该队列细节是我们对群内"逐层搜索"的实现解释，待与裁判对照，不能写成读到了引擎实现。
  - TC-06 [technical] 所有配置仍在 match_config.hpp（编译期常量）；本轮有界默认取舍未重新自动搜索到所谓最优值；此前选定的采集/任务权重保持不变。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/implementation/NAVIGATION.md:18
      ev: 所有配置仍在match_config.hpp：loop_recovery=true、loop_window_ticks=12……这些是本轮有界默认取舍，未重新自动搜索到所谓最优值。此前选定的采集/任务权重保持不变。
  - TC-07 [technical] 模型名采用明确的 deepseek-flash，不按名称猜测能力或自动更换模型；SDK 的 base_url 和 curl 的完整 POST 地址不是同一个配置值。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/implementation/MATERIALS_CHECK.md:16
      ev: 模型名采用明确的deepseek-flash，没有按名称猜测能力或自动更换模型。……模型服务的SDK base_url和curl的完整POST地址也不是同一个配置值。
  - TC-08 [technical] 正式上场前仍需实战验证与按规则封存参数（夹具自建对手池非官方标准车）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/implementation/PLANNING.md:60
      ev: 其中陪练不是官方标准车。正式上场前仍需实战验证与按规则封存参数。
  - TC-09 [technical] 无收益证据时保留实现供赛前试验，不默认投入比赛（参数可能过度防守，必须用对照测分）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/implementation/PLANNING.md:74
      ev: 参数可能使它过度防守，必须用对照测分；没有收益证据时保留实现供赛前试验，不默认投入比赛。
  - TC-10 [process] 用户已明确授权"跑大量局，不同地图不同对手，轮番检测看回放找问题"（批量实验授权范围）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/28-first-real-llm-dds-battle-2026-10-29.md:107
      ev: 用户已明确授权"跑大量局，不同地图不同对手，轮番检测看回放找问题"
  - TC-11 [technical] 联调要求：Ubuntu22.04/ROS2 Humble DDS 双向联调（尚未完成时如实标注，不得写成已完成）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/06-delivery-and-schedule.md:23
      ev: 联调 Ubuntu22.04/ROS2 Humble DDS双向
  - TC-12 [protocol] 每局每席位 34–46 条公开事件记录少于配置 128 条历史容量即可，事件使用证据链应计数：唯一公告事件数→解释正确数→最晚可用时刻前送达数→可兑现机会数→改变行为数→实际收益；多调用、多改动作都不是优化目标，净得分/名次与费用才是。
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:171
      ev: 建议将计数改为：唯一公告事件数 → 关键字段解释正确数 → 最晚可用时刻前送达数 → 有可兑现机会数 → 改变行为数 → 实际收益。……多调用、多改动作都不是优化目标；净得分/名次与费用才是。
  - TC-13 [process] 阶段晋级（rrh10 续跑）前提：内存回升至安全边际且用户确认后，用 --only 3..6 逐局干净续跑，不重打已完成局。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/37-race-batches-real-battles-2026-10-29.md:21
      ev: 驱动支持 --only <vid>，可逐局干净续跑（vid 配置由 seed 确定性生成，不重打已完成局）。……续跑须待内存回升且用户确认。

## result 1: scope=doc-analysis-b
- checks: [{"req_id": "gates-35-recorded", "status": "met", "evidence": "docs/35 §3 pre-registered criteria table recorded at D:\\code\\The-Logical-Structure-of-RMT-C\\docs\\35-t30-opening-metrics-batch-2026-10-29.md:19-30, self-labeled '写于批量运行中，结果未读' (line 19). Git: pre-registration commit ea21e56 ('docs/35: pre-register t30 opening metrics criteria for batch 20261101 (before results)') precedes results commit dbeae9c; git diff ea21e56..HEAD shows §3 unchanged — only §4 was filled in after the run. Next-batch gates pre-registered at docs/35:86 (份额回升/拾取数回升/t30≥0.356/deaths≥9且median≥8).", "gap": "Only one row of the §3 table is an actual judgment gate (A deaths ≥9且≥8); other rows are explicitly '记录，不作晋升判据' — a design choice, not a violation, but the §3 table reads like a fuller gate set than it is.", "action": "None required for docs/35. When citing §3 as 'gates', refer to the deaths guard + §5.4 batch gates to avoid overstating the pre-registered set."}, {"req_id": "gates-35-satisfiable", "status": "met", "evidence": "Gate tooling exists and ran: D:\\code\\The-Logical-Structure-of-RMT-C\\scripts\\t30_opening_metrics.py (present, referenced docs/35:13 '随本档案提交'); batch data archived in D:\\code\\The-Logical-RMT-C-log\\batch-2026-10-29-seed-20261101 (7 practice-* dirs + batch_summary.json + config_0..6.json); result table with per-game values at docs/35:56-64.", "gap": "None material. Variant 7 was rejected by validate_config (7/8 ran) and is reported as a generator/validation failure per U7, not silently dropped (docs/35:33-35).", "action": "None."}, {"req_id": "gates-36-recorded-applied", "status": "met", "evidence": "docs/36 §3 (docs\\36-race-reach-holdoff-2026-10-29.md:26-31) records train-selection, heldout-promotion (≥0.8298625, frozen baseline must reproduce 0.7710073) and family-close gates; git diff da85c33..HEAD for docs/36 is empty (never edited after first write). §4 numbers verified against /home/frank/cst/tests/results/levers-race-2026-10-29.json: base_off objectiv
- requirements: 199
  - AG-01 [constraint] 通常禁止修改、合并或推送 main。2026-10-28 用户明确新增授权：可直接扩充 main/README.md 的进度矩阵及相应总览说明；本次例外仅限该文件，不授权合并研究分支或修改 main 的其他文件。不要自动创建指向 main 的合并操作。
      src: D:/code/The-Logical-Structure-of-RMT-C/AGENTS.md:4
      ev: 通常禁止修改、合并或推送 main……本次例外仅限该文件
  - AG-02 [process] 所有机制结论标来源，所有策略假设标“待测试”。保留原件哈希、版本和许可说明。
      src: D:/code/The-Logical-Structure-of-RMT-C/AGENTS.md:6
      ev: 所有机制结论标来源，所有策略假设标“待测试”
  - AG-03 [constraint] 运行裁判或真实 AI 前读取接入说明；不得把观赛真值、内部 ROS、管理端或练习配置作为参赛决策输入。
      src: D:/code/The-Logical-Structure-of-RMT-C/AGENTS.md:8
      ev: 不得把观赛真值、内部 ROS、管理端或练习配置作为参赛决策输入
  - AG-04 [process] 不要把读取/解析通过说成运行通过，也不要把全仓扫描说成所有源文件逐行审查。
      src: D:/code/The-Logical-Structure-of-RMT-C/AGENTS.md:9
      ev: 不要把读取/解析通过说成运行通过
  - AG-05 [constraint] 这两支是保密预备区。禁止在其他分支、PR、Issue、标签、公开发布渠道暴露名称、入口或存在历史；不将研究历史合并到正式开发分支。
      src: D:/code/The-Logical-Structure-of-RMT-C/AGENTS.md:11
      ev: 禁止在其他分支、PR、Issue、标签、公开发布渠道暴露名称、入口或存在历史
  - 20-01 [protocol] 每条规则路径的结果仍以裁判回执为准。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/20-state-machines-and-opponent-prediction.md:9
      ev: 每条路径的结果仍以裁判回执为准
  - 20-02 [constraint] 信封不可靠时不建立状态、不发布动作；已知世界分裂强制等待或动作前必死时，策略也可明确不发布。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/20-state-machines-and-opponent-prediction.md:39
      ev: 信封不可靠时不建立状态、不发布动作
  - 20-03 [technical] 第二阶段存活时的普通回退是 DEFEND，第一阶段和阵亡时不发违法防御；当前策略不生成默认 WAIT。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/20-state-machines-and-opponent-prediction.md:39
      ev: 第二阶段存活时的普通回退是DEFEND，第一阶段和阵亡时不发违法防御
  - 20-04 [protocol] 语言须兼容接口且能解释；提交版本与运行路径一致。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/20-state-machines-and-opponent-prediction.md:67
      ev: 提交版本与运行路径一致
  - 20-05 [constraint] 席位、令牌、网络、模型和参数按本场通知；不猜隐藏地图或未公告日程。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/20-state-machines-and-opponent-prediction.md:68
      ev: 不猜隐藏地图或未公告日程
  - 20-06 [constraint] 决策参数、Prompt 不能赛中任改；登记重启不补时。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/20-state-machines-and-opponent-prediction.md:70
      ev: 决策参数、Prompt不能赛中任改
  - 20-07 [constraint] mock 不取得真实 AI 资格；练习真值只供人工调试。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/20-state-machines-and-opponent-prediction.md:71
      ev: mock不取得真实AI资格
  - 20-08 [technical] 0 不是通行证明；本车每帧绝对定位；漏帧不累计位移。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/20-state-machines-and-opponent-prediction.md:73
      ev: 0不是通行证明；本车每帧绝对定位
  - 20-09 [technical] 资源无交互动作、不刷新；不反复追已观测消失资源。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/20-state-machines-and-opponent-prediction.md:74
      ev: 不反复追已观测消失资源
  - 20-10 [constraint] 规则常量不参与调参；伤害/保护和状态由公开参数与有效事件解释约束。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/20-state-machines-and-opponent-prediction.md:75
      ev: 规则常量不参与调参
  - 20-11 [protocol] 动作只回填当前场次/Tick；晚到不补执行；同Tick缓存，旧Tick丢弃；单次正常提交。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/20-state-machines-and-opponent-prediction.md:76
      ev: 只回填当前场次/Tick；晚到不补执行
  - 20-12 [constraint] 当前移动不能躲已命中攻击；死亡车不移动；下一步风险只能用于未来决策。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/20-state-machines-and-opponent-prediction.md:77
      ev: 当前移动不能躲已命中攻击
  - 20-13 [constraint] MOVE 不能交换、跟进刚离开格或争同格；失败不是位置变化，不触发入点。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/20-state-machines-and-opponent-prediction.md:78
      ev: 不能交换、跟进刚离开格或争同格
  - 20-14 [constraint] 普通攻击只打最近敌车；保护车挡后车，墙不挡弹；有保护不能攻击。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/20-state-machines-and-opponent-prediction.md:79
      ev: 普通只打最近敌车；保护车挡后车
  - 20-15 [protocol] DEFEND 每 Tick 重新提交、本 Tick 生效，不沿用上一帧防御。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/20-state-machines-and-opponent-prediction.md:80
      ev: 不沿用上一帧防御
  - 20-16 [technical] 等待没有防御收益；策略普通回退采用 DEFEND，不能合法行动时不发布。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/20-state-machines-and-opponent-prediction.md:81
      ev: 等待没有防御收益
  - 20-17 [constraint] 每次死亡 D 扣 60；资源/任务保留。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/20-state-machines-and-opponent-prediction.md:82
      ev: 每次死亡D扣60
  - 20-18 [technical] 随机文本只由 LLM 解释；去重不按 Tick 删掉不同公告；迟到按绝对期限处理。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/20-state-machines-and-opponent-prediction.md:83
      ev: 迟到按绝对期限处理
  - 20-19 [technical] 幻术缺激活位置历史则不猜方向；离区/死亡不解除。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/20-state-machines-and-opponent-prediction.md:85
      ev: 缺激活位置历史则不猜方向
  - 20-20 [constraint] 天使恩泽原地站点不触发；战斗后才回血，不能救已死亡车辆。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/20-state-machines-and-opponent-prediction.md:86
      ev: 原地站点不触发；战斗后才回血，不能救已死亡车辆
  - 20-21 [constraint] 天下无双区域按公告，不能固定堡垒位置；未完成进度离区/死亡清零。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/20-state-machines-and-opponent-prediction.md:87
      ev: 区域按公告……未完成进度离区/死亡清零
  - 20-22 [goal] 第一阶段争取 100 Tick 内资源，最终恢复默认节奏验收。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/20-state-machines-and-opponent-prediction.md:92
      ev: 争取100Tick内资源
  - 20-23 [constraint] 不写死三项任务内容或坐标；按 ID 去重；D 降低不撤销完成。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/20-state-machines-and-opponent-prediction.md:93
      ev: 不写死三项任务内容或坐标
  - 20-24 [metric] R 封顶 120、D 计分封顶 500 但累计不截断。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/20-state-machines-and-opponent-prediction.md:94
      ev: R封顶120、D计分封顶500但累计不截断
  - 20-25 [constraint] 不要求逐 Tick 由模型出动作；不部署本地小模型；HTTP 超时不延长窗口。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/20-state-machines-and-opponent-prediction.md:95
      ev: 不部署本地小模型；HTTP超时不延长窗口
  - 20-26 [constraint] 正式赛只用官方网关。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/20-state-machines-and-opponent-prediction.md:96
      ev: 正式赛只用官方网关
  - 20-27 [constraint] 不靠非法消息试探；E_OOB/E_BLOCKED 不增加 invalid。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/20-state-machines-and-opponent-prediction.md:100
      ev: 不靠非法消息试探
  - 20-28 [constraint] 不读其他席位/内部数据，不串通、不干扰、不利用漏洞。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/20-state-machines-and-opponent-prediction.md:101
      ev: 不读其他席位/内部数据，不串通、不干扰、不利用漏洞
  - 20-29 [process] 本队故障无补时；记录场次/Tick。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/20-state-machines-and-opponent-prediction.md:102
      ev: 本队故障无补时；记录场次/Tick
  - 20-30 [constraint] 私聊不能单独覆盖规则；封存后不自行改变计分或策略；保留来源与适用范围。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/20-state-machines-and-opponent-prediction.md:103
      ev: 私聊不能单独覆盖规则；封存后不自行改变计分或策略
  - 20-31 [technical] 相同批次连续三次坏/不完整回复后暂停该批重试，新公告可重新触发。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/20-state-machines-and-opponent-prediction.md:162
      ev: 相同批次连续三次坏/不完整回复后暂停该批重试
  - 20-32 [constraint] 轨迹预测不改变确定占位、不封锁路径、不替代当前致命防御和环境避险，也不预测一长串必然动作。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/20-state-machines-and-opponent-prediction.md:183
      ev: 预测不改变确定占位、不封锁路径、不替代当前致命防御和环境避险
  - 20-33 [constraint] 不能由状态机图承诺必胜。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/20-state-machines-and-opponent-prediction.md:208
      ev: 不能由状态机图承诺必胜
  - 20-34 [process] 完整赛后数据出来前不把合成场景通过写成实战成功。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/20-state-machines-and-opponent-prediction.md:214
      ev: 完整赛后数据出来前不把合成场景通过写成实战成功
  - 21-01 [process] 先通过真实裁判和 AI 链路，再进行复杂搜索；保持规则正确性与信息权限硬约束。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/21-ahc068-to-rmtc-decision-study-2026-10-28.md:12
      ev: 先通过真实裁判和 AI 链路，再进行复杂搜索
  - 21-02 [technical] 只执行计划首步，下一 Tick 重新规划。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/21-ahc068-to-rmtc-decision-study-2026-10-28.md:12
      ev: 只执行计划首步，下一 Tick 重新规划
  - 21-03 [constraint] λ 全部待赛前实证调参，不可代替规则常量。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/21-ahc068-to-rmtc-decision-study-2026-10-28.md:53
      ev: λ 全部待赛前实证调参，不可代替规则常量
  - 21-04 [technical] Beam 时间预算不足立即回退到当前合法基线动作。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/21-ahc068-to-rmtc-decision-study-2026-10-28.md:56
      ev: 时间预算不足立即回退到当前合法基线动作
  - 21-05 [constraint] 未知地图和未来敌人决策不能当成真值，且不要替换现有 8 Tick 安全接续检查。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/21-ahc068-to-rmtc-decision-study-2026-10-28.md:58
      ev: 未知地图和未来敌人决策不能当成真值
  - 21-06 [constraint] 已经结算的 Tick 不能修改；不能把置换群等价变换伪装成实际历史回滚。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/21-ahc068-to-rmtc-decision-study-2026-10-28.md:62
      ev: 已经结算的 Tick 不能修改
  - 21-07 [constraint] 赛制硬约束：攻击先于移动；普通攻击射线最近敌人、保护车挡后车、障碍不挡攻击；资源必须合法存活占格；堡垒区域以当场公告为准，不能固定 [11,11]-[13,13]；爆炸/分裂激活结算在 MOVE 之前，迟到解释不能救当前 Tick；辣椒须实际成功进入公告点才触发；真实统一网关、同场同席位资格、HTTP 不阻塞动作。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/21-ahc068-to-rmtc-decision-study-2026-10-28.md:66-73
      ev: 区域以当场公告为准，不能固定 [11,11]-[13,13]
  - 21-08 [process] 不能把环境启动失败写成策略战败，也不能把 HTTP 200 写成赛事 AI 资格已达成。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/21-ahc068-to-rmtc-decision-study-2026-10-28.md:79
      ev: 不能把环境启动失败写成策略战败
  - 21-09 [goal] P0：在正常 Ubuntu 22.04 / ROS 2 Humble 完成同条件标准车对局，记录 A 坐标、动作回执、R/D/M/总分、无效动作及真正的 AI 资格；同时测公告在生效前被理解并影响行动的比例。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/21-ahc068-to-rmtc-decision-study-2026-10-28.md:83
      ev: P0：在正常 Ubuntu 22.04 / ROS 2 Humble 完成同条件标准车对局
  - 21-10 [goal] P4：同地图、种子、席位与对手进行配对消融，比较总分、资源、伤害、死亡、任务、无效动作和及时率。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/21-ahc068-to-rmtc-decision-study-2026-10-28.md:87
      ev: P4：同地图、种子、席位与对手进行配对消融
  - 21-11 [constraint] 赛前按规则封存，不擅自赛中调参。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/21-ahc068-to-rmtc-decision-study-2026-10-28.md:87
      ev: 赛前按规则封存，不擅自赛中调参
  - 21-12 [process] 每个步骤独立区分研究已审查/代码已实现/测试已运行/结果已通过；失败、阻塞保留错误证据，不画成功勾。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/21-ahc068-to-rmtc-decision-study-2026-10-28.md:89
      ev: 失败/阻塞保留错误证据，不画成功勾
  - 21-13 [constraint] 主仓库 README 的工作台汇总公开可共享的状态，不暴露私密研究分支结构。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/21-ahc068-to-rmtc-decision-study-2026-10-28.md:89
      ev: 不暴露私密研究分支结构
  - 22-01 [technical] 资源计划使用同一虚拟R累加后再取封顶分差，不能把各资源按初始R各算一次。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/22-latest-branches-and-ahc-review-2026-10-28.md:61
      ev: 使用同一虚拟R累加后再取封顶分差
  - 22-02 [technical] 禁止同一资源重复计分；要记录途中已取资源。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/22-latest-branches-and-ahc-review-2026-10-28.md:62
      ev: 禁止同一资源重复计分
  - 22-03 [process] H=3/B=5 是提议，不是已调好的参数；先保证单步结算准确。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/22-latest-branches-and-ahc-review-2026-10-28.md:63
      ev: H=3/B=5 是提议，不是已调好的参数
  - 22-04 [technical] Beam 后续候选须保留不同首动作，不能只增大束宽却全走同路。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/22-latest-branches-and-ahc-review-2026-10-28.md:64
      ev: 不能只增大束宽却全走同路
  - 22-05 [constraint] 只能重排尚未执行目标与路径，不能回滚裁判 Tick。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/22-latest-branches-and-ahc-review-2026-10-28.md:65
      ev: 不能回滚裁判 Tick
  - 22-06 [technical] 目标迟滞：危险、目标消失、任务完成、不可达必须能立即打断。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/22-latest-branches-and-ahc-review-2026-10-28.md:67
      ev: 危险、目标消失、任务完成、不可达必须能立即打断
  - 22-07 [constraint] 对手继续移动/攻击/防御只能是情景，不能改写当前真实占位或假设 MOVE 躲当前攻击。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/22-latest-branches-and-ahc-review-2026-10-28.md:69
      ev: 只能是情景，不能改写当前真实占位
  - 22-08 [constraint] 保留确定规则与八 Tick 已知危险筛选；H=3 不能替换它。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/22-latest-branches-and-ahc-review-2026-10-28.md:70
      ev: H=3 不能替换它
  - 22-09 [technical] 目标持续性：换场清空，死亡不强行延续追击；原目标消失、已完成、过期、不可达即失效。迟滞是决策成本，不能加到官方分数里。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/22-latest-branches-and-ahc-review-2026-10-28.md:78
      ev: 迟滞是决策成本，不能加到官方分数里
  - 22-10 [technical] 资源只收一次，途中顺路资源也应计入；未知格不当空地，预测收益不回写真实 score；两资源比较必须同时受剩余比赛时间、路线危险和已有任务目标约束。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/22-latest-branches-and-ahc-review-2026-10-28.md:79
      ev: 未知格不当空地，预测收益不回写真实 score
  - 22-11 [constraint] Beam 预算耗尽交回已有合法基线动作；未知对手动作分情景，不能宣称已标定概率。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/22-latest-branches-and-ahc-review-2026-10-28.md:80
      ev: 不能宣称已标定概率
  - 22-12 [process] 原版完整对局和 AI 及时率仍是 P0；不能跳过整局验收就给策略提升打勾。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/22-latest-branches-and-ahc-review-2026-10-28.md:82
      ev: 不能跳过整局验收就给策略提升打勾
  - 22-13 [process] 未来参赛算法改动后应重新审查预期，不把旧结果贴到新代码上。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/22-latest-branches-and-ahc-review-2026-10-28.md:55
      ev: 不把旧结果贴到新代码上
  - 22-14 [constraint] 旧原件、practice、上游快照及其哈希不改；只在现有研究分支提交，不创建新分支、不动 main 或参赛 PR。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/22-latest-branches-and-ahc-review-2026-10-28.md:88
      ev: 旧原件、practice、上游快照及其哈希不改
  - 23-01 [constraint] main README 扩充为有限例外，只改 README；不合并研究历史，不将两支名称/入口写入 main 或代码 PR。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/23-incoming-analysis-and-planning-2026-10-28.md:11
      ev: 只改README；不合并研究历史
  - 23-02 [technical] 搜索结果只交首步，下一帧读裁判位置和回执；没有预先改写真实状态。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/23-incoming-analysis-and-planning-2026-10-28.md:26
      ev: 结果只交首步，下一帧读裁判位置和回执
  - 23-03 [goal] 后续在正常 Ubuntu22.04/Humble 环境按原 PDF 流程先仅接 A 再接 B/C/D，固定地图/席位/种子、记录 R/D/M/死亡/无效动作/AI 及时率；只修改集中配置再编译，原 practice 不动。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/23-incoming-analysis-and-planning-2026-10-28.md:44
      ev: 先仅接A再接B/C/D，固定地图/席位/种子
  - 23-04 [constraint] 用户授权网络不改变当前平台实际拒绝的系统调用，没有绕过权限限制。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/23-incoming-analysis-and-planning-2026-10-28.md:42
      ev: 没有绕过权限限制
  - 24-01 [constraint] 原版 practice 的 18 文件逐字节未变。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/24-multistyle-arena-tuning-and-gateway-2026-10-28.md:7
      ev: 原版practice的18文件逐字节未变
  - 24-02 [constraint] 比赛从编译期 match_config 生成固定值对象；只有离线评测注入参数。不存在赛中 JSON/ROS 调参入口，伤害距离/结算常量不搜索。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/24-multistyle-arena-tuning-and-gateway-2026-10-28.md:13
      ev: 不存在赛中JSON/ROS调参入口
  - 24-03 [constraint] 绝不回滚已执行 Tick，也不把路线当真实位置。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/24-multistyle-arena-tuning-and-gateway-2026-10-28.md:14
      ev: 绝不回滚已执行Tick
  - 24-04 [constraint] 对手情景权重不是概率或纳什解。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/24-multistyle-arena-tuning-and-gateway-2026-10-28.md:15
      ev: 情景权重不是概率或纳什解
  - 24-05 [constraint] 连续失败改道只按可信 last_action 核对；未按意图自增坐标。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/24-multistyle-arena-tuning-and-gateway-2026-10-28.md:16
      ev: 未按意图自增坐标
  - 24-06 [metric] 每轮保留基线和只开改道参照，无非法动作且采集训练平均不得下降超过 1 分才可入选。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/24-multistyle-arena-tuning-and-gateway-2026-10-28.md:25
      ev: 无非法动作且采集训练平均不得下降超过1分才可入选
  - 24-07 [process] 首轮训练优胜者在 19001 留出种子退步，没有采纳；不能继续称 19001 未见。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/24-multistyle-arena-tuning-and-gateway-2026-10-28.md:25
      ev: 不能继续称19001未见
  - 24-08 [constraint] 小样本/地图席位相关，不做正式显著性或必胜判断。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/24-multistyle-arena-tuning-and-gateway-2026-10-28.md:36
      ev: 不做正式显著性或必胜判断
  - 24-09 [constraint] 赛事网关行为只据该转贴；未取得独立官方公告网址。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/24-multistyle-arena-tuning-and-gateway-2026-10-28.md:50
      ev: 赛事网关行为只据该转贴
  - 24-10 [constraint] 未将用户“模型调用没问题”的推进指令扩大成目标 WSL 已联通或正式资格通过的结论。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/24-multistyle-arena-tuning-and-gateway-2026-10-28.md:54
      ev: 未将……扩大成……正式资格通过的结论
  - 24-11 [goal] 下一步验收：在正常 ROS 环境运行原版完整对局与正式网关，核对保护倒数、全部事件组合和解释生效前可用率。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/24-multistyle-arena-tuning-and-gateway-2026-10-28.md:58
      ev: 在正常ROS环境运行原版完整对局与正式网关
  - 24-12 [process] 扩展对手池后使用新的训练/留出批次，保留失败，不追求把所有新增模块默认打开。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/24-multistyle-arena-tuning-and-gateway-2026-10-28.md:58
      ev: 使用新的训练/留出批次，保留失败
  - 25-01 [process] 复现同类问题，不冒充原场复盘。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/25-motion-loops-and-recovery-2026-10-28.md:3
      ev: 复现同类问题，不冒充原场复盘
  - 25-02 [technical] 公开席位打破同分对称，未知图不补成空地。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/25-motion-loops-and-recovery-2026-10-28.md:9
      ev: 公开席位打破同分对称，未知图不补成空地
  - 25-03 [constraint] 当前致命防御/已知危险仍优先；原本正常移动默认不改成 WAIT。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/25-motion-loops-and-recovery-2026-10-28.md:11
      ev: 原本正常移动默认不改成WAIT
  - 25-04 [constraint] 四个新增导航参数集中原头文件，旧权重不重调，新阈值不称优化到最优。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/25-motion-loops-and-recovery-2026-10-28.md:11
      ev: 旧权重不重调，新阈值不称优化到最优
  - 25-05 [constraint] 持续 500Tick 反伤是放大错误的压力用例，不当作正式标准事件时长。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/25-motion-loops-and-recovery-2026-10-28.md:15
      ev: 不当作正式标准事件时长
  - 25-06 [constraint] 小样本、地图席位相关、自建规则及延迟 oracle 均限制结论，不宣传正式胜率。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/25-motion-loops-and-recovery-2026-10-28.md:17
      ev: 不宣传正式胜率
  - 25-07 [process] 尚未输出带条件的未来动作队列，也没有按事件截止动态调整 HTTP 超时；本轮未借导航修复冒称完成这一时效调度设想。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/25-motion-loops-and-recovery-2026-10-28.md:25
      ev: 本轮未借导航修复冒称完成这一时效调度设想
  - 25-08 [constraint] 研究材料不进入代码 PR 或其他公开导航。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/25-motion-loops-and-recovery-2026-10-28.md:27
      ev: 研究材料不进入代码PR或其他公开导航
  - 26-01 [process] 区分来源叙述与可运行证据，逐项记录采纳/已有/暂缓/不适用，不转载原字幕或模型思考内容。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/26-subtitle-counterexamples-and-risk-ordering-2026-10-28.md:3
      ev: 区分来源叙述与可运行证据
  - 26-02 [constraint] 每版 32 例是 4 席位×4 旋转×2 固定敌方动作，不是 32 独立地图；未伪造无风险保证。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/26-subtitle-counterexamples-and-risk-ordering-2026-10-28.md:7
      ev: 不是32独立地图……未伪造无风险保证
  - 26-03 [constraint] 固定六风格 NPC 使用公开局部观测及公告后延迟 oracle，不是官方标准车、LLM 调用或正式资格证明。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/26-subtitle-counterexamples-and-risk-ordering-2026-10-28.md:9
      ev: 不是官方标准车、LLM调用或正式资格证明
  - 26-04 [constraint] 该修复针对确定反例，不能宣称普遍提高分数。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/26-subtitle-counterexamples-and-risk-ordering-2026-10-28.md:15
      ev: 该修复针对确定反例，不能宣称普遍提高分数
  - 26-05 [process] 既有 PR 保持开放未合并；main 矩阵按已有授权扩至 R45，仅 README。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/26-subtitle-counterexamples-and-risk-ordering-2026-10-28.md:17
      ev: 既有PR保持开放未合并
  - 27-01 [constraint] 复核为只读离线分析，观赛真值不交给参赛策略，没有修改 practice、回放地图到生产程序或发送模型请求。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/27-late-practice-log-integrity-2026-10-28.md:5
      ev: 观赛真值不交给参赛策略
  - 27-02 [process] 没有把重复日志计为两局或 1000Tick，也不据此判程序重复推进策略。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/27-late-practice-log-integrity-2026-10-28.md:10
      ev: 没有把重复日志计为两局
  - 27-03 [constraint] 不同场数据不能拼接；观察到归档不一致时不无证据修改原裁判。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/27-late-practice-log-integrity-2026-10-28.md:16
      ev: 不无证据修改原裁判
  - 27-04 [constraint] A 25 成功仅为该场网关审计，不能代替正式网关资格。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/27-late-practice-log-integrity-2026-10-28.md:18
      ev: 不能代替正式网关资格
  - 27-05 [process] 仅凭新提交 until 字样不作精确二进制归因。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/27-late-practice-log-integrity-2026-10-28.md:20
      ev: 仅凭新提交until字样不作精确二进制归因
  - 28-01 [constraint] 单局样本：所有策略修复建议均为假设，标待测试，批量对局验证前不改集中参数默认值。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/28-first-real-llm-dds-battle-2026-10-29.md:3
      ev: 批量对局验证前不改集中参数默认值
  - 28-02 [goal] 用户已明确授权跑大量局，不同地图不同对手，轮番检测看回放找问题。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/28-first-real-llm-dds-battle-2026-10-29.md:107
      ev: 跑大量局，不同地图不同对手，轮番检测看回放找问题
  - 28-03 [process] 批量对局矩阵：地图 × 对手 × 参数；每组合跑多局，每局完整留存 ai.jsonl/score/frames/四 bot 日志与回放。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/28-first-real-llm-dds-battle-2026-10-29.md:109
      ev: 每局完整留存 ai.jsonl/score/frames/四 bot 日志与回放
  - 28-04 [metric] 每局自动产出核对表（R/D/M/分数、LLM 审计、词表裁决、问题清单），逐 tick 比对回放，不只看终局分数；把静止段-死亡模式作为批量统计指标。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/28-first-real-llm-dds-battle-2026-10-29.md:110
      ev: 逐 tick 比对回放，不只看终局分数
  - 28-05 [constraint] 回放驱动修复候选全部标待测试，批量验证前不改集中参数默认值。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/28-first-real-llm-dds-battle-2026-10-29.md:111
      ev: 全部标待测试，批量验证前不改集中参数默认值
  - 28-06 [constraint] 计分实现在原版 ELF 中、源码不可审，公式的完全验证以裁判输出为准。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/28-first-real-llm-dds-battle-2026-10-29.md:124
      ev: 公式的完全验证以裁判输出为准
  - 29-01 [constraint] 全部新杠杆以冠军逐位一致为默认（0/false），晋升必须经过 train 评估与 heldout 一次性验证。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/29-review-fixes-and-postcap-lever-2026-10-29.md:11
      ev: 晋升必须经过 train 评估与 heldout 一次性验证
  - 29-02 [goal] post_cap_combat_weight=0.02 晋升进正式配置（heldout 一次性验证通过）；stale_grace_ticks 与 worst_case_survival 保持默认关。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/29-review-fixes-and-postcap-lever-2026-10-29.md:5
      ev: post_cap_combat_weight=0.02 晋升进正式配置
  - 29-03 [process] run_arena.py 非调参入口不再读过期 selected-parameters.json；每份报告记录 competition_parameters 与 binary_sha256，自证测的就是当前比赛程序。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/29-review-fixes-and-postcap-lever-2026-10-29.md:26
      ev: 自证测的就是当前比赛程序
  - 29-04 [metric] 验证：bash tests/run.sh 退出码 0；announcement_benchmark 退出码 0。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/29-review-fixes-and-postcap-lever-2026-10-29.md:28
      ev: bash tests/run.sh 退出码 0
  - 29-05 [metric] 真实对局风险标注：若真实局 deaths 显著上升而无平局翻盘，回退 0。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/29-review-fixes-and-postcap-lever-2026-10-29.md:97
      ev: 若真实局 deaths 显著上升而无平局翻盘，回退 0
  - 29-06 [process] 已知代价（deaths 上升）记录在 match_config 注释。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/29-review-fixes-and-postcap-lever-2026-10-29.md:48
      ev: 已知代价记录在 match_config 注释
  - 30-01 [metric] 对照判据（预先注册）：deaths 显著上升 = A deaths 均值 ≥ 9 且中位数 ≥ 8。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/30-real-battle-baseline-and-postcap-batch-2026-10-29.md:33
      ev: 显著上升 = 均值 ≥ 9 且中位数 ≥ 8
  - 30-02 [metric] 回退判据：若 deaths 显著上升（均值≥9 且中位数≥8）且平局翻盘 0 次 → 回退 0.02；若翻盘 ≥1 次，保留 0.02 并把死亡代价记入 match_config 注释。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/30-real-battle-baseline-and-postcap-batch-2026-10-29.md:39
      ev: 回退判据（docs/29 §4.3 落地）
  - 30-03 [metric] 口径（已逐帧验证）：死亡 = alive true→false 边沿；死亡窗口 3 tick（hp=0），重生回满 100；每次死亡 effective_damage −40。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/30-real-battle-baseline-and-postcap-batch-2026-10-29.md:7-8
      ev: 死亡 = alive true→false 边沿
  - 30-04 [process] 批量归档须会话自洽校验通过、key 扫描干净。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/30-real-battle-baseline-and-postcap-batch-2026-10-29.md:43
      ev: 8 局会话自洽校验通过，key 扫描干净
  - 30-05 [metric] 判定：保留 post_cap_combat_weight=0.02（死亡未显著上升 6.62<7.0，D 大幅上升 +314，R 反升 6.2）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/30-real-battle-baseline-and-postcap-batch-2026-10-29.md:67
      ev: 判定：保留 post_cap_combat_weight=0.02
  - 30-06 [process] 若确认本地圈耗尽后目标选择被战斗劫持，考虑新杠杆（默认关，train 评估 + heldout 一次性验证后决定）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/30-real-battle-baseline-and-postcap-batch-2026-10-29.md:77
      ev: 考虑新杠杆（默认关，train 评估 + heldout 一次性验证后决定）
  - 31-01 [constraint] 没有合法输入能让 A 知道该资源存在——规则不允许读全图。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/31-replay-investigation-two-losses-2026-10-30.md:23
      ev: 规则不允许读全图
  - 31-02 [constraint] 杠杆候选全部否决（合法输入内无解）：未侦察资源价值外推读全图违规；vision=4 规则固定。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/31-replay-investigation-two-losses-2026-10-30.md:39
      ev: 读全图违规
  - 31-03 [process] 探索方向覆盖最大化列为下轮候选 L-c（默认关，train 评估 + heldout 一次性验证后再议）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/31-replay-investigation-two-losses-2026-10-30.md:42
      ev: 列为下轮候选 L-c（默认关，train 评估 + heldout 一次性验证后再议）
  - 31-04 [metric] 对照指标沿用 docs/30 §4，新增开局 t30 内收集完成率与零浪费率作为观察项。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/31-replay-investigation-two-losses-2026-10-30.md:47
      ev: 新增开局 t30 内收集完成率与零浪费率作为观察项
  - 32-01 [process] 预注册协议：train 评估按 [train[:6], train[:16], train] 赛程（保 6→2，baseline+collision_only 恒在）；selection_guard（invalid=0、stage1 ≥ baseline_stage1−1）；heldout 只在选定后评一次；不迭代 h
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/32-lc-coverage-exploration-2026-10-30.md:30
      ev: heldout 只在选定后评一次；不迭代 heldout
  - 32-02 [process] 若 train 无正收益或决策改变率 ≈0 → 杠杆关闭；混合信号 → 按 frontier 分拆先例把参数改为仅 stage-2 生效再评，不在本轮直接晋升。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/32-lc-coverage-exploration-2026-10-30.md:30
      ev: 不在本轮直接晋升
  - 32-03 [process] 判据在 heldout 运行前已定，不做事后改口。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/32-lc-coverage-exploration-2026-10-30.md:49
      ev: 判据在 heldout 运行前已定，不做事后改口
  - 32-04 [metric] heldout 晋升条件（预注册）：heldout objective(selected) ≥ objective(baseline) + 0.01 且 invalid=0；任一不满足 → 家族关闭，explore_component_value 保持 0。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/32-lc-coverage-exploration-2026-10-30.md:65
      ev: 晋升条件：heldout objective(selected) ≥ objective(baseline) + 0.01 且 invalid=0
  - 32-05 [process] 协议修正：杠杆 heldout 的晋升基准是冠军封存 heldout，冻结基线只作可比性校验（修正方向与晋升相反、从严）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/32-lc-coverage-exploration-2026-10-30.md:79
      ev: 晋升基准是冠军封存 heldout，冻结基线只作可比性校验
  - 32-06 [metric] 裁决：L-c 家族关闭，explore_component_value 保持 0，永久保留（代码保留、默认关、冠军逐位一致，供后人对照）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/32-lc-coverage-exploration-2026-10-30.md:83
      ev: 家族关闭，explore_component_value 保持 0
  - 32-07 [technical] L-c 参数默认 0 = 冠军逐位一致（标号整段跳过，提前停止界与 utility 表达式在 +0.0 恒等下与旧式全等）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/32-lc-coverage-exploration-2026-10-30.md:11
      ev: 默认 0 = 冠军逐位一致
  - 33-01 [metric] 死亡分类判据：burst n≤2；sustained n≥3；retreatable n≥4 且死亡 tick 存在安全方向（四方向一步至界内非墙、与全部敌人切比雪夫>2）且 hp<80。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/33-t5-announcement-windows-and-death-predictability-2026-10-29.md:17-20
      ev: retreatable：n ≥ 4 且死亡 tick 存在安全方向且 hp < 80
  - 33-02 [process] 勘误声明：撤回易伤窗口内伤害 4680 旧口径（正确 180）与 docs/31 B0 无预告事件伤害归因（实为 B 三次普通攻击）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/33-t5-announcement-windows-and-death-predictability-2026-10-29.md:23-25
      ev: 本档案撤回两处早期口径
  - 33-03 [metric] 易伤克制类杠杆头寸不足（窗口内战斗伤害 180、死亡 2），本轮降级不做。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/33-t5-announcement-windows-and-death-predictability-2026-10-29.md:72
      ev: 可干预对象只有 180 伤害、2 死。降级
  - 33-04 [technical] low_hp_attack_discount 杠杆设计：默认 1.0 = 冠军逐位一致；自身 hp<60 且本 tick 未被火力波及（incoming==0）时攻击估值乘折扣因子；还手不折扣；两处落点 strategy.cpp §6 攻击估值与 tactics.cpp 深度 0 攻击分支同口径。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/33-t5-announcement-windows-and-death-predictability-2026-10-29.md:114-117
      ev: 默认 1.0 = 冠军逐位一致……还手不折扣
  - 33-05 [process] sweep {0.7, 0.4, 0.1}；协议同前：train 全量评估 + selection_guards，选中后 heldout 一次性 vs 冠军封存 0.8299。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/33-t5-announcement-windows-and-death-predictability-2026-10-29.md:118
      ev: heldout 一次性 vs 冠军封存 0.8299
  - 33-06 [process] U3 勘误：爆炸区零伤害降级为与预告一致，因果未证实；战斗归因（切比雪夫≤2）标候选；8 例可撤退改待复核（攻击先于移动，需更早 Tick 行动反事实）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/33-t5-announcement-windows-and-death-predictability-2026-10-29.md:136
      ev: 8 例可撤退改待复核
  - 34-01 [metric] 预注册判据：1. train 选择 = 满足 selection_guards 的候选中取 train objective 最高者。2. heldout 晋升判据 = 选中者的 heldout objective ≥ 冠军封存 0.8299（同 30 场景）；冻结 baseline 行必须逐位复现 0.7710073（
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/34-lowhp-attack-discount-2026-10-29.md:19-23
      ev: 冻结 baseline 行必须逐位复现 0.7710073（确定性钉）
  - 34-02 [process] 判据写于 heldout 运行前（heldout 正在后台运行），结果与裁决在判据之后补写。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/34-lowhp-attack-discount-2026-10-29.md:19
      ev: 写于 heldout 运行前
  - 34-03 [process] train 数字不作结论，由 heldout 一次性裁决。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/34-lowhp-attack-discount-2026-10-29.md:39
      ev: train 数字不作结论
  - 34-04 [metric] 裁决：0.8286479 < 0.8298625，差 −0.0012 → 不达标。家族关闭：low_hp_attack_discount 保持 1.0，不作第二次 heldout（不回头改）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/34-lowhp-attack-discount-2026-10-29.md:53
      ev: 家族关闭：low_hp_attack_discount 保持 1.0
  - 34-05 [process] 事后解读写死于此，不用于翻案。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/34-lowhp-attack-discount-2026-10-29.md:57
      ev: 事后解读（写死于此，不用于翻案）
  - 35-01 [process] 本档案在批量完成前预注册判据，结果与裁决补写在后。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/35-t30-opening-metrics-batch-2026-10-29.md:3
      ev: 在批量完成前预注册判据
  - 35-02 [metric] 新指标定义：t30 收集完成率 = R@t30 / 200（图总 R 恒 200）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/35-t30-opening-metrics-batch-2026-10-29.md:15
      ev: t30 收集完成率 = R@t30 / 200
  - 35-03 [metric] 零浪费率：相邻拾取间隔 ticks 与 18×18 无障碍 BFS 最短移动数的比值 Σmin/Σactual；BFS 是可达下界。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/35-t30-opening-metrics-batch-2026-10-29.md:16
      ev: 零浪费段 = 间隔恰等于下界
  - 35-04 [metric] deaths 护栏沿用：显著上升 = 均值≥9 且中位≥8。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/35-t30-opening-metrics-batch-2026-10-29.md:27
      ev: 显著上升 = 均值≥9 且中位≥8
  - 35-05 [process] 本轮目的不是杠杆裁决；发现明确损失路径才写下一个改进，否则不写。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/35-t30-opening-metrics-batch-2026-10-29.md:31
      ev: 发现明确损失路径才写下一个改进，否则不写
  - 35-06 [technical] 下一个杠杆（预注册）：拾取任务资源后，若地图仍有剩余资源，优先以最短路径抢最近剩余资源，到达 [9,9] 推迟至地图耗尽或无可达资源；默认关（冠军逐位一致）；按协议 train 全量评估 + selection_guards + 预注册一次性 heldout。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/35-t30-opening-metrics-batch-2026-10-29.md:85
      ev: 到达 [9,9] 推迟至地图耗尽或无可达资源
  - 35-07 [metric] 下轮真实批量预注册判据：耗尽时 A 份额均值回升、拾取数回升、t30 完成率 ≥0.356；deaths/damage_events 沿用均值≥9 且中位≥8 防线。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/35-t30-opening-metrics-batch-2026-10-29.md:86
      ev: t30 完成率 ≥0.356
  - 35-08 [process] 被 validate_config 拒绝的变体按终局处理、单独报告，不当作机器人输赢。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/35-t30-opening-metrics-batch-2026-10-29.md:35
      ev: 变体 7 被 validate_config 拒绝（……），驱动器按终局处理
  - 36-01 [technical] race_reach_holdoff 杠杆设计：double [0,1]，默认 0.0 = 冠军逐位一致；条件 stage_==2 && holdoff>0 && resource_value<120 && 存在已知可达资源；作用 reach_mission 估值 × (1−holdoff)；资源清空后恢复原权重；不动
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/36-race-reach-holdoff-2026-10-29.md:16-19
      ev: 默认 0.0 = 冠军逐位一致
  - 36-02 [process] 诚实边界：V0/V2 型发现力损失（冻结时已知资源为 0）不在本杠杆射程内。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/36-race-reach-holdoff-2026-10-29.md:20
      ev: 不在本杠杆射程内
  - 36-03 [metric] 预注册判据：train 选择 = selection_guards 下 objective 最高者；train 全胜零差异 → 不选（家族关闭，默认 0.0 保持）；heldout 晋升 = objective ≥ 冠军封存 0.8298625；冻结 baseline 逐位复现 0.7710073（确定性钉）否则作废重
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/36-race-reach-holdoff-2026-10-29.md:26-30
      ev: heldout 晋升判据：选中者的 heldout objective ≥ 冠军封存 0.8298625
  - 36-04 [constraint] 杠杆触发条件只依据本队感知（known-reachable tiles_：tile.value>0 && !tile.wall && paths 有解），不读取 config、观赛 map_view 或地图真值——符合参赛程序只能依据本队感知估计的要求。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/36-race-reach-holdoff-2026-10-29.md:52
      ev: 不读取 config、观赛 map_view 或地图真值
  - 36-05 [metric] 裁决：家族在 train 关闭，race_reach_holdoff 保持 0.0（冠军配置不变），不做 heldout；真实检验转实战批次。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/36-race-reach-holdoff-2026-10-29.md:48-50
      ev: 家族在 train 关闭：race_reach_holdoff 保持 0.0
  - 36-06 [process] 真实检验 = docs/35 §5 预注册批次判据，按 batch_practice 惯例以 config 参数覆盖 A=rrh10/rrh08 对照冠军，赛后按真值指标离线核算。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/36-race-reach-holdoff-2026-10-29.md:54
      ev: 赛后按真值指标离线核算
  - 37-01 [process] rrh10 中断（Windows 内存回收杀驱动，非对局故障）如实记录；battle 3–6 未跑；驱动支持 --only <vid> 逐局干净续跑；续跑须待内存回升且用户确认。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/37-race-batches-real-battles-2026-10-29.md:16-21
      ev: 续跑须待内存回升且用户确认
  - 37-02 [metric] 判据核对（docs/35 §5 预注册）：耗尽时 A 份额、拾取数、t30 完成率三项回升判据；deaths/damage_events 护栏需 mean≥9 且 median≥8 才触发。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/37-race-batches-real-battles-2026-10-29.md:23-32
      ev: deaths mean/median……未触发 revert 守卫（需 mean≥9 且 median≥8）
  - 37-03 [metric] 最终裁决：t30 完成率是预注册硬门槛（≥0.356），终值 0.306 未过线 → 不晋升，race_reach_holdoff 家族关闭于 0.0，冠军保持位元钉 eb321df。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/37-race-batches-real-battles-2026-10-29.md:85
      ev: t30 完成率是预注册硬门槛（≥0.356），终值 0.306 未过线
  - 37-04 [process] 已执行：match_config.hpp 还原 0.0（与 HEAD 逐位一致）+ 重建；scenario_test.py 12/12 OK（重建后重跑）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/37-race-batches-real-battles-2026-10-29.md:85
      ev: match_config.hpp 还原 0.0（与 HEAD 逐位一致）+ 重建（29.1s）
  - 37-05 [metric] 公告窗口场景对完成并采纳：timely/late 分支（180 开局/200 断点/205 终点）；12/12 回归全绿。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/37-race-batches-real-battles-2026-10-29.md:89
      ev: 12/12 回归全绿
  - 37-06 [goal] stage-2 证据缺口（原版对局 + 自战联赛）仍待 C7/U6 版本联赛实施；当前唯一 stage2 锚点仍是训练集 41.25，距离 50 目标尚远。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/37-race-batches-real-battles-2026-10-29.md:60
      ev: 距离 50 目标尚远
  - 37-07 [goal] 下一站：docs/38 版本联赛（seat 变体 + 原版对局 + 自战），补齐 stage-2 证据缺口。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/37-race-batches-real-battles-2026-10-29.md:99
      ev: 补齐 stage-2 证据缺口
  - 37-08 [process] 首分钟资源争抢 = 损失路径仍成立（剂量-响应 0.0/0.8/1.0：份额 0.279/0.336/0.344、均分 42.50/45.36/45.94）；后续回合按 T5 处方优先处理尚未闭环项（低血量预测失败、资源争抢时间线、可用公告窗口、同分 D 争夺）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/37-race-batches-real-battles-2026-10-29.md:98
      ev: 后续回合按 T5 处方优先处理尚未闭环项
  - 38-01 [goal] 版本联赛目的：补齐 stage-2 证据缺口——与原版的一局 + 自己打自己不同模型（原版证据部分成立 + 冻结二进制自战版本联赛）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/38-version-league-spec-2026-10-29.md:3
      ev: 补齐 stage-2 证据缺口
  - 38-02 [constraint] 本规格不启动任何构建/对局（内存未恢复），先冻结设计。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/38-version-league-spec-2026-10-29.md:4
      ev: 本规格不启动任何构建/对局
  - 38-03 [protocol] 每个版本一个独立构建目录（colcon --build-base build-v-X --install-base install-v-X），二进制 sha256 冻结；同一版本在全部对局中位元不变。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/38-version-league-spec-2026-10-29.md:18
      ev: 二进制 sha256 冻结；同一版本在全部对局中位元不变
  - 38-04 [protocol] 选手参数只在 match_config.hpp（编译期），无运行时参数注入；席位/令牌也是 constexpr；自战第二席位 = 同源码换席位重建；每版本构建 4 个席位变体（A/B/C/D）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/38-version-league-spec-2026-10-29.md:18
      ev: 无运行时参数注入……每版本构建 4 个席位变体
  - 38-05 [metric] 144 场/版本起步 = 12 图 × 4 席位 × 3 对手混合（M1 原版陪练、M2 自战旧冠军、M3 自战候选）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/38-version-league-spec-2026-10-29.md:22-28
      ev: 144 场/版本起步 = 12 图 × 4 席位 × 3 对手混合
  - 38-06 [protocol] 12 张图 = 固定 12 个 practice seed（一次性选定并随清单冻结）；4 席位 = 本版本轮换出生席位（每图每混合各 1 局，席位轮换消出生位置偏差）。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/38-version-league-spec-2026-10-29.md:30-31
      ev: 12 seed 一次性选定并随清单冻结
  - 38-07 [metric] 先 24 场试点（2 图 × 4 席位 × 3 混合）验证调度器与双选手同场后再放量；144 场/版本 ≈ 12 小时。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/38-version-league-spec-2026-10-29.md:33
      ev: 先 24 场试点……验证调度器与双选手同场后再放量
  - 38-08 [protocol] 每局归档：代码 SHA、完整参数（params_digest）、AI 模式、session_id、最终名次、score/R/D/M/hp/invalid；版本级报告：原始分、平均名次、首末位比、R/D/M 均值、无效动作、死亡数、卡住、超预算；按初始地图成组，保留最差样本；全部随批上传 log 分支（batch 归档 
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/38-version-league-spec-2026-10-29.md:35-37
      ev: 按初始地图成组，保留最差样本
  - 38-09 [protocol] 短序列差分验收：向原版 practice 与自建引擎输入相同合法动作序列，核对攻击/死亡/重生/增益时序与分数；差分只作一致性证据，不替代原版对局；practice 原文件保持只读，测试驱动/临时配置/结果放外部。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/38-version-league-spec-2026-10-29.md:39-41
      ev: 差分只作一致性证据，不替代原版对局
  - 38-10 [process] 里程碑：1. 内存恢复 → 还原冠军二进制（holdoff 1.0→0.0 + rebuild，恢复位元钉）→ 跑 12 场景回归。2. tools/ 入库。3. 版本联赛调度器 + 席位变体构建脚本 → 24 场试点 → 放量 144×3 版本。4. rrh10 battle 3–6 续跑（--only 3..6，与
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/38-version-league-spec-2026-10-29.md:43-48
      ev: 内存恢复 → 还原冠军二进制 → 跑 12 场景回归
  - 38-11 [goal] stage2 目标 50 的当前锚点：训练集 41.25；联赛数据将给出原版/自战维度的真实名次与分数分布，作为 50 分验收的第一手证据。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/38-version-league-spec-2026-10-29.md:50
      ev: stage2 目标 50 的当前锚点：训练集 41.25
  - R-01 [protocol] 双方只 append，按实际写入时间顺序，不改写、删除、重排历史；每条注明北京时间、身份、回应 ID、接受/异议/待验证、相关提交 SHA、证据和下一步；旧记录有错时新增勘误，保留原记录；并发更新先重新读取再追加。
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:7
      ev: 双方只 append……不改写、删除、重排历史
  - R-02 [process] 归档检查：文件内所有 session 匹配目录、起止 Tick 完整、客户端/网关次数同一场、构建 SHA 和配置哈希对应；归档失败就标不配套，不要自动拼接；原日志不删除，追加勘误/对应说明。
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:17
      ev: 归档失败就标“不配套”，不要自动拼接
  - R-03 [protocol] 后续评测直接读取裁判 rank，并保留平局判定键；改善自己原始分与改善最终名次须分开报。
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:28
      ev: 改善自己原始分与改善最终名次须分开报
  - R-04 [process] 当前固定图做开发/回归；新种子和对手组做验证；代码、参数与验收口径冻结后，再用一次未看过的地图族/种子作最终检查；旧冠军的 0.8437 应连同其源码 SHA、参数与对手版本保存。
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:34
      ev: 再用一次未看过的地图族/种子作最终检查
  - R-05 [process] 若保留墙钟方式，至少轮换 A→B / B→A 顺序、重复场景、报告成对差值范围与超预算次数。
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:40
      ev: 至少轮换 A→B / B→A 顺序、重复场景
  - R-06 [process] T5 处方：把下一轮精力放在可复现失误与真实对局（低血量预测失败、资源争抢时间线、可用公告窗口、同分 D 争夺）；先找一条明确损失路径，再写一个小改进与一组配对反例。
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:48
      ev: 先找一条明确损失路径，再写一个小改进与一组配对反例
  - R-07 [process] 新增研究段落和实验档案迁到 docs/implementation/ 与 checks/code-results/，保留旧来源 SHA 和文件哈希；不迁入整段研究分支历史；不删原始材料、不改 practice/。
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:52
      ev: 保留旧来源 SHA 和文件哈希
  - R-08 [process] 运行完整原版 practice 时，把本场的代码 SHA、参数、AI 模式、session 与最终名次一起归档。
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:58
      ev: 把本场的代码 SHA、参数、AI 模式、session 与最终名次一起归档
  - R-09 [constraint] 规则规定不变的尺寸、总资源和时序不作为可调策略。
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:161
      ev: 规则规定不变的尺寸、总资源和时序不作为可调策略
  - R-10 [constraint] 不要将六个风格名等同于六套独立算法；对手先补共享前置判断之外的行为（低血量仍攻击、诱导防御、隘口占位、抢增益、持续追击与及时撤追）。
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:163
      ev: 不要将六个风格名等同于六套独立算法
  - R-11 [metric] 事件使用计数链：唯一公告事件数 → 关键字段解释正确数 → 最晚可用时刻前送达数 → 有可兑现机会数 → 改变行为数 → 实际收益；每层都允许合理的不行动；多调用、多改动作都不是优化目标，净得分/名次与费用才是。
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:171
      ev: 多调用、多改动作都不是优化目标；净得分/名次与费用才是
  - R-12 [protocol] 四组公告消融（U4）：A 不送结构化解释（保持同资格）/ B 公告后及时正确解释 / C 回放实际模型的解释错误与送达 Tick / D 同 C 只关一项行动机制；四组使用相同初态、事件安排、对手程序与随机种子、席位；回放不算新的真实成功，也不用于正式参赛输入。
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:185-192
      ev: 四组使用相同初态、事件安排、对手程序与随机种子、席位
  - R-13 [technical] 八类事件各自应验收效果（U5 矩阵）：爆炸/幻术/治疗/天下无双/世界分裂/火爆辣椒/洁身自好/易伤各须构造机会与冲突并记录效果（是否最后可出发点前改道、净少受伤/死亡、绕路成本、正确率、净D等）；另加同 Tick 多事件、增益与负面叠加、重复/改写公告、缺字段、过期返回、旧 session 返回。
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:196-208
      ev: 八类事件各自应验收的“效果”，不是只检查 JSON
  - R-14 [protocol] U6 版本联赛落地条款：冻结旧冠军/当前冠军/候选完整源码 SHA、参数与二进制；每版本独立 worker 保留跨 Tick 状态；144 场/版本起步（12 图×4 席位×3 混合）；不要把旋转/镜像或四席位计作独立新地图；报告原始分、平均名次、第一/末位比例、R/D/M、无效动作、死亡、卡住、超预算；差异按初始地图
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:213-219
      ev: 按请求数/token/费用设停止条件
  - R-15 [constraint] U7：参赛程序只能依据本队感知、回执、可用公开公告与合法记忆估计，不能读取 config、观赛 map_view 或别车感知；试验时把资源总量真值用于赛后指标，策略触发条件另写清楚；配置被拒绝的一场应计为生成/校验失败并单独报告，不能当作机器人输赢，也不应静默减少样本量。
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:227
      ev: 不能读取 config、观赛 map_view 或别车感知
  - R-16 [constraint] 人工夹具不等同正式比赛已发生状态；夹具仅用于构造反例，不作为对战证据。
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:297
      ev: 夹具仅用于构造反例，不作为对战证据
  - R-17 [technical] 断点只在完整 Tick 边界，不在同 Tick 的攻击/移动中间（已知限制，接受）。
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:297
      ev: 断点当前只在完整Tick边界
  - R-18 [process] 首个场景实验定为 180 开局 → 200 断点 → 205 终点，公告及时 vs 迟到分支（对应 T5 处方可用公告窗口失误族）。
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:299
      ev: 180 开局 → 200 断点 → 205 终点
  - R-19 [technical] base_off={} 会继承已晋升的 post_cap=0.02，今天重跑不再是关闭态；需先修口径再扩大规模。
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:213
      ev: 需先修口径再扩大规模
  - R-20 [process] 定时检查未创建成功（too_many_active_automations）；后续若启用，按远端实质变更追加，跳过纯 ChatGPT review 提交。
      src: D:/code/The-Logical-Structure-of-RMT-C/review.md:62
      ev: 没有创建成功，也没有停用现有任务
  - 09-01 [process] 清单是任务队列，不是已经实现的功能；每项应关联验证日志和规则来源；不把参考 repo 高分作为完成证明。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/09-implementation-checklist.md:23
      ev: 以上是任务队列，不是已经实现的功能
  - 09-02 [goal] 在目标 ROS 2 环境完成公开话题接入、正确 QoS、session/tick 处理和真实 last_action 回执。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/09-implementation-checklist.md:13
      ev: 完成公开话题接入、正确QoS、session/tick处理和真实last_action回执
  - 09-03 [process] 固定地图/座位/对手比较新旧版，再上未调参种子验收；保留最佳。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/09-implementation-checklist.md:19
      ev: 固定地图/座位/对手比较新旧版，再上未调参种子验收
  - 09-04 [goal] 赛前在预期有线/主机/虚拟机网络配置下完成 DDS 双向、真实动作回执与完整对局；按 10-31 20:00 前材料递交准备。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/09-implementation-checklist.md:21
      ev: 按10-31 20:00前材料递交准备
  - 09-05 [technical] 复活路径禁止复用障碍会截断搜索的普通寻路。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/09-implementation-checklist.md:18
      ev: 禁止复用障碍会截断搜索的普通寻路
  - 09-06 [constraint] 不把任务 [12,12] 与堡垒区域合成同一固定对象。
      src: D:/code/The-Logical-Structure-of-RMT-C/docs/09-implementation-checklist.md:25
      ev: 不把任务[12,12]与堡垒区域合成同一固定对象

## result 2: scope=doc-comparison-main
- checks: [{"req_id": "GL-01", "status": "met", "evidence": "docs/01-source-review.md:76 — evidence string matches verbatim at cited line (FULL check on working tree ec9bb4e)"}, {"req_id": "GL-02", "status": "met", "evidence": "docs/01-source-review.md:77 — verbatim at cited line (FULL)"}, {"req_id": "GL-03", "status": "met", "evidence": "docs/38-version-league-spec-2026-10-29.md:50 — read directly: 'stage2 目标 50 的当前锚点：训练集 41.25；联赛数据将给出…50 分验收的第一手证据' (FULL)"}, {"req_id": "GL-04", "status": "met", "evidence": "docs/37-race-batches-real-battles-2026-10-29.md:60 — read directly (§6 item 4) verbatim (FULL); unchanged since cbd9fb7"}, {"req_id": "GL-05", "status": "met", "evidence": "docs/38-version-league-spec-2026-10-29.md:3 — read directly: '目的：补齐 stage-2 证据缺口…U6 判定：多 profile 自战档案不能代表旧版本或原版 robot_node' (PART due to ellipsis quoting)"}, {"req_id": "GL-06", "status": "met", "evidence": "docs/implementation/LESSONS.md:76 — read directly: '阶段一40分受TSP下界约束不可达（天花板≈37）；阶段二50分需要R≈90+M3+D500…两目标在当前规则与视野4下均不可达' (SLICE)", "gap": "trailing clause reworded: current text reads '不因此宣称已达到，也不宣称留出更差的结果是提升' instead of '目标是锚点，按不可达口径如实记载'; 锚点 framing now at docs/38:50", "action": "none — substance covered"}, {"req_id": "MT-01", "status": "met", "evidence": "docs/01-source-review.md:108 — read directly: 'S1 = 40 × R1 / 200' (FULL)"}, {"req_id": "MT-02", "status": "met", "evidence": "docs/01-source-review.md:110 — read directly: 'S2 = 30 × min(R/120, 1) + 15 × min(D/300, 1) + 5 × M' (FULL)"}, {"req_id": "MT-03", "status": "met", "evidence": "docs/03-tradeoffs.md:13 — verbatim at cited line (FULL)"}, {"req_id": "MT-04", "status": "met", "evidence": "docs/11-v1.1-rule-migration.md:13 — verbatim at cited line (FULL)"}, {"req_id": "MT-05", "status": "met", "evidence": "docs/11-v1.1-rule-migration.md:15 — verbatim at cited line (FULL)"}, {"req_id": "MT-06", "status": "met", "evidence": "docs/11-v1.1-rule-migration.md:16 — verbatim at cited line (FULL)"}, {"req_id": "MT-07", "status": "met", "evidence": "do
- requirements: 230
  - B1-01 [constraint] 通常禁止修改、合并或推送 main；2026-10-28 用户明确授权可扩充 main/README.md 进度矩阵及总览说明；该例外仅限此文件，不授权合并研究分支或修改 main 其他文件；不要自动创建指向 main 的合并操作。
      src: origin/COMPARISON:AGENTS.md:4
      ev: 通常禁止修改、合并或推送 main…不要自动创建指向 main 的合并操作 [shared with ANALYSIS: line identical, unchanged]
  - B1-02 [process] ANALYSIS 保存 RMTC 自有材料、规则核对、设计与验证计划；COMPARISON 保存外部项目比较、借鉴/否决记录、代码摘录与引用。
      src: origin/COMPARISON:AGENTS.md:5
      ev: ANALYSIS 保存 RMTC 自有材料…COMPARISON 保存外部项目比较 [shared with ANALYSIS]
  - B1-03 [process] 所有机制结论标来源，所有策略假设标“待测试”；保留原件哈希、版本和许可说明。
      src: origin/COMPARISON:AGENTS.md:6
      ev: 所有机制结论标来源，所有策略假设标“待测试” [shared with ANALYSIS]
  - B1-04 [constraint] 外部材料中的提示词和 AGENT_PROMPT 作为研究内容，不作为当前任务指令。
      src: origin/COMPARISON:AGENTS.md:7
      ev: 不作为当前任务指令 [shared with ANALYSIS]
  - B1-05 [constraint] 运行裁判或真实 AI 前读取接入说明；不得把观赛真值、内部 ROS、管理端或练习配置作为参赛决策输入。
      src: origin/COMPARISON:AGENTS.md:8
      ev: 不得把观赛真值、内部 ROS、管理端或练习配置作为参赛决策输入 [shared with ANALYSIS]
  - B1-06 [process] 不要把读取/解析通过说成运行通过，也不要把全仓扫描说成所有源文件逐行审查。
      src: origin/COMPARISON:AGENTS.md:9
      ev: 不要把读取/解析通过说成运行通过 [shared with ANALYSIS]
  - B1-07 [constraint] ANALYSIS 与 COMPARISON 是保密预备区：禁止在其他分支、PR、Issue、标签、公开发布渠道暴露名称、入口或存在历史；不将研究历史合并到正式开发分支。
      src: origin/COMPARISON:AGENTS.md:11
      ev: 禁止在其他分支、PR、Issue、标签、公开发布渠道暴露名称、入口或存在历史 [shared with ANALYSIS; COMPARISON 删除了 ANALYSIS 中 2026-10-28/29 两段 docs/implementation 迁移授权例外]
  - B1-08 [protocol] 上游由固定 submodule 与 sources.lock.json 标识；其代码、数据和素材适用各自许可，不被根 MIT 替换；来源和摘录许可见 references/ 与 snippets/manifest.json。
      src: origin/COMPARISON:NOTICE.md:3
      ev: 上游…适用各自许可，不被根MIT替换 [COMPARISON-unique: NOTICE.md 相对 ANALYSIS 重写]
  - B1-09 [constraint] 本分支属于研究比较：未宣称参考 bot 可直接用于 RMTC，未对所有上游程序作功能审查或全面重跑。
      src: origin/COMPARISON:NOTICE.md:4
      ev: 未宣称参考bot可直接用于RMTC，未对所有上游程序作功能审查或全面重跑 [COMPARISON-unique]
  - B1-10 [process] 不把新增模块一律开启，也不把自建对手池称作官方比赛；910 局含失败和消融。
      src: origin/COMPARISON:README.md:7
      ev: 不把新增模块一律开启，也不把自建对手池称作官方比赛 [COMPARISON-unique: README.md 全新]
  - B1-11 [process] 上游以 submodule 固定在 b1893e19d1fe204bbba4e5c36af5b289f2b7b4ad；克隆本分支后执行 git submodule update --init --recursive 取得完整上游。
      src: origin/COMPARISON:README.md:23
      ev: 上游以 submodule 固定在 b1893e19…执行 git submodule update --init --recursive [COMPARISON-unique]
  - B1-12 [constraint] 所有策略迁移均需在 RMTC 验证；当前没有宣称已实现参赛 bot；新增 9 仓库的明确阅读范围不扩大为全仓语义审计；本轮用户明确授权仅更新 main/README 矩阵，除此不改 main、不合并研究历史。
      src: origin/COMPARISON:README.md:27
      ev: 所有策略迁移均需在RMTC验证；当前没有宣称已实现参赛bot [COMPARISON-unique]
  - B1-13 [constraint] 本分支为私密预备资料：不进入其他分支或公开导航；未来公开使用干净历史导出。
      src: origin/COMPARISON:README.md:29
      ev: 本分支不进入其他分支或公开导航；未来公开使用干净历史导出 [COMPARISON-unique]
  - B1-14 [constraint] recompute_statistics.py 只处理存档及纯评分函数，不运行 bot 或真实模型。
      src: origin/COMPARISON:checks/README.md:10
      ev: recompute_statistics.py 只处理存档及纯评分函数，不运行bot或真实模型 [COMPARISON-unique: checks/README.md 重写]
  - B1-15 [process] 所有检查通过只表示列出的不变量成立，不等于所有源代码正确、不等于已重新评测全部 98780 局，也未重新计算所有 bootstrap 区间。
      src: origin/COMPARISON:checks/README.md:12
      ev: 所有检查通过只表示列出的不变量成立，不等于…已重新评测全部98780局 [COMPARISON-unique]
  - B1-16 [constraint] ANALYSIS 与 COMPARISON 是用户指定的临时保密预备区，禁止在其他分支、PR、Issue、标签、公开工作流、发布说明或网站暴露其名称、入口或存在历史；不要将研究分支合并进正式开发历史。
      src: origin/COMPARISON:governance/private-preparation.md:3
      ev: 禁止在其他分支、PR、Issue、标签、公开工作流、发布说明或网站暴露其名称、入口或存在历史 [COMPARISON-unique: 相对 ANALYSIS 重写]
  - B1-17 [process] 删除分支引用不保证清除旧提交、缓存、其他 refs 或克隆；未来公开优先使用审查过的文件导出与干净新历史/独立发布仓库，不携带本分支的 Git 对象、文档、链接或 submodule 研究入口。
      src: origin/COMPARISON:governance/private-preparation.md:5
      ev: 未来公开优先使用审查过的文件导出与干净新历史/独立发布仓库 [COMPARISON-unique]
  - B1-18 [constraint] 本次不公开仓库、不创建 PR、不删除这些分支、不重写 main；若未来仍要公开原仓库，需单独审查 refs、提交和 GitHub 缓存，不能只删分支。
      src: origin/COMPARISON:governance/private-preparation.md:7
      ev: 本次不公开仓库、不创建PR、不删除这些分支、不重写main [COMPARISON-unique]
  - B1-19 [process] 使用 AI 生成或修改的代码，应先提交到非 main 分支，再通过 Pull Request（PR）合并到 main。
      src: origin/COMPARISON:governance/original-collaboration-guidelines.md:5
      ev: 使用 AI 生成或修改的代码，应先提交到非 "main" 分支，再通过 PR 合并 [shared with ANALYSIS: 与 ANALYSIS 版本一致，未改动]
  - B1-20 [process] 较大的功能改动使用 Create a merge commit 保留完整提交历史；较小的功能改动优先 Rebase and merge，若无法使用再考虑 Squash and merge。
      src: origin/COMPARISON:governance/original-collaboration-guidelines.md:9-10
      ev: 较大的功能改动：使用 Create a merge commit…较小的功能改动：优先使用 Rebase and merge [shared with ANALYSIS]
  - B1-21 [process] 方案尚未确定或效果有待验证的改动，无论大小都应先提交到非 main 分支，验证后再通过 PR 合并；内容明确且已验证的补丁可以直接提交到 main。
      src: origin/COMPARISON:governance/original-collaboration-guidelines.md:16-17
      ev: 方案尚未确定或效果有待验证：…先提交到非 "main" 分支…内容明确且已验证的补丁：可以直接提交到 "main" [shared with ANALYSIS]
  - B1-22 [process] “否决”指不适用于当前 RMTC 任务或证据不足，不表示在原游戏中无效。
      src: origin/COMPARISON:decisions/reuse-register.md:3
      ev: “否决”指不适用于当前RMTC任务或证据不足，不表示在原游戏中无效 [COMPARISON-unique: 新文件]
  - B1-23 [process] 采用顺序：规则不变量→稳定基线→任务评价→准确局部推演→有限对手情景→必要时再增加搜索；来源借鉴不等于已经证明 RMTC 效果；数值权重不直接复制。
      src: origin/COMPARISON:decisions/reuse-register.md:39
      ev: 采用顺序：规则不变量→稳定基线→任务评价→准确局部推演→有限对手情景→必要时再增加搜索 [COMPARISON-unique]
  - B1-24 [process] 标记语义：✅ 有对应证据；◐ 仅部分范围；⬜ 尚未；⛔ 阻塞；“不适用”是明确否决，不应视为待实现任务；不能将外部 AHC 提交成绩或本地 mock 结果标为 RMTC 胜率验证。
      src: origin/COMPARISON:decisions/reuse-register.md:60
      ev: 不能将外部 AHC 提交成绩或本地 mock 结果标为 RMTC 胜率验证 [COMPARISON-unique]
  - B1-25 [process] 每项后续试验须先保证 RMTC 规则与输入权限，再做相同地图/席位/对手/种子的比较；不复制完整外部源码；采纳原则不等于引入依赖，更不等于已验证胜率。
      src: origin/COMPARISON:decisions/reuse-register.md:90
      ev: 每项后续试验须先保证RMTC规则与输入权限，再做相同地图/席位/对手/种子的比较 [COMPARISON-unique]
  - B1-26 [process] AHC 068 表中“已审查”只表示已对比规则与主要代码思想；“实现/验证”另由代码和测试证据决定；完整 RMTC 对局成绩仍没有。
      src: origin/COMPARISON:decisions/reuse-register.md:43
      ev: 此处“已审查”只表示已对比规则与主要代码思想；“实现/验证”另由代码和测试证据决定 [COMPARISON-unique]
  - B1-27 [process] C37 基础行为已定位到当前代码（BFS 只保存首方向、Session 缓存同 Tick、新 Tick 重算）；不能把 Beam 未实现扩写为整个首步闭环未实现；上述状态据固定代码 90af9851a40ed962c7fe24c855ecf3712487d146，不表示完成实战验收。
      src: origin/COMPARISON:decisions/reuse-register.md:64
      ev: 不能把Beam未实现扩写为整个首步闭环未实现 [COMPARISON-unique]
  - B1-28 [technical] C30/C31 新增两个离线诊断夹具，不是参赛新算法；目标迟滞、跨目标评价和 Beam 的实施状态仍保留尚未。
      src: origin/COMPARISON:decisions/reuse-register.md:66
      ev: C30/C31新增两个离线诊断夹具，不是参赛新算法 [COMPARISON-unique]
  - B1-29 [process] 旧的两步诊断现已发展为实际参赛资源串实现；原诊断和当时状态仍保留，不能把它当作当前无代码；本表“实战验证”一列仍保持尚未或阻塞，局部验证不越级。
      src: origin/COMPARISON:decisions/reuse-register.md:70
      ev: 原诊断和当时状态仍保留，不能把它当作当前无代码…局部验证不越级 [COMPARISON-unique]
  - B1-30 [technical] C36/C37 补充（代码 4ba9dcdaf2056248505ebd2479077b77cf68a7ef）：新增 12 帧真实进展窗口、24 Tick 坏目标暂缓、12 Tick 脱困目的地及无出口持续防御；不回滚已执行 Tick，不假定对手合作；反伤下不再奖励接近预测防御目标。
      src: origin/COMPARISON:decisions/reuse-register.md:110
      ev: 新增12帧真实进展窗口、24Tick坏目标暂缓、12Tick脱困目的地…不回滚已执行Tick，不假定对手合作 [COMPARISON-unique]
  - B1-31 [metric] 12 局导航专门回归及 60 局新地图验证通过，不是原版或用户地图；压力往返 500→16 Tick；阈值未重新优化，仍保留致命守卫，不能保证所有攻防僵局脱离；不扩写成全部上游语义审计。
      src: origin/COMPARISON:decisions/reuse-register.md:112
      ev: 压力往返500→16Tick…不能保证所有攻防僵局脱离；没有新增外部仓库阅读，不扩写成全部上游语义审计 [COMPARISON-unique]
  - B1-C01 [technical] 圈地收益/闭环耗时：借鉴评价方法；RMTC 换成预期计分/路径及行动成本，不能搬轨迹规则。
      src: origin/COMPARISON:decisions/reuse-register.md:7
      ev: 不能搬轨迹规则 [COMPARISON-unique]
  - B1-C02 [technical] 炸弹人时间展开可生存集合：适配；用 RMTC 事件窗口、攻击先行时序、局部未知信息。
      src: origin/COMPARISON:decisions/reuse-register.md:8
      ev: 用RMTC事件窗口、攻击先行时序、局部未知信息 [COMPARISON-unique]
  - B1-C03 [technical] 夺旗任务生成与联合分配：部分借鉴；目标评价可用；每队一机器人，无三角色分配问题。
      src: origin/COMPARISON:decisions/reuse-register.md:9
      ev: 每队一机器人，无三角色分配问题 [COMPARISON-unique]
  - B1-C04 [protocol] 夺旗边移动边攻击：否决照搬；RMTC 每 Tick 仅一个动作，且攻击在移动前。
      src: origin/COMPARISON:decisions/reuse-register.md:10
      ev: RMTC每Tick仅一个动作，且攻击在移动前 [COMPARISON-unique]
  - B1-C05 [technical] 全图最短路/全敌人真值：否决依赖前提；RMTC 只有局部视野；分开未知与历史观测。
      src: origin/COMPARISON:decisions/reuse-register.md:11
      ev: RMTC只有局部视野；分开未知与历史观测 [COMPARISON-unique]
  - B1-C06 [metric] 追敌旗手/击杀奖励权重：否决原值；CTF 只交旗得分；RMTC v1.1 有调整后 D、死亡扣除与致死批次分奖。
      src: origin/COMPARISON:decisions/reuse-register.md:12
      ev: RMTC v1.1有调整后D、死亡扣除与致死批次分奖 [COMPARISON-unique]
  - B1-C07 [technical] 多情景对手预测：适配；预测是概率/假设，不能把敌人上一动作当承诺。
      src: origin/COMPARISON:decisions/reuse-register.md:13
      ev: 预测是概率/假设，不能把敌人上一动作当承诺 [COMPARISON-unique]
  - B1-C08 [technical] 外交身份/条约推理：暂缓直接实现；RMTC 无外交接口；保留事实/声明/预测分离习惯。
      src: origin/COMPARISON:decisions/reuse-register.md:14
      ev: RMTC无外交接口；保留事实/声明/预测分离习惯 [COMPARISON-unique]
  - B1-C09 [technical] 仓储增量缓存与精确回退：借鉴工程机制；先必要条件，再昂贵寻路；失效条件写清。
      src: origin/COMPARISON:decisions/reuse-register.md:15
      ev: 先必要条件，再昂贵寻路；失效条件写清 [COMPARISON-unique]
  - B1-C10 [technical] 从终点反向 BFS 必定等价：否决无条件使用；上游被封起点可离开导致距离非对称；RMTC 也应逐项检查。
      src: origin/COMPARISON:decisions/reuse-register.md:16
      ev: 上游被封起点可离开导致距离非对称；RMTC也应逐项检查 [COMPARISON-unique]
  - B1-C11 [technical] 坦克权威 step 和候选矩阵：适配；自建 RMTC 单步规则模型；未知信息用情景，非全局真值。
      src: origin/COMPARISON:decisions/reuse-register.md:17
      ev: 自建RMTC单步规则模型；未知信息用情景，非全局真值 [COMPARISON-unique]
  - B1-C12 [technical] 更深搜索必然更强：否决；模型误差、预算与候选质量可能主导；需配对测试。
      src: origin/COMPARISON:decisions/reuse-register.md:18
      ev: 模型误差、预算与候选质量可能主导；需配对测试 [COMPARISON-unique]
  - B1-C13 [constraint] 内嵌神经网络权重：否决；RMTC 禁止本地模型，单 CPP 也可能包含模型。
      src: origin/COMPARISON:decisions/reuse-register.md:19
      ev: RMTC禁止本地模型，单CPP也可能包含模型 [COMPARISON-unique]
  - B1-C14 [metric] 单榜分数跨集比较模型：否决；计分、对手池、渠道、机器、时间/重赛条件不同。
      src: origin/COMPARISON:decisions/reuse-register.md:20
      ev: 计分、对手池、渠道、机器、时间/重赛条件不同 [COMPARISON-unique]
  - B1-C15 [technical] 最终版总比中间版强：否决；上游版本演化反例；保留最佳与留出集。
      src: origin/COMPARISON:decisions/reuse-register.md:21
      ev: 上游版本演化反例；保留最佳与留出集 [COMPARISON-unique]
  - B1-C16 [metric] fast 模式成绩代表正式稳定：否决；Tank fast 不执行正式 CPU 超时处罚。
      src: origin/COMPARISON:decisions/reuse-register.md:22
      ev: Tank fast不执行正式CPU超时处罚 [COMPARISON-unique]
  - B1-C17 [metric] 两个独立榜单直接相减当进步：否决；需要同一对手池或联合拟合。
      src: origin/COMPARISON:decisions/reuse-register.md:23
      ev: 需要同一对手池或联合拟合 [COMPARISON-unique]
  - B1-C18 [metric] 仅平均总分评测：否决；需资源/伤害/任务资格、无效动作及事件失败分项。
      src: origin/COMPARISON:decisions/reuse-register.md:24
      ev: 需资源/伤害/任务资格、无效动作及事件失败分项 [COMPARISON-unique]
  - B1-C19 [technical] 明确输入/输出与代表例：采纳设计/待测；v1.1 语义与字段校验。
      src: origin/COMPARISON:decisions/reuse-register.md:25
      ev: v1.1语义与字段校验 [COMPARISON-unique]
  - B1-C20 [technical] 分层 harness：采纳架构/未实现；异步语义、校验、控制、反馈。
      src: origin/COMPARISON:decisions/reuse-register.md:26
      ev: 异步语义、校验、控制、反馈 [COMPARISON-unique]
  - B1-C21 [technical] Self-Consistency 默认多请求：暂缓；准确率、配额、延迟先比较。
      src: origin/COMPARISON:decisions/reuse-register.md:27
      ev: 准确率、配额、延迟先比较 [COMPARISON-unique]
  - B1-C22 [technical] ToT 逐 Tick 模型搜索：否决默认；控制周期与调用预算。
      src: origin/COMPARISON:decisions/reuse-register.md:28
      ev: 控制周期与调用预算 [COMPARISON-unique]
  - B1-C23 [technical] ReAct 反馈结构：适配；公开回执闭环，不任意开放工具。
      src: origin/COMPARISON:decisions/reuse-register.md:29
      ev: 公开回执闭环，不任意开放工具 [COMPARISON-unique]
  - B1-C24 [constraint] 外网 RAG/本地向量模型：否决照搬；信息权限与模型禁令。
      src: origin/COMPARISON:decisions/reuse-register.md:30
      ev: 信息权限与模型禁令 [COMPARISON-unique]
  - B1-C25 [constraint] 赛中自动改 Prompt：否决；封存前离线开发，赛中守版本。
      src: origin/COMPARISON:decisions/reuse-register.md:31
      ev: 封存前离线开发，赛中守版本 [COMPARISON-unique]
  - B1-C26 [constraint] 本地策略 LM/权重：否决；不得借 Prompt 优化绕过模型禁令。
      src: origin/COMPARISON:decisions/reuse-register.md:32
      ev: 不得借Prompt优化绕过模型禁令 [COMPARISON-unique]
  - B1-C27 [constraint] 生成知识补未知事件参数：否决；来源必须为本场公告。
      src: origin/COMPARISON:decisions/reuse-register.md:33
      ev: 来源必须为本场公告 [COMPARISON-unique]
  - B1-C28 [metric] 历史采样参数/长角色保证效果：否决保证；按当前模型和对局测量。
      src: origin/COMPARISON:decisions/reuse-register.md:34
      ev: 按当前模型和对局测量 [COMPARISON-unique]
  - B1-C29 [metric] D 单调/永久满分缓存：否决；死亡后 D 和对抗分可下降。
      src: origin/COMPARISON:decisions/reuse-register.md:35
      ev: 死亡后D和对抗分可下降 [COMPARISON-unique]
  - B1-C30 [technical] AHC 全局距离势函数：改造；用虚拟 R 逐次计算封顶收益；位置、死亡与多车联合价值仍是有限启发式。
      src: origin/COMPARISON:decisions/reuse-register.md:47
      ev: 用虚拟R逐次计算封顶收益…仍是有限启发式 [COMPARISON-unique]
  - B1-C31 [technical] 批量操作让多个目标协同受益：借鉴；一 Tick 一动作；已比较短资源串，不是完整任务/战斗协同。
      src: origin/COMPARISON:decisions/reuse-register.md:48
      ev: 一Tick一动作；已比较短资源串，不是完整任务/战斗协同 [COMPARISON-unique]
  - B1-C32 [technical] Beam Search 保留多候选：部分实施（3 目标/5 束/8 候选）；目标深度不等于 3 Tick；10ms 软预算；完整攻防状态 Beam 未建。
      src: origin/COMPARISON:decisions/reuse-register.md:49
      ev: 目标深度不等于3Tick；10ms软预算；完整攻防状态Beam未建 [COMPARISON-unique]
  - B1-C33 [technical] Beam 多样性剪枝：部分实施；不同首方向名额、相同拾取集合状态去重；不保证穷尽所有路线/情景。
      src: origin/COMPARISON:decisions/reuse-register.md:50
      ev: 不保证穷尽所有路线/情景 [COMPARISON-unique]
  - B1-C34 [protocol] Retroactive Insertion 历史插入：拒绝照搬；RMTC 已结算 Tick 不能改写；仅保留未执行计划重排思想。
      src: origin/COMPARISON:decisions/reuse-register.md:51
      ev: RMTC 已结算 Tick 不能改写；仅保留未执行计划重排思想 [COMPARISON-unique]
  - B1-C35 [technical] OperationLocalSearch / 置换群共轭：拒绝直接移植；RMTC 有对手和动态状态，不能直接按静态排列等价变换。
      src: origin/COMPARISON:decisions/reuse-register.md:52
      ev: RMTC 有对手和动态状态，不能直接按静态排列等价变换 [COMPARISON-unique]
  - B1-C36 [technical] 未来短期计划重排、目标迟滞：部分实施（有效目标 10% 迟滞）；危险、失效、失败 MOVE、断帧/复活打断；通用局部重排尚无。
      src: origin/COMPARISON:decisions/reuse-register.md:53
      ev: 危险、失效、失败MOVE、断帧/复活打断；通用局部重排尚无 [COMPARISON-unique]
  - B1-C37 [technical] 滚动规划只执行首步：采纳；新 Tick 重新读取真值；核心与采集夹具通过，完整战斗推演/实战验收另记。
      src: origin/COMPARISON:decisions/reuse-register.md:54
      ev: 新Tick重新读取真值；核心与采集夹具通过，完整战斗推演/实战验收另记 [COMPARISON-unique]
  - B1-C38 [technical] 短期对手多情景预测：部分采纳（已有一步软惩罚）；预测不更改当前真实占位或已知致命时序。
      src: origin/COMPARISON:decisions/reuse-register.md:55
      ev: 预测不更改当前真实占位或已知致命时序 [COMPARISON-unique]
  - B1-C39 [technical] 重做已有 BFS / 8 Tick 安全接续：否决重复开发；现行策略已实现，优先补多目标长期收益而非从零重写。
      src: origin/COMPARISON:decisions/reuse-register.md:56
      ev: 否决重复开发…优先补多目标长期收益而非从零重写 [COMPARISON-unique]
  - B1-C40 [metric] AHC 分差可推断 RMTC 提升幅度：否决；两竞赛评分、可观测性和对手机制不同。
      src: origin/COMPARISON:decisions/reuse-register.md:57
      ev: 两竞赛评分、可观测性和对手机制不同 [COMPARISON-unique]
  - B1-C41 [process] 先进行原版完整对局与配对消融：部分执行（7 例采集配对）；参考/标准车启动失败（DDS 阻塞）；无整局 R/D/M、死亡、AI 和对手池消融。
      src: origin/COMPARISON:decisions/reuse-register.md:58
      ev: 参考/标准车启动失败；已有资源夹具，无整局R/D/M、死亡、AI和对手池消融 [COMPARISON-unique]
  - B1-C42 [technical] PacmanAI 启发式/风险模式：借鉴原则；核对 README 和 heuristicTeam 关键函数；不抄食物回家奖励或本地 CNN/DQL。
      src: origin/COMPARISON:decisions/reuse-register.md:78
      ev: 不抄食物回家奖励或本地CNN/DQL [COMPARISON-unique]
  - B1-C43 [technical] pacman-mcts-agent-v2 选择性搜索：借鉴预算意识；默认 0.82 秒过长；不直接移植原 MCTS。
      src: origin/COMPARISON:decisions/reuse-register.md:79
      ev: 真文件myTeam(1).py，默认0.82秒过长；不直接移植原MCTS [COMPARISON-unique]
  - B1-C44 [technical] DXJ3X1 CTF 设计：仅概念参考；无选手源码，Further Improvements 不是已实现；PPT 未读。
      src: origin/COMPARISON:decisions/reuse-register.md:80
      ev: 无选手源码，Further Improvements不是已实现 [COMPARISON-unique]
  - B1-C45 [technical] Milad OP 贪心：拒绝直接搬；原函数反例实得 0、可行 10；只借预算/收益表达。
      src: origin/COMPARISON:decisions/reuse-register.md:81
      ev: 原函数反例实得0、可行10；只借预算/收益表达 [COMPARISON-unique]
  - B1-C46 [technical] Alii OP 八法：仅基线对比；8 脚本已读，DP/未完成 DFS 各有实际反例；不称通用精确算法。
      src: origin/COMPARISON:decisions/reuse-register.md:82
      ev: DP/未完成DFS各有实际反例；不称通用精确算法 [COMPARISON-unique]
  - B1-C47 [technical] op-solver 插入/删除/可行性：待离线试验；关键 cp/heur 函数选读，未集成/运行整个求解器。
      src: origin/COMPARISON:decisions/reuse-register.md:83
      ev: 关键cp/heur函数选读，未集成/运行整个求解器 [COMPARISON-unique]
  - B1-C48 [technical] mrtsp Frontier 成本与信息：独立适配一部分；原库为 Python/Jazzy 贪心，未搬 Nav2/精确 TSP。
      src: origin/COMPARISON:decisions/reuse-register.md:84
      ev: 已做RMTC信息增益；原库为Python/Jazzy贪心，未搬Nav2/精确TSP [COMPARISON-unique]
  - B1-C49 [technical] AutoFrontierSearch Humble：借边界定义；未搬世界坐标、近墙参数或随机选点；非 SLAM 集成。
      src: origin/COMPARISON:decisions/reuse-register.md:85
      ev: 未搬世界坐标、近墙参数或随机选点；非SLAM集成 [COMPARISON-unique]
  - B1-C50 [technical] CodeCraft 缓存/方向持续/预约：选择性借鉴；独立做目标迟滞；对手不承诺队内优先级，未知图不作全图。
      src: origin/COMPARISON:decisions/reuse-register.md:86
      ev: 独立做目标迟滞；对手不承诺队内优先级，未知图不作全图 [COMPARISON-unique]
  - B1-C51 [process] 云盘 AHC #77562268：关键算法已核对；2195 行取得、选读核心、未编译运行；不回滚比赛历史，不自证实时冠军。
      src: origin/COMPARISON:decisions/reuse-register.md:87
      ev: 2195行取得、选读核心、未编译运行；不回滚比赛历史，不自证实时冠军 [COMPARISON-unique]
  - B1-C52 [technical] Gemini Rmtc Bot Node：仅参考，不替换；888 行全文、真实头文件语法通过；缺 model/短超时/场次等静态风险，未运行节点。
      src: origin/COMPARISON:decisions/reuse-register.md:88
      ev: 888行全文、真实头文件语法通过；缺model/短超时/场次等静态风险，未运行节点 [COMPARISON-unique]
  - B1-C53 [technical] 炸弹人不确定风险误封唯一逃路：修复同类真问题；possible_fire 改排序/折扣；4 席位 4 旋转配对，不踩点旧 16 死新 0 死，实际踩点仍 16 死。
      src: origin/COMPARISON:decisions/reuse-register.md:118
      ev: 不踩点旧16死新0死，实际踩点仍16死 [COMPARISON-unique]
  - B1-C54 [technical] 光轮对手共用一方观测、虚假高胜率：检查并加契约；现有 arena 按 seat 单独 observe；新增四方身份/位置/成绩/自他区分断言。
      src: origin/COMPARISON:decisions/reuse-register.md:119
      ev: 现有arena按seat单独observe；新增四方身份/位置/成绩/自他区分断言 [COMPARISON-unique]
  - B1-C55 [technical] 整数/字符、首步、行步长、跨局串缓存：大部已有，继续验证；ASan/UBSan 不证明所有未初始化读已排除。
      src: origin/COMPARISON:decisions/reuse-register.md:120
      ev: JSON坐标、首步、session/generation、帧内缓存；ASan/UBSan不证明所有未初始化读已排除 [COMPARISON-unique]
  - B1-C56 [technical] 深搜/低血量原地拖死：保留待试；致命守卫仍可长期 DEFEND，三 Tick 模块继续关闭；不搬其他游戏时序/便宜死亡。
      src: origin/COMPARISON:decisions/reuse-register.md:121
      ev: 致命守卫仍可长期DEFEND，三Tick模块继续关闭；不搬其他游戏时序/便宜死亡 [COMPARISON-unique]
  - B1-C57 [technical] 缓存提速但改语义、先算再筛：不重写现有路径；帧内缓存/有界候选；自建共享 rules 验证不等于原版差分。
      src: origin/COMPARISON:decisions/reuse-register.md:122
      ev: 不重写现有路径…自建共享rules验证不等于原版差分 [COMPARISON-unique]
  - B1-C58 [protocol] 规则特例比算法名重要：采纳验证原则；原公告绝对时间、多辣椒交点、普攻最近、攻击先行；他游规则不移植。
      src: origin/COMPARISON:decisions/reuse-register.md:123
      ev: 原公告绝对时间、多辣椒交点、普攻最近、攻击先行；他游规则不移植 [COMPARISON-unique]
  - B1-C59 [metric] 弱对手自对弈/末版最强/小样本提升：拒绝保证；固定 NPC 与地图独立配对、轮席位、失败/摘要；新种子不用于反复调权。
      src: origin/COMPARISON:decisions/reuse-register.md:124
      ev: 固定NPC与地图独立配对、轮席位、失败/摘要；新种子不用于反复调权 [COMPARISON-unique]
  - B1-33 [process] 必须准确区分全量文件读取/结构化处理与逐段语义精读；不能把全量扫描说成每一份历史 bot、每条外交私信、每个回放帧和每个内嵌权重都做过逐行人工审查；没有重新打完仓库的全部对局。
      src: origin/COMPARISON:reports/01-six-episodes.md:13
      ev: 不能把全量扫描说成…逐行人工审查。这里也没有重新打完仓库的全部对局 [COMPARISON-unique: 新文件]
  - B1-34 [process] 三类结论分开：程序实现能直接确认的机制；数据复算能确认的结果；仍需在 RMTC 测试的策略判断；选手交接文档和赛后复盘属于选手自述，不能自动视为实现正确性或性能保证。
      src: origin/COMPARISON:reports/01-six-episodes.md:15
      ev: 本报告将三类结论分开…选手自述，不能自动视为实现正确性或性能保证 [COMPARISON-unique]
  - B1-35 [technical] 圈地的轨迹安全公式不能直接当作 RMTC 的攻击安全公式；对 RMTC 的启发是给远目标计算往返或兑现成本、记住对手到达时间，并保留恢复路径。
      src: origin/COMPARISON:reports/01-six-episodes.md:44
      ev: 圈地的轨迹安全公式不能直接当作 RMTC 的攻击安全公式 [COMPARISON-unique]
  - B1-36 [technical] 对 RMTC 最有价值的是按绝对 tick 管理效果和危险窗口、检查下一步之外的后续可达性，以及为复杂判断保留轻量兜底。
      src: origin/COMPARISON:reports/01-six-episodes.md:60
      ev: 按绝对 tick 管理效果和危险窗口 [COMPARISON-unique]
  - B1-37 [protocol] RMTC 是每队一机器人、局部视野、攻击先于移动；不能搬三角色动作组合，也不能依赖公开的全场敌人位置。
      src: origin/COMPARISON:reports/01-six-episodes.md:85
      ev: 不能搬三角色动作组合，也不能依赖公开的全场敌人位置 [COMPARISON-unique]
  - B1-38 [technical] 给不同接口不同保证：完整距离查询必须精确；只选下一步的接口可以在有证明时复用旧距离，但不能混用。
      src: origin/COMPARISON:reports/01-six-episodes.md:122
      ev: 例如完整距离查询必须精确；只选下一步的接口可以在有证明时复用旧距离，但不能混用 [COMPARISON-unique]
  - B1-39 [constraint] “单个 C++ 文件”不意味着“没有本地模型”；RMTC 禁止本地模型，因此不能把内嵌权重的社区实现直接移植。
      src: origin/COMPARISON:reports/01-six-episodes.md:164
      ev: RMTC 禁止本地模型，因此不能把这类社区实现直接移植 [COMPARISON-unique]
  - B1-40 [metric] 第二阶段计分：S = 30 min(R/120,1) + 15 min(D/500,1) + 5M；致死批次正贡献队伍去重均分 60、全部入账后每次死亡扣 60；v1.1 死亡会扣 D，超额 D 有缓冲与同分价值。
      src: origin/COMPARISON:reports/01-six-episodes.md:174-176
      ev: S = 30 min(R/120,1) + 15 min(D/500,1) + 5M…致死批次正贡献队伍去重均分60、全部入账后每次死亡扣60 [COMPARISON-unique]
  - B1-41 [protocol] 官方 AI 负责规则要求的自然语言事件理解，返回结构化结果；本地代码校验并按绝对 tick 维护效果起止；不能拿关键词或正则替代规则明确要求的官方 AI 理解。
      src: origin/COMPARISON:reports/01-six-episodes.md:184
      ev: 不能拿关键词或正则替代规则明确要求的官方 AI 理解 [COMPARISON-unique]
  - B1-42 [technical] 动作层按真实“攻击先于移动”的顺序推演，保留 DEFEND/WAIT 等合法兜底；视野外的位置属于未知或带时效的记忆，不能当作已知全场状态。
      src: origin/COMPARISON:reports/01-six-episodes.md:186
      ev: 按真实“攻击先于移动”的顺序推演，保留 DEFEND/WAIT 等合法兜底 [COMPARISON-unique]
  - B1-43 [process] 优先验证规则时序和接口稳定，再比较策略强弱；用相同地图、相同座位和相同对手配对比较两个版本，记录资源/伤害/任务分项分数、无效动作、超时、死亡机会损失、AI 成功资格与效果到期；必须专测移动目标被占据、多人抢同一格、当前回合攻击无法靠本回合移动躲开、幻觉反向移动、效果跨死亡仍按绝对时间到期、AI 延迟或失败、缓存路径被
      src: origin/COMPARISON:reports/01-six-episodes.md:201-203
      ev: 必须专测：移动目标被当前占据、多人抢同一格…不能让练习环境的高胜率掩盖规则偏差 [COMPARISON-unique]
  - B1-44 [process] 保留基线、当前最佳、候选三个版本；调参地图与验收地图分开；遇到失败先看回放定位具体机制，再做最小必要改动。
      src: origin/COMPARISON:reports/01-six-episodes.md:205
      ev: 保留基线、当前最佳、候选三个版本。调参地图与验收地图分开 [COMPARISON-unique]
  - B1-45 [process] 今后讨论本仓库时应指明集数、文件、版本、对手池和测试条件；对于 RMTC 优先引用自己的正式规则。
      src: origin/COMPARISON:reports/01-six-episodes.md:224
      ev: 今后讨论本仓库时应指明集数、文件、版本、对手池和测试条件 [COMPARISON-unique]
  - B1-46 [metric] 按地图成块重抽样，固定对手池和座位，人数设置等权，重复程序合并身份；圈地归一化、CTF/Bomber 多人拆比较、Tank 固定参照和社区小赛程不可混用；BT 点估计只是给定对手池的拟合，不是绝对 Elo。
      src: origin/COMPARISON:reports/02-experiments-and-risks.md:3
      ev: 圈地归一化、CTF/Bomber多人拆比较、Tank固定参照和社区小赛程不可混用 [COMPARISON-unique]
  - B1-47 [process] RMTC 实验记录应包含版本、规则/配置版本、地图/座位/对手池、机器和并行数、分项分、任务 AI 资格、异常、失败回放；留出地图不参加调参；一次改动尽量对应一个机制假设；输出正确与性能稳定分别验证。
      src: origin/COMPARISON:reports/02-experiments-and-risks.md:9
      ev: RMTC实验记录应包含…留出地图不参加调参 [COMPARISON-unique]
  - B1-48 [process] 不要只复制某个 README 然后称完整上游已归档；本分支同时保存全仓哈希、结构化索引和原始数据核查，可初始化 submodule 恢复全部 1078 个文件。
      src: origin/COMPARISON:reports/03-source-integrity-and-next-steps.md:3
      ev: 不要只复制某个README然后称完整上游已归档 [COMPARISON-unique]
  - B1-49 [process] 后续有必要增加参考对象时，用新来源 ID、固定提交、许可、读取范围和独立对照；不能用未经读取的项目补充榜单。
      src: origin/COMPARISON:reports/03-source-integrity-and-next-steps.md:7
      ev: 用新来源ID、固定提交、许可、读取范围和独立对照；不能用未经读取的项目补充榜单 [COMPARISON-unique]
  - B1-50 [process] B 站截图仅用于记录参考 repo 的发现来源；视频本体未完整观看，不声称完成视频核验或转写。
      src: origin/COMPARISON:reports/03-source-integrity-and-next-steps.md:9
      ev: 不声称完成视频核验或转写 [COMPARISON-unique]
  - B1-51 [metric] v1.1 计分：D=max(0,旧D+本Tick实际攻击贡献+击杀奖励−60×死亡次数)，对抗 15×min(D/500,1)；致死批次正贡献队伍去重均分每名死者 60，反伤/辣椒损血不算普通攻击贡献但可获得奖励，爆炸/分裂死亡仅扣罚。
      src: origin/COMPARISON:reports/04-v1.1-transfer-update.md:5
      ev: D=max(0,旧D+本Tick实际攻击贡献+击杀奖励−60×死亡次数)，对抗15×min(D/500,1) [COMPARISON-unique]
  - B1-52 [metric] 群预告不能覆盖正式 v1.1；不能把分奖理解成可串通互刷；依赖旧分数前提的候选必须重评（D 不单调、满分可跌落）。
      src: origin/COMPARISON:reports/04-v1.1-transfer-update.md:12-13
      ev: 群预告不能覆盖正式v1.1；…D不单调、满分可跌落；依赖旧分数前提的候选必须重评 [COMPARISON-unique]
  - B1-53 [metric] 控制直接用公开 score.effective_damage，不在官方值上二次加减；本地模型只用于评价，内部裁判记录仅供人工复核；不能沿用“曾满分就永久关闭战斗”的缓存策略；不把六集榜单说成 RMTC 胜率证明。
      src: origin/COMPARISON:reports/04-v1.1-transfer-update.md:16
      ev: 控制直接用公开score.effective_damage，不在官方值上二次加减 [COMPARISON-unique]
  - B1-54 [protocol] 官方 LLM 语义层验收：不能以正则/关键词替代 LLM；不要求大量自由推理文本；格式合格不等于语义正确；跨场结果拒绝。
      src: origin/COMPARISON:reports/05-prompt-harness-review.md:21
      ev: 不能以正则/关键词替代LLM [COMPARISON-unique]
  - B1-55 [metric] 500ms 是动作周期，不是 LLM 耗时承诺；同一公告重复不重复调用，同 Tick 不同公告不能丢；每公告采样 k 次，N 份公告至少 Nk 次请求，另有任务、资格确认与重试；预算按当场公告，不能把暂定 100 永久硬编码。
      src: origin/COMPARISON:reports/05-prompt-harness-review.md:26
      ev: 500ms是动作周期，不是LLM耗时承诺…N份公告至少Nk次请求…不能把暂定100永久硬编码 [COMPARISON-unique]
  - B1-56 [constraint] 采用与否决表：ToT 每 Tick 模型搜索否决默认；任意网页 RAG/本地向量模型否决直接搬用；赛中自动改 Prompt 否决（赛中遵守版本封存与登记切换）；本地策略语言模型/内嵌权重否决（不借 Prompt 优化名义绕过禁令）；生成常识补未知事件参数否决（参数来自本场公告，缺项标未知，不造规则）；长角色/历史采样参
      src: origin/COMPARISON:reports/05-prompt-harness-review.md:32-40
      ev: 赛中自动改Prompt 否决…不借Prompt优化名义绕过禁令…参数来自本场公告，缺项标未知，不造规则 [COMPARISON-unique]
  - B1-57 [technical] v1.2 限制：普通移动 BFS 遇墙不展开的逻辑不能直接当复活搜索；外部游戏的基地复活机制不等于本赛；固定旗点坐标、绝对中心常量和从配置读取全图真值不可用；任务坐标与堡垒对象不能合并。
      src: origin/COMPARISON:reports/06-v1.2-transfer-update.md:8-9
      ev: 普通移动BFS遇墙不展开的逻辑不能直接当复活搜索…任务坐标与堡垒对象不能合并 [COMPARISON-unique]
  - B1-58 [constraint] 外部容器只是工具，不能把交镜像当成规则必做或用上游运行结果代替本队证据；语言不限不解除本地模型限制。
      src: origin/COMPARISON:reports/06-v1.2-transfer-update.md:10
      ev: 不能把交镜像当成规则必做或用上游运行结果代替本队证据；语言不限不解除本地模型限制 [COMPARISON-unique]
  - B1-59 [constraint] 事件须经官方 LLM 理解，异步解释与本地动作分层；不引入未经许可的模型、外部 AI 或观赛真值。
      src: origin/COMPARISON:reports/06-v1.2-transfer-update.md:12
      ev: 事件须经官方LLM理解，异步解释与本地动作分层；不引入未经许可的模型、外部AI或观赛真值 [COMPARISON-unique]
  - B1-60 [technical] v1.2 采用/否决：否决把外部夺旗静态目标点直接转为 RMTC 堡垒固定坐标；否决因 C++ 仅推荐就大规模改写已可运行代码；否决因不再必交镜像就取消依赖说明与检录验证。
      src: origin/COMPARISON:reports/06-v1.2-transfer-update.md:14
      ev: 否决：把外部夺旗静态目标点直接转为RMTC堡垒固定坐标… [COMPARISON-unique]
  - B1-61 [technical] 对称性讨论：借鉴外部项目的对称探索或地图推断时，只能保留为可撤销假设，不把镜像猜测填成已观测真值；中心对称与轴对称分开建模，实际观测优先；否决基于聊天占比断言全图布局；否决使用关键词进入固定堡垒并绕过官方 LLM 语义理解。
      src: origin/COMPARISON:reports/06-v1.2-transfer-update.md:18
      ev: 只能保留为可撤销假设，不把镜像猜测填成已观测真值；中心对称与轴对称分开建模，实际观测优先 [COMPARISON-unique]
  - B1-62 [constraint] AHC 068 与 RMTC 的根本差别：本赛每 Tick 有局部视野、对手同时行动、动态事件和截止时间，已结算动作不可撤回，也不能为搜索取用练习全图/观赛真值。
      src: origin/COMPARISON:reports/07-ahc068-rectangle-swap-transfer-2026-10-28.md:11
      ev: 已结算动作不可撤回，也不能为搜索取用练习全图/观赛真值 [COMPARISON-unique]
  - B1-63 [protocol] Retroactive Insertion 只可对未执行路径插入资源点/新任务/危险绕行；已结算 Tick 不可撤销。
      src: origin/COMPARISON:reports/07-ahc068-rectangle-swap-transfer-2026-10-28.md:40
      ev: 对未执行路径插入资源点/新任务/危险绕行 | 已结算 Tick 不可撤销 [COMPARISON-unique]
  - B1-64 [technical] 目标持续性和切换成本，防止多目标振荡；危险和目标失效必须立即打断迟滞。
      src: origin/COMPARISON:reports/07-ahc068-rectangle-swap-transfer-2026-10-28.md:42
      ev: 危险和目标失效必须立即打断迟滞 [COMPARISON-unique]
  - B1-65 [technical] 建议小规模 MPC/Beam：每 Tick 将本席位感知作为真值、生成合法候选、用准确规则推演有限步、保留多个不同方案、只执行第一步、下一 Tick 重算；局部未来计划允许改写，过去不允许；正式 AI 事件理解仍应异步，不让模型推理阻塞每 Tick 动作。
      src: origin/COMPARISON:reports/07-ahc068-rectangle-swap-transfer-2026-10-28.md:52
      ev: 只执行第一步、下一 Tick 重算…局部未来计划允许改写，过去不允许 [COMPARISON-unique]
  - B1-66 [metric] 短爆炸预告 5 Tick、默认 500ms/Tick 仅约 2.5 秒，解释虽正确也可能错过逃生时机；两次样本不能形成可靠延迟分布；没有可归因的现行策略胜率。
      src: origin/COMPARISON:reports/07-ahc068-rectangle-swap-transfer-2026-10-28.md:56
      ev: 短爆炸预告 5 Tick、默认 500ms/Tick 仅约 2.5 秒 [COMPARISON-unique]
  - B1-67 [goal] 执行先后：P0 正常 Humble/DDS 完整对局和 LLM 及时率 → P1 目标迟滞与多目标评价 → P2 小范围 Beam 和合法超时回退 → P3 有限对手情景 → P4 配对消融和赛前封存；对失败、被否决和未测试项目分别记录，不能一律打勾。
      src: origin/COMPARISON:reports/07-ahc068-rectangle-swap-transfer-2026-10-28.md:58
      ev: P0 正常 Humble/DDS 完整对局和 LLM 及时率 → P1 目标迟滞…对失败、被否决和未测试项目分别记录，不能一律打勾 [COMPARISON-unique]
  - B1-68 [process] 已审查（有规则或源码定位）≠已实现（有代码提交）≠已执行（有运行日志）≠已验证成功（有能支撑结论的完整结果）；跨赛事的排名、分数和程序长短不能证明迁移方案实际提升；本赛官方规则优先。
      src: origin/COMPARISON:reports/07-ahc068-rectangle-swap-transfer-2026-10-28.md:62
      ev: 已审查≠已实现≠已执行≠已验证成功 [COMPARISON-unique]
  - B1-69 [technical] PacmanAI 可借鉴低风险/进攻模式切换、依据连续观测更新目标；原游戏的食物带回本方和旗区机制不属于 RMTC；原权重不直接抄，也不带本地训练模型上场。
      src: origin/COMPARISON:reports/08-gemini-repository-suggestions-2026-10-28.md:7
      ev: 原权重不直接抄，也不带本地训练模型上场 [COMPARISON-unique]
  - B1-70 [metric] pacman-mcts-agent-v2 默认搜索 0.82 秒，对 100ms/500ms 动作窗口过长；代码不能仅凭 README 当作完整多对手随机模拟器；可采纳“只在分歧有价值时分配有限预算”；不把回家距离奖励、原时间预算当 RMTC 常量。
      src: origin/COMPARISON:reports/08-gemini-repository-suggestions-2026-10-28.md:9
      ev: 默认搜索0.82秒，对100ms/500ms动作窗口过长 [COMPARISON-unique]
  - B1-71 [process] 脚本只校验固定 Git blob，只用 AST 取已审查函数，不执行外部模块顶层、绘图或整个框架；三个反例验证具体函数缺陷，不构成整个项目的性能排名。
      src: origin/COMPARISON:reports/08-gemini-repository-suggestions-2026-10-28.md:27
      ev: 只用AST取已审查函数，不执行外部模块顶层、绘图或整个框架 [COMPARISON-unique]
  - B1-72 [technical] RMTC 已有离散格和裁判坐标，应独立计算真实视野能新看到几格；不能把未知当空、不能直接用米制缩放/随机目标。
      src: origin/COMPARISON:reports/08-gemini-repository-suggestions-2026-10-28.md:35
      ev: 不能把未知当空、不能直接用米制缩放/随机目标 [COMPARISON-unique]
  - B1-73 [technical] CodeCraft 原机器人 ID 优先级/预约是队内协作规则，不保证 RMTC 敌人让行；也不能用全图货物真值、港口/船舶或原权重。
      src: origin/COMPARISON:reports/08-gemini-repository-suggestions-2026-10-28.md:41
      ev: 原机器人ID优先级/预约是队内协作规则，不保证RMTC敌人让行 [COMPARISON-unique]
  - B1-74 [metric] AHC main/verify 的预算、可行性检查与已验证回退思路可借鉴，但搜索约 1920ms、留 180ms 收尾的预算不能把 2 秒赛题预算塞进 500ms Tick。
      src: origin/COMPARISON:reports/09-drive-ahc-and-gemini-node-review-2026-10-28.md:17
      ev: 不能把2秒赛题预算塞进500ms Tick [COMPARISON-unique]
  - B1-75 [constraint] 原备份可能含浏览器账号数据，所以只保存元数据/哈希，不发布 MHTML 或全 HTML。
      src: origin/COMPARISON:reports/09-drive-ahc-and-gemini-node-review-2026-10-28.md:19
      ev: 只保存元数据/哈希，不发布MHTML或全HTML [COMPARISON-unique]
  - B1-76 [technical] 可借鉴的主线是“真实坐标→地图记忆→少量未来资源→首步→回执”；但不能为简洁而失去 model、场次隔离、正式事件语义与动作期限；语法通过不能验证线程、网络或行为。
      src: origin/COMPARISON:reports/09-drive-ahc-and-gemini-node-review-2026-10-28.md:38
      ev: 不能为简洁而失去model、场次隔离、正式事件语义与动作期限 [COMPARISON-unique]
  - B1-77 [process] 本次未新增真实 LLM 请求；既有两次成功不得当成此节点成功或本轮正式资格。
      src: origin/COMPARISON:reports/09-drive-ahc-and-gemini-node-review-2026-10-28.md:40
      ev: 既有两次成功不得当成此节点成功或本轮正式资格 [COMPARISON-unique]
  - B1-78 [constraint] 本轮将此前已研读的原则转为独立 RMTC 实现，不搬原游戏规则或直接粘贴许可证不明代码；不把本轮扩写成所有上游逐行审计。
      src: origin/COMPARISON:reports/10-applied-search-and-arena-results-2026-10-28.md:3
      ev: 不搬原游戏规则或直接粘贴许可证不明代码 [COMPARISON-unique]
  - B1-79 [technical] 限制表：已执行 Tick 不回滚，不做置换群共轭；不允许不可达高收益目标使搜索直接退出；不假设地图永久不变，不为对手预约路线或约定让路；不是已校准概率或精确 Nash，不能从父模拟中读隐藏真值；不搬 SLAM/Nav2 坐标或全图路线前提；自建裁判共享规则不能替代原版；延迟 oracle 不证明 LLM 理解。
      src: origin/COMPARISON:reports/10-applied-search-and-arena-results-2026-10-28.md:9-13
      ev: 已执行Tick不回滚，不做置换群共轭…自建裁判共享规则不能替代原版 [COMPARISON-unique]
  - B1-80 [metric] 结果口径：首轮训练优胜者留出平均 32.09→30.87，未采纳；补连续受阻改道后换新种子，最终对抗 33.54→34.72、获胜份额 29.2%→37.5%，死亡 81→89；不是每个模块都提高成绩，非官方标准车结果。
      src: origin/COMPARISON:reports/10-applied-search-and-arena-results-2026-10-28.md:15
      ev: 首轮…32.09→30.87，未采纳…最终对抗33.54→34.72…非官方标准车结果 [COMPARISON-unique]
  - B1-81 [technical] 假设火线保留为风险：相同最短距离优先较小风险的首步；目标收益除以 1 + 假设伤害 / max(1, 当前剩余HP)；这是启发式折扣，不是校准过的发生概率。
      src: origin/COMPARISON:reports/11-subtitle-lessons-and-rmtc-counterexamples-2026-10-28.md:16
      ev: 目标收益除以`1 + 假设伤害 / max(1, 当前剩余HP)`。这是启发式折扣，不是校准过的发生概率 [COMPARISON-unique]
  - B1-82 [technical] 当前格存在可能致命火线且有更低风险邻格时仍优先避险；没有这种邻格，也保留躲避已公告爆炸的出口。
      src: origin/COMPARISON:reports/11-subtitle-lessons-and-rmtc-counterexamples-2026-10-28.md:18
      ev: 没有这种邻格，也保留躲避已公告爆炸的出口 [COMPARISON-unique]
  - B1-83 [metric] 32 例是同一最小反例的对称变换（四席位×四方向旋转×敌方防御/实际踩点），不是 32 张独立地图；防御不踩点旧 16 死新 0 死，移动踩点仍 16 死，没有伪造安全保证。
      src: origin/COMPARISON:reports/11-subtitle-lessons-and-rmtc-counterexamples-2026-10-28.md:20
      ev: 它们是同一最小反例的对称变换，不是32张独立地图 [COMPARISON-unique]
  - B1-84 [constraint] run_risk.py 不启动 ROS、不访问观赛真值、不请求模型；--before-binary/--after-binary 仅供已编译同夹具程序，使用者须确保二进制对应指定源码。
      src: origin/COMPARISON:reports/11-subtitle-lessons-and-rmtc-counterexamples-2026-10-28.md:33
      ev: 它不启动ROS、不访问观赛真值、不请求模型 [COMPARISON-unique]
  - B1-85 [technical] 不添加“距离必须单调下降”条件（保留严格坐标/类型校验、墙后绕路、目标迟滞和 12 帧无进展检测）。
      src: origin/COMPARISON:reports/11-subtitle-lessons-and-rmtc-counterexamples-2026-10-28.md:39
      ev: 不添加“距离必须单调下降”条件 [COMPARISON-unique]
  - B1-86 [protocol] RMTC 禁止跟入敌车本 Tick 起始占格，不能搬其抢格招数；生产入口是 ROS 完整消息回调，无整段 stdin 等待。
      src: origin/COMPARISON:reports/11-subtitle-lessons-and-rmtc-counterexamples-2026-10-28.md:42
      ev: RMTC禁止跟入敌车本Tick起始占格，不能搬其抢格招数 [COMPARISON-unique]
  - B1-87 [technical] 字幕所述游戏的低代价死亡、三车角色分配、扛旗交付、基地血量、子弹飞行、可破坏墙、光轮轨迹墙及轮流抢格均不属于 RMTC，未移植；更深搜索、MCTS、棋盘黑白格估值也没有仅因他人使用就加入。
      src: origin/COMPARISON:reports/11-subtitle-lessons-and-rmtc-counterexamples-2026-10-28.md:52
      ev: 更深搜索、MCTS、棋盘黑白格估值也没有仅因他人使用就加入 [COMPARISON-unique]
  - B1-88 [process] 原版 practice/ 18 文件不变；字符串契约测试仅证明提示存在，不证明真实模型必然理解。
      src: origin/COMPARISON:reports/11-subtitle-lessons-and-rmtc-counterexamples-2026-10-28.md:56
      ev: 原版`practice/`18文件不变。…字符串契约测试仅证明提示存在，不证明真实模型必然理解 [COMPARISON-unique]
  - B1-89 [metric] 49009 起六类新地图各版 6 采集+24 对抗：采集均分 32.67 不变，对抗均分 37.77、获胜份额 45.8%、死亡 79、受阻 87 均不变，无效动作 0；不把边界修复宣传成总分提升；没有把这些运行叫官方标准车对局或真实 LLM 测试。
      src: origin/COMPARISON:reports/11-subtitle-lessons-and-rmtc-counterexamples-2026-10-28.md:58
      ev: 本批采集均分32.67不变，对抗均分37.77…不把边界修复宣传成此批总分提升 [COMPARISON-unique]
  - B1-90 [process] 10ms 仍仅资源搜索软预算；自建裁判共享部分 rules，不是完全独立 oracle；ASan/UBSan 也不是 MSan 或所有未初始化读的证明；未因字幕自动开启三 Tick 模块。
      src: origin/COMPARISON:reports/11-subtitle-lessons-and-rmtc-counterexamples-2026-10-28.md:66
      ev: 10ms仍仅资源搜索软预算；自建裁判共享部分rules，不是完全独立oracle [COMPARISON-unique]
  - B1-91 [process] 本轮代码按两次提交发布：24774f4 修复/契约，826c4da 夹具/来源取舍/结果；既有 PR 保持开放未合并；main 矩阵按已有授权扩至 R45，仅 README。
      src: origin/COMPARISON:reports/11-subtitle-lessons-and-rmtc-counterexamples-2026-10-28.md:68
      ev: 既有PR保持开放未合并。main矩阵按已有授权扩至R45，仅README [COMPARISON-unique]
  - B1-92 [process] 全量读取/结构化处理不等于所有历史源文件逐行人工审查，不能声称每条外交私信、每个回放帧、每个权重数字都已语义核验；没有模型原始完整会话、未公开官方外交 PDF 或封闭源码，不能补造；当前未重新执行全部 98780 局对战。
      src: origin/COMPARISON:indexes/reading-coverage.md:7
      ev: 全量读取/结构化处理不等于所有历史源文件逐行人工审查…不能补造 [COMPARISON-unique: 新文件]
  - B1-93 [process] 所有 JSON/CSV 解析通过不等于功能正确；程序作者 NOTES、模型复盘是自述而不是独立验证；后续若新增精读或运行实验，更新此页和检查结果。
      src: origin/COMPARISON:indexes/reading-coverage.md:9
      ev: 所有JSON/CSV解析通过不等于功能正确 [COMPARISON-unique]
  - B1-94 [protocol] 上游总体 MIT，但外交依赖 diplomacy 包是 AGPL、回放地图含 jDip GPL 图形、角色素材另有声明；不能把所有回放和素材统称本仓库 MIT；submodule 仍需遵守其原许可。
      src: origin/COMPARISON:references/README.md:5
      ev: 保留上游README的许可说明，不能把所有回放和素材统称本仓库MIT [COMPARISON-unique: 新文件]
  - B1-95 [constraint] 代码片段保留上游出处、MIT 声明链接；它们依赖原文件上下文，不作为可直接编译的 RMTC 模块。
      src: origin/COMPARISON:references/README.md:7
      ev: 它们依赖原文件上下文，不作为可直接编译的RMTC模块 [COMPARISON-unique]
  - B1-96 [process] RMTC 当前规则为 RULES-03 v1.2；未新增外部 repo 或代码摘录，不更改上游固定提交。
      src: origin/COMPARISON:references/README.md:15
      ev: 未新增外部repo或代码摘录，不更改上游固定提交 [COMPARISON-unique]
  - B1-97 [constraint] 摘录保持上游正文，前四行是本次添加的来源/许可/用途说明；不可将这些上下文片段直接当作 RMTC 实现。
      src: origin/COMPARISON:snippets/README.md:3
      ev: 不可将这些上下文片段直接当作RMTC实现 [COMPARISON-unique: 新文件]
  - B1-98 [technical] 片段使用限制：bomberman 时间展开须将火焰/缩圈替换成 RMTC 真实事件与行动顺序；tank 候选矩阵只在已列候选内近似，未知动作和局部信息需适配；warehouse 增量修复必须保留图契约/起点语义/内存所有权，无法证明时回退。
      src: origin/COMPARISON:snippets/README.md:7-9
      ev: 将火焰/缩圈替换成RMTC真实事件与行动顺序…图契约/起点语义/内存所有权必须保留，无法证明时回退 [COMPARISON-unique]
  - B1-99 [constraint] check_links.py 只校验自撰相对 Markdown 目标，不修改原始存档（leave original archives unchanged）。
      src: origin/COMPARISON:tools/check_links.py:2
      ev: Validate authored relative Markdown targets; leave original archives unchanged [COMPARISON-unique: 新工具; 与 ANALYSIS scripts/check_links.py 同功能但重写]
  - B1-100 [constraint] check_op_examples.py 只运行已核对函数的三个小反例；不执行外部脚本的顶层代码或比赛框架。
      src: origin/COMPARISON:tools/check_op_examples.py:1
      ev: 只运行已核对函数的三个小反例；不执行外部脚本的顶层代码或比赛框架 [COMPARISON-unique]
  - B1-101 [constraint] recompute_statistics.py 只复算选定已发布数据不变量，从不启动对局或模型（never starts a game or model）。
      src: origin/COMPARISON:tools/recompute_statistics.py:2
      ev: Recompute selected published-data invariants; never starts a game or model [COMPARISON-unique]
  - B1-102 [process] verify_upstream.py 验证固定 submodule、全部记录源哈希与精确摘录（commit b1893e19d1fe204bbba4e5c36af5b289f2b7b4ad，1078 文件，3 摘录，errors 为空）。
      src: origin/COMPARISON:tools/verify_upstream.py:2
      ev: Verify the fixed submodule, all recorded source hashes, and exact excerpts [COMPARISON-unique]
  - B1-103 [process] op-counterexamples 证据范围：三个已核对函数级合成反例，不是整个仓库执行（not full repository execution）。
      src: origin/COMPARISON:checks/op-counterexamples-2026-10-28.json:2
      ev: scope: Three reviewed function-level synthetic counterexamples; not full repository execution [COMPARISON-unique: 新证据文件]
  - B1-104 [process] 字幕阅读范围：七份字幕全文已读，是二手叙述，不作为原程序执行或排行榜的证明（secondary narrative, not proof of original code execution or leaderboards）。
      src: origin/COMPARISON:checks/subtitle-reading-2026-10-28.json:3
      ev: scope: Seven attached subtitles read in full…secondary narrative, not proof of original code execution or leaderboards [COMPARISON-unique]
  - B1-105 [process] 云盘 AHC 源码范围：取得完整 2195 行，所列算法核心已静态审读，不是逐行语义审计；未编译未执行；快照不独立验证实时冠军排名；仅语法核对 Gemini 节点（真实 Humble 头文件，无节点/对局/HTTP 执行）。
      src: origin/COMPARISON:checks/drive-source-review-2026-10-28.json:55,70-71
      ev: not every line semantically audited; not compiled or executed…syntax-only compile passed with genuine Humble headers. No node/game/HTTP execution [COMPARISON-unique]
  - B1-106 [constraint] 保存范围：仅源哈希、元数据和已观察 URL；不重新发布原始 MHTML、签名传输 URL、账号数据或完整外部代码（no raw MHTML, signed transfer URL, account data or complete external code republished）。
      src: origin/COMPARISON:checks/drive-source-review-2026-10-28.json:73
      ev: preservation: Source hashes, metadata and observed URLs only [COMPARISON-unique]
  - B1-107 [metric] 重算统计证据：CTF 32010 行全部 score=captures、评级点估计最大误差 0.0、故障计数 33；外交三局得分均与公式一致；仓储团队分重算均在舍入内（这些是记录口径核查，不等于重新评测 98780 局）。
      src: origin/COMPARISON:checks/recomputed-statistics.json:2-47
      ev: rating_point_max_error 0.0; diplomacy score_matches true; warehouse all_within_rounding true [COMPARISON-unique: 新证据文件]
  - B2-01 [process] 勾号只代表已有对应证据的阶段，不表示该方案已经提高胜率；仓库用于规则整理、算法方案论证、实施和测试证据跟踪，实际参赛 C++/ROS 2 工程另存。
      src: origin/main:README.md:3
      ev: 这里的勾号只代表已有对应证据的阶段，不表示该方案已经提高胜率 [main-unique]
  - B2-02 [process] 状态基线 2026-10-29：矩阵扩至 R49；代码固定 b27397f788b9ce0c950eece0b8ef296e7e716af8；规则 v1.2、通信协议/教程 v1.1；原版 practice 18 文件未改；当前补丁仍无本工具执行的完整原版裁判对标准车验收；真实 HTTP 与模拟资格分开。
      src: origin/main:README.md:5
      ev: 代码固定b27397f…原版practice18文件未改…真实HTTP与模拟资格分开 [main-unique]
  - B2-03 [process] 打勾图例：✅ 已完成且可核查（有规则/源码定位、提交 SHA、测试输出或裁判结果）；◐ 部分完成/只验证较小范围；⬜ 尚未完成或没有证据，不能因“已有想法/代码似乎存在”自动打勾；⛔ 被外部条件阻塞须写清日志；❌ 确认执行失败须有可复现错误；— 明确拒绝/不适用。
      src: origin/main:README.md:9-16
      ev: ⬜ 尚未完成或没有证据 不能因“已有想法/代码似乎存在”自动打勾 [main-unique]
  - B2-04 [process] 四道独立检查：审查=已核对规则/外部研究/代码并写明适用边界；实现=在可定位的参赛代码中完成；执行=实际运行了相应测试并保留日志；验收=运行结果证实该行声称的具体目标，不得跨范围扩大结论；每行四列分别更新，一个 ✅ 不能覆盖其他三列。
      src: origin/main:README.md:18
      ev: 验收：运行结果证实该行声称的具体目标…不得跨范围扩大结论。每行四列分别更新；一个 ✅ 不能覆盖其他三列 [main-unique]
  - B2-R01 [goal] R01 正式规则 v1.2、攻击先于移动、任务和评分边界：已有条款映射和核心回归，仍需原版对局。
      src: origin/main:README.md:24
      ev: 已有条款映射和核心回归，仍需原版对局 [main-unique]
  - B2-R02 [goal] R02 本队 ROS 2 感知与动作、QoS、场次/Tick 缓存：截图场已见 26 个不同 Tick 成功移动、执行 Tick29；源码 SHA 未提供，完整对局未验收；工具环境 DDS 仍阻塞。
      src: origin/main:README.md:25
      ev: 截图场已见26个不同Tick成功移动、执行Tick29；完整对局未验收 [main-unique]
  - B2-R03 [goal] R03 地图局部感知、历史记忆、未知格与真实坐标区分：有局部回归，未证实实战最优。
      src: origin/main:README.md:26
      ev: 有局部回归，未证实实战最优 [main-unique]
  - B2-R04 [goal] R04 已知地图 BFS 资源寻路与合法未知格试探：尚需真实陪练的收集效率/撞墙率数据。
      src: origin/main:README.md:27
      ev: 尚需真实陪练的收集效率/撞墙率数据 [main-unique]
  - B2-R05 [goal] R05 未来 8 Tick 安全接续动态规划：仅对有限已知格有效。
      src: origin/main:README.md:28
      ev: 仅对有限已知格有效 [main-unique]
  - B2-R06 [goal] R06 攻击/防御/事件时序与八类事件状态：自建规则边界通过（八事件与同时分奖）；共享部分规则、未原版差分，不能扩为全部组合/实战验收。
      src: origin/main:README.md:29
      ev: 共享部分规则、未原版差分，不能扩为全部组合/实战验收 [main-unique]
  - B2-R07 [goal] R07 官方计分边际函数、R/D 封顶与死亡扣 D：多人情景待整局核对。
      src: origin/main:README.md:30
      ev: 多人情景待整局核对 [main-unique]
  - B2-R08 [goal] R08 堡垒动态区域、驻留、增益兑现：覆盖授予时序和跨死亡保留；隐藏敌方进度及原版对局仍待。
      src: origin/main:README.md:31
      ev: 隐藏敌方进度及原版对局仍待 [main-unique]
  - B2-R09 [goal] R09 辣椒入点、爆炸/分裂提前避险：本地八事件/火线批次与激活顺序通过；罕见组合和独立裁判差分未验收。
      src: origin/main:README.md:32
      ev: 罕见组合和独立裁判差分未验收 [main-unique]
  - B2-R10 [goal] R10 对手连续轨迹的一步预测（只作软惩罚）：没有经对手池校准准确率。
      src: origin/main:README.md:33
      ev: 没有经对手池校准准确率 [main-unique]
  - B2-R11 [goal] R11 LLM 公告理解与本地每 Tick 动作决策分离：HTTP 成功不等于正式资格。
      src: origin/main:README.md:34
      ev: HTTP 成功不等于正式资格 [main-unique]
  - B2-R12 [goal] R12 真实 DeepSeek 上游及事件结构化解析：当前 C++ 经原 Handler 两项 200 且契约通过，4169/3772ms；用户本机 direct 仍读超时，不能跨环境判成功；短预告及时率待测。
      src: origin/main:README.md:35
      ev: 用户本机direct仍读超时，不能跨环境判成功；短预告及时率待测 [main-unique]
  - B2-R13 [goal] R13 累积公告重复膨胀修复：该具体回归复现后修复并复测通过（✅ 仅此回归，不表示 AI 在所有事件上正确）。
      src: origin/main:README.md:36
      ev: 该具体回归复现后修复并复测通过 [main-unique]
  - B2-R14 [goal] R14 正常 Humble/DDS 环境下的原版参考车验证：启动失败（接口权限）记 ❌ 执行失败与 ⛔ 阻塞；须在目标环境重跑；❌ 是测试执行失败而非算法已输。
      src: origin/main:README.md:37
      ev: 启动失败，原因是接口权限；须在目标环境重跑 [main-unique]
  - B2-R15 [goal] R15 A 对标准 B/C/D 的完整对局与真实得分：本机已运行至暂停 Tick30，但未完赛且 LLM 为 0；仍无有效整局胜率。
      src: origin/main:README.md:38
      ev: 本机已运行至暂停Tick30，但未完赛且LLM为0…仍无有效整局胜率 [main-unique]
  - B2-R16 [goal] R16 每 Tick 动作真实回执、不同场次和同 Tick 幂等验证：还需目标环境回执串联。
      src: origin/main:README.md:39
      ev: 还需目标环境回执串联 [main-unique]
  - B2-R17 [process] R17 AHC068 自身提交的势函数+BFS 逆层剥离分析：仅外部算法研究（— 表示不适用/拒绝项）。
      src: origin/main:README.md:40
      ev: 仅外部算法研究 [main-unique]
  - B2-R18 [process] R18 AHC068 高分提交的 Beam/历史插入/序列局部优化比较：2195 行源码已核对；未运行原程序，未独立核实实时冠军排名。
      src: origin/main:README.md:41
      ev: 未运行原程序，未独立核实实时冠军排名 [main-unique]
  - B2-R19 [goal] R19 多目标、跨 Tick 的边际收益估值：模型有隐藏状态误差，三 Tick 模块当前关闭。
      src: origin/main:README.md:42
      ev: 模型有隐藏状态误差，三Tick模块当前关闭 [main-unique]
  - B2-R20 [goal] R20 目标迟滞与未执行计划的局部重排：12 次反转/插入/删除共享 10ms；只资源目标，本批消融同分，不称成绩增益。
      src: origin/main:README.md:43
      ev: 本批消融同分，不称成绩增益 [main-unique]
  - B2-R21 [goal] R21 小束宽 Beam Search 与滚动规划：比赛资源深度 4、束 5、候选 8；可选三 Tick 战斗已实现并测试但训练选择关闭；不是完整整场搜索。
      src: origin/main:README.md:44
      ev: 可选三Tick战斗已实现并测试但训练选择关闭；不是完整整场搜索 [main-unique]
  - B2-R22 [goal] R22 多对手情景预测与收益评估：五种情景与可能无双情景，公共续步只发首步；非校准概率/纳什解，当前关闭。
      src: origin/main:README.md:45
      ev: 非校准概率/纳什解，当前关闭 [main-unique]
  - B2-R23 [goal] R23 R/D/M、死亡、争格与风险配对消融：910 局含训练/消融，首轮失败保留；仍是自建裁判与延迟 oracle。
      src: origin/main:README.md:46
      ev: 910局含训练/消融，首轮失败保留…仍是自建裁判与延迟oracle [main-unique]
  - B2-R24 [constraint] R24 明确拒绝：AHC 置换群共轭和已执行历史操作插入照搬 RMTC；RMTC 已结算 Tick 不能回滚。
      src: origin/main:README.md:47
      ev: 明确拒绝：RMTC 已结算 Tick 不能回滚 [main-unique]
  - B2-R25 [process] R25 赛前封存 Prompt、参数与构建一致性：训练固定参数、无在线调参；正式赛封存/现场复核仍待。
      src: origin/main:README.md:48
      ev: 训练固定参数、无在线调参；正式赛封存/现场复核仍待 [main-unique]
  - B2-R26 [constraint] R26 PacmanAI 选读：实际获胜后备队是启发式，CNN/DQL 训练不足；借鉴风险/记忆，不部署本地训练模型；未运行原游戏。
      src: origin/main:README.md:49
      ev: 借鉴风险/记忆，不部署本地训练模型；未运行原游戏 [main-unique]
  - B2-R27 [metric] R27 pacman-mcts-agent-v2：默认 0.82 秒不适合直接放进 100/500ms 动作窗口；未运行原游戏。
      src: origin/main:README.md:50
      ev: 默认0.82秒不适合直接放进100/500ms动作窗口 [main-unique]
  - B2-R28 [process] R28 Pacman-Capture-the-Flag：该仓库没有选手源码；提高单位步食物收益属于 Further Improvements，不能当作已实现算法；PPT 未读。
      src: origin/main:README.md:51
      ev: 不能当作已实现算法。PPT未读 [main-unique]
  - B2-R29 [metric] R29 Orienteering-Problem 贪心可行性反例：已固定源码执行函数级反例（预算 2 实得 0，另有距离 1/得分 10 的可行路径）；仅验收此反例，非完整项目或比赛。
      src: origin/main:README.md:52
      ev: 预算2时先选不可达高比值点后退出，实得0，另有距离1/得分10的可行路径。仅验收此反例 [main-unique]
  - B2-R30 [metric] R30 Algorithm-OP 8 种示例逐项核对：函数级反例确认 DP 仅按递增编号（预算 3 得 10 而可行重排得 20）；不能称通用精确 DP；未运行整个项目。
      src: origin/main:README.md:53
      ev: 预算3时得10而可行重排得20。不能称通用精确DP；未运行整个项目 [main-unique]
  - B2-R31 [goal] R31 op-solver 可行插入、删除与预算恢复选读：静态全图与闭合路线前提不同；尚未集成或运行求解器。
      src: origin/main:README.md:54
      ev: 尚未集成或运行求解器 [main-unique]
  - B2-R32 [technical] R32 mrtsp_exploration_ros2：实际为 Python/Jazzy、贪心排序，不能直接称精确 TSP 或 Humble C++ 包；信息增益已独立适配见 R36。
      src: origin/main:README.md:55
      ev: 不能直接称精确TSP或Humble C++包 [main-unique]
  - B2-R33 [technical] R33 AutoFrontierSearch：RMTC 使用自身格图/视野，未搬 SLAM、Nav2 坐标与随机目标。
      src: origin/main:README.md:56
      ev: 未搬SLAM、Nav2坐标与随机目标 [main-unique]
  - B2-R34 [technical] R34 CodeCraft_2024 选读：可参考反向 BFS、收益场和队内让行；RMTC 对手不承诺让路，未知地图也不等于物流全图；未运行原赛事。
      src: origin/main:README.md:57
      ev: RMTC对手不承诺让路，未知地图也不等于物流全图 [main-unique]
  - B2-R35 [goal] R35 阶段结束与剩余动作数守卫：明确 100/500 动作 Tick，最终状态不发布；末步/两阶段窗口核心回归通过；此勾仅验收守卫，不代表实战获胜。
      src: origin/main:README.md:58
      ev: 明确100/500动作Tick，最终状态不发布；末步/两阶段窗口核心回归通过 [main-unique]
  - B2-R36 [goal] R36 已知可达观察点的信息增益探索：按实际视野计算新增未知格/路程，只走已知路径；局部下一帧覆盖 9→12，未有整局覆盖率统计。
      src: origin/main:README.md:59
      ev: 只走已知路径；局部下一帧覆盖9→12，未有整局覆盖率统计 [main-unique]
  - B2-R37 [metric] R37 新旧采集策略的同条件夹具：7 例无受阻 MOVE，两步新增 R20→30、四步 40→50、密集资源 200 的耗时 40→36；迷宫均 18 步；单次决策最大观测 2.28ms 仅一轮样本；不是标准车胜率或完整回调延迟。
      src: origin/main:README.md:60
      ev: 7例无受阻MOVE，两步新增R20→30、四步40→50…不是标准车胜率或完整回调延迟 [main-unique]
  - B2-R38 [goal] R38 练习代理的上游出网诊断：用户已运行并报 direct/read_timeout/10065ms；TLS 握手亦可能被标 read_timeout，需继续区分 DNS/TCP/TLS/响应，不计比赛资格。
      src: origin/main:README.md:61
      ev: 需继续区分DNS/TCP/TLS/响应，不计比赛资格 [main-unique]
  - B2-R39 [goal] R39 六地图、六陪练的独立规则测试裁判：公开局部观测/公告后延迟 oracle；18 地图边界、八事件测试；未原版差分或真实 AI 验收。
      src: origin/main:README.md:62
      ev: 未原版差分或真实AI验收 [main-unique]
  - B2-R40 [metric] R40 训练筛选、失败留存与新留出调参：首轮退步未采纳，第二轮对抗均分 33.54→34.72、获胜 29.2%→37.5%；小样本非官方结果，死亡增加及对照胜率更高均保留。
      src: origin/main:README.md:63
      ev: 首轮退步未采纳，第二轮对抗均分33.54→34.72…小样本非官方结果 [main-unique]
  - B2-R41 [goal] R41 新公告模型/顶层关闭思考与 JSON 透传：deepseek-flash、thinking disabled、json_object；未正式网关验收；512 是示例。
      src: origin/main:README.md:64
      ev: 未正式网关验收；512是示例 [main-unique]
  - B2-R42 [goal] R42 连续两次移动失败后的安全改道：只按真实回执，两次失败且有安全替代时重算首步；新留出受阻 1178→282，原版实战仍待。
      src: origin/main:README.md:65
      ev: 只按真实回执，两次失败且有安全替代时重算首步 [main-unique]
  - B2-R43 [metric] R43 成功往返/争格的无进展检测与脱困：12 可信帧窗口、目标暂缓/脱困期限；压力往返 500→16 Tick，正常绕路保留；另 60 局新地图均分 37.37→38.16；未取得用户地图、未原版 DDS 验收，致命守卫仍可能停留。
      src: origin/main:README.md:66
      ev: 压力往返500→16Tick…未原版DDS验收，致命守卫仍可能停留 [main-unique]
  - B2-R44 [metric] R44 假设火线保留唯一已知爆炸逃路：每版 32 个席位/方向/敌动作变换，不踩点旧 16 死→新 0 死，实际踩点仍 16 死；另 60 局新地图分数未变，参数未重调；不是 32 独立地图或原版实战，保留风险。
      src: origin/main:README.md:67
      ev: 不踩点旧16死→新0死，实际踩点仍16死…不是32独立地图或原版实战 [main-unique]
  - B2-R45 [goal] R45 自建裁判四席位观测隔离契约：逐席位身份、坐标、R/D 和自他区分断言通过 ASan/UBSan；仅验收该观测契约，不代表完整裁判差分一致。
      src: origin/main:README.md:68
      ev: 逐席位身份、坐标、R/D和自他区分断言通过ASan/UBSan；仅验收该观测契约 [main-unique]
  - B2-R46 [process] R46 用户新增练习日志的场次与重复数据核验：1000 帧有 500 份完全重复，去重后才统计；7fb 归档中 27835 目录 score 却属于 2a4ed，拒绝串场归因；未精确绑定每场二进制，不冒充本工具新补丁实战。
      src: origin/main:README.md:69
      ev: 1000帧有500份完全重复，去重后才统计…拒绝串场归因…不冒充本工具新补丁实战 [main-unique]
  - B2-R47 [process] R47 分析文档和历史报告迁入独立仓库：迁移点名五篇、拆出 ARENA 历史结论、14 份 JSON 保留原字节；运行/源码/规则接口、测试用法及仍使用的选定参数留代码仓库；跨仓引用已修复，practice 不变。
      src: origin/main:README.md:70
      ev: 14份JSON保留原字节…跨仓引用已修复，practice不变 [main-unique]
  - B2-R48 [metric] R48 未来堡垒前置规划及公告采纳追踪：同夹具及时解释时无双窗口 5→11；迟到不补时；首版 59011 退步保留，恢复 active 策略后 69013 对抗 36.21→36.44、胜率持平；非原版新补丁实战。
      src: origin/main:README.md:71
      ev: 同夹具及时解释时无双窗口5→11；迟到不补时。首版59011退步保留 [main-unique]
  - B2-R49 [metric] R49 第一阶段 38/40 回跳 30 的同场取证：三场每 Tick 各有 stage1 与 stage2 计分；R190 对应 38/30，R200 对应 40/30，score.json 及 scoring.log 为 40；未改原裁判，冲突消息进程身份仍待维护方溯源。
      src: origin/main:README.md:72
      ev: R190对应38/30，R200对应40/30，score.json及scoring.log为40。未改原裁判 [main-unique]
  - B2-05 [process] “验收”必须对应具体范围：R13 的 ✅ 仅表示重复公告回归通过；R14/R15 的 ❌ 是测试执行失败而非算法已输；R17/R18/R24 及 R26–R34 的实现栏破折号表示外部研究或拒绝项；R29/R30 的执行/验收只指函数反例。
      src: origin/main:README.md:74
      ev: 本表“验收”必须对应具体范围 [main-unique]
  - B2-06 [goal] P0（最高优先）：在正常 Ubuntu 22.04 / ROS 2 Humble/DDS 环境获取 A 与标准 B/C/D 的真实回执、R/D/M、得分、死亡、无效动作、模型调用与事件可用时间；不要动裁判原件。
      src: origin/main:README.md:78
      ev: 在正常 Ubuntu 22.04 / ROS 2 Humble/DDS 环境获取 A 与标准 B/C/D 的真实回执…不要动裁判原件 [main-unique]
  - B2-07 [goal] P1：实测新增目标规划（迟滞、资源串和信息增益），下一步在正常 DDS 原版裁判与标准对手下复核。
      src: origin/main:README.md:79
      ev: 下一步在正常DDS原版裁判与标准对手下复核 [main-unique]
  - B2-08 [goal] P2：补齐搜索模型再决定是否扩展；继续只执行首步，下一 Tick 依据裁判回执重算。
      src: origin/main:README.md:80
      ev: 继续只执行首步，下一Tick依据裁判回执重算 [main-unique]
  - B2-09 [goal] P3：多情景与消融——测试改动是否真实提升、什么地图/对手下失效；失败可回退基线。
      src: origin/main:README.md:81
      ev: 失败可回退基线 [main-unique]
  - B2-10 [goal] P4：赛前封存与验收——确认版本、配置、协议、运行入口和规则权限，保持可追溯。
      src: origin/main:README.md:82
      ev: 确认版本、配置、协议、运行入口和规则权限，保持可追溯 [main-unique]
  - B2-11 [process] 更新协议：每次处理一个稳定 ID，先核对当前仓库/选手工程的实际 HEAD、规则版本和已有测试证据；当前这套研究/追踪工作仅使用已经存在的目标分支，不擅自创建分支；只有在对应阶段确实完成时改成 ✅，尚未做保留 ⬜；任何改动应记录日期、提交 SHA、测试命令、输入场景、预期与实际结果；不许基于文档、旧回放或别人的 moc
      src: origin/main:README.md:86
      ev: 不擅自创建分支…不许基于文档、旧回放或别人的 mock 记录填“实战通过” [main-unique]
  - B2-12 [constraint] 把研究与参赛代码分开；赛中遵守正式的封存、统一 AI 接口及公开感知权限，不允许读取观赛全图、内部 ROS 或未经许可模型；本 README 仅含适合总览的状态，不包含内部准备材料的入口和私密记录。
      src: origin/main:README.md:88
      ev: 不允许读取观赛全图、内部 ROS 或未经许可模型 [main-unique]
  - B2-13 [process] 原有协作约定（历史保留；新任务以当前明确授权和上面的追踪规范为准）：使用 AI 生成或修改的代码，应先提交到非 main 分支，再通过 PR 合并到 main。
      src: origin/main:README.md:92,98
      ev: 使用 AI 生成或修改的代码，应先提交到非 "main" 分支，再通过 PR 合并 [main-unique: 内容与 ANALYSIS governance 规范一致，但作为 main README 的一部分重新收录]
  - B2-14 [process] 历史约定：较大的功能改动使用 Create a merge commit 保留完整提交历史；较小的功能改动优先 Rebase and merge，若无法使用再考虑 Squash and merge。
      src: origin/main:README.md:102-103
      ev: 较大的功能改动：使用 Create a merge commit [main-unique]
  - B2-15 [process] 历史约定：方案尚未确定或效果有待验证的改动，无论大小都应先提交到非 main 分支验证后再通过 PR 合并；内容明确且已验证的补丁可以直接提交到 main。
      src: origin/main:README.md:109-110
      ev: 方案尚未确定或效果有待验证：…都应先提交到非 "main" 分支 [main-unique]
  - B2-16 [process] 历史用户约定：代码提交到另一个仓库；对 AI 让其新建 branch 分析并把结果记录到新建的 branch，不提交 PR；最后提交的是只有代码的那个仓库。
      src: origin/main:README.md:114-118
      ev: 让他们新建branch分析把结果记录到新建的branch，不提交pr…最后提交的是只有代码的那个仓库 [main-unique: 用户原文引述]

## result 3: scope=code-iterate-arena
- checks: [{"req_id": "GL-01", "status": "met", "evidence": "docs/01-source-review.md:76 原文一致：\"每队 1–2 人；第一阶段独立采集 100 Tick，100 ms/Tick，共 10 秒，满分 40\"。（注：任务文本中 Requirements JSON 为空，实际校验对象为工作区 reqs-doc-analysis-a.json，即 check_evidence.py 所读文件；cited 路径属分析仓，WSL /home/frank/cst 仅为代码仓，HEAD 已前移至 8da0ede，代码核对均以 git show 05a0afe 固定）"}, {"req_id": "GL-02", "status": "met", "evidence": "docs/01-source-review.md:77 原文一致：\"第二阶段最多四队同场 500 Tick，500 ms/Tick，共 250 秒，满分 60\""}, {"req_id": "GL-03", "status": "met", "evidence": "docs/38-version-league-spec-2026-10-29.md:50 原文一致：\"stage2 目标 50 的当前锚点：训练集 41.25；联赛数据将给出原版/自战维度的真实名次与分数分布，作为 50 分验收的第一手证据\""}, {"req_id": "GL-04", "status": "met", "evidence": "docs/37-race-batches-real-battles-2026-10-29.md:60 原文一致：\"stage-2 证据缺口（原版对局 + 自战联赛）仍待 C7/U6 版本联赛实施 —— 当前唯一 stage2 锚点仍是训练集 41.25，距离 50 目标尚远\""}, {"req_id": "GL-05", "status": "met", "evidence": "docs/38-version-league-spec-2026-10-29.md:3 即 cited 行，原文含\"目的：补齐 stage-2 证据缺口 —— 与原版的一局 + 自己打自己不同模型\"与\"U6 判定：多 profile 自战档案不能代表旧版本或原版 robot_node\"（**加粗与句尾\"）。\"致自动匹配误判，人工核对一致）"}, {"req_id": "GL-06", "status": "met", "evidence": "docs/implementation/LESSONS.md:76 原文一致：\"结论：阶段一40分受TSP下界约束不可达（天花板≈37）；阶段二50分需要R≈90+M3+D500……两目标在当前规则与视野4下均不可达；目前经验已到（锚点，按不可达口径如实记载）\""}, {"req_id": "MT-01", "status": "met", "evidence": "docs/01-source-review.md:108 原文一致：\"第一阶段：S1 = 40 × R1 / 200\""}, {"req_id": "MT-02", "status": "met", "evidence": "docs/01-source-review.md:110 原文一致（标注 v1.0）：\"第二阶段：S2 = 30 × min(R/120, 1) + 15 × min(D/300, 1) + 5 × M\""}, {"req_id": "MT-03", "status": "met", "evidence": "docs/03-tradeoffs.md:13 原文一致：\"S2=30 min(R/120,1)+15 min(D/500,1)+5M。未封顶时资源斜率0.25分/价值，调整后有效伤害0.03分/点；普通资源直接2.5分、高级5分，任务每项5分\""}, {"req_id": "MT-04", "status": "met", "evidence": "docs/11-v1.1-rule-migration.md:13 原文一致：\"| 对抗分 | 15×min(D/500,1)，最高仍15分，替代旧D/300 | RULES-02 §10.2，第18页 |\""}, {"req_id": "MT-05", "status": "met", "evidence": "docs/11-v1.1-rule-migration.md:15 原文一致：\"本Tick所有伤害/奖励先入账，再每次死亡扣60，最低0；分裂立即复活也扣 | RULES-02 §5.2第
- requirements: 205
  - C-01 [process] 比赛前只改 match_config.hpp，然后 bash build.sh；全部为明确配置，不读环境变量、不猜缺失值。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:3
      ev: // 比赛前只改这里，然后 bash build.sh。以下都是明确配置，不读环境变量、不猜缺失值。
  - C-02 [technical] 席位 team="A" 为裁判分配的本场席位（constexpr）。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:5
      ev: inline constexpr const char *team = "A"; // 裁判分配的本场席位。
  - C-03 [technical] team_name 仅注册显示队名，不代替席位或令牌身份。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:6
      ev: // 注册显示队名，不代替席位或令牌身份。
  - C-04 [technical] stage 为 1=采集、2=对抗（constexpr，当前 2）。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:7
      ev: inline constexpr int stage = 2; // 1：采集；2：对抗。
  - C-05 [technical] stage1_ticks=100：正式规则§3 动作 0–99，100 是最终状态。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:8
      ev: inline constexpr int stage1_ticks = 100; // 正式规则§3：动作0–99，100是最终状态。
  - C-06 [technical] stage2_ticks=500：动作 0–499，500 是最终状态；改练习长度须在此处明确修改。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:9
      ev: inline constexpr int stage2_ticks = 500; // 动作0–499，500是最终状态；改练习长度时在这里明确改。
  - C-07 [technical] ros_domain_id="27" 为同一比赛 ROS 网络的域编号。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:11
      ev: inline constexpr const char *ros_domain_id = "27"; // 同一比赛ROS网络的域编号。
  - C-08 [technical] ros_localhost_only="0"：0 允许局域网通信；1 只在本机通信。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:12
      ev: // 0允许局域网通信；1只在本机通信。
  - C-09 [technical] RMW 实现固定为 rmw_fastrtps_cpp。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:13
      ev: inline constexpr const char *rmw_implementation = "rmw_fastrtps_cpp";
  - C-10 [constraint] url/token/model 三项必须明确；url 必须是完整的 /chat/completions 地址；正式赛填官方网关，不填模型服务主页。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:15
      ev: // 三项必须明确……url 必须是完整的 /chat/completions 地址。正式赛填官方网关，不填模型服务主页。
  - C-11 [process] 练习裁判须另以 real 模式连接真实模型；mock 只验证通信。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:18
      ev: // 练习裁判须另以 real 模式连接真实模型，mock 只验证通信。
  - C-12 [constraint] ai_token="practice-A" 仅为公开练习令牌；正式令牌不要提交。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:20
      ev: inline constexpr const char *ai_token = "practice-A"; // 仅公开练习令牌；正式令牌不要提交。
  - C-13 [technical] ai_model="deepseek-flash" 为请求体中的模型名；练习启动器同时设置 PRACTICE_MODEL。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:21
      ev: // 请求体中的模型名；练习启动器同时设置PRACTICE_MODEL。
  - C-14 [technical] ai_timeout_ms=35000 后台等完整响应，覆盖练习代理 5 秒连接+25 秒读取，不阻塞动作。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:22
      ev: // 后台等完整响应；覆盖练习代理5秒连接+25秒读取，不阻塞动作。
  - C-15 [technical] ai_connect_timeout_ms=5000：建连单独限 5 秒。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:23
      ev: // 建连单独限5秒；原来的500ms对出网/TLS过短。
  - C-16 [technical] ai_max_tokens=2200 为多事件 JSON 预算；公告示例 512 不是已确认的赛事硬上限，按实际配额修改。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:24
      ev: // 多事件JSON预算；公告示例512不是已确认的赛事硬上限，按实际配额修改。
  - C-17 [technical] ai_http_proxy=""：空串明确表示直连。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:25
      ev: // 机器人→网关的网络代理；空串明确表示直连。
  - C-18 [protocol] 2026-10-28 正式公告：ai_thinking="disabled" 必须在请求 JSON 顶层明确写入；不是改 URL，也不是只改练习裁判配置。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:26
      ev: // 必须在请求JSON顶层明确disabled；不是改URL，也不是只改练习裁判配置。
  - C-19 [technical] ai_json_output=true 明确请求 JSON 模式；Prompt 也要求 JSON，仍需本地校验。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:29
      ev: // 明确请求JSON模式；Prompt也要求JSON，仍需本地校验。
  - C-20 [constraint] practice 组上游配置只供 bash practice.sh 使用，正式赛不使用；真实服务密钥与 practice-A 是两种不同的凭据。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:31
      ev: // 只供 bash practice.sh 使用：练习代理→真实模型。正式赛不使用这组上游配置。真实服务密钥与practice-A是两种不同的凭据。
  - C-21 [technical] practice_port=8080 为原版练习代理监听端口，须与本机 ai_url 一致。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:33
      ev: // 原版练习代理监听端口，须与本机ai_url一致。
  - C-22 [technical] practice_llm_url 为 DeepSeek 文档给出的完整 POST 端点。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:34
      ev: // DeepSeek文档给出的完整POST端点。
  - C-23 [constraint] practice_llm_key=《临时练习密钥》为临时验证用：用后即还原为空并重建，绝不提交（提交版本为 ""）。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:35
      ev: // 临时验证用，用后即还原为空并重建，绝不提交。工作树当前为临时填值（只显示占位，不显示密钥正文），已提交值为空。
  - C-24 [constraint] practice_llm_proxy 为临时 WSL 出网代理：用后还原为空，不提交。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:36
      ev: // 临时验证用：WSL出网代理；用后还原为空，不提交。
  - C-25 [constraint] 攻击距离、伤害、计分公式和结算顺序按规则实现，不在配置里调。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:38
      ev: // 下面只调策略取舍。攻击距离、伤害、计分公式和结算顺序按规则实现，不在这里调。
  - C-26 [technical] prepare_fortress_value=0.0：堡垒预告提前占点杠杆默认关，待竞技场评估。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:45
      ev: // 自visible-resource-bfs采纳的行为杠杆，默认关，待竞技场评估。
  - C-27 [technical] stale_grace_ticks=0：资源离视野当 Tick 即衰减；默认关，待竞技场评估晋升。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:48
      ev: // 未观测≠消失……0=离视野当Tick即衰减。默认关，待竞技场评估晋升。
  - C-28 [metric] stage1_frontier_value 与阶段二 frontier_value 分离：arena-frontier-2026-10-29 轮证实探索权重对两阶段影响相反（阶段二受益/阶段一受害），共享会互相绑架。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:54
      ev: // 与阶段二分离——arena-frontier-2026-10-29轮证实探索权重对两阶段影响相反……共享会互相绑架。
  - C-29 [technical] stage2_race_gate=false：两轮实验均显示早期主动交火有压制对手扫资源的价值，关闭。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:60
      ev: // 第二阶段竞速闸门：两轮实验均显示早期主动交火有压制对手扫资源的价值，关闭。
  - C-30 [technical] race_reach_holdoff=0.0（0-1）：竞速期到点任务暂缓折扣；0=旧行为。工作树实测为 0.0，未发现 1.0 改动。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:61
      ev: // docs/35 损失路径=首分钟资源争抢……资源清空后恢复原权重（M 点晚拿不丢）……0=旧行为。
  - C-31 [technical] stage2_explore_gate_tick=0：第二阶段扫图关闭时刻闸门；0 为关闭。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:62
      ev: // Tick≥此值且已知资源已清空时关闭扫图……0为关闭。
  - C-32 [technical] stage2_shadow_value=0.0：影子跟踪只利用对手行为蕴含的信息，不假设未知格里有资源；0 为关闭。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:66
      ev: // 不假设未知格里有资源，只利用对手行为蕴含的信息。
  - C-33 [technical] worst_case_survival=false：预测防御只作机会估值，不作伤害上界的确定排除项；默认关，待竞技场评估晋升。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:84
      ev: // 1=生存判定按全敌攻击最坏情形（预测防御只作机会估值，不作伤害上界的确定排除项）……默认关，待竞技场评估晋升。
  - C-34 [technical] low_hp_attack_discount=1.0：hp<60 且未被火力波及时攻击估值乘此值；1.0=旧行为（冠军逐位一致）。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:85
      ev: // 策略层§6+战术层深度0攻击分支同口径……1.0=旧行为（冠军逐位一致）。
  - C-35 [metric] explore_component_value=0：家族已永久关闭——heldout 一次性验证 vs 冠军封存 0.8299 为 0.7906 即 −0.039，stage2 score 42.06<43.875、R 增益未复现；0=旧行为，永久关闭。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:86
      ev: // heldout一次性验证 vs 冠军封存0.8299……为0.7906即−0.039……0=旧行为，永久关闭。
  - C-36 [metric] post_cap_combat_weight=0.02 为唯一晋升杠杆：train objective 0.7891→0.8056；heldout 一次性验证通过 0.771→0.830，stage2 score 40.8→43.9、invalid 0（arena-postcap-heldout-2026-10-29）
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:87
      ev: // train晋升：objective 0.7891→0.8056……heldout一次性验证通过：objective 0.771→0.830……stage2 score 40.8→43.9、R 61.3→69.6、win_share 0.375→0.458、invalid 0。
  - SP-01 [technical] 正式入口只取编译期配置；第二个 Strategy 构造入口只供离线评测注入参数，不提供 ROS 热更新。
      src: src/rmtc_bot/include/rmtc_bot/strategy_parameters.hpp:7
      ev: // 正式入口只取编译期配置；第二个Strategy构造入口只供离线评测注入参数，不提供ROS热更新。
  - SP-02 [process] loop_recovery 离线可关闭作对照；正式仍由唯一配置封存。
      src: src/rmtc_bot/include/rmtc_bot/strategy_parameters.hpp:32
      ev: // 离线可关闭作对照；正式仍由唯一配置封存。
  - SP-03 [constraint] validate() 拒绝非法策略权重与预算：权重须有限且 0..1000，healing_below_hp≤100，折扣类 0..1，plan_depth 1..8，beam_width 1..32，loop_window 6..32 等，否则抛异常。
      src: src/rmtc_bot/include/rmtc_bot/strategy_parameters.hpp:51
      ev: if (!std::isfinite(value) || value<0 || value>1000) throw std::runtime_error("invalid strategy weight"); …throw std::runtime_error("invalid strategy budget");
  - R-01 [constraint] rules 为 v1.2 的确定结算，比赛策略和测试端共用，数值不参与调参。
      src: src/rmtc_bot/include/rmtc_bot/rules.hpp:10
      ev: // v1.2的确定结算；比赛策略和测试端共用，数值不参与调参。
  - R-02 [technical] 基础数值：max_hp=100、普通伤害 20、防御伤害 10、击杀奖励 60、死亡扣减 60、重生等待 3 Tick、出生保护 2 Tick。
      src: src/rmtc_bot/include/rmtc_bot/rules.hpp:11
      ev: inline constexpr double max_hp = 100, ordinary_damage = 20, defended_damage = 10; inline constexpr double kill_reward = 60, death_loss = 60; inline constexpr int respawn_wait = 3, protection_ticks = 2
  - R-03 [technical] 防御只认本 Tick 动作，绝不沿用上帧 defending。
      src: src/rmtc_bot/include/rmtc_bot/rules.hpp:78
      ev: const bool defending=actions[target].kind==ActionKind::defend; // 只认本Tick动作，绝不沿用上帧defending。
  - R-04 [technical] 过量伤害按比例分摊，不多计 D。
      src: src/rmtc_bot/include/rmtc_bot/rules.hpp:93
      ev: const double actual=std::min(fighters[target].hp,total); // 过量伤害按比例分摊，不多计D。
  - R-05 [metric] D 不在 500 截断；互杀也是先入账再扣除。
      src: src/rmtc_bot/include/rmtc_bot/rules.hpp:105
      ev: return std::max(0.0,previous+earned-death_loss*deaths); // D不在500截断；互杀也是先入账再扣除。
  - R-06 [technical] 重生选点墙只排除落点、不阻断搜索；无合法格则继续等待，不能把坐标伪造成出生点。
      src: src/rmtc_bot/include/rmtc_bot/rules.hpp:129
      ev: // 墙只排除落点，不阻断“曼哈顿层、上右下左”的选点搜索。……return {-1,-1}; // 无合法格则继续等待，不能把坐标伪造成出生点。
  - R-07 [protocol] none 是不提交/裁判等待，不是选手默认 WAIT。
      src: src/rmtc_bot/include/rmtc_bot/rules.hpp:16
      ev: enum class ActionKind { none, move, attack, defend }; // none是不提交/裁判等待，不是选手默认WAIT。
  - R-08 [metric] 第一阶段独立采集赛满分 40 分；第二阶段多队对抗按三项任务单场最高 60 分，逐轮晋级；两阶段分数不相加决定晋级。
      src: practice/rules.txt:10
      ev: + 第一阶段为独立采集赛，满分 40 分，用于种子排位；第二阶段为多队对抗赛，按三项任务单场最高 60 分，逐轮晋级。+ 两阶段分数不相加决定晋级。
  - R-09 [constraint] 代码审查及个人答辩用于纳新综合评定，不计入公开竞赛排名。
      src: practice/rules.txt:11
      ev: + 代码审查及个人答辩用于纳新综合评定，不计入公开竞赛排名。
  - R-10 [protocol] 正式比赛必须自主决策，禁止人工实时操控；不存在随机命中、暴击、闪避或随机伤害；相同配置和动作可重复得到相同结果。
      src: practice/rules.txt:13
      ev: 正式比赛必须自主决策，禁止人工实时操控。……不存在随机命中、暴击、闪避或随机伤害；“随机事件”按照本场安排及公开公告生效，相同配置和动作可重复得到相同结果。
  - R-11 [constraint] 一人一队：每名学生只能在一支队伍登记。
      src: practice/rules.txt:31
      ev: | 一人一队 | 每名学生只能在一支队伍登记 |
  - R-12 [constraint] 参数调整必须在适用比赛开始前通过官方公告公布；同一竞赛条件下不得对不同队伍采用不同参数（除随机事件外）。
      src: practice/rules.txt:83
      ev: 参数调整在适用比赛开始前通过官方公告向所有参赛队伍公布，同一竞赛条件下不得对不同队伍采用不同参数(除随机事件外)。
  - R-13 [process] 每队须完成前置检录（编译启动、接收感知、回填正确 tick/session_id、提交合法动作），截图或录屏于 2026 年 10 月 31 日 20:00 前递交；工作人员不帮助设计或修改策略。
      src: practice/rules.txt:88
      ev: 每队须在正式比赛前完成编译启动……统一于2026年10月31日20：00前随其他材料一起递交……工作人员可协助排查环境和接口问题，不帮助设计或修改策略。
  - R-14 [constraint] 禁止现场修改源代码、算法实现、Prompt、其他决策参数或人工发送具体动作。
      src: practice/rules.txt:110
      ev: 比赛期间允许队内讨论、按规定重启已封存程序……禁止现场修改源代码、算法实现、Prompt、其他决策参数或人工发送具体动作。
  - R-15 [constraint] decision_type 的值只能来自本队已登记的枚举；decision_config.json 现场只允许修改 decision_type，不得夹带坐标、动作、目标 ID、任意指令或新增算法参数。
      src: practice/rules.txt:112
      ev: decision_type 的值只能来自本队已登记的枚举。……现场只允许修改 decision_type，不得夹带坐标、动作、目标ID、任意指令或新增算法参数。
  - R-16 [constraint] 每队每场最多申请两次人工策略切换，须在比赛暂停期间或加赛之前提出，经裁判批准并登记；可选策略须属于赛前封存枚举，不得借此实施逐 Tick 人工控制。
      src: practice/rules.txt:114
      ev: 每队每场最多申请两次人工策略切换。切换须在比赛暂停期间或加赛之前提出，经裁判批准并登记后进行……不得修改程序逻辑或借此实施逐 Tick 人工控制。
  - R-17 [constraint] 程序异常后可登记重启，每阶段原则上最多 2 次人工重启，不暂停比赛、不补偿时间，且必须使用封存版本；席位/队名/令牌调整不得借此绕过决策类型切换流程。
      src: practice/rules.txt:116
      ev: 每阶段原则上最多 2 次人工重启，不暂停比赛、不补偿时间，且必须使用封存版本。……不得借此绕过上述决策类型切换流程。
  - R-18 [process] 第一阶段全部结束后设置统一调整窗口，可修改参数、Prompt 和任务解析逻辑；窗口结束后重新确认第二阶段版本；后续淘汰轮次不自动构成新的策略修改窗口。
      src: practice/rules.txt:118
      ev: 第一阶段全部结束后设置统一调整窗口，可修改参数、Prompt 和任务解析逻辑；窗口结束后重新确认第二阶段版本。后续淘汰轮次不自动构成新的策略修改窗口。
  - R-19 [protocol] 公开测试裁判的话题名称、消息类型、感知和动作格式与正式比赛公开接口一致；测试场景/地图/事件安排和成绩仅用于练习，不代表正式赛场条件或正式成绩。
      src: practice/rules.txt:121
      ev: 测试端话题名称、消息类型、感知和动作格式与正式比赛公开接口一致。测试场景、地图、事件安排和成绩仅用于练习……
  - R-20 [constraint] 测试端人工查看全图、编辑练习配置和使用陪练车不得作为参赛程序的策略输入；参赛程序只能使用通信协议允许的公开接口；随机事件须通过公开自然语言公告交由 LLM 理解判断。
      src: practice/rules.txt:123
      ev: 这些功能不得作为参赛程序的策略输入。参赛程序只能使用通信协议允许的公开接口，随机事件须通过公开自然语言公告交由 LLM 理解判断。
  - R-21 [metric] 第二阶段 500ms/Tick、500 Tick、4 分 10 秒；第一阶段动作 Tick 0–99、最终状态 tick=100；第二阶段动作 Tick 0–499、最终状态 tick=500；最终状态发布后不接收新动作。
      src: practice/rules.txt:135
      ev: | 第二阶段 | 分组资源争夺与对抗 | 500 ms/Tick | 500 Tick | 4 分 10 秒 |……最终状态发布后不接收新动作。
  - R-22 [technical] 胜者组与败者组分别按原种子蛇形分组，每组最多 4 队，同一赛道各组人数差不超过 1。
      src: practice/rules.txt:140
      ev: 胜者组与败者组分别按原种子蛇形分组，每组最多 4 队，同一赛道各组人数差不超过 1。
  - R-23 [process] 技术报告含整体设计思路、功能完成情况与方式、队内分工、日程规划及遇到的问题与解决，每参赛队提交一份（语雀文档）。
      src: practice/rules.txt:56
      ev: + 技术报告内容：含整体设计思路、功能完成情况与方式、队内分工、日程规划及遇到的问题与解决
  - R-24 [metric] 第二阶段 D 达到 500 时对抗项取得满分 15 分；已完成任务不因之后死亡被撤销。
      src: practice/测试使用教程.md:132
      ev: 达到 500 时对抗项取得满分 15 分……完成的任务不因之后死亡被撤销。
  - R-25 [technical] 击杀奖励拆分：每批次去重正贡献者均分；chili 批次统一结算；环境死亡无击杀奖励；战斗中死亡的车不重复获得 chili 奖励。
      src: practice/测试使用教程.md:134
      ev: 击杀奖励拆分规则（dedup positive contributors per batch；chili batch settled together；environmental death no kill reward……）
  - R-26 [constraint] 参赛程序只能使用通信协议允许的接口，不能从网页或本地文件读取全图、事件参数作为决策输入。
      src: practice/测试使用教程.md:136
      ev: 参赛程序只能使用通信协议允许的接口，不能从网页或本地文件读取全图、事件参数作为决策输入
  - R-27 [constraint] 不要硬编码测试 token、session、地图、事件时间。
      src: practice/测试使用教程.md:4
      ev: 不要硬编码测试 token/session/地图/事件时间。
  - P-01 [protocol] 统一 LLM 网关可用于高层决策；正式第二阶段每场须满足本场真实成功调用要求。
      src: practice/CONTESTANT_PROTOCOL.md:9
      ev: + 统一 LLM 网关可用于高层决策；正式第二阶段每场须满足本场真实成功调用要求；
  - P-02 [protocol] QoS：感知/动作 RELIABLE+VOLATILE+KEEP_LAST(1)；注册/任务/队伍名录 RELIABLE+TRANSIENT_LOCAL(1)；事件公告 RELIABLE+TRANSIENT_LOCAL(128)。
      src: practice/CONTESTANT_PROTOCOL.md:54
      ev: | 感知、动作 | RELIABLE | VOLATILE | 1 | … | 事件公告 | RELIABLE | TRANSIENT_LOCAL | 128 |
  - P-03 [protocol] self.position 为绝对坐标数组、visible_entities[].position 为九行相对位置字符串，不能使用同一种类型解析两者；接收端须检查字段类型并处理解析异常，不得因字段缺失或类型错误导致进程退出；无法形成可靠决策时不提交臆测动作。
      src: practice/CONTESTANT_PROTOCOL.md:150
      ev: 接收端须检查字段类型并处理解析异常，不得因字段缺失或类型错误导致进程退出；无法形成可靠决策时不提交臆测动作。
  - P-04 [protocol] team_name 为 1–96 UTF-8 字节、不含换行，仅注册显示，不用于路由或身份验证。
      src: practice/CONTESTANT_PROTOCOL.md:8
      ev: team_name 1-96 UTF-8 字节无换行，不用于路由或身份。
  - P-05 [protocol] 动作消息上限 4096 字节；每 tick 每队最多 128 条消息；每 tick 保留最新合法候选。
      src: practice/CONTESTANT_PROTOCOL.md:123
      ev: 4096-byte action cap, 128 msgs/tick/team; latest valid candidate kept。
  - P-06 [protocol] 同一 tick 重发缓存结果 OK；新 session 清空全部缓存。
      src: practice/CONTESTANT_PROTOCOL.md:132
      ev: same-tick resubmit cache OK, new session clears caches。
  - P-07 [protocol] 只处理最新 tick；只订阅/发布本席位话题。
      src: practice/CONTESTANT_PROTOCOL.md:148
      ev: only newest tick processed; own-seat topics only。
  - P-08 [protocol] 不得读取其他席位的感知或观众数据；不得使用截屏反馈。
      src: practice/CONTESTANT_PROTOCOL.md:169
      ev: cannot read other seats' perception or spectator data, no screen-capture feedback.
  - P-09 [protocol] 动作必须回填正确 tick 和 session_id（echo）。
      src: practice/CONTESTANT_PROTOCOL.md:205
      ev: action echo tick+session_id。
  - P-10 [protocol] 位置字符串为 89 字符的 9×9 编码；相对位置字符串与绝对坐标数组类型不同。
      src: practice/CONTESTANT_PROTOCOL.md:231
      ev: 89-char 9×9 position strings.
  - P-11 [protocol] 请求体 ≤2MiB；只 2xx 消耗配额；不允许查询配额剩余。
      src: practice/CONTESTANT_PROTOCOL.md:384
      ev: 2MiB request cap; no quota remaining query; only 2xx consume quota.
  - P-12 [protocol] 统一 LLM 网关仅用于高层决策（公告理解/事件提交），不得绕开官方网关。
      src: practice/CONTESTANT_PROTOCOL.md:320
      ev: 统一 LLM 网关可用于高层决策……only official gateway allowed, no bypass.
  - P-13 [protocol] 网关限流契约：每 token 最多 2 个在途调用；100 POST/10s/IP；5 秒读取超时；不跟随重定向。
      src: practice/CONTESTANT_PROTOCOL.md:382
      ev: 100 POST/10s/IP, 2 in-flight per token, 5s read timeout, no redirects.
  - P-14 [protocol] 在途调用占用名额但尚未计入成功调用次数，失败即释放；成功返回后即消耗次数，模型输出不理想或客户端未及时收到不因此退回配额。
      src: practice/CONTESTANT_PROTOCOL.md:386
      ev: + 在途调用占用名额但尚未计入成功调用次数，失败即释放。成功返回后即消耗次数，模型输出不理想或客户端未及时收到，不因此退回配额；
  - P-15 [protocol] 本场 AI 调用资格以主办方确认的本场、本席位成功调用记录为准；其他场次或联调中的调用不能替代本场资格。
      src: practice/CONTESTANT_PROTOCOL.md:391
      ev: 本场 AI 调用资格以主办方确认的本场、本席位成功调用记录为准。其他场次或联调中的调用不能替代本场资格。
  - P-16 [protocol] 配额耗尽（quota_exceeded 429）必须停止并自降级；瞬时 429 按退避处理。
      src: practice/CONTESTANT_PROTOCOL.md:387
      ev: quota_exceeded 429 stops vs transient 429 backoff; quota exhausted must self-degrade.
  - P-17 [metric] 阶段二每场最终结算前要求至少一次属于本场、本席位的真实统一 AI 成功调用；否则任务分为 0，原始任务数也不作为同分优势，资源和对抗分保留（M=0）。
      src: practice/CONTESTANT_PROTOCOL.md:395
      ev: + 阶段二每场最终结算前要求至少一次属于本场、本席位的真实统一 AI 成功调用；否则任务分为 0，原始任务数也不作为同分优势，资源和对抗分保留。
  - P-18 [process] 公开测试端提供 stage1、stage2；第一阶段模板 100ms/Tick、100 Tick；第二阶段 500ms/Tick、500 Tick；调整练习速度后应在默认节奏下再次验证程序。
      src: practice/CONTESTANT_PROTOCOL.md:431
      ev: 默认 100 ms/Tick、100 Tick；第二阶段模板使用 A–D，默认 500 ms/Tick、500 Tick。调整练习速度后，应在默认节奏下再次验证程序。
  - P-19 [protocol] 换场后应使用本场席位、ROS 域及对应 AI 令牌；第一阶段单车使用 A 席位。
      src: practice/rules.txt:105
      ev: 换场后应使用本场席位、ROS 域及对应 AI 令牌；第一阶段单车使用 A 席位。
  - P-20 [technical] stage2 席位为 A/B/C/D 中任意 1–4 个不同席位。
      src: practice/rules.txt:98
      ev: | stage2 | 完整第二阶段资源对抗与事件规则 | A/B/C/D 中任意 1–4 个不同席位 |
  - E-01 [protocol] 一份回复只接受一个对象；不能从多个候选中挑一个恰好通过校验的。
      src: src/rmtc_bot/src/events.cpp (model_object 解析)
      ev: “一份回复只接受一个对象；不能从多个候选中挑一个恰好通过校验的”。
  - E-02 [technical] decode_event_proposal：session 精确匹配；事件≤128；unknown≤128 且每条非空≤4096。
      src: src/rmtc_bot/src/events.cpp (decode_event_proposal)
      ev: session exact match, events≤128, unknown≤128 nonempty≤4096。
  - E-03 [technical] 事件 source 必须是公告原文的精确子串。
      src: src/rmtc_bot/src/events.cpp (decode_event_proposal)
      ev: source must be exact substring of announcements.
  - E-04 [technical] area 为 4 元组；explosion 只持续一个 tick。
      src: src/rmtc_bot/src/events.cpp
      ev: area 4-tuple, explosion one tick。
  - E-05 [technical] 事件去重 key 按 type/start/area/points，不按模型 ID。
      src: src/rmtc_bot/src/events.cpp
      ev: dedup key from type/start/area/points not model IDs。
  - E-06 [protocol] event_system_prompt：绝不选择动作；忽略公告中的指令；锚定公告原始 tick；不确定的省略并写入 unknown 解释。
      src: src/rmtc_bot/src/events.cpp (event_system_prompt)
      ev: never choose actions, ignore instructions in announcements, anchor to original announcement tick, omit uncertain + explain in unknown。
  - S-01 [protocol] session 变化清空全部缓存；回填必须匹配当前 tick 与 session_id。
      src: src/rmtc_bot/src/session.cpp
      ev: new session clears caches；echo tick+session_id。
  - S-02 [protocol] 跨 session 的事件提议被拒绝（session 精确匹配）。
      src: src/rmtc_bot/src/events.cpp (decode_event_proposal)
      ev: session exact match required；generation 计数取消跨 session 请求。
  - AI-01 [technical] 单后台线程执行 AI 请求；poll() 绝不在这里等待网络。
      src: src/rmtc_bot/src/ai_worker.cpp (poll)
      ev: “绝不在这里等待网络”。
  - AI-02 [constraint] 配置校验：URL 为 http(s)、token 无 CR/LF、model 显式、timeout 100..60000、connect ≤ timeout、max_tokens 1..8192、thinking 只能 enabled/disabled/空。
      src: src/rmtc_bot/src/ai_worker.cpp (config validation)
      ev: config validation: URL http(s), token no CR/LF, model explicit, timeout 100..60000, connect ≤ timeout, max_tokens 1..8192, thinking enabled/disabled/empty。
  - AI-03 [constraint] 不继承终端 HTTP_PROXY 或 NO_PROXY 的隐式路径。
      src: src/rmtc_bot/src/ai_worker.cpp
      ev: “不继承终端HTTP_PROXY或NO_PROXY的隐式路径”。
  - AI-04 [protocol] 不跟随重定向；401/403/400/404 停止该场请求。
      src: src/rmtc_bot/src/ai_worker.cpp
      ev: no redirects; 401/403/400/404 stop。
  - AI-05 [protocol] 429 quota_exceeded 停止；rate-limit 429 指数退避 1<<(failures-1) 秒。
      src: src/rmtc_bot/src/ai_worker.cpp
      ev: 429 quota_exceeded stop vs rate-limit backoff (1<<(failures-1) seconds)。
  - AI-06 [technical] generation 计数取消跨 session 请求；只采纳第一个 choice 的 content，绝不采用 reasoning_content；finish==length→model_output_truncated。
      src: src/rmtc_bot/src/ai_worker.cpp
      ev: only first choice's content adopted, never reasoning_content; finish==length→model_output_truncated。
  - AI-07 [technical] 请求 ≤2MiB；公告按精确字节去重，>65536→announcement_too_large；history>131072 不截断。
      src: src/rmtc_bot/src/ai_worker.cpp
      ev: request ≤2MiB; announcement dedup by exact bytes, >65536→announcement_too_large, history>131072 no truncation。
  - AI-08 [technical] invalid_replies≥3 停止重请求。
      src: src/rmtc_bot/src/ai_worker.cpp
      ev: invalid_replies≥3 stops re-request。
  - AI-09 [technical] 第一帧总是排队一次请求（understood_=false）。
      src: src/rmtc_bot/src/ai_worker.cpp
      ev: first frame always queues a request (understood_=false)。
  - AI-10 [protocol] 阶段一必须零 AI 调用（回归测试 /stage1-must-not-call 期望 0）。
      src: tests/strategy_test.cpp (stage1-must-not-call)
      ev: stage1 must make zero AI calls；gateway scenario /stage1-must-not-call==0。
  - ST-01 [protocol] 只执行规划的第一步，绝不缓存未来动作队列。
      src: src/rmtc_bot/src/strategy.cpp
      ev: only first step executed, never cache future action queues。
  - ST-02 [protocol] 坐标始终来自感知；回执只确认移动与效果，不充当坐标来源。
      src: src/rmtc_bot/src/strategy.cpp
      ev: coordinates always from perception, receipts only confirm moves/effects。
  - ST-03 [technical] tick≥tick_limit→skip（finished）；dead→skip（dead）；非法帧→fallback，仅阶段二存活时 DEFEND（绝不 WAIT）。
      src: src/rmtc_bot/src/strategy.cpp
      ev: tick≥tick_limit→skip "finished"; dead→skip "dead"; invalid frame→fallback (DEFEND only if stage2 alive); defend fallback never WAIT。
  - ST-04 [technical] 致命移动前爆炸→skip；分裂激活于非出生点→强制等待。
      src: src/rmtc_bot/src/strategy.cpp
      ev: lethal pre-move explosion→skip; split activation on non-spawn→forced wait。
  - ST-05 [technical] 生存判定受 worst_case_survival 杠杆控制；预测绝不作为伤害上界的确定排除项。
      src: src/rmtc_bot/src/strategy.cpp (survival)
      ev: survival uses worst_case_survival lever (prediction never deterministic exclusion of damage upper bound)。
  - ST-06 [technical] MOVE 不能躲避当前 tick 战斗；illusion 只在提交时反转 MOVE，绝不反转 ATTACK。
      src: src/rmtc_bot/src/strategy.cpp
      ev: MOVE can't dodge current-tick combat; illusion inverts MOVE only at submission, ATTACK never。
  - ST-07 [metric] 采集估值封顶 score_delta（R=119+20 credits 只值 1 分）。
      src: src/rmtc_bot/src/strategy.cpp
      ev: capped score_delta for collection valuation (R=119+20 credits only 1 point)。
  - ST-08 [technical] 对手预测：2 次连续相同位移→只预测一步；匿名车绝不按位置匹配。
      src: src/rmtc_bot/src/strategy.cpp
      ev: opponent forecast = 2 consecutive same displacements → one step only, anonymous never matched by position。
  - ST-09 [technical] 堡垒占领仅从连续回执确认；buff 存活至事件结束（死亡不中断）。
      src: src/rmtc_bot/src/strategy.cpp
      ev: fortress capture only from consecutive receipts, buff survives death until event end。
  - ST-10 [metric] prepare_fortress 关闭态必须与无公告时逐位一致（L1000-1013 关闭态检查）。
      src: src/rmtc_bot/src/strategy.cpp:1000
      ev: prepare_fortress (L1000-1013, off-state must be identical to no-announcement)。
  - ST-11 [technical] 循环恢复需要可信回执；无安全出口→显式 defend，绝不伪造移动（L1401）。
      src: src/rmtc_bot/src/strategy.cpp:1401
      ev: loop recovery needs trusted receipts, no safe exit→explicit defend never fake movement (L1401)。
  - ST-12 [technical] safe_first_steps 为 horizon-8 时空安全路线；无认证路线→返回不受限。
      src: src/rmtc_bot/src/strategy.cpp (safe_first_steps)
      ev: safe_first_steps horizon-8 spatiotemporal, returns unrestricted if no certified route。
  - ST-13 [technical] chili 仅入口触发；己方点位免疫己方火力。
      src: src/rmtc_bot/src/strategy.cpp
      ev: chili entry-only trigger, own point immune to own fire only。
  - ST-14 [constraint] 探索绝不假设未知格里有资源。
      src: src/rmtc_bot/src/strategy.cpp (explore)
      ev: explore never assumes unknown contents ("不假设未知格里有资源")。
  - ST-15 [technical] stage1 flood/ring/tour 全部默认关闭。
      src: src/rmtc_bot/src/strategy.cpp
      ev: stage1 flood/ring/tour all off by default。
  - ST-16 [constraint] shadow 跟踪只使用对手行为蕴含的信息，不读取对手感知。
      src: src/rmtc_bot/src/strategy.cpp
      ev: shadow tracking uses only opponent behavior-implied info。
  - ST-17 [technical] tactical search 3-tick horizon、每首动作 beam 5、只发布第一个动作。
      src: src/rmtc_bot/src/strategy.cpp (tactical)
      ev: tactical search 3-tick horizon, beam 5 per first action, only first action published。
  - ST-18 [protocol] tactics::advance() 遵循裁判结算顺序（激活→战斗→移动→环境/治疗/堡垒→任务）。
      src: src/rmtc_bot/src/tactics.cpp (advance)
      ev: advance() follows referee order (activation→combat→move→environment/heal/fortress→tasks)。
  - ST-19 [protocol] task_reward +5 仅在 model_reply_seen 时计入；正式资格仍由裁判认定。
      src: src/rmtc_bot/src/tactics.cpp
      ev: task_reward +5 only if model_reply_seen ("正式资格仍由裁判认定")。
  - ST-20 [technical] low_hp_attack_discount 同口径应用于战术层深度 0 攻击分支（与策略层 §6 一致）。
      src: src/rmtc_bot/src/tactics.cpp
      ev: low_hp_attack_discount same口径 as strategy §6 at depth-0 attack branches。
  - ST-21 [technical] bounded simulated_steps ≤600（5 或 6 场景上限）。
      src: src/rmtc_bot/src/tactics.cpp
      ev: bounded simulated_steps ≤600 (5 or 6 scenarios)。
  - ST-22 [technical] tactical_risk 最差情景权重不是经训练的概率（scenario-mean/worst 混合不是经校准的概率）。
      src: src/rmtc_bot/src/tactics.cpp
      ev: scenario-mean/worst mix "不是经校准的概率"。
  - ST-23 [technical] 竞速闸门五处：stage2_race_gate L931-940、race_reach_holdoff L941-951、stage2_explore_gate_tick L1281-1284、stage2_pie_attack_discount L1358-1361、low_hp_attack_discount L1
      src: src/rmtc_bot/src/strategy.cpp:931
      ev: race gates (stage2_race_gate L931-940, race_reach_holdoff L941-951, stage2_explore_gate_tick L1281-1284, stage2_pie_attack_discount L1358-1361, low_hp_attack_discount L1362-1365, post_cap_combat_weigh
  - PL-01 [technical] 练习启动器同时设置 PRACTICE_MODEL；网关以请求体 model 优先于 PRACTICE_MODEL。
      src: practice/practice.py (launcher)
      ev: practice launcher sets PRACTICE_MODEL; body model preferred over PRACTICE_MODEL。
  - PL-02 [technical] start_bot.sh 校验席位必须为 A|B|C|D（否则 exit 2），并设置 RMTC_TEAM_TOKEN=practice-$TEAM。
      src: practice/start_bot.sh
      ev: start_bot validates seat A|B|C|D (exit 2 otherwise) and sets RMTC_TEAM_TOKEN=practice-$TEAM。
  - CA-01 [constraint] ai_check_test.py 断言 KEY 绝不出现在诊断输出（8 个 HTTP 用例 + 6 个异常用例）。
      src: tests/ai_check_test.py
      ev: ai_check_test.py asserts KEY never appears in diagnostics (8 HTTP + 6 exception cases)。
  - CA-02 [constraint] ai_worker 诊断只含计数，不含 URL 中的凭据或令牌。
      src: src/rmtc_bot/src/ai_worker.cpp (diagnostics)
      ev: ai_worker diagnostics contain counts only ("不含URL中的凭据或令牌")。
  - SH-01 [process] build.sh 只保存配置摘要，不保存密钥正文；run/practice 用它拒绝“改头文件但没重新编译”的旧程序。
      src: build.sh:6
      ev: # 只保存配置摘要，不保存密钥正文。run/practice用它拒绝“改头文件但没重新编译”的旧程序。
  - SH-02 [process] build.sh 将 match_config.hpp 的 sha256 写入 build/rmtc_bot/match_config.sha256。
      src: build.sh:12
      ev: printf '%s\n' "$rmtc_config_digest" > build/rmtc_bot/match_config.sha256
  - SH-03 [process] ai_check.sha256 覆盖 practice_launcher.cpp + check_ai.py + check_ai.sh + 已构建的 practice_launcher 二进制。
      src: build.sh:14
      ev: sha256sum src/rmtc_bot/src/practice_launcher.cpp scripts/check_ai.py check_ai.sh install/rmtc_bot/lib/rmtc_bot/practice_launcher > build/rmtc_bot/ai_check.sha256
  - SH-04 [constraint] run.sh 在 match_config.sha256 缺失或校验失败时拒绝启动（exit 2）。
      src: run.sh:16
      ev: if [[ ! -f build/rmtc_bot/match_config.sha256 ]] || ! sha256sum --check --status build/rmtc_bot/match_config.sha256; then … exit 2
  - SH-05 [technical] run.sh 使用 set -eo pipefail。
      src: run.sh:2
      ev: set -eo pipefail
  - SH-06 [technical] pipefail 保留机器人失败状态（机器人输出经 tee 写日志）。
      src: run.sh:29
      ev: "$rmtc_bot_executable" 2>&1 | tee "$rmtc_run_log" # pipefail保留机器人失败状态；无需再手工加tee。
  - SH-07 [constraint] run.sh 拒绝命令行参数（exit 2）。
      src: run.sh:7
      ev: run.sh rejects CLI args (exit 2)。
  - SH-08 [constraint] practice.sh 与 check_ai.sh 同样在摘要不匹配时拒绝启动。
      src: practice.sh / check_ai.sh
      ev: run.sh/practice.sh/check_ai.sh refuse to start on digest mismatch。
  - AR-01 [protocol] 竞技场 PARAMETER 白名单：未知参数抛 std::runtime_error("unknown arena parameter: "+entry.key())。
      src: tests/arena_main.cpp:30
      ev: for (const auto &entry:values.items()) if (!recognized.count(entry.key())) throw std::runtime_error("unknown arena parameter: "+entry.key());
  - AR-02 [process] 每轮竞技场评估必有 baseline（styles[i]=="baseline" 或 baseline_parameters 注入）。
      src: tests/arena_main.cpp:45
      ev: if (i==seat || styles[i]=="baseline") players[i]=std::make_unique<Strategy>(stage,i==seat ? parameters : baseline); … configure(baseline,input.at("baseline_parameters"))
  - AR-03 [metric] 候选资格门槛：invalid==0 且第一阶段训练平均分 ≥ baseline_stage1−1.0。
      src: tests/run_arena.py:156
      ev: eligible = [p for p in ranked if summaries[p["name"]]["invalid"] == 0 and summaries[p["name"]]["stage1"]["score_mean"] >= baseline_stage1 - 1.0]
  - AR-04 [metric] selection_guard 写入报告：{stage1_min_score: baseline_stage1−1.0, invalid_max: 0}。
      src: tests/run_arena.py:160
      ev: report["selection_guard"] = {"stage1_min_score": baseline_stage1 - 1.0, "invalid_max": 0, …}
  - AR-05 [process] 每轮按 objective 降序排名取前 keep 名；每轮打印 round/best/summary。
      src: tests/run_arena.py:142
      ev: ranked = sorted(profiles, key=lambda p: summarize(rows[p["name"]])["objective"], reverse=True) … print(json.dumps({"round": round_number, "best": ranked[0]["name"]…}))
  - AR-06 [process] 报告包含每文件 source_sha256 与整体 binary_sha256。
      src: tests/run_arena.py:181
      ev: hashes[path] = hashlib.sha256((ROOT/path).read_bytes()).hexdigest(); report["source_sha256"] = hashes; report["binary_sha256"] = …
  - AR-07 [process] 重新运行已选定参数属于重复验算，不再是首次留出验证。
      src: ARENA.md:41
      ev: re-running selected params "属于重复验算，不再是首次留出验证"。
  - AR-08 [metric] 选定候选必须没有非法动作，且第一阶段训练平均分不能比基线少超过 1 分。
      src: ARENA.md:57
      ev: “选定候选必须没有非法动作，且第一阶段训练平均分不能比基线少超过 1 分”。
  - AR-09 [process] 不能看着留出分数反复修改同一批候选。
      src: ARENA.md:59
      ev: “不能看着留出分数反复修改同一批候选”。
  - AR-10 [constraint] 独立测试裁判不是官方裁判。
      src: ARENA.md:5
      ev: independent test referee not official。
  - AR-11 [constraint] 结果文件只供赛前查看，不被机器人读取。
      src: ARENA.md:15
      ev: results files "只供赛前查看，不被机器人读取"。
  - AR-12 [technical] 延迟公告 0/6/10 ticks；不得在公告发出前送达。
      src: ARENA.md:37
      ev: delayed oracle 0/6/10 ticks, no delivery before announcement。
  - AR-13 [technical] 无免费解释：announce oracle 仅在 simulated_ai_success 时送达。
      src: ARENA.md:51
      ev: announcement oracle delivered after interpretation_delay only when simulated_ai_success (no free explanations)。
  - AR-14 [process] heldout 种子固定 [29003]，仅在选定后评估一次；train_seeds [101,307]；pilot 种子 19001 被拒。
      src: tests/arena_settings.json
      ev: heldout seeds [29003] evaluated once after selection (pilot 19001 rejected), train_seeds [101,307]。
  - AR-15 [constraint] 报告绝不覆盖密封的 arena-2026-10-28.json。
      src: tests/run_arena.py (report writing)
      ev: report never overwrites sealed arena-2026-10-28.json。
  - AR-16 [metric] 排名顺序：score→qualified_M→R→D→invalid 少者优先。
      src: tests/arena.cpp (排名比较)
      ev: rank order score→qualified_M→R→D→fewer invalid。
  - AR-17 [metric] 测试裁判 score()：阶段一 40×R/200；阶段二 30×min(R/120,1)+15×min(D/500,1)+5×M（M 仅 simulated_ai_success 时计入）。
      src: tests/arena.cpp:229
      ev: score() stage1 40*R/200, stage2 30*min(R/120,1)+15*min(car.damage/500,1)+5*M when simulated_ai_success。
  - AR-18 [metric] 测试裁判的 D 不在 500 截断（平局决胜与任务累计值保留全量 D）。
      src: tests/arena.cpp:229
      ev: D "不在500截断"; cumulative D never truncated at 500 for tiebreaks/tasks。
  - AR-19 [protocol] observe(seat) 每席位仅局部感知，无上帝视角。
      src: tests/arena.cpp (observe)
      ev: observe(seat) per-seat local perception only。
  - AR-20 [technical] step() 实现 10 步结算顺序：1-2 环境、3 冻结+非法计数、4 战斗、5 移动、6 chili 批量、7 堡垒占领+治疗、8 死亡扣减、9 资源/任务/重生。
      src: tests/arena.cpp (step)
      ev: step() implements the 10-step settlement order (environment, freeze+invalid counting, combat, move, chili batch, fortress capture+heal, death deduction, resources/missions/respawn)。
  - AR-21 [metric] 冠军位元钉：base_off 三份报告（lowhp/coverage/race）逐位一致 objective 0.7970931712962963 / deaths 83 / blocked 93。
      src: review.md:147
      ev: 自 postcap 晋升后 base_off={} 即“冠军基线”……以 base_off 三份报告（lowhp/coverage/race）逐位一致（objective 0.7970931712962963 / deaths 83 / blocked 93）作为冠军位元钉。
  - AR-22 [process] race 轮固定代码 eb321df03d46d8e05fe7ccc762a76389a4111a88（含 race_reach_holdoff 杠杆与 race 轮封存结果）。
      src: review.md:139
      ev: 本轮固定代码 eb321df03d46d8e05fe7ccc762a76389a4111a88（含 race_reach_holdoff 杠杆与 race 轮封存结果）。
  - AR-23 [process] 杠杆晋升协议：新杠杆默认关闭=冠军逐位一致；晋升须 train 之后仅做一次 heldout 验证。
      src: ARENA.md:43
      ev: promoted only after train + one-time heldout verification; levers default off = champion bit-identical。
  - AR-24 [metric] post_cap_combat_weight=0.02 是唯一晋升杠杆（arena-postcap-heldout-2026-10-29，invalid 0）。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:87
      ev: Only promoted lever: post_cap_combat_weight=0.02 (train 0.7891→0.8056; heldout one-time passed 0.771→0.830, stage2 score 40.8→43.9)。
  - AR-25 [metric] explore_component_value=0 永久关闭（heldout −0.039 vs 密封冠军 0.8299；0.02 崩 R 50.8）。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:86
      ev: explore_component_value=0 permanently closed (heldout −0.039 vs sealed champion 0.8299)。
  - SC-01 [technical] 场景 JSON schema=1。
      src: tests/scenarios/announcement_window_timely.json:2
      ev: "schema": 1
  - SC-02 [protocol] 场景工具退出码：0=pass、1=断言失败（保留 checkpoint）、2=配置/构建/恢复错误。
      src: tests/scenario_test.py:103
      ev: exit codes 0=pass, 1=assertion fail (checkpoint kept), 2=config/build/restore error；test_assertion_failure_keeps_checkpoint assertEqual(completed.returncode, 1)。
  - SC-03 [technical] 重放包携带 _integrity_sha256。
      src: tests/run_scenarios.py
      ev: _integrity_sha256 replay bundles。
  - SC-04 [constraint] build_id 不同→checkpoint 恢复被拒（exit 2）。
      src: tests/scenario_test.py:123
      ev: test_rejects_edited_or_different_build_checkpoint: changed build_id → returncode 2。
  - SC-05 [technical] warm fork 复制 memory+rng；文件恢复重放公开输入并校验已保存动作。
      src: tests/scenario_test.py:62
      ev: test_warm_forks_copy_memory_and_rng；文件恢复重放公开前缀；随机NPC与策略必须重现已保存动作，然后再跑同一后半段。
  - SC-06 [technical] --export-scene 清空策略记忆（cold）；新摆局可以修改血量，但不能把这次新世界叫做原策略记忆的精确恢复。
      src: tests/scenario_test.py:151
      ev: test_export_edit_and_run_new_cold_scene: report["runs"][0]["mode"] == "cold"；// 新摆局可以修改血量，但不能把这次新世界叫做原策略记忆的精确恢复。
  - SC-07 [technical] fork 名只允许 [A-Za-z0-9_-]。
      src: tests/run_scenarios.py (fork name validation)
      ev: fork names [A-Za-z0-9_-]。
  - SC-08 [technical] resume 剥离 forks/warm_until；--until-tick 清除 expect。
      src: tests/run_scenarios.py
      ev: resume strips forks/warm_until; --until-tick clears expect。
  - SC-09 [technical] event_delivery 只允许 oracle|none。
      src: tests/scenarios/announcement_window_timely.json:77
      ev: "event_delivery": "oracle"
  - SC-10 [protocol] 世界不一致或拼错字段→exit 2（重叠位置、tick 小数、错字段名 hhp、hp=−1）。
      src: tests/scenario_test.py:111
      ev: test_rejects_inconsistent_world_and_misspelled_fields: 4 cases each returncode 2。
  - SC-11 [constraint] 编辑后的 checkpoint 摘要不符→exit 2。
      src: tests/scenario_test.py:123
      ev: edited checkpoint (hp=100 篡改) → completed.returncode == 2。
  - SC-12 [process] 断言失败保留 checkpoint 供排查。
      src: tests/scenario_test.py:103
      ev: self.assertTrue((self.work / "case.main.checkpoint.json").exists())
  - SC-13 [protocol] 策略输入不含隐藏世界：扩大地图后感知为空但世界保留资源。
      src: tests/scenario_test.py:194
      ev: test_strategy_inputs_exclude_hidden_world: observation["visible_entities"]==[], run["world"]["resources"] 仍保留 [17,17] 资源。
  - SC-14 [metric] 无公告 fork 不得移除计分资格（qualified 与 qualified_M 保持 1）。
      src: tests/scenario_test.py:138
      ev: test_no_notice_fork_does_not_remove_scoring_qualification: bundle["scene"]["qualified"] True, run["result"][0]["qualified_M"]==1。
  - SC-15 [technical] announcement-window 及时/晚达场景：seed 17、tick195 初始、t204 爆炸 [5,4]-[8,4] 伤害35；及时送达 195（until 204）、晚达 200（until 205, save_at [200]）；expect hp=100 且 position/0 ≤4。
      src: tests/scenarios/announcement_window_timely.json:40
      ev: timely delivery 195 (until 204), late delivery 200 (until 205, save_at [200]); expect hp=100 and position/0 ≤4 (两个场景文件由提交 1ff8f23 添加)。
  - SC-16 [technical] warm fork 只改变未来脚本动作/事件送达；事件经正式契约解码。
      src: tests/scenario_test.py:165
      ev: test_warm_fork_changes_only_future_enemy_action: first["tape"][:2]==second["tape"][:2]，tape[2]["actions"]["B"] 不同；事件解码走正式契约。
  - PR-01 [process] 原版练习包（practice.py/practice_gateway.py 等）绝不修改。
      src: practice/practice.py
      ev: Original practice package (never modified)。
  - PR-02 [technical] practice.py 钉住上游超时 (5,25)（5 秒连接 + 25 秒读取）。
      src: practice/practice.py
      ev: practice.py pins upstream timeout (5,25)。
  - PR-03 [technical] 练习网关提供 mock 与 real 两种模式。
      src: practice/practice.py
      ev: mock vs real mode。
  - PR-04 [technical] 每席位 BoundedSemaphore(1)，并发超限→429。
      src: practice/practice.py
      ev: per-seat BoundedSemaphore(1)→429。
  - PR-05 [technical] practice_gateway.py 钉住 blob hash abd400db06ade29c548e4a7b34dfc0bc1acc013f。
      src: practice/practice_gateway.py
      ev: blob hash pin abd400db06ade29c548e4a7b34dfc0bc1acc013f。
  - PR-06 [constraint] 预提交清单：提交材料不得包含模型密钥；提交前须按清单核对。
      src: practice/测试使用教程.md:257
      ev: pre-submission checklist; materials must not contain model keys; deadline 2026-10-31 20:00。
  - M-01 [process] review.md 协议：双方只 append，按实际写入时间顺序排列；不改写、删除、重排旧记录。
      src: review.md:7
      ev: **给 DeepSeek：请在这个 `review.md` 的末尾直接回复。双方只 append，按实际写入时间顺序排列；不改写、删除、重排旧记录。**
  - M-02 [process] review 回复须写时间（Asia/Shanghai）、身份、所回应条目 ID、接受/异议/待验证、修复提交 SHA、验证命令与结果；修正旧结论追加勘误。
      src: review.md:7
      ev: 回复请写时间（Asia/Shanghai）、身份、所回应的条目 ID，以及“接受 / 异议 / 待验证”、修复提交 SHA、验证命令与结果。修正旧结论也请追加勘误。
  - M-03 [process] 继续本地工作前先读取远端新增记录；有并发冲突就重新拉取、保留双方内容后追加，不强推覆盖。
      src: review.md:7
      ev: 继续本地工作前先读取远端新增记录；有并发冲突就重新拉取、保留双方内容后追加，不强推覆盖。
  - M-04 [metric] 版本联赛起步量：12 图×4 席位×3 对手混合=144 场/版本，离线无真实 API；真实 LLM 只对选出的新样例采集一次，固定模型/请求与预算，之后明确以离线回放复用，不虚增真实调用成功次数。
      src: review.md:133
      ev: 第一批可以只选 12 张图×4 席位×3 对手组合=144 场/版本，离线无真实 API；这只是起步，不是“144 场即全面”。……不虚增真实调用成功次数。
  - M-05 [process] race 轮固定代码 eb321df03d46d8e05fe7ccc762a76389a4111a88；race 轮封存报告 tests/results/levers-race-2026-10-29.json。
      src: review.md:139
      ev: 本轮固定代码 eb321df03d46d8e05fe7ccc762a76389a4111a88（含 race_reach_holdoff 杠杆与 race 轮封存结果）。
  - M-06 [metric] base_off={} 即“冠军基线”而非关闭态；待实现 versions 清单（旧冠军/新冠军/候选各固定 commit SHA+参数+二进制哈希+独立构建目录）与 tests/version_league.py 统一调度（与 U6 同做）。
      src: review.md:147
      ev: 自 postcap 晋升后 base_off={} 即“冠军基线”而非关闭态……待实现（与 U6 同做）：versions 清单……tests/version_league.py 作统一调度入口；144 场/版本起步。
  - M-07 [process] 批量驱动器（batch_practice.py）、归档与筛选/验证脚本现位于 /mnt/d 临时路径；下一轮迁入代码仓 tools/ 并随批提交（C9）。
      src: review.md:159
      ev: 批量驱动器（batch_practice.py）、归档与筛选/验证脚本现位于 /mnt/d 临时路径——同意不可复现的批评，下一轮把它们迁入代码仓 tools/ 并随批提交。
  - M-08 [process] 本轮 ChatGPT 未改参赛代码与参数、未新增付费调用，已核对。
      src: review.md:159
      ev: 本轮 ChatGPT 未改参赛代码与参数、未新增付费调用，已核对。
  - M-09 [process] race 轮无候选超冠军→按 docs/36 §3 预注册判据 train 关闭，race_reach_holdoff 保持 0.0，不作 heldout。
      src: review.md:164
      ev: 无候选超冠军 → 按 docs/36 §3 预注册判据 train 关闭，race_reach_holdoff 保持 0.0，不作 heldout。封存：tests/results/levers-race-2026-10-29.json（eb321df）。
  - M-10 [process] 采纳提交已推送 origin/strategy/iterate-arena-2026-10-28 特性分支 @ 9c84659。
      src: review.md:194
      ev: 采纳提交（已推送 origin/strategy/iterate-arena-2026-10-28 @ 9c84659）：
  - M-11 [process] 仓库中不存在显式“绝不推送 main/主干”条款；最近的控制性约束为 review.md:7 追加式、不强推覆盖协议，以及 review.md:194 实际推送的是 origin/strategy/iterate-arena-2026-10-28 特性分支（非 main）。
      src: review.md:7
      ev: 全仓 grep（push|main 分支|主干|强推|推送|origin）未发现“never push main”字样；review.md:7“不强推覆盖”，review.md:194 推送 origin/strategy/iterate-arena-2026-10-28。
  - M-12 [constraint] 许可证为 MIT，Copyright (c) 2026 Jun Zhu。
      src: LICENSE
      ev: MIT license Copyright (c) 2026 Jun Zhu。
  - M-13 [process] tests/results 本地评测输出不作为源码提交；selected-parameters.json 除外（历史报告归分析仓库）。
      src: .gitignore:76
      ev: /tests/results/* except selected-parameters.json，注释“本地评测输出不作为源码提交；历史报告归分析仓库，选定参数仍供评测器读取”。
  - M-14 [technical] rmtc_strategy 为 ROS 无关静态库供离线复用；bot+strategy 启用 -Wall -Wextra -Wpedantic；CTest 注册 strategy_regression 与 arena_rules_regression。
      src: src/rmtc_bot/CMakeLists.txt
      ev: rmtc_strategy static lib ROS-free for offline reuse; -Wall -Wextra -Wpedantic on bot+strategy; CTest registers strategy_regression + arena_rules_regression。
  - M-15 [technical] 风险/脱困/规划基准编译旗标固定 -std=c++17 -O2 -Wall -Wextra -Wpedantic -Werror，报告含 source_sha256。
      src: tests/run_risk.py
      ev: build flags -std=c++17 -O2 -Wall -Wextra -Wpedantic -Werror; reports include source_sha256。
  - M-16 [constraint] 基准/测试裁判范围声明：不是官方裁判、对手、事件、任务或 AI。
      src: tests/planning_benchmark.cpp
      ev: scopes explicitly "not official judge/opponents/events/missions or AI"。
  - M-17 [process] 审查记录（review.md）不代替本机真实 DDS 对局。
      src: review.md:5
      ev: 这里记录具体证据、审查结论和建议，不代替你在本机进行的真实 DDS 对局。
  - M-18 [metric] explore_toward_resource_value=0.5 在 gate-frontier 组合调参中验证为正。
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:55
      ev: // 只影响排序，不把未知格当空地；gate-frontier调参在组合中验证为正。
  - W-01 [process] 工作树临时状态（非缺陷，仅记录）：match_config.hpp 的 practice_llm_key/practice_llm_proxy 为临时填值（用后还原为空并重建，绝不提交，已提交值为 ""）；tests/eval_levers.py 新增 fortress 组（pf03/pf06/pf12/pf24=pr
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:35
      ev: git status: M match_config.hpp（练习密钥/代理临时填值，密钥正文不显示）+ M tests/eval_levers.py（fortress 杠杆组）；按任务指示不列为缺陷。

## result 4: scope=code-vrb
- checks: [{"req_id": "GL-01", "status": "met", "evidence": "cst@05a0afe practice/rules.txt:9 '每队 1–2 人，设队长 1 人'; :12 '第一阶段为独立采集赛，满分 40 分'; :125 表 '第一阶段…100 ms/Tick | 100 Tick | 10 秒'; match_config.hpp:8 stage1_ticks=100", "gap": "", "action": "None — stage-1 config (100 Tick/100 ms/10 s/40 分) present in frozen practice docs and match_config.hpp."}, {"req_id": "GL-02", "status": "met", "evidence": "cst@05a0afe practice/rules.txt:12 '第二阶段为多队对抗赛…单场最高 60 分'; :135 '500 ms/Tick | 500 Tick | 4 分 10 秒'; match_config.hpp:9 stage2_ticks=500; arena 4 席位 A–D", "gap": "", "action": "None."}, {"req_id": "GL-03", "status": "partial", "evidence": "cst@05a0afe review.md:65 'stage2 score 41.25→37.57'; review.md:133/147 联赛计划 144 场/版本但标注待实现", "gap": "'stage2 目标 50 分' 与 '联赛数据作为 50 分验收第一手证据' 的目标表述不在 cst（仅分析仓 docs/38）；grep '50 分|目标 50' 无命中", "action": "如需代码仓承载目标口径，可把目标/锚点一句并入 review.md 或 ARENA.md。"}, {"req_id": "GL-04", "status": "partial", "evidence": "cst@05a0afe review.md:145-147 C7 接受 'profile 对打 ≠ 冻结版本…联赛待实现'; review.md:65 41.25 训练锚点在场", "gap": "证据缺口补法（原版对局+自战联赛）全文在分析仓 docs/37；cst 仅以 C7 接受条目体现", "action": "联赛实现后回填（见 PR-18/PR-20 动作）。"}, {"req_id": "GL-05", "status": "partial", "evidence": "cst@05a0afe review.md:113 '不要用当前类加旧参数冒充旧版本'; review.md:147 '同意 profile 对打 ≠ 冻结版本'", "gap": "U6 判定原文（多 profile 自战档案不能代表旧版本/原版 robot_node）未逐字迁入，仅改编进 C7 答复", "action": "保持现状即可（内容已适配入 review 协议流）。"}, {"req_id": "GL-06", "status": "unmet", "evidence": "cst@05a0afe 无 LESSONS.md（9bc72a7 已删）；grep '不可达|天花板' 无该结论；结论原由 521ea50 写入 LESSONS.md+15行，后随迁移移除", "gap": "两目标结构不可达结论只存分析仓 docs/implementation/LESSONS.md:76", "action": "按 PR-01/PR-02 属分析类内容，无需回迁代码仓。"}, {"req_id": "MT-01", "status": "met", "evidence": "cst@05a0afe tests/arena.cpp:228 'if (scenario_.stage==1) return 40*car.resource/200;'", "gap": "公式实现在测试裁判而非 bot 源码（bot 只用 scoring.hpp score_delta 估算分差）", "action": "None."}, {"req_id": "MT-02", "status": "superseded", "evidence": "v1.0 公式仅存于冻结原件 practice/rules.txt:380-381 '资源得分 = 30 × min(R2/120,1)；对抗得分 = 15 × min(D/30
- requirements: 78
  - B1-01 [process] run.sh 必须自动创建 $PWD/log 并把本次A端完整输出保存到 log/bot_<YYYYmmdd_HHMMSS>_<pid>.log，与裁判 run_dir 分开保存。
      src: run.sh:26-27
      ev: 「本次A端的完整输出，与裁判run_dir分开保存」— 7e80792；已逐字采纳（iterate-arena 4dc7ffc）。
  - B1-02 [process] run.sh 必须经 tee 同时输出并保留机器人失败状态：pipefail 必须保持机器人真实退出码。
      src: run.sh:29
      ev: 「pipefail保留机器人失败状态；无需再手工加tee」
  - B1-03 [technical] startup_test 必须断言经 run.sh 启动后 log/ 下生成 bot_*.log 且内容包含夹具二进制输出。
      src: tests/startup_test.py:54
      ev: assert any("fixture-binary" in p.read_text() for p in (work/"log").glob("bot_*.log"))
  - B1-04 [technical] tee 不得把真实机器人失败伪装成成功：追加 exit 7 的二进制必须得到 returncode 7。
      src: tests/startup_test.py:57-58
      ev: 「tee不能把真实机器人失败伪装成成功」
  - B1-05 [technical] 改配置后仍旧二进制必须被拒绝（returncode 2），不得偷偷运行旧构建。
      src: tests/startup_test.py:61
      ev: 「改配置后仍旧二进制：必须拒绝」
  - B2-01 [technical] AiWorker::Result/Job 必须携带 request_tick＝发起请求时的逻辑Tick；-1 表示没有来源，不能用返回时刻倒推请求时刻。
      src: src/rmtc_bot/include/rmtc_bot/ai_worker.hpp:33
      ev: 「发起请求时的逻辑Tick；-1表示没有来源，不能用返回时刻倒推」— 3b610cb；已采纳（f13948c，两分支tip该文件一致）。
  - B2-02 [technical] Job 必须保存任务建立时的感知Tick，与 HTTP 墙钟耗时分开。
      src: src/rmtc_bot/include/rmtc_bot/ai_worker.hpp:57
      ev: 「此任务建立时的感知Tick，与HTTP墙钟耗时分开」
  - B2-03 [technical] Session::event_diagnostics() 必须把 HTTP 完成、解释校验、迟到与当前有效事件分开统计。
      src: src/rmtc_bot/include/rmtc_bot/session.hpp:19
      ev: 「HTTP完成、解释校验、迟到与当前有效事件分开统计」
  - B2-04 [constraint] EventFlow 的错误信息必须是固定分类，不得输出模型正文、思考或凭据。
      src: src/rmtc_bot/include/rmtc_bot/session.hpp:24
      ev: 「固定分类，不输出模型正文、思考或凭据」
  - B2-05 [technical] event_flow_ 换场必须清空，同Tick 不得重复推进计数。
      src: src/rmtc_bot/include/rmtc_bot/session.hpp:26
      ev: 「换场清空，同Tick不推进」
  - B2-06 [constraint] 最近事件摘要不得包含原文 source 字段。
      src: src/rmtc_bot/src/session.cpp:45
      ev: summary.erase("source")；「不含原文source」
  - B2-07 [technical] 拒绝的事件必须按固定分类记录：invalid_json（JSON解析错误101）、missing_or_wrong_event_field、event_contract_rejected；HTTP成功不等于事件合法。
      src: src/rmtc_bot/src/session.cpp:52-57
      ev: error.id==101 ? "invalid_json" : "missing_or_wrong_event_field" / "event_contract_rejected"；测试断言「HTTP success concealed invalid event fields」
  - B2-08 [technical] 部分理解必须与完整校验分开计数（partial→error=events_incomplete），仅完整理解计 validated。
      src: src/rmtc_bot/src/session.cpp:49-50
      ev: if(partial) {++event_flow_.partial;...} else ++event_flow_.validated
  - B2-09 [process] Bot 日志只在换场或收到新回包时输出 event_update；逐Tick行保留 events_known/events_active/empowered。
      src: src/rmtc_bot/src/bot.cpp:82-84,99-100
      ev: 「只在收到新回包时写详细事件，避免每Tick重复整份解释」
  - B2-10 [technical] Strategy::event_diagnostics(tick) 必须只读统计已校验事件按当前Tick的 pending/active/expired 及本车已重建效果（empowered/reversed/reverse_unknown）。
      src: src/rmtc_bot/src/strategy.cpp:171
      ev: 「是已校验解释的状态，不是假装裁判公开了事件真值」（strategy.hpp:29「供人工排查」）
  - B2-11 [technical] 堡垒预告抢点仅限：阶段2、已校验堡垒事件、start>tick、start<tick_limit、候选格在事件区域内、本车未获无双。
      src: src/rmtc_bot/src/strategy.cpp:810
      ev: if (stage_ == 2 && e.kind == Kind::fortress && !empowered_ && e.start > tick && e.start < tick_limit && e.contains(cell))
  - B2-12 [technical] 到达Tick计算必须为 tick + max(0, BFS距离-1)：本Tick MOVE 在结算后到达，站在原地则是当前Tick；路程必须用已知格BFS。
      src: src/rmtc_bot/src/strategy.cpp:811-812
      ev: 「路程用已知格BFS」「本TickMOVE在结算后到达，站在原地则是当前Tick」
  - B2-13 [technical] first_capture 必须取 max(事件start, 到达Tick)——不能提前于事件激活累计驻留进度；needed＝capture_ticks，未激活时当前不能已有该堡垒的占领进度。
      src: src/rmtc_bot/src/strategy.cpp:813-814
      ev: 「不能提前累计进度」「还未激活，当前不能已有这次堡垒的占领进度」
  - B2-14 [technical] finish 必须为 first_capture + max(0, needed-1)——增益在该Tick结算后授予，不能补打本Tick。
      src: src/rmtc_bot/src/strategy.cpp:815
      ev: 「增益在这一Tick结算后授予，不能补打本Tick」
  - B2-15 [constraint] 仅当 finish < min(事件end, tick_limit) 且 start-tick ≤ 路程+占领Tick 时才提前抢点；不得为遥远预告放弃整局采集。
      src: src/rmtc_bot/src/strategy.cpp:816-817
      ev: 「只在出发后至多多等一段占领时间时提前抢点；不为遥远预告放弃整局采集」
  - B2-16 [technical] 早到等待成本 wait 必须为 max(0, start-arrival)，不得修改事件绝对期限。
      src: src/rmtc_bot/src/strategy.cpp:818
      ev: 「早到的等待成本，不修改事件绝对期限」
  - B2-17 [technical] 已在事件格内用 hold_fortress（fortress_hold_value/(wait+1)），否则用 prepare_fortress（fortress_capture_value/(距离+needed+wait)）赶向已公告的未来堡垒。
      src: src/rmtc_bot/src/strategy.cpp:819-820
      ev: consider(node.first,parameters_.fortress_capture_value/(node.distance+needed+wait),"prepare_fortress",cell)
  - B2-18 [technical] 事件生效后的既有策略保持：当前驻留重视进度（hold_fortress），外部目标按路程/占领时间比较（capture_fortress）。
      src: src/rmtc_bot/src/strategy.cpp:828-830
      ev: 「生效后的既有策略保持：当前驻留重视进度，外部目标按路程/占领时间比较」
  - B2-19 [technical] announced_fortress 回归必须断言：未来堡垒影响激活前路线（reason=prepare_fortress）、早到不得离开（hold_fortress）、结算前不得授予无双（tick>=9才 empowered）、比赛结束后的堡垒不得消耗剩余动作、未来收益不得越过当前致命攻击守卫。
      src: tests/full_strategy_test.cpp:514-533
      ev: 「fortress buff was awarded before actual capture settlement」「fortress after the game consumed remaining actions」「future reward bypassed current lethal attack guard」
  - B2-20 [technical] gateway 事件诊断回归必须断言：validated/imported/known 各为1且 rejected=0、request_tick=0、last_events 无 source、同Tick不重复计一次回包、过期响应与有效收益区分（arrived_expired=1且active=0）、新场不得继承旧场采纳
      src: tests/full_strategy_test.cpp:606-632
      ev: 「valid HTTP event had no adoption diagnostics」「same tick counted an AI reply twice」「expired response was not distinguished from an active benefit」「new session inherited event adoption diagnostics」
  - B2-21 [technical] announcement_benchmark 配对夹具：生产策略只收到本队局部感知与已公告的解释，没有未来真值输入；解释由手工 oracle 延迟交付（0/8/20 三种延迟）；夹具停用其他车不得改变生产复活规则。
      src: tests/announcement_benchmark.cpp:7-33
      ev: 「生产策略只收到本队局部感知与已经公告的解释，没有未来真值输入」「公告后延迟交付，不提前泄漏未公告安排」「生产复活规则不变」
  - B3-01 [process] 本地评测输出不得作为源码提交：/tests/results/* 必须 gitignore，仅保留 selected-parameters.json；历史报告归分析仓库。
      src: .gitignore:76-77
      ev: 「本地评测输出不作为源码提交；历史报告归分析仓库，选定参数仍供评测器读取」— b27397f；已采纳（9bc72a7，两分支tip .gitignore 仅差 iterate-arena 的 __pycache__ 行）。
  - B3-02 [process] 代码仓库只保留评测器接口、运行方法和仍使用的选定参数；新生成报告属于本地输出，不自动提交到代码仓库。
      src: ARENA.md:65
      ev: 「历史记录已迁至分析仓库」「新生成报告属于本地输出，不自动提交到代码仓库」
  - B3-03 [process] 移出的研究文档（REAL_TEST/LESSONS/NAVIGATION/PLANNING/MATERIALS_CHECK）必须以分析仓库链接引用，不得在本仓保留副本。
      src: CODE_GUIDE.md:21-37
      ev: 「表中跨仓链接为研究记录，已从代码仓库移出」
  - B3-04 [protocol] 第一阶段采满200资源应为40分；网页在38/40与30之间跳动时须按同一session、同一Tick核对stage；30分不能理解为采集被扣分。
      src: README.md:157
      ev: 「已发现原练习日志混有stage=1与stage=2计分消息。原版practice保持不动」
  - B3-05 [process] 模型回包时新增 event_update 日志，分别显示请求/采纳Tick、校验通过/拒绝、已过期事件和实际合并参数；每Tick显示 events_known/events_active/empowered；run.sh 自动保存到 log/bot_时间_进程号.log。
      src: README.md:159
      ev: 「与裁判日志目录分开」
  - B3-06 [technical] 公告前置与诊断入口约定：event_diagnostics 只读；request_tick 不能用返回时刻重置事件；event_update 只在换场/新回包输出；模型原文、思考、令牌均不打印；未激活不提前计算驻留，prepare_fortress 仅表示赶往已公告的未来堡垒。
      src: CODE_GUIDE.md:254-260
      ev: 「模型原文、思考、令牌均不打印」「prepare_fortress仅表示赶往已公告的未来堡垒」
  - B3-07 [constraint] 已校验的未来堡垒可在激活前比较路程/等待/驻留成本选择 prepare_fortress；早到驻留不得提前授予无双；生效后原有路径不变；Session 的请求/消费Tick、校验/拒绝及迟到计数是诊断，不作为额外比赛信息输入。
      src: STATE_MACHINE.md:277
      ev: 「这些是诊断，不作为额外比赛信息输入」
  - B4-01 [constraint] Game::checkpoint()/restore() 仅限测试端：保存『下一Tick尚未执行』的完整世界，不包含策略记忆；生产机器人永远没有这个接口。
      src: tests/arena.hpp:52-53
      ev: 「测试端：保存...不包含策略记忆」「生产策略永远没有这个接口」（arena_checkpoint.cpp:1「只供场景工具链接；正式机器人不包含本文件」）— 3234a00；逐字cherry-pick为1713988。
  - B4-02 [protocol] 恢复快照必须要求 schema=1 且 phase=before_tick（下一Tick尚未执行）。
      src: tests/arena_checkpoint.cpp:57-58
      ev: "checkpoint requires schema=1 and phase=before_tick"
  - B4-03 [technical] 整数与浮点字段必须分开做有限数/范围校验：200.5 Tick 或负血量不得偷偷变成合法状态。
      src: tests/arena_checkpoint.cpp:9-16
      ev: 「有限数/整数分开检查，避免把 200.5 Tick 或负血量偷偷变成合法状态」
  - B4-04 [constraint] 效果/名字集合必须去重且关联事件必须存在且类型匹配，不能从不存在的增益凭空获得能力。
      src: tests/arena_checkpoint.cpp:24,74
      ev: 「集合必须去重；关联事件还要存在且类型匹配，不能从不存在的增益凭空获得能力」
  - B4-05 [technical] restore 必须校验：资源不叠墙/不重复、alive⇔hp>0、存活车辆不叠墙/不与他车同格、保护布尔与剩余时间一致、存活则respawn_in=0、last_action 必须属于前一Tick、已完成任务必须已知、car字段必须逐项已知。
      src: tests/arena_checkpoint.cpp:64-97
      ev: "checkpoint alive/hp disagree"「checkpoint last_action must belong to preceding tick」
  - B4-06 [constraint] 所有恢复校验必须先作用于副本：失败时不得留下半恢复的世界。
      src: tests/arena_checkpoint.cpp:60
      ev: 「所有校验都先作用于副本；失败时不留下半恢复的世界」
  - B4-07 [technical] 恢复后伤害/无双/易伤必须由已保存的授予记录和当前时间通过 refresh_effects() 重新计算。
      src: tests/arena_checkpoint.cpp:106
      ev: 「伤害/无双/易伤由已保存的授予记录和当前时间重新计算」
  - B5-01 [constraint] scenarios.sh 必须纯离线运行：不读比赛网关，不启动ROS。
      src: scenarios.sh:3
      ev: 「场景文件和结果都在测试目录；不读比赛网关，不启动ROS」— 3c345b8；逐字cherry-pick为bffd50e。
  - B5-02 [process] 构建必须按源码/头文件/编译器/选项做指纹缓存；配置改动后使用另一个独立二进制，不复用旧构建。
      src: tests/run_scenarios.py:24-45
      ev: 「按源码/头文件/编译器/选项缓存；配置改动后使用另一个独立二进制，不复用旧构建」
  - B5-03 [constraint] 回放包必须带完整性校验：误改世界或历史输入必须报错；不同构建也会被C++入口拒绝，不能冒充原程序恢复；校验值只防误改，不当安全签名。
      src: tests/run_scenarios.py:19,53-57
      ev: 「只防误改，不把校验值当作安全签名」「回放包已被改动；请用场景JSON另开冷启动测试」
  - B5-04 [protocol] 场景工具退出码协议：0=全部通过；1=断言失败但仍保存现场；2=输入、构建或恢复错误。
      src: SCENARIOS.md:23
      ev: 「退出码：0为全部通过；1为断言失败，仍保存现场；2为输入、构建或恢复错误」— 65c8714；逐字cherry-pick为9c84659。
  - B5-05 [protocol] 所有时间为绝对Tick，快照固定在 before_tick（该Tick动作尚未执行）：initial.tick=200/until_tick=205 执行200-204并保存205之前状态；事件期限用 [start,end)。
      src: SCENARIOS.md:27
      ev: 「快照固定在before_tick：该Tick的动作尚未执行」「事件期限用[start,end)」
  - B5-06 [technical] 工具不得实际等待墙钟秒数，也不得在同一Tick的攻击与移动之间暂停；该先后关系用单Tick反例检查。
      src: SCENARIOS.md:29
      ev: 「工具不实际等待这些秒数，也不在同一Tick的攻击与移动之间暂停」
  - B5-07 [constraint] 世界真值只存在于裁判/断言；Strategy 和 NPC 始终只收到自己的 observe() 与按时交付的解释。
      src: tests/scenario_runner.cpp:2
      ev: 「世界真值只在裁判/断言里；Strategy 和 NPC 始终只收到自己的 observe() 与按时交付的解释」
  - B5-08 [technical] 场景必须 schema=1；必须有四个出生点且不与墙/彼此重叠；资源不得叠墙或重复；vision_radius 仅允许0-4（当前实体图固定9×9，不伪装支持更大实体协议）。
      src: tests/scenario_runner.cpp:43-58
      ev: "scene schema must be 1""four spawns required"「不伪装支持更大的实体协议」
  - B5-09 [technical] 事件必须复用正式事件契约检查器解码；场景JSON是明示的测试oracle，不进行真实HTTP请求。
      src: tests/scenario_runner.cpp:71
      ev: 「复用正式事件契约检查字段；这里的JSON是明示的测试oracle，不进行真实HTTP请求」
  - B5-10 [technical] null 动作＝明确不提交（常用于第一阶段），不得当作第二阶段默认动作。
      src: tests/scenario_runner.cpp:81
      ev: 「明确不提交，常用于第一阶段；不作为第二阶段的默认动作」
  - B5-11 [technical] 每辆启用车辆必须配一个agent；省略的席位是明示的测试停用车，不宣称是正式比赛的复活状态；完整比赛测试应显式启用四台车。
      src: tests/scenario_runner.cpp:134
      ev: 「省略的席位是明示的测试停用车，不参与短片段；不是正式比赛复活规则」（SCENARIOS.md:62）
  - B5-12 [technical] 人工摆局必须明确 position 与 hp；未知车辆字段必须报错（防拼错造成假通过）。
      src: tests/scenario_runner.cpp:140
      ev: 「人工摆局必须明确位置与血量，其余字段在模板/文档列明初值」"unknown car field"
  - B5-13 [protocol] 恢复必须校验 schema/build 匹配（用原构建或新建冷场景）；tape 不得有缺口；公开前缀重放必须逐Tick复现已保存动作，否则报 warm replay diverged。
      src: tests/scenario_runner.cpp:176,183-192
      ev: "checkpoint schema/build mismatch; use original build or create a new cold fixture""warm replay diverged"
  - B5-14 [technical] warm_until 不得超过 until_tick。
      src: tests/scenario_runner.cpp:255
      ev: "warm_until must not exceed until_tick"
  - B5-15 [constraint] fork 只能修改未来脚本动作或后续解释交付方式；不得改写旧动作，也不得抹掉已理解的事件；绝不替换已经暖起来的策略/NPC对象。
      src: tests/scenario_runner.cpp:208-213
      ev: "fork cannot rewrite earlier actions"「只校验声明；绝不替换已经暖起来的策略/NPC对象」
  - B5-16 [protocol] fork 名称仅允许字母、数字、下划线、减号，且必须非空不重复；forks 不得为空。
      src: tests/run_scenarios.py:124-125
      ev: re.fullmatch(r"[A-Za-z0-9_-]+", name)；「fork名称仅允许字母、数字、下划线、减号」
  - B5-17 [protocol] 条件检查协议：break_when 任一成立即在下一动作前停止；always 检查起点与每个结算边界；expect 只检查终点；路径不存在时除 exists 外直接报错，防止错拼假通过。
      src: SCENARIOS.md:88-108
      ev: 「路径不存在时，除exists外直接报错，防止错拼造成假通过」
  - B5-18 [process] 保存协议：每次保存前缀.json 与 前缀.分支名.checkpoint.json；save_at 额外保存 tick-N 快照；报告含逐Tick动作/原因/结算后世界；断言失败也保留最后现场。
      src: SCENARIOS.md:112
      ev: 「报告含逐Tick动作、原因与结算后世界，断言失败也保留最后现场」
  - B5-19 [constraint] --resume 保留世界并用保存的本队公开输入、已交付解释和动作重建策略/NPC，验证历史动作一致；拒绝误改回放包、不同构建或历史动作分歧；不宣称跨机器逐位序列化全部私有状态。
      src: SCENARIOS.md:125
      ev: 「文件重放不宣称跨机器逐位序列化全部私有状态」
  - B5-20 [constraint] --export-scene 明确清掉策略记忆；修改血量/位置后的测试不能称为原历史的精确恢复。
      src: SCENARIOS.md:127
      ev: 「不能把修改血量/位置后的测试叫原历史的精确恢复」
  - B5-21 [constraint] 世界与策略记忆必须区分：把世界中A设成已获无双不代表新建策略知道驻留历史；要测『自己知道获增益』须先跑足够重建效果的公开前缀；裁判真值不会直接注入策略。
      src: SCENARIOS.md:86
      ev: 「裁判真值不会直接注入策略」
  - B5-22 [protocol] 每个agent必须写 event_delivery 为 oracle 或 none；交付方式不得改变 qualified（模拟计分资格与是否提供解释独立，不冒充真实调用成功）。
      src: SCENARIOS.md:66,45
      ev: 「每个agent必须写event_delivery为oracle或none」「都不改变qualified」
  - B6-01 [technical] 四个入库示例场景必须全部通过（checked-in regression）。
      src: tests/scenario_test.py:57-60
      ev: test_checked_in_examples: 遍历 tests/scenarios/*.json 并断言 passed
  - B6-02 [technical] warm forks 必须复制策略记忆与随机流：两分支世界/轨迹一致；文件恢复必须重现已保存动作后再跑后半段。
      src: tests/scenario_test.py:62-73
      ev: 「随机NPC与策略必须重现已保存动作，然后再跑同一后半段」
  - B6-03 [technical] 断点必须在下一动作之前停止（end_tick/steps/stop == (201,1,"breakpoint")，A仍存活）。
      src: tests/scenario_test.py:75-80
      ev: self.assertEqual((run["end_tick"], run["steps"], run["stop"]), (201, 1, "breakpoint"))
  - B6-04 [technical] 世界往返恢复必须保留效果/资源/复活状态（empowered、capture、heal、respawn保护）。
      src: tests/scenario_test.py:82-101
      ev: test_world_roundtrip_keeps_effects_resources_and_respawn
  - B6-05 [technical] 断言失败必须保留 checkpoint 文件。
      src: tests/scenario_test.py:103-109
      ev: self.assertTrue((self.work / "case.main.checkpoint.json").exists())
  - B6-06 [technical] 矛盾世界与拼错字段必须拒绝：重叠、200.5 Tick、未知字段、负血量均须 exit 2。
      src: tests/scenario_test.py:111-121
      ev: test_rejects_inconsistent_world_and_misspelled_fields: assertEqual(completed.returncode, 2)
  - B6-07 [technical] 被改动的回放包或不同构建的恢复必须被拒绝（exit 2）。
      src: tests/scenario_test.py:123-136
      ev: test_rejects_edited_or_different_build_checkpoint
  - B6-08 [technical] 无解释分支不得移除计分资格（qualified 与 qualified_M 保持）。
      src: tests/scenario_test.py:138-149
      ev: test_no_notice_fork_does_not_remove_scoring_qualification: bundle["scene"]["qualified"] 为真且 qualified_M==1
  - B6-09 [technical] 导出-编辑-重跑必须产生冷场景（mode=cold）；允许改血量，但不能称为原策略记忆的精确恢复。
      src: tests/scenario_test.py:151-163
      ev: 「新摆局可以修改血量，但不能把这次新世界叫做原策略记忆的精确恢复」
  - B6-10 [technical] warm fork 只能改变未来对手动作（前缀tape一致，改动Tick的动作不同）。
      src: tests/scenario_test.py:165-178
      ev: test_warm_fork_changes_only_future_enemy_action: first["tape"][:2]==second["tape"][:2] 且 tape[2] 的B动作不同
  - B6-11 [technical] 待交付解释必须能跨快照存活（delivery_tick 晚一Tick时正确解释也可能赶不上爆炸前撤离）。
      src: tests/scenario_test.py:180-192
      ev: test_pending_explanation_survives_checkpoint: tape[0] event_ids==[] 且 tape[1]==["blast"]
  - B6-12 [constraint] 策略输入必须排除隐藏世界：视野外资源不出现在 visible_entities，map 只含宽高，世界真值仅在 world 中。
      src: tests/scenario_test.py:194-213
      ev: observation["visible_entities"]==[] 且 observation["map"]=={"width":18,"height":18}，而 run["world"]["resources"] 保留真值
  - B7-01 [metric] 分支封存参数（预merge-base，两分支共享）：资源任务机会权重4.0、到点任务4.0、目标保持余量0.1（10%排序余量，不是官方加分）、tactical_death_cost 0.25、frontier_value 0.02（信息权重，不是资源概率）、治疗阈值40、资源计划深度4/束宽5/候选8/软预算10ms
      src: src/rmtc_bot/include/rmtc_bot/match_config.hpp:40-51,64
      ev: 「同一有效目标给10%排序余量，抑制小波动；不是官方加分」「每份潜在新视野的信息权重；不是资源分或必然有资源的概率」— iterate-arena 已在后续竞技场轮次重调为 5.0/8.0/0.0/0.0，属主动重调而非未采纳。
  - B8-01 [technical] NOT ADOPTED AS-IS：分支上 prepare_fortress 默认开启（无条件执行，按 fortress_capture_value=12.0 估值）；iterate-arena 采纳后把该行为置于 prepare_fortress_value 杠杆且默认0.0关闭（『默认关，待竞技场评估』），因此分支
      src: src/rmtc_bot/src/strategy.cpp:816-820
      ev: 分支:817 无条件 `if(finish<min(e.end,tick_limit) && e.start-tick<=node.distance+e.capture_ticks)`；iterate-arena strategy.cpp:1009 增加 `&& parameters_.prepare_fortress_value>0`（match_config.hpp 默认0.0）；其 anno
  - B8-02 [technical] SUPERSEDED：分支的 check_ai.py 探针仅用 user 消息请求裸JSON；iterate-arena 未采用该版本，改以系统消息强化（『Output exactly one JSON object: no prose, no markdown fences, no commentary』，39f21
      src: scripts/check_ai.py:15
      ev: 分支: "messages": [{"role": "user", "content": 'Return only this JSON object: {"ok":true}'}]；iterate-arena 增加 system 消息要求裸JSON输出。
  - B8-03 [process] 已完整采纳（逐字或严格超集）：7e80792→4dc7ffc（run.sh/startup_test.py 一致）；b27397f→9bc72a7（两tip文档 ARENA/CODE_GUIDE/DEV/README/STATE_MACHINE/SCENARIOS 完全一致）；3234a00→1713988、3c345
      src: branch:strategy/visible-resource-bfs@65c87145 vs strategy/iterate-arena-2026-10-28@1ff8f23
      ev: git diff <original> <adopted> -- <touched-files> 为空；tip 级净差异仅剩 fortress 杠杆门（B8-01）、探针强化（B8-02）与 iterate-arena 追加内容（如 1ff8f23 公告窗口及时/迟到场景对，分支没有）。

## critic
### coverage_gaps
[
 {
  "domain": "champion-pins / arena determinism metrics",
  "known_constraint": "champion pins: base_off 0.7970931712962963/deaths 83/blocked 93/stage2 41.25/D2 1026.67; heldout 0.8298625; determinism pin 0.7710073; bit-pin eb321df",
  "gap_description": "Every pin component is covered by an extracted requirement except D2 1026.67: base_off objective/deaths/blocked -> AR-21/M-06; stage2 41.25 -> GL-03/GL-04; heldout 0.8298625 -> MT-08; determinism 0.7710073 -> MT-09; bit-pin eb321df -> AR-22/M-05. No requirement in any of the five scopes records D2 1026.67. Grep of the live tree shows the value exists in docs/36 and docs/39, so this is an extraction omission, not a tree absence.",
  "recommendation": "Add D2 1026.67 to the champion-pin record (code-repo review.md:147 pin paragraph or the planned tools/versions.json manifest) and re-verify against the sealed reports; confirm the complete pin set going forward."
 },
 {
  "domain": "branch coverage (both repos)",
  "known_constraint": "every requirement in every branch of BOTH repos must be satisfied (doc repo D:/code/The-Logical-Structure-of-RMT-C incl. non-log branches; code repo ~/cst incl. non-main branches)",
  "gap_description": "The five scopes cover doc-repo ANALYSIS (docs 01-38 + review + governance), origin/COMPARISON, origin/main, and code-repo strategy/iterate-arena-2026-10-28 + strategy/visible-resource-bfs. Not extracted: (a) doc-repo log branch (only spot-checked as archive evidence via PR-26); (b) docs/39 at working-tree HEAD d689911 (fortress/survival lever families 16/17 closed, scenario probes, three rule findings — a whole requirement domain); (c) code-repo main branch (compliance-checked in CN-30/CN-35, never extracted as a requirement set); (d) remotes/moved/* refs. No full branch inventory appears in the payload, so KNOWN 'every branch' is unverifiable as-is.",
  "recommendation": "Extract requirement-bearing files from docs/39 and log-branch batch READMEs; run git branch -a on ~/cst and extract code-repo main; diff the full inventory against the five scopes and document any intentionally excluded branch."
 }
]

### meta_gaps
"Coverage blind spots confirmed against the live tree: (1) the extraction stops at docs/38 but HEAD is d689911 ('docs/39: fortress/survival 两轮竞技场关闭裁决（16/17号家族）+ 场景探针与三条规则发现') — an entire domain (fortress/survival lever closures 16/17, scenario probes, three rule findings) is unextracted, and MT-13's '14 families closed' is now three behind (15 per docs/37 §7, 16/17 per docs/39). (2) Branch inventory (git branch -a): doc repo has ANALYSIS, log, main, origin/COMPARISON, moved/* — log branch never extracted as a requirement source; code-repo main never extracted; no ~/cst inventory in payload. (3) Modalities not run / claims unverified: 24-game pilot and 144-game league (PR-20, MT-12) are frozen design only; differential acceptance vs 原版 practice (PR-22) not executed; race-family heldout gates recorded-but-unexercised (train closed first); tools/versions.json, version_league.py, seat-variant build script do not exist (PR-18/PR-19/PR-25); old-champion 0.8437 sealing (MT-14) unimplemented; wired/DDS bidirectional 联调 evidence absent (CN-14/TC-11); C9 event_update evidence chain (TC-12) accepted-but-unimplemented; 15-min cron is session-only, dies on restart (PR-06/PR-07). (4) Cross-repo referential integrity only spot-checked: L2-CHECK found docs/35 §5 vs docs/36:50 wording contradiction + dangling 'docs/35 §6' reference at docs/36:31, and blob/ANALYSIS branch-name links leak in both repos — a systematic link/reference check across all docs is missing. (5) Stale-vs-current records inside the extraction: PR-07 ('每小时' + '未启用实时监控' vs live 15-min cron c3da6305), MT-13 (14 vs 17 closed families), TC-13 (superseded by docs/37 §7), PR-06 snapshot table (457d99a vs HEAD d689911) — follow-up rounds must read final-verdict sections, not requirement text alone."

### conflicts
[
 "KNOWN 'never push main/master; new branches only' vs extracted CN-33/22-14 '只在现有研究分支提交，不创建新分支' and B2-11 '不擅自创建分支' — the no-new-branch rule contradicts the 'new branches only' clause; needs an explicit user ruling on which governs.",
 "Confidential-branch secrecy (CN-32/AG-05/B1-16/21-13: 不得在其他分支/公开渠道暴露名称、入口) contradicted by actual commits: doc-repo main README b1c15ad carries 19 blob/ANALYSIS links (checks CN-31/CN-32 = partial) and code-repo strategy-branch files carry blob/ANALYSIS links (ARENA.md:53/63, DEV.md:121, README.md:5; code-vrb CN-31/CN-32 = unmet).",
 "MT-13 states '14 个杠杆家族关闭' while docs/37 §7 (HEAD ec9bb4e) records the 15th closure (race_reach_holdoff 0.0) and current HEAD d689911 docs/39 records families 16/17 (fortress/survival) — the extracted count is three behind the live tree.",
 "PR-04/R-01 (append-only, 不改写旧记录) vs commit b4d1946 rewriting an existing review.md line in place ('sk-cbc 扫描通过'→'密钥扫描通过') — literal protocol violation recorded in doc-analysis-b checks; fix = appended errata line.",
 "PR-07 text says '每小时自动检查状态' and '本文件不代表已启用实时监控', contradicting KNOWN '15-min cron' and the live session cron c3da6305 ('3,18,33,48 * * * *') — cadence mismatch, stale record, and session-only persistence (dies on restart).",
 "KNOWN 'hardcoding allowed (competition)' vs CN-01 '不能写死坐标' and CN-11 '不写死练习目标' — scope-reconciled in docs (PR-19: seat/token constexpr '能写死就写死'合规; fortress areas/missions must come from announcements), but the reconciliation should be cited wherever the general allowance is invoked.",
 "GL-01/GL-03 numeric goals (stage1 40, stage2 50) vs GL-06 declaring both unreachable under current rules/vision-4 (TSP ceiling ≈37; 50 needs R≈90+M3+D500) — intentional anchor doctrine; any future 'progress toward 40/50' claim would contradict the recorded unreachability (GL-01 check already prescribes anchor framing).",
 "MT-02 v1.0 formula (D/300) vs MT-03/MT-04 current formula (D/500) — version supersession; check MT-02 marked 'superseded', practice/rules.txt retains old text read-only by design (supersession, not error)."
]

