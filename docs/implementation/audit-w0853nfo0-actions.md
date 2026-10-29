## doc-analysis-a
- GL-01 [partial] gap: stage1 ≥40 目标未达成（32.67）；LESSONS.md:76 已按不可达口径如实记载（TSP 下界天花板≈37）
    action: 保持锚点口径；若冲 40 需突破 TSP 下界，否则按目标锚点如实记载
- GL-02 [partial] gap: stage2 ≥50 未达成；rrh10 最终裁决（docs/37 §7，HEAD ec9bb4e）race 家族关闭于 0.0，最高 51.7 均值来自 n=3 部分批次不能作为达标
    action: 执行 docs/38 版本联赛（先 24 场试点）补 stage-2 证据；继续新杠杆（如 prepare_fortress_value 实验）
- GL-03 [partial] gap: 联赛尚未执行——原版/自战维度真实名次与分数分布证据缺失
    action: 内存允许后按 docs/38 先跑 24 场试点再放量
- GL-04 [partial] gap: 证据缺口未补齐：唯一 stage2 锚点仍是训练集 41.25
    action: 执行联赛试点（与 GL-03 同一动作）
- GL-05 [partial] gap: 原版对局维度已有证据；self-play 冻结二进制联赛（M3 混合）未执行
    action: 按 docs/38 §1 M1/M2/M3 混合先 24 场试点
- MT-14 [partial] gap: 冻结清单工具未建：代码仓 tools/ 目录不存在、无 versions.json（docs/38 §1 冻结为设计未落地）
    action: 随 PR-25 tools/ 迁移创建 tools/versions.json 冻结 champion/old_champion/candidate 的 SHA/params_digest/binary_sha256
- CN-31 [partial] gap: main README 进度矩阵证据列以 blob/ANALYSIS 深链暴露 ANALYSIS 分支名，与「不将两支名称/入口写入 main」字面冲突（矩阵本身属授权例外）
    action: 请用户确认该深链形式是否在授权范围内；若否，改为 main 可见路径或相对链接；若可，在 governance 补一条书面豁免
- CN-32 [partial] gap: 公开 main 分支 README 暴露 ANALYSIS 分支名与入口（深层链接）
    action: 与 CN-31 一并处理；优先把 main README 证据链接改指 main 自身上可见的文档或去掉分支名
- PR-18 [partial] gap: tools/versions.json 冻结工具未创建：/home/frank/cst/tools/ 目录不存在，find versions.json 零命中；比赛无运行时参数注入已满足（match_config.hpp 全 constexpr）
    action: 联赛执行前先建 tools/versions.json（champion/old_champion/candidate 的 commit SHA、params_digest、binary_sha256、独立构建目录）
- PR-19 [partial] gap: 4 席位变体构建脚本（临时改头文件→build→还原）尚未实现，随联赛执行落地
    action: 24 场试点前实现席位变体构建流程并归档 binary_sha256
- PR-20 [partial] gap: 试点未执行（依赖内存 + 用户确认 + PR-18/PR-19 工具）
    action: 按 docs/38 §2 顺序：versions.json → 席位变体构建 → 24 场试点
- PR-22 [partial] gap: 差分验收未执行（scenario 工具只覆盖自建引擎侧）
    action: 联赛试点期间按 docs/38 §4 执行向原版 practice 与自建引擎输入相同动作序列的差分核对
- PR-25 [unmet] gap: tools/ 迁移未开始；C6/U4 ablation 夹具拆分、C9 event_update 日志归档同属未落地
    action: 创建代码仓 tools/ 并迁入 batch_practice.py、copy_batch_artifacts.sh、analyze_batch_race.py 等，随下批提交
- TC-12 [partial] gap: C9 event_update 独立日志归档已接受但未实现（review.md:245 的条款），「唯一公告→解释正确→送达→兑现→改变行为→收益」计数链尚无落地工具
    action: 与 PR-25 同批实现 C9 event_update 日志并按链计数归档
