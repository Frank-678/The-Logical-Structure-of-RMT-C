# docs/57 语雀技术报告草稿（10-31 20:00 材料提交底稿）

- 用途：按 2026-10-30 参赛手册「材料提交」节，每队一份语雀协作文档，内容八项：整体设计思路、功能完成情况与实现方式、队内分工、日程规划、遇到的问题与解决方法、AI 协同开发情况、测试截图、代码运行逻辑及指令；**前置检录截图放在报告内**（①程序完成编译并正常启动；②收到本队感知，取得当前 tick、session_id 和 self.position）。
- 本文件为仓库内底稿（doc 仓 ANALYSIS 分支，保密预备区）；最终以语雀文档为准，粘贴时删去本行说明。事实口径与 SHA 出处：docs/52（联赛结果）、docs/53（M5 同池）、docs/54（策略·算法·参数总清单，逐行核对冠军构建 eb321df）、docs/56（收尾台账）。
- 权限：无法公开的文件添加群主及学辅为协作者，提交前确认语雀文档与代码仓库权限可用。

---

## 1. 整体设计思路

单机器人、三层决策架构（docs/54 §架构一句话）：

1. **导航/规划层**——已知格 BFS 全场距离图、倒推 DP 危险守卫、资源串 beam search、巡回 2-opt；
2. **选择层**——所有收益分支统一 utility 贪心 argmax，加情境折扣（先到先得、低血攻击、封顶口径）；
3. **理解层**——后台线程异步调用统一 AI 网关理解自然语言公告事件，**从不阻塞每 Tick 决策**；动作本地生成，事件交 LLM 理解（规则 v1.2 §11.1 允许）。

两阶段明确分离：第一阶段 100 Tick ×100ms 单车采集（MOVE/WAIT），作种子排位；第二阶段 500 Tick ×500ms 四队对抗（MOVE/ATTACK/DEFEND/WAIT），计分 S2=30×min(R/120,1)+15×min(D/500,1)+5×M（docs/16 行21、docs/28 实战四席复算吻合）。

状态机五态（Observe/Collect/Guard/Combat/Dead）按协议 turn_mode 过滤候选动作；阶段2 存活兜底 DEFEND、阵亡与阶段1 不发违法防御。

## 2. 功能完成情况与实现方式

每 Tick 决策管道（strategy.cpp `decide()`，docs/54 §1）：感知校验 → 状态重建 → 移动前危险 → 危险守卫（8 Tick 倒推 DP + 碰撞改道 + 辣椒火线假设 + 公告避险）→ 全图 BFS → 收益候选（采集/任务/回血/堡垒/辣椒/接近敌方/前沿探索）→ ATTACK 搜索（四向贪心）→ 终选（脱困→战术层[关]→攻击机会→最优 MOVE→未知格试探→防御兜底）→ 发动作（幻术方向反转补偿）。

| 功能 | 状态 | 实现方式 |
|---|---|---|
| 感知/回执校验 | 完成 | 解析+校验，旧帧丢弃、同 Tick 复用缓存 |
| 危险守卫 | 完成 | 8 Tick 倒推 DP、possible_fire 火线假设（LESSONS 修复）、hazard_lead_ticks=2 |
| 导航 | 完成 | BFS 首步方向表、loop_recovery 脱困（12/12/24 Tick 参数） |
| 资源采集 | 完成 | 单目标贪心 + 资源串 beam（宽5深4、10ms 软预算、12 次局部改进）+ stage1 巡回 2-opt + 边界试探 |
| 战斗 | 完成 | §6 贪心 argmax + 情境折扣（post_cap 0.02 开；pie/低血/assassin 杠杆已实现默认关，待竞技场评估） |
| 堡垒 | 完成 | capture/hold 估值、驻留进度全量重建 |
| 事件理解 | 完成 | 后台 LLM 异步、公告去重、结果校验；**不阻塞动作窗口** |
| 两阶段切换 | 完成 | match_config.hpp 编译期 stage，`tools/build_stage.sh 1|2` 一键重建，README「两阶段切换」章节；阶段间 10min 调整窗口内换版本，版本摘要 build/rmtc_bot/match_config.sha256 |
| LLM 每局调用预算 | 完成 | AiConfig.max_calls + cfg::ai_max_calls_per_match（0=不限，默认不改变行为）；observe() 在既有排队护栏后闸 started_，预算耗尽本地策略照常、日志状态 budget_exhausted；现场配额公布后在阶段间窗口改参数 |
| AI 链路自检 | 完成 | practice_launcher --check-ai / check_ai.sh → **request_ok / http 200**（2026-10-30 实测，临时凭证验证后即还原，key 不入库） |

