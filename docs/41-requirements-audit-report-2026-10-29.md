# 41. 全仓需求审计报告（w0853nfo0 · 2026-10-29）

> 状态：**完成**。审计工作流 w0853nfo0（11 agents / 1,182,956 tokens / 454 工具调用）提取两仓全分支需求并逐条核验；本报告给出裁决统计、非 met 项处置、批评者（critic）覆盖缺口采纳与冲突裁决。
> 依据：用户约束"必须满足两个仓库每个分支的每一条要求"；AGENTS.md 分支协作约定与 2026-10-29 补充（分析类文件放本仓库，与代码强相关的除外）。
> 蒸馏附件：docs/implementation/audit-w0853nfo0-distill.md（逐条证据）、audit-w0853nfo0-actions.md（全部非 met 项与 critic 全文）。

## 1. 审计方法与快照边界

**方法**：五范围并行提取 → 逐条核验（证据=具体文件行 + live tree 复核）→ 批评者专设一轮"什么没被覆盖、什么自相矛盾"。提取件以"要求"为单位（含 goal/metric/constraint/process 分类），核验结论四档：met / partial / unmet / superseded。

**快照边界（如实声明）**：
1. 审计快照：分析仓 HEAD **d689911**（即 docs/39 提交）；代码仓早于 tools/ 入库（6e13b18）与试点开跑。故 PR-25/MT-14/PR-18/PR-19/PR-20 在快照时为未落地，**快照后已闭合**（见 §4）。
2. 未提取面：docs/39（d689911 内容，快照内但不在提取范围）、log 分支（仅按归档证据抽查）、代码仓 main 分支（仅合规核查未作需求集提取）。全部列入 §4 缺口。
3. 验证覆盖不对称：doc-analysis-b 199 条仅 11 条代表性核验（8 met / 3 partial）；doc-comparison-main、code-iterate-arena 各 112 条 bulk 核验全 met。此不对称如实记录，不宣称"全量逐条核验"。

## 2. 裁决统计

| 范围 | 内容 | 提取 | 核验记录 | met | partial | unmet | superseded |
|---|---|---|---|---|---|---|---|
| doc-analysis-a | 分析仓 docs 01–38 + review + governance | 112 | 113 | 97 | 13 | 2 | 1 |
| doc-analysis-b | 分析仓协议类追加核验 | 199 | 11（代表性） | 8 | 3 | 0 | 0 |
| doc-comparison-main | COMPARISON + main 分支 | 230 | 112（bulk） | 112 | 0 | 0 | 0 |
| code-iterate-arena | 代码仓策略分支（含 vrb 工作树） | 205 | 112（bulk） | 112 | 0 | 0 | 0 |
| code-vrb | 代码仓逐字核验（原文迁入条款） | 78 | 112 | 47 | 41 | 23 | 1 |
| **合计** | | **824** | **460** | **376** | **57** | **25** | **2** |

非 met 合计 84 条（57 partial + 25 unmet + 2 superseded），其中**绑定动作项**全部在本批或快照后闭合（§4）；其余为"无需回迁/机制已合规"类，按用户 2026-10-29 补充口径判定维持现状（§3.2）。

## 3. 非 met 项处置

### 3.1 分析仓 doc-analysis-a（13 partial / 2 unmet / 1 superseded）