- L2-CHECK [unmet] gap: U7 勘误未同步进 docs/35：同一仓库两处措辞矛盾 + 一个失效交叉引用（均在当前 HEAD ec9bb4e）
    action: docs/35 §5 结论第 1 条追加勘误注（引 docs/36:50 口径），并修正 docs/36:31 的「docs/35 §6」指向（改为 §5 或删除）

## code-vrb
- GL-03 [partial] gap: 'stage2 目标 50 分' 与 '联赛数据作为 50 分验收第一手证据' 的目标表述不在 cst（仅分析仓 docs/38）；grep '50 分|目标 50' 无命中
    action: 如需代码仓承载目标口径，可把目标/锚点一句并入 review.md 或 ARENA.md。
- GL-04 [partial] gap: 证据缺口补法（原版对局+自战联赛）全文在分析仓 docs/37；cst 仅以 C7 接受条目体现
    action: 联赛实现后回填（见 PR-18/PR-20 动作）。
- GL-05 [partial] gap: U6 判定原文（多 profile 自战档案不能代表旧版本/原版 robot_node）未逐字迁入，仅改编进 C7 答复
    action: 保持现状即可（内容已适配入 review 协议流）。
- GL-06 [unmet] gap: 两目标结构不可达结论只存分析仓 docs/implementation/LESSONS.md:76
    action: 按 PR-01/PR-02 属分析类内容，无需回迁代码仓。
- MT-05 [partial] gap: '分裂立即复活也扣' 未显式陈述（arena.cpp:125-129 split 死亡按通用 death 计数处理，无专文）
    action: 如需逐字对齐可在 rules.hpp 注释补一句分裂复活照扣。
- MT-08 [partial] gap: 完整数值 0.8298625 与 arena-postcap-heldout-2026-10-29.json 结果文件不在 cst tests/results（ls-tree 无该文件），仅在分析仓
    action: 如代码仓需自足，把 postcap heldout 结果 JSON 补入 tests/results/。
- MT-10 [unmet] gap: 真实对局护栏（deaths 均值≥9 且中位≥8 且平局翻盘0 → 回退 0.02）全文只在分析仓 docs/30
    action: 护栏已过时（0.02 已晋升），无需回迁；如批量对局复用该防线可写入 tools/ 驱动。
- MT-11 [unmet] gap: t30 完成率≥0.356 等预注册判据只在分析仓 docs/35
    action: 判据已随 race 轮闭合消耗，无需回迁；后续批量预注册判据应写入随批提交的 tools/ 脚本（PR-25）。
- MT-14 [partial] gap: 旧冠军 0.8437 的源码 SHA/参数/对手版本逐局复现封存尚未实现（联赛版本冻结待做）
    action: 随 PR-18 的 versions 清单一并落地。
- CN-03 [partial] gap: '提交与现场运行版本须一致' 不在 cst
    action: 现场提交纪律属人工流程，可入 STATE_MACHINE.md §2.3 一行。
- CN-04 [unmet] gap: 只在分析仓 docs/13
    action: 非代码仓内容，无需回迁。
- CN-05 [partial] gap: 原句 '封存后不能随意修改源代码、Prompt 或策略参数' 未逐字出现
    action: None — 机制（编译期常量+sha256门禁）已落实。
- CN-06 [partial] gap: '每阶段原则上最多两次' 的次数上限不在 cst
    action: 可在 STATE_MACHINE.md §2.3 补 '最多两次'。
- CN-07 [unmet] gap: 提交/比赛日程只在分析仓 docs/01
    action: 日程属分析类信息，无需回迁。
- CN-08 [unmet] gap: 只在分析仓 docs/16
    action: 无需回迁。
- CN-09 [unmet] gap: 只在分析仓 docs/15
    action: 无需回迁。
- CN-14 [unmet] gap: 有线联调要求只在分析仓 docs/10
    action: 验收动作类条目，无需回迁。
- CN-15 [unmet] gap: 只在分析仓 docs/02
    action: 写作纪律，无需回迁。
- CN-16 [partial] gap: '源代码、Prompt、策略参数一起版本化' 原句未出现；Prompt 以 ai_thinking/ai_model 常量存在 match_config.hpp:28-31，与源码同仓同提交
    action: None — 机制满足，仅缺一句表述。