算法命名表：BFS（导航/边界）、倒推 DP（危险守卫）、beam search（资源串）、有界 2-opt（巡回）、贪心 argmax（终选）、LLM（事件理解）。50 项参数全表见 docs/54 §参数总表（语雀内可链仓库文档，不逐项复制）。

## 3. 队内分工

- **Frank（队长）**：架构与参数裁定、席位/检录/现场流程、联赛运行决策；
- **DeepSeek**：策略实现与调试、导航/战斗/事件模块、联赛执行与逐局审计、收尾台账（docs/56）；
- **ChatGPT**：独立审计（112 条要求 GL/MT/CN）、追逃实验室（tools/tests 23/23 单测）、互补逐局台账（milestones/RUN_INDEX.md + match_registry.csv 222 局）。
- 协作协议：review.md 追加式回执、两仓同文、完整 SHA + 验证命令与全量正负结果（以最终提交为准）。

## 4. 日程规划

| 时间 | 事项 |
|---|---|
| 10-21~27 | 规则 v1.2 学习与基线、源码核读（docs/01-16） |
| 10-28 | 首次真实 LLM 对局（REAL_TEST 2 样本）、调参竞技场启动 |
| 10-29 | 参数轮与候选筛选、联赛规格冻结、League-192 收批（192 局） |
| 10-30 | M5 同池对照 32 局收批（docs/53）、AI 链路验证（request_ok）、收尾台账（docs/56） |
| 10-31 20:00 | 材料提交（代码仓库 + 本语雀报告 + 前置检录截图） |
| 11-01 | 正式比赛（第一阶段 → 10min 调整窗口 → 第二阶段） |

## 5. 遇到的问题与解决方法

| 问题 | 解决 |
|---|---|
| possible_fire 把「对手可能踩辣椒」当必然，删掉唯一逃生动作致爆炸死 | 火线改为风险折扣 + 首步风险比较 + 保留公告避险出口（LESSONS） |
| 500 Tick 卡地图上沿往返 | loop_recovery：循环窗口 12 Tick 判定 + 12 Tick 脱困目标 + 24 Tick 冷却（NAVIGATION） |
| 真实调用 5977ms 赶不上 5 Tick 爆炸预告（HTTP 200 ≠ 避险完成） | 后台异步 + 超时分离（35s/5s）+ 公告累积去重；max_tokens 按手册 512 缩短输出 |
| 联赛批次 AI 全 502（10-29 22:00 后空 key→上游 401→502） | check_ai.sh 前置校验 + 链路验证 request_ok；练习证据口径如实声明（见 §9） |
| 联赛运行中改 match_config.hpp 被哈希护栏拦截（M5 事故） | 纪律：联赛中配置冻结；临时凭证验证须全批次收批后即用即还 |
| 密钥管理 | key/proxy 绝不入 git 提交；提交文本附「密钥扫描通过」；全仓 0 处真实 sk- 密钥 |

## 6. AI 协同开发情况

DeepSeek + ChatGPT 双模型分工协作：实现与调参（DeepSeek）、独立审计与实验室（ChatGPT）；全部回复经 review.md 追加式回执（Asia/Shanghai 时间戳、完整 SHA、验证命令与结果），两仓同文。ChatGPT 审计 112 条要求（GL 目标 6 条 / MT 机制 7 条 / CN 约束若干）已逐条吸收进 docs/52-56；追逃实验室（pursuit-evasion 可行性）结论：只做带经济基线+退出条件+不确定性边界的短程截击，追「晋级线附近对手」不可直接实现（公开感知无对手得分/名次）。

## 7. 测试与检录证据