| ID | 结论 | 处置 |
|---|---|---|
| GL-01 阶段一 ≥40 | partial（32.67，TSP 下界≈37） | 锚点口径维持（GL-06 met）；不宣称进展 |
| GL-02 阶段二 ≥50 | partial（锚点 41.25；51.7 为 n=3 部分批次，不作数） | 联赛证据行动中（GL-03 同） |
| GL-03 联赛未执行 | partial | **行动中**：docs/40 试点 16 局（17:25 开跑），结果入 docs/42 |
| GL-04 证据缺口 | partial | 同上，试点补齐第一手证据 |
| GL-05 self-play 冻结联赛 | partial | 试点 M2（vs old_champion 冻结二进制）执行中 |
| MT-14 旧冠军封存 | partial | **已闭合**（快照后）：9bc72a7 源树 worktree + params_digest + 席位变体二进制 sha256 入 versions.json |
| CN-31/CN-32 main README 深链暴露分支名 | partial | 代码仓侧已修（§4）；main README 矩阵侧形式**待用户裁定**（§6） |
| PR-18/PR-19/PR-20 冻结清单/席位变体/试点规格 | partial | **已闭合**（快照后）：tools/versions.json + build_seat_variants.sh + 试点预注册 docs/40 |
| PR-22 原版差分 | partial | **待办**：等 ChatGPT 真实裁判通道（review C4） |
| TC-12 公告六段计数链 | partial | 已接受待实现（backlog，§6） |
| PR-25 tools/ 迁移 | unmet | **已闭合**（快照后）：6e13b18 六件套入库 |
| L2-CHECK docs/35 与 docs/36 措辞矛盾 + 失效交叉引用 | unmet | **本批已修**：docs/35 §5 追加勘误注（docs/36:50 口径）；docs/36:31「docs/35 §6」→「§5」 |
| TC-13 rrh10 续跑驱动 | superseded | docs/37 §7 裁决已取代（race 家族关闭于 0.0）；--only 干净续跑并入 tools/ backlog |

### 3.2 代码仓 code-vrb（41 partial / 23 unmet / 1 superseded）

分三组处置：

**(a) 无需回迁类（判定原则 = 用户 2026-10-29 补充"分析类文件放本仓库"）**：CN-04/CN-07/CN-08/CN-09/CN-14/CN-15、EV-05/EV-06/EV-09、PR-06/PR-07/PR-16/PR-26、TC-10、MT-10（0.02 护栏已过时）、MT-11（判据已随 race 轮消耗）、CN-28/CN-29/CN-34（如需自足才回迁）。裁决：**维持现状**，内容由分析仓承载，本报告即处置记录。

**(b) 机制已合规、仅缺条文类**：CN-03/CN-05/CN-06/CN-16/CN-17/CN-23/CN-25/CN-26/CN-27、EV-01/EV-02/EV-03/EV-04/EV-07/EV-11/EV-13、PR-04/PR-05/PR-13/PR-24、TC-05/TC-08。裁决：**维持现状**（编译期常量 + sha256 门禁 + 边界声明均已落实；不为一句话破坏既有结构）。特例 **MT-05**（分裂复活照扣未显式陈述）：为补注释改动 rules.hpp 会脏化 bit-pin 源树（CN-05 封存纪律优先），维持现状——行为本身由 arena.cpp:125–129 通用死亡计数覆盖。

**(c) 真实动作项**：

| ID | 结论 | 处置 |
|---|---|---|
| CN-31/CN-32 分支名链接泄露 | partial/unmet | **本批已修**：ARENA.md/DEV.md/README.md 共 10 处 blob/ANALYSIS → blob/提交SHA 永久链接（0f17e5f） |
| PR-14 记录清单缺机器/并行数 | partial | **本批已修**：archive_batch.py 战报表补两字段（0f17e5f） |
| MT-08 heldout JSON 不在 cst | partial | 维持现状：结果文件属分析类，按 2026-10-29 补充留分析仓（数值 0.8298625 已入 versions.json pins） |
| GL-03/GL-04/GL-05 联赛证据 | partial | **行动中**（docs/40 试点） |
| MT-14 旧冠军封存 | partial | **已闭合**（§3.1 同） |
| PR-10/PR-16 预注册判据写入 tools/ | partial | 采纳为今后规则：下轮批量判据随批写入驱动脚本（试点判据已入 docs/40 §3） |
| PR-17 rejected-config 计数、PR-21/PR-27/PR-28 归档字段与自洽校验、PR-30 原版逐局归档自动化、TC-12 公告链、TC-13 --only 续跑 | partial/unmet | **backlog**（§6 表） |
| MT-02 D/300 旧公式 | superseded | 版本替代（MT-03/MT-04 D/500）；practice/rules.txt 旧文只读保留，非错误 |

## 4. critic 覆盖缺口与采纳