- CN-17 [partial] gap: '不修改原裁判，不让机器人发布或覆盖成绩' 无逐字声明
    action: 可在 CODE_GUIDE.md 补一句边界声明。
- CN-23 [partial] gap: 全句（只能依据本队感知/回执/公告/合法记忆估计耗尽）未逐字迁入
    action: 机制已合规，无需回迁。
- CN-25 [partial] gap: '提示其撤销轮换' 与 '测试仅使用 fixture 凭据' 的事件处理叙述不在 cst
    action: 事件已结案，现状合规即可。
- CN-26 [partial] gap: '临时Key只用于测试，没有写入代码、日志或结果文件' 原句不在 cst，以空值+注释形式承载
    action: None。
- CN-27 [partial] gap: '临时副本测试后已删除' 无法从仓库验证
    action: 无需动作。
- CN-28 [unmet] gap: 网关核验流程只在分析仓 docs/37
    action: 如需代码仓自足，可把核验脚本并入 tools/（随 PR-25）。
- CN-29 [partial] gap: 哈希/validated/rejected/partial/去重/token/费用字段不齐，event_update 日志归档在分析仓
    action: None — 凭据不入库的要求已满足。
- CN-31 [partial] gap: 违反点不在 main/PR 而在 strategy 分支文件里出现分支名链接——与 CN-32 的线索禁令交叉
    action: 与用户确认 cross-repo 'blob/ANALYSIS' 链接是否算泄露线索；若算，改为按提交 SHA 链接或去掉分支名。
- CN-32 [unmet] gap: 保密预备分支条款未采纳进 cst，且存在分支名线索散落于代码仓文件的合规风险
    action: 审计结论：要么替换/移除这些链接中的分支名，要么取得用户书面确认该 ANALYSIS 为公开归档分支（CN-34 口径）。
- CN-34 [unmet] gap: 只在分析仓 docs/08
    action: 无需回迁。
- PR-03 [partial] gap: '原代码基线 826c4da' 迁移说明本身在分析仓 docs/implementation/README.md，未在 cst 出现
    action: 无需回迁。
- PR-04 [partial] gap: 改编版：'北京时间' 写作 'Asia/Shanghai'，'证据和下一步' 写作 '验证命令与结果'
    action: None — 协议实质一致。
- PR-05 [partial] gap: '代码条目回代码分支同名文件、理论与日志条目回本文件' 的分流句未写入 cst（以两仓各持 review.md 的实践落实）
    action: None。
- PR-06 [unmet] gap: 只在分析仓 docs/22
    action: 监控属分析仓工作，无需回迁。
- PR-07 [unmet] gap: 只在分析仓 review.md:62
    action: 无需回迁。
- PR-10 [partial] gap: 预注册判据条文本身（写于批量运行中、结果未读）在分析仓 docs/35，未随批写入 cst
    action: 下轮批量前把判据写入随批提交的 tools/ 脚本（PR-25）。
- PR-13 [partial] gap: 全句（反复使用的集合只能称'反复使用的验证成绩'等）未逐字迁入
    action: None — 纪律实质已入 ARENA.md。
- PR-14 [partial] gap: '机器/并行数/规则版本' 未列入 ARENA.md 记录清单
    action: 在 ARENA.md 结果记录清单补机器/并行数两字段。
- PR-16 [unmet] gap: 只在分析仓 review.md:82
    action: 如继续批量对照，把该口径写入 tools/ 驱动。
- PR-17 [partial] gap: '被校验器拒绝的配置计为生成/校验失败单独报告' 未实现为独立报告项
    action: 可在 run_arena.py 报告加 rejected-config 计数。
- PR-18 [partial] gap: tools/versions.json 尚未创建（cst 无 tools/ 目录）
    action: 联赛阶段实现 versions.json 冻结清单。
- PR-19 [partial] gap: '每版本构建 4 个席位变体（A/B/C/D）临时改头文件→build→还原' 的构建脚本未实现
    action: 随版本联赛（PR-18）一并实现席位变体构建脚本。