离线测试（联赛批次无真实 AI，规则引擎路径，口径如实）：League-192 192 局（vs 原版陪练与自有模型四 mix，docs/52）；M5 同池 32 局（candidate vs champion Δ+1.20 分，docs/53）；复杂图手动测试（maze/spiral/fortress/islands，docs/51）；参数竞技场多轮（docs/implementation/ARENA_RESULTS）。

真实调用（练习档案 ai.jsonl 全库口径，2026-10-30 深夜复核）：**90 个会话 real 模式 HTTP 200 共 5912 次**（10-28 21:21～10-29 21:51，success 与 status 逐条一致；82 个会话同时含 200/502 记录），含 EVENT_USE 真实对局 dfcef97（45 分第一，A 席 26/26 成功）与 178b15（55 分第一，A 席 29/29 成功，两局其余席位亦有成功记录）；另有 6 个早期会话 200 条 mock 模式记录（非真实调用，不计入）。单项核对：2026-10-28 REAL_TEST 2 样本（200+校验通过）；2026-10-30 链路验证 request_ok/http 200/1163ms。**2026-10-31 冲刺后按正式节奏（500ms×500 tick）新增单局实证（docs/61）**：席位 A 经本地网关→上游真实模型 **25/25 成功**（bot 计数器 24/24、全 200、单次 ~0.6-1.0s），约每 20 tick 一次——每局限额富余 24 倍于「≥1 次」及格线；同局 R=120/120。

**前置检录截图（用户侧操作，截图后贴入本节）**：
1. 程序完成编译并正常启动：`bash build.sh` 输出「构建完成」+ 进程启动日志截图；
2. 收到本队感知：日志中出现本队 tick、session_id、self.position 的截图。

## 8. 代码运行逻辑及指令

- 赛前配置只改 `src/rmtc_bot/include/rmtc_bot/match_config.hpp`：team/席位、stage、ros_domain_id、ai_url（官方网关，以发放值为准）、ai_token（本场席位令牌，不提交）、ai_model=deepseek-flash、ai_max_tokens=512、ai_max_calls_per_match（每局调用预算，配额公布后填）、ai_thinking="disabled"、ai_json_output=true、ai_http_proxy 空串直连；
- 构建：`bash build.sh`（产物 install/rmtc_bot/lib/rmtc_bot/bot）；
- 自检：`bash check_ai.sh`（须返回 request_ok）；
- 短场景验证：`bash scenarios.sh`（四例，不启 ROS 不调模型）；
- 离线联赛：`bash league.sh freeze/suite/run`（LEAGUE.md）；练习代理：`bash practice.sh` / practice_league.sh；
- 启动无需输入参数或环境变量；第二阶段缺必要值拒绝启动，没有隐式补值。

## 9. 合规声明（如实）

- 第二阶段每场每席位须≥1 次真实统一 AI 成功调用，否则任务分=0（2026-10-30 参赛手册）——本队已具备：正式链路自检 request_ok；比赛现场按官方网关+席位令牌执行；
- **练习对局证据口径（2026-10-30 深夜勘误）**：联赛批次（League-192 / M5 / 竞技场，10-29 22:00 起空 key→上游 401→502 时代）AI 调用全 502（league-192 3640/3640 全败），这些批次的离线结果为规则引擎路径证据；**练习档案另有真实调用实据**：90 个会话 real 模式 HTTP 200 共 5912 次（10-28 21:21～10-29 21:51，success 与 status 逐条一致，含 EVENT_USE 两局真实对局），6 个早期会话 200 条 mock 记录不计入——本队真实统一 AI 调用证据 = 5912 次练习实据 + REAL_TEST 2 样本 + 2026-10-30 链路验证；
- 随机事件必须交 LLM 理解判断，不以关键词/正则/固定时间表替代——本队事件处理走统一网关异步理解；
- 不把观赛真值、内部 ROS、管理端或练习配置作为参赛决策输入；镜像非必交。

## 10. 提交前待办

- [ ] 用户：前置检录截图（编译启动 + 感知 tick/session_id/self.position）贴入 §7；
- [ ] 用户：语雀文档权限（群主 + 学辅为协作者）与仓库权限确认；
- [ ] 用户：现场席位令牌填入 match_config.hpp（不提交）后重建；
- [ ] 核对最终提交版本与运行版本一致（git 状态记录）。