| 缺口 | 处置 |
|---|---|
| **缺口 1：D2 1026.67 无任何要求记录**（其余锚点钉均有：objective/deaths/blocked→AR-21/M-06，stage2→GL-03/04，heldout→MT-08，determinism→MT-09，bit-pin→AR-22/M-05） | **本批已修**：tools/versions.json champion 补完整 pins（train objective 0.7970931712962963 / deaths 83 / blocked 93 / stage1 33.333 / stage2 41.25 / **D2 1026.67** / heldout 0.8298625 / determinism 0.7710073），0f17e5f；与 docs/36 §4 封存表逐位一致 |
| **缺口 2：分支覆盖**（docs/39 未提取、log 分支仅抽查、代码仓 main 未提取） | 边界声明入 §1；docs/39 内容已自带证据（19 场景 12/12 回归 + 勘误 56da8b3）；后续轮次计划：docs/39+ 追加提取、log 分支 README 战报表批量提取、代码仓 main 需求集提取（低优先，main 为公开门面） |
| meta：有线/DDS 双向联调证据缺失（CN-14/TC-11） | **未决现场项**：当前环境网卡枚举权限阻塞，已在 ARENA.md/REAL_TEST.md 如实记录；赛前有线实测纳入验收清单 |
| meta：15 分钟 cron 会话级 | 如实记录：cron 随会话重挂（3,18,33,48 分），不宣称常驻 |
| meta：MT-13「14 家族」计数过时 | 以 docs/39 为准：**17 个杠杆家族关闭**（docs/37 §7 第 15 个 + docs/39 第 16/17 个）；本报告覆盖提取件 |
| meta：跨仓引用完整性仅抽查 | L2-CHECK 两处已修（§3.1）；全量链接/交叉引用系统性扫描入 backlog |

## 5. 冲突清单与裁决

| 冲突 | 裁决 |
|---|---|
| 不创建新分支（CN-33/22-14/B2-11）vs 只推新分支（KNOWN） | **实践调和**：本周期零新分支创建，只推既有长驻分支（ANALYSIS / log / strategy/iterate-arena-2026-10-28），两条同时满足 |
| 保密禁令（CN-32/AG-05）vs 实际 blob/ANALYSIS 链接 | 代码仓侧已改 SHA 永久链接（本批）；分析仓 main README 矩阵 19 处深链形式**待用户裁定**（CN-34 口径：确认 ANALYSIS 是否公开归档分支，或授权改 SHA/去分支名） |
| MT-13「14」vs 现树「15/16/17」 | 现树为准（§4），提取件计数作废 |
| PR-04/R-01 追加式 vs b4d1946 就地改写 | **已追加勘误承认**（代码仓 review.md 本批，严格追加式此后执行） |
| PR-07「每小时」vs 现 15 分钟 cron | 旧记录过时；本报告记录现状（15 分钟、会话级） |
| 能写死就写死 vs CN-01/CN-11 不写死 | 已调和（docs PR-19 口径）：席位/令牌编译期常量合规；堡垒区域与任务必须读公告 |
| GL-01/03 目标 vs GL-06 不可达 | 锚点原则（GL-06 met）持续有效；本报告不含任何"向 40/50 进展"声明 |
| MT-02 v1.0 vs MT-03/04 现行 | 版本替代；rules.txt 旧文只读保留 |

## 6. 本批闭合动作与待办

**本批两仓提交**：

| 仓 | 提交 | 内容 |
|---|---|---|
| 代码仓 | 0f17e5f | versions.json pins（critic 缺口1）、10 处 SHA 永久链接（CN-31/32）、归档字段（PR-14）、review.md 闭合记录 + R-01 追加勘误；密钥扫描通过 |
| 分析仓 | 本批 | docs/35 §5 勘误注、docs/36:31 指向修复（L2-CHECK）、docs/40 预注册更新（§4 执行记录）、docs/41 本报告、audit-w0853nfo0-* 蒸馏附件 |

**待用户裁定**：main README 矩阵深链形式（CN-31/CN-32 分析仓侧；CN-34 口径）。

**待办 backlog**（无阻塞，按优先级）：PR-22 原版差分（等 ChatGPT 通道 C4）→ 试点结果分析 docs/42 → TC-12 公告链、TC-13 --only、PR-17/21/27/28/30 归档硬化 → 有线/DDS 联调现场项 → 审计后续轮次（docs/39+ 与 log/main 提取、全量引用扫描）。

**进行中**：docs/40 试点 16 局（2026-10-29 17:25 开跑，§4 进度快照 3/16），完成后归档 log 分支并写 docs/42（试点预注册判定规则见 docs/40 §3，不放量、不晋升——放量 144 场才裁决）。