- PR-20 [unmet] gap: 试点规格只在分析仓 docs/38:33
    action: 联赛实现前先补 24 场试点规格到代码仓。
- PR-21 [partial] gap: 代码 SHA/AI 模式/session_id/最终名次/hp 全字段与 '版本级按初始地图成组、保留最差样本' 未实现（联赛待建）
    action: 随联赛实现补齐归档字段。
- PR-24 [partial] gap: '不要把旋转/镜像后的同一张图或四席位计作独立新地图' 无逐字条文，但夹具口径一致（旋转=同图变体）
    action: None — 实质合规。
- PR-25 [unmet] gap: 'batch 驱动器、归档与筛选/验证脚本迁入代码仓 tools/ 并随批提交' 未执行
    action: 下轮批量实施时落 tools/ 并随批提交。
- PR-26 [unmet] gap: 只在分析仓 docs/37
    action: 归档流程属分析仓操作，无需回迁。
- PR-27 [partial] gap: session 匹配目录、起止 Tick 完整、客户端/网关次数同一场等归档自洽校验未在代码仓实现
    action: 可并入 PR-25 的归档校验脚本。
- PR-28 [partial] gap: '当局结束后立即从该局路径拷贝 bot_A.log、禁止共享路径统一拷贝' 的 copy_batch_artifacts.sh 机制不在 cst（分析仓侧）
    action: 批量归档脚本实现时把该拷贝规则固化其中。
- PR-30 [partial] gap: 原版 practice 对局的逐局归档自动化（读裁判 rank、保留平局判定键、改善原始分与名次分开报）未实现
    action: 真实对局归档脚本实现时落实。
- EV-01 [partial] gap: 原句未逐字出现，以证据分级声明承载
    action: None。
- EV-02 [partial] gap: '所有机制结论标来源，所有策略假设标待测试' 未逐字入 cst
    action: None — 实践已普遍执行。
- EV-03 [partial] gap: 未完成事项如实标注的实践在 cst 成立，但无统一条文
    action: None。
- EV-04 [partial] gap: 口径声明已分散落地，无逐字条文
    action: None。
- EV-05 [unmet] gap: 只在分析仓 docs/09
    action: 无需回迁。
- EV-06 [unmet] gap: 只在分析仓 docs/27
    action: 无需回迁。
- EV-07 [partial] gap: '不把文件清单、静态阅读或模拟测试称为真实比赛通过' 原句未出现
    action: None — 实质已遵守。
- EV-09 [unmet] gap: 只在分析仓 docs/25
    action: 无需回迁。
- EV-11 [partial] gap: '夹具没有敌车、随机事件、任务或AI' 的枚举与原句未逐字出现（cst 夹具实有敌车/任务）
    action: None — 边界如实声明已满足精神。
- EV-13 [partial] gap: NOTICE.md 与原件哈希/许可说明记录不在 cst（存分析仓）
    action: 如代码仓需自足可补 NOTICE.md，否则维持现状。
- TC-05 [partial] gap: '待与裁判对照，不能写成读到了引擎实现' 以 ARENA.md 待核对口径承载
    action: None。
- TC-08 [partial] gap: '正式上场前仍需实战验证与按规则封存参数' 未逐字出现
    action: None — 边界声明已在。
- TC-10 [unmet] gap: 批量实验授权范围只在分析仓 docs/28
    action: 授权记录属分析仓，无需回迁。
- TC-12 [partial] gap: 六段计数链（唯一公告事件数→…→实际收益）未实现
    action: 公告证据链实现时落 session 诊断日志。
- TC-13 [unmet] gap: rrh10 续跑 --only 3..6 的驱动与分析在分析仓
    action: 批量驱动迁入 tools/ 时一并实现 --only 干净续跑（PR-25）。

## critic
{
 "coverage_gaps": [
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
 ],
 "meta_gaps": "Coverage blind spots confirmed against the live tree: (1) the extraction stops at docs/38 but HEAD is d689911 ('docs/39: fortress/survival 两轮竞技场关闭裁决（16/17号家族）+ 场景探针与三条规则发现') — an entire domain (fortress/survival lever closures 16/17, scenario probes, three rule findings) is unextracted, and MT-13's '14 families closed' is now three behind (15 per docs/37 §7, 16/17 per docs/39). (2) Branch inventory (git branch -a): doc repo has ANALYSIS, log, main, origin/COMPARISON, moved/* — log branch never extracted as a requirement source; code-repo main never extracted; no ~/cst inventory in payload. (3) Modalities not run / claims unverified: 24-game pilot and 144-game league (PR-20, MT-12) are frozen design only; differential acceptance vs 原版 practice (PR-22) not executed; race-family heldout gates recorded-but-unexercised (train closed first); tools/versions.json, version_league.py, seat-variant build script do not exist (PR-18/PR-19/PR-25); old-champion 0.8437 sealing (MT-14) unimplemented; wired/DDS bidirectional 联调 evidence absent (CN-14/TC-11); C9 event_update evidence chain (TC-12) accepted-but-unimplemented; 15-min cron is session-only, dies on restart (PR-06/PR-07). (4) Cross-repo referential integrity only spot-checked: L2-CHECK found docs/35 §5 vs docs/36:50 wording contradiction + dangling 'docs/35 §6' reference at docs/36:31, and blob/ANALYSIS branch-name links leak in both repos — a systematic link/reference check across all docs is missing. (5) Stale-vs-current records inside the extraction: PR-07 ('每小时' + '未启用实时监控' vs live 15-min cron c3da6305), MT-13 (14 vs 17 closed families), TC-13 (superseded by docs/37 §7), PR-06 snapshot table (457d99a vs HEAD d689911) — follow-up rounds must read final-verdict sections, not requirement text alone.",
 "conflicts": [
  "KNOWN 'never push main/master; new branches only' vs extracted CN-33/22-14 '只在现有研究分支提交，不创建新分支' and B2-11 '不擅自创建分支' — the no-new-branch rule contradicts the 'new branches only' clause; needs an explicit user ruling on which governs.",
  "Confidential-branch secrecy (CN-32/AG-05/B1-16/21-13: 不得在其他分支/公开渠道暴露名称、入口) contradicted by actual commits: doc-repo main README b1c15ad carries 19 blob/ANALYSIS links (checks CN-31/CN-32 = partial) and code-repo strategy-branch files carry blob/ANALYSIS links (ARENA.md:53/63, DEV.md:121, README.md:5; code-vrb CN-31/CN-32 = unmet).",
  "MT-13 states '14 个杠杆家族关闭' while docs/37 §7 (HEAD ec9bb4e) records the 15th closure (race_reach_holdoff 0.0) and current HEAD d689911 docs/39 records families 16/17 (fortress/survival) — the extracted count is three behind the live tree.",
  "PR-04/R-01 (append-only, 不改写旧记录) vs commit b4d1946 rewriting an existing review.md line in place ('sk-cbc 扫描通过'→'密钥扫描通过') — literal protocol violation recorded in doc-analysis-b checks; fix = appended errata line.",
  "PR-07 text says '每小时自动检查状态' and '本文件不代表已启用实时监控', contradicting KNOWN '15-min cron' and the live session cron c3da6305 ('3,18,33,48 * * * *') — cadence mismatch, stale record, and session-only persistence (dies on restart).",
  "KNOWN 'hardcoding allowed (competition)' vs CN-01 '不能写死坐标' and CN-11 '不写死练习目标' — scope-reconciled in docs (PR-19: seat/token constexpr '能写死就写死'合规; fortress areas/missions must come from announcements), but the reconciliation should be cited wherever the general allowance is invoked.",
  "GL-01/GL-03 numeric goals (stage1 40, stage2 50) vs GL-06 declaring both unreachable under current rules/vision-4 (TSP ceiling ≈37; 50 needs R≈90+M3+D500) — intentional anchor doctrine; any future 'progress toward 40/50' claim would contradict the recorded unreachability (GL-01 check already prescribes anchor framing).",
  "MT-02 v1.0 formula (D/300) vs MT-03/MT-04 current formula (D/500) — version supersession; check MT-02 marked 'superseded', practice/rules.txt retains old text read-only by design (supersession, not error)."
 ]
}