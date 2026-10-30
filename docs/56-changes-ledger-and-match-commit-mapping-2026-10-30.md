# 56 · 收尾台账：2026-10-29 20:00 起全部改动与每一次比赛→提交链接

- 身份：DeepSeek
- 时间：2026-10-30 21:41 +0800
- 范围：北京时间 **2026-10-29 20:00** 起，至 2026-10-30 深夜收尾。用户指令（10-30 21:0x）：「我们不再跑比赛了，做好收尾工作」「写好自昨天 20:00 开始做了哪些改动；将每一次比赛链接到提交上」。
- 四轨：code `strategy/visible-resource-bfs`（vrb）、code `strategy/iterate-arena-2026-10-28`（iterate-arena）、doc `ANALYSIS`、doc `log`（worktree `D:\code\The-Logical-RMT-C-log`）。
- 结构：§1 改动时间线台账（四轨合并）→ §2 **每一次比赛→提交对照总表（本文件核心）** → §3 席位冻结契约全表 → §4 事故与处置 → §5 收尾状态与未决事项 → §6 验证命令。
- 提交链接：code 仓 `https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/commit/<sha>`；doc 仓 `https://github.com/Frank-678/The-Logical-Structure-of-RMT-C/commit/<sha>`（表内仅列短 SHA，全文见 §3 及两仓历史）。
- **逐局机器可读对照表**：`milestones/RUN_INDEX.md`（逐场 222 局，每局含摘要/Tick 日志/配置直链与归档提交）+ `milestones/match_registry.csv`（同 222 局，binary_sha256/source_commit/config_sha256/session_id 全字段）——本文件的批次级台账与其互补。

## 1. 改动时间线台账（2026-10-29 20:00 → 2026-10-30 21:30）

「双轨」= 同一提交同时落在 vrb 与 iterate-arena（或内容同文两提交）。ANALYSIS/log 为 doc 仓分支。

### 1.1 10-29 晚间：16 局试点、scale-96、R2 候选对照、M3 冻结、联赛设施

| 时间 | 轨道 | 提交 | 改动 |
|---|---|---|---|
| 20:30 | vrb+iter | bbdf688 | review.md 推送 DeepSeek |
| 20:34 | log | 73c2f96 | 归档 16 局试点批次（pilot-new） |
| 20:38 | ANALYSIS | 871d879 | docs/45 新路径 16 局正式证据（T11 全表） |
| 20:48 | ANALYSIS | c03daf0 | 修复 docs/45 路径名 CRLF 污染 |
| 20:49 | vrb+iter | 27c3bcd | referee 启动失败静置重试 3×15s + 局间静置 3s |
| 22:06 | ANALYSIS | ba6a598 | docs/47 scale-96 部分批次（12/96，护栏中止记录） |
| 22:06 | log | d0a80d1 | 归档 scale-96 partial（12 session 10 件套） |
| 22:45 | log | 021ae79 | 归档 R2 候选对照第一~五轮证据（73 份 per-variant 报告） |
| 22:49 | ANALYSIS | 231fe1e | docs/46 R2 候选对照八轮收口 + M3 冻结 old7_no_etr0 |
| 22:51 | log | e90a8b4 | 归档 R2 第六~八轮证据（11 份报告） |
| 22:54 | vrb+iter | 9d23def | 联赛设施全家桶采纳（league.sh/practice_batch/version_league + 12 项工具修复） |
| 22:54 | vrb+iter | 3a37703 | 新增 explore_probe_mission_bonus_scale 参数（默认 1.0=旧行为，行为类默认关） |
| 22:55 | vrb | e7e5c43 | merge iterate-arena → vrb |
| 22:59 | vrb / iter | 38b5d09 / d2fb085 | M3 交接（candidate 五参数冻结） |
| 23:12 | log | c1c64dd | 离线联赛全量磁带归档 |
| 23:13 | ANALYSIS | 5f23fac | chase 分析归档 |
| 23:18 | iter | 8856734 | M4 焦点位混合 + tdc 死参数冻结修订（五参数）+ Ready 每次尝试独立基线 + 聚合退出码回归 + 席位构建修复 |
| 23:18 | ANALYSIS | f1675c8 | docs/48 联赛 192 场预注册 + M3 冻结修订 |
| 23:21 | log | a79fcfb | 归档完整性修正 |
| 23:22 | iter | 203ab35 | relay Frank 追击/墙角/逃脱测试诉求 |
| 23:23 | vrb+iter / ANALYSIS | 3a76daa / b7c3e0b | 保留追击交接、不合并策略分支 |
| 23:31 | ANALYSIS | fc3f0f1 | HANDOFF 两块答复 + docs/46 §6 勘误（tdc 死参数） |
| 23:32 | iter | eacb963 | review.md 逐条答复 HANDOFF-FINAL/FINAL-HANDOFF |
| 23:36 | iter / ANALYSIS | 2e5a394 / f76b00a | 逐项答复 CHASE-USER Q1-Q6（感知契约静态核实） |
| 23:42 | log | aa75811 | ablate9 第九轮四格消融证据（tdc 6/6 逐位实证） |
| 23:42 | iter / ANALYSIS | 3c93bce / 1e27a2a | log 核验收据（a79fcfb 三包 verify、ablate9 归档） |
| 23:43 | ANALYSIS | b73b363 | docs/49 追击/墙角故障测试计划（CHASE 预注册） |
| 23:46 | ANALYSIS | f893844 | docs/50 wide_lanes 代码层二分候选静态预筛 |
| 23:48 | iter | 27bd678 | 原版 ROS 席位差分适配器草案（observe/drive） |
| 23:51 | vrb+iter | a4ccba5 | ChatGPT 同时行动追逃实验室（纯 tools/tests） |
| 23:52 | log | 63a0784 | 追击矩阵/结算/LP 证书归档 |
| 23:54 | ANALYSIS | 3a588dc | 追击推导分析（advancement-aware pursuit） |
| 23:58 | iter / ANALYSIS | 901aed3 / bbfebf0 | pursuit 交接 + frontier 权重澄清 |

### 1.2 10-30 凌晨–午间：探针修复、答复块、规则文本、复杂图诊断

| 时间 | 轨道 | 提交 | 改动 |
|---|---|---|---|
| 00:01 | iter | ffe334b | 关闭 review_handoff_probe R1/R2/R3（Ready 改 (行数,mtime_ns) 契约） |
| 00:07 | iter | 00dfb35 | R3 exec 数组 colcon + R3/R4 永久回归（16/16 OK） |
| 00:07 | iter | c416ecd | original_ros_diff drive 回填 session_id/tick |
| 00:09 | iter | e51efcf | 采纳追逃实验室（a4ccba5 辨别性合入，23/23 复跑） |
| 00:10 | ANALYSIS | 348f3bd | docs/48 勘误 M4 对手池 + M5 同池焦点对照追加；docs/50 修正差分嫌疑 |
| 00:12 | iter / ANALYSIS | abd49ba / 996f76b+cbc76f0 | 答复 PURSUIT-CAUSAL-HANDOFF（R1-R4 采纳 SHA、诉求三条；cbc76f0 修正行尾改写保 CRLF） |
| 00:19 | ANALYSIS | 5b7e3f3 | docs/49 并入上游追击可行性约束 |
| 10:28 | iter | 5a689bf | review.md 推送（规则文本块） |
| 10:33 | iter | cc2b34d | review.md 更新 |
| 10:42 | iter | eef40e9 | 答复规则文本块（采纳地图尺寸/同分次序/事件机制、不登记 decision_type、指出调整窗口矛盾、重申三问） |
| 10:43 | ANALYSIS | a423fb5 | 同文：答复规则文本块 |
| 11:04 | ANALYSIS | b47e83a | docs/51 复杂图手动测试逐 tick 诊断（败局=纯 RV 经济缺口，反事实 47.5/50.0） |

### 1.3 10-30 午后：League-192 收批、M5 启动、参数总清单、AUD 答复

| 时间 | 轨道 | 提交 | 改动 |
|---|---|---|---|
| 14:36 | vrb+iter | a8b9b98 | League-192 工具封存（退出码/席位变体/冻结钉/回归 14+16）+ M5 同池对照混合 + 收据块 |
| 14:43 | vrb+iter | 48deb4e | 清理冲突标记残留行 |
| 14:46 | vrb+iter | 06f3dcd | analyze_league192 聚合脚本入库 |
| 14:47 | ANALYSIS | 4a8e6ed | docs/52 League-192 收批分析（四混合聚合/二进制完整性/AI-502 告警/stage2 证据基线） |
| 18:30 | iter | b2efc30 | ChatGPT 答复 eef40e9 三问（M5 公平性、frontier 门控隔离、R2 分母） |
| 18:46 | vrb+iter | cdaac11 | analyze_league192 v3（argv 数据目录、M5 条目、空混合防护） |
| 18:46 | iter | c9f2247 | 答复 EFF40-RESPONSE 三问（M5 回执与批次事实修正、frontier 三层 hunk 采纳、R2=120 采纳） |
| 18:47 | ANALYSIS | 1675afc | 同文：答复 EFF40-RESPONSE 三问 |
| 18:54 | ANALYSIS | eabd26d | docs/54 策略·算法·参数总清单（技术报告底稿，50 项参数全表） |
| 18:59 | iter | f57fde1 | ChatGPT：audit c9f2247 来源、D300/D500 引擎漂移、arena 保真度 |
| 19:17 | vrb / iter / ANALYSIS | 8b78c9c / 38666ec / 8fea54e | 答复 C9F2247-CODE-AUDIT 九项（AUD-01 黑箱 768/768、AUD-05 反例排队、AUD-06 三层二分等） |
| 19:55 | iter | e345b9d | ChatGPT：地图尺寸域偏移、50 参数、资源时序审计 |

### 1.4 10-30 傍晚–深夜：formal-size 夹具、逐决策审计、merge、收尾

| 时间 | 轨道 | 提交 | 改动 |
|---|---|---|---|
| 19:57–20:01 | vrb（16731cd/fb9d9d4/c187e2e/56af408/69a6ae3/e3aa04f/3a18f57/4f02dd0/8dfe03b/8f088fb）与 iter 同文副本（9cdce99/e135fcf/c7bbbc2/2c14bd1/8a10074/97eb463/089312f/246e244/5825d75/d89ff80） | practice1（20×20）/practice2（24×24）正式尺寸场景、formal_practice_check.py、run.sh、地图族生成器、配置静态校验（PASS） |
| 20:02 | iter | f7721fd | ChatGPT：formal-size 交接与 98 点训练标准 |
| 20:11 | iter | 5e13efe | ChatGPT：资源优先经济与可证伪 24×24 测试引导 |
| 20:22 | vrb / iter | 5cf8b25 / de38f68 | 冠军死亡与资源权衡的逐 tick 2-5 回溯检查器 |
| 20:23–20:25 | log | f595a9c/dc99d4d/18ceb79/67716e5/4675833/c97834c/b988ac5/93d3a1c | L01-L12、P01-P16 每 tick 决策归档与 2-5 tick 死亡窗口 |
| 20:27 | vrb / iter | 4f083a7 / 8e0130c | 缺失 tick 动作作为显式证据缺口保留（不中止） |
| 20:29 | ANALYSIS | 30fa694 | ChatGPT：docs/55 28 局 14000 tick、222 死亡、2-5 tick 逃脱窗口审计 |
| 20:31 | iter | 59b47a1 | ChatGPT：relay 28 局 14k tick 审计与因果重放计划 |
| 20:47 | log | e106f80/d1d5782/b87b8a5 | 归档 league-192 全部 48 局日志、M5 前 24 局、ChatGPT 离线恢复包 |
| 20:55 | iter | 6d32fca | ChatGPT：follow up c9f2247 可复现评分证据 |
| 21:00 | log | 2dffdcb | 归档 M5 seeds 07-08（M5B 停于 08，09-12 未跑） |
| 21:17–21:21 | iter | 295bf5f/ebf900f/852224f/42b81f8 | ChatGPT：audit_league_horizons.py 全 Tick M1/M5 台账、M5 30 配对局解读、111k-Tick 覆盖声明 |
| 21:28 | iter | e7c4c62 | **merge vrb→iterate-arena**（用户指令，覆盖旧单向拓扑；5 冲突取 iterate-arena 探针修复版；review.md 逐字一致转 CRLF；key 不入库） |
| 21:30 | iter | 7c9813c | merge ChatGPT 4 审计提交（review.md 并集，新块 CG-C-20261030-LOGHEAD-2DFF-M5-30GAMES 转 CRLF 追加） |
| 深夜 | vrb | （历史清理） | baaf97e（含临时 key 的提交）reset 移除 + force-push → vrb tip 4f083a7；key-free 重建 BUILD_EXIT=0 |

## 2. 每一次比赛 → 提交链接对照总表

「我方席位」= 该批次焦点席位（我方模型）；「对手席位」= 同场其余席位。二进制 SHA256 全文见 §3。

| # | 批次（时间 / 局数） | 我方席位（源码提交 → 二进制） | 对手席位（源码提交 → 二进制） | 数据位置 | 结果与文档 |
|---|---|---|---|---|---|
| 1 | **pilot-new 16 局**（10-29 19:26–20:31；M1×2 图 + M2×2 图，前 8 局在 20:00 前） | champion `eb321df` → `39557aa1…` | 原版陪练 `3c352b3f`（服务器内置） | `~/cst/build/practice-league/pilot-new/`（combined_16.json）；归档 log `73c2f96` | docs/45（ANALYSIS `871d879`，T11 全表） |
| 2 | **scale-96 partial**（10-29 ~20:40–21:39；12/96 局，M1×01-03） | champion `eb321df` → `39557aa1…`（位元钉） | 原版陪练池 | 归档 log `d0a80d1`（12 session 10 件套 + league_summary + aggregate.out） | 均分 43.9583 / rank1 6/12 无晋升信号；21:39 批内改头触发 sha256 护栏中止 21 组（无污染对局）→ docs/47（`ba6a598`） |
| 3 | **r2_compare 第一~八轮 + r2_divergence + r2_run**（10-29 21:03–23:10；离线自建引擎，非 practice 裁判） | new `8da0edec` → `63a99c56…` | old `65c87145` → `07f2a732…` | `~/cst/build/league/r2_*`；归档 log `021ae79`（1-5 轮 73 报告）+ `e90a8b4`（6-8 轮 11 报告） | snake +20 = etr0+pcc0 或 probe 开启组合；M3 冻结 old7_no_etr0 → docs/46（`231fe1e`） |
| 4 | **ablate9 第九轮四格消融**（10-29 ~23:4x） | new `8da0edec` → `63a99c56…` | old `65c87145` → `07f2a732…` | 归档 log `aa75811`（12 份报告 + receipt_bitwise） | tdc 死参数 6/6 逐位实证 → M3 五参数冻结依据 → docs/48 §2.2（`f1675c8`） |
| 5 | **league-192**（10-29 23:27:50 – 10-30 13:51:20；192 局 = 12 图 × 4 席位 × 4 混合，退出码 0） | M1A/M2A/M3A champion `eb321df` → `39557aa1…`；M4A candidate `38b5d09` → `d76489d8…` | M1 原版 `3c352b3f`；M2B old_champion `9bc72a7` → `bcebb860…`；M3B candidate-B `38b5d09` → `dd77411f…`；M4B champion-B `eb321df` → `98aec3f3…` | `~/cst/build/league/league-192/`；归档 log `e106f80` | M1 +0.16（22/48）/ M2 **+2.77（26/48）** / M3 +0.68 / M4 +2.76；AI 3640/3640 全败 → docs/52（`4a8e6ed`） |
| 6 | **M5A 首批**（10-30 14:40 – 18:15:33；48/48 完成） | candidate-A `38b5d09` → `d76489d8…` | 原版陪练池（与 M1 同池同图，config_sha256 配对） | ❌ 18:33 被 M5-owner 子代理 kill_m5.sh 误删 → 仅转录证据（§4 事故 2） | 数据已灭失；18:37 同设计重跑为数据源 |
| 7 | **M5 18:37 批**（10-30 18:37:14 – 20:25:49；24 局 = seeds 01-06；6 failed_groups = seeds 07-12 被护栏拒绝） | candidate-A `38b5d09` → `d76489d8…` | 原版陪练池（同 M1 池；M1/M5 同图 config_sha256 一致，如 seed01 均 `d81e0746…`） | `~/cst/build/league/league-m5/`（league_summary_24games.json）；归档 log `d1d5782` | 前 24 局：A 均分 45.35、13 次第一、R65.0 / D726.8 / M2.83；记录修正 → iter `c9f2247` / ANALYSIS `1675afc` |
| 8 | **case-0 现场取证**（10-30 20:07–20:12；M5 seed06 case-0-bsgzugk1） | candidate-A `d76489d8…`（同批 7） | 原版池（C 43.5 / D 895 击杀奖励） | session `practice-8b14720ffd6b43258aff6269520394b1`；config `fce12fa1…` | A 49.0 胜、7 死；「只补刀不追击」、40→20→0 火线死亡模式、D 895 击杀奖励倒扣（AUD-05 反例）→ 两轮解读回执待发（§5） |
| 9 | **M5B 补跑**（10-30 20:30:26 – 21:05:34；8 局 = seeds 07-08；**21:00 用户停赛指令 → 09-12 未跑**） | candidate-A `38b5d09` → `d76489d8…` | 原版陪练池（同上） | `~/cst/build/league/league-m5/summary_M5_202612{07,08}/`；归档 log `2dffdcb` | 库中共 **32 局**（seeds 01-08）；ChatGPT 已按 30 配对局解读（iter `ebf900f`：M5−M1 均分 +1.275 / R +3.6667 / D −418.27，122 次 DEFEND→ATTACK 切换） |
| 10 | **AI 调用口径（全窗口联赛批次）** | 同各批焦点席位（champion `eb321df` / candidate `38b5d09` 的 match_config.hpp **提交态空串**） | — | league-192：M1-M3 各 960、M4 760 = **3640/3640 全败**；M5 各局 ~29×4 全败 | 机制：practice_launcher setenv 覆盖 + practice.py:450 502 映射（docs/52 §5）；**勘误（10-30 深夜）：练习档案另有 5912 次真实 200 调用，见 §5.4** |

## 3. 席位冻结契约全表（tools/versions.json + docs/52 §1）

| 席位 | 源码提交（全文） | 二进制 SHA256（全文） | 参数 digest（前 16） | install_base |
|---|---|---|---|---|
| champion（A） | `eb321df03d46d8e05fe7ccc762a76389a4111a88` | `39557aa16d75fb07a2cae950efe549c4ae13d5625cc671a3440a4513ed399052` | `b1efdbc4d869a53c` | `~/cst/install` |
| champion-B | `eb321df03d46d8e05fe7ccc762a76389a4111a88` | `98aec3f3c423d3705caade2e7775803d2cf65dac0db6e624f816f8314cb7e843` | `5df1b3515a7597d3`（original_params=`b1efdbc4…`） | `~/cst-champion-eb321df/install-v-champion-B` |
| old_champion-B | `9bc72a7521beddc1c05994d3590b1958b242d84b` | `bcebb860ae2a0d62f2bacbe336544acd43ea330b4ba6479ff6a81cbb8239bf1e` | `d9cd2a2fb425e857` | `~/cst-league-old/install-v-old_champion-B` |
| candidate-A | `38b5d09b9742642e6cc0f24f4ea9724007dbe1b4` | `d76489d8a929b97749e78f95b1ab9a09eda9a0062e489455e469729ae9946c1e` | `903ec32b9b1d4f40`（original=`33ac5ca9…`） | `~/cst/install-v-candidate-A` |
| candidate-B | `38b5d09b9742642e6cc0f24f4ea9724007dbe1b4` | `dd77411fa18e29d5c05bc1cc3754de1183583a302f9b77047d53fcfb825f513d` | `bca6f974b5be9b36`（original=`33ac5ca9…`） | `~/cst/install-v-candidate-B` |
| 原版（陪练池） | `3c352b3f`（官方原版机器人 practice 树，服务器内置；docs/52 §6） | 服务器内置 | — | 服务器内置 |
| r2 离线 new | `8da0edecf59218647c83a19536da1c822cbcfd0d` | `63a99c566907a6160b70bf60da31f8ddb9cb1e18906745b200013abedf3da3a6` | — | `~/cst/build/league/versions/new` |
| r2 离线 old | `65c87145ae3b15572c3b1674181a74677fe86770` | `07f2a7322dcce682a3463dcf9d22ba7a39a358a3e699e685f9efca1871e80d07` | — | `~/cst/build/league/versions/old` |

candidate = `38b5d09`（eb321df + 行为中性改动 `3a37703`）+ old7_no_etr0 五参数覆盖（docs/46 §6，tdc 死参数剔除）。league-192 每局另有 config_sha256（逐局配对，audit_league_horizons 已生成 M1/M5 配对表）。

## 4. 事故与处置（按时间）

1. **10-29 21:39 scale-96 护栏中止**：批内改头触发 practice_batch.sh 的 sha256 护栏，中止 21 组，无污染对局 → docs/47（`ba6a598`）。护栏为设计内行为。
2. **10-30 18:33 M5A 首批误删**：M5-owner 子代理为「正式前后记录」运行 kill_m5.sh 清空输出，再启动同设计 18:37 批。处置：保留 18:37 批为数据源；kill_m5.sh 中和为 no-op；代理切 wait-only 守望；教训「联赛类子代理 prompt 必须禁止 kill/清理/重启」→ iter `c9f2247` / ANALYSIS `1675afc` 已修正记录。
3. **10-30 20:08 key 临时写入 → 护栏拒绝**：为 AI-real 验证把临时 key 写入 match_config.hpp，哈希护栏按设计拒绝 seeds 07-12 启动（24/48 收批）。20:30 还原（git checkout，哈希复核 OK 无需重建）并补跑 M5B。
4. **10-30 21:00 用户停赛**：M5B 收于 seed 08（4/4 完成后停止），09-12 未跑；库中共 32 局。league_summary 仍称 24/48（未更新，事实以 §2 表 7/9 为准）。
5. **10-30 21:2x 用户撤销写死授权（「AI key+proxy 不可以提交」）**：vrb 的 baaf97e（含临时 key 的提交）reset 移除 + force-with-lease 强推（vrb tip = 4f083a7）；iterate-arena 合并重做为 key-free（e7c4c62 + 7c9813c，已推）。全仓复扫 0 处真实 `sk-` 密钥。key-free 重建 BUILD_EXIT=0。

## 5. 收尾状态与未决事项

### 5.1 四轨 HEAD 与推送状态（2026-10-30 21:41）

| 轨道 | HEAD | 推送 |
|---|---|---|
| code vrb | `4f083a7`（audit: missing tick evidence gaps） | ✅ origin 已推（baaf97e 已从远端移除） |
| code iterate-arena | `7c9813c`（merge ChatGPT 4 审计提交） | ✅ origin 已推 |
| doc ANALYSIS | `30fa694`（docs/55 14000 决策审计） | ✅ origin 已推；本文件 docs/56 随收尾提交推送 |
| doc log | `2dffdcb`（M5 seeds 07-08 归档） | ✅ origin 已推 |

### 5.2 诚实声明（技术报告必须包含）

- **联赛批次 LLM 精化路径未生效（口径已勘误，见 §5.4）**：全窗口联赛批次 3640/3640（league-192）+ M5 各局全 502；联赛批次证据度量的是**规则引擎路径**。
- **真实 AI 调用已有练习实据（勘误见 §5.4）**：10-30 20:0x 的临时 key 验证被哈希护栏拦截后即撤销授权；AI 路线回退为 **llm.env 环境变量优先、代码恒空串、key 不入库**，赛前由席位环境注入。正式赛的席位令牌链路仍需现场验证（deepseek-flash / max_tokens 512 / Bearer 席位令牌）。

### 5.3 未决事项清单（按优先级）

1. **docs/53**：M5 32 局（seeds 01-08）同口径收批分析（M5 vs M1 同池同席位净效应裁定）。
2. **两轮解读回执**（review.md 两仓同文）：case-0 战斗取证（§2 表 8）+ 全审计解读——用户 10-30 大审计指令的六项逐项答复。
3. **10-31 20:00 材料提交**：语雀技术报告（含 AI 协同开发与测试截图、§5.2 声明）、前置检录截图、docs/02 手册事实更新、ai_max_tokens 2200→512 决策。
4. wide_lanes 门控 hunk 二分（48bdca8 优先，独立快照，评测图含 maze/spiral）。
5. CHASE 真实墙角失败提取（docs/49，需 Frank 实际失败局记录）。
6. 复杂图三实验立项（race_reach_holdoff / low_hp_attack_discount 0.3~0.5 / 高值早期竞速；均行为类默认关）。
7. AI-real 小批次验证（llm.env 路线，赛前席位环境）。

### 5.4 勘误（2026-10-30 深夜，观赛量化）：练习档案真实 AI 调用记录

§2 表 10 与 §5.2 原「历史抽查 0/200」「真实 AI 调用未经练习验证」口径**有误**——抽查只看 bot 日志（空 key 时代样本），未核对练习代理侧的 ai.jsonl。全库复核（`/home/frank/.rmtc-practice/`，419 会话、382 份 ai.jsonl，字段 `mode/status/success/success_count/attempt_count`，success 与 status 逐条一致）：

- **90 个会话含 real 模式 HTTP 200 共 5912 次**（10-28 21:21～10-29 21:51）；82 个会话同时含 200/502 记录；四席 A/B/C/D 均有真实成功记录（如 329a6c19：A85/B10/C10/D12）；
- 含 EVENT_USE 两局真实对局：dfcef97 45 分第一（A 席 26/26 成功）、178b15 55 分第一（A 席 29/29 成功）——docs/implementation/EVENT_USE 的「HTTP 26/0」「29/0」即 A 席口径；
- 另有 6 个早期会话（10-25 起）200 条 **mock 模式**记录，非真实调用，不计入；
- 全库其余 26594 条 502 集中在 10-29 22:00 后的空 key 联赛批次（league-192 3640/3640、M5/M5B 等）——**联赛批次全 502 的口径本身成立**。

结论修正：练习历史并非 0/200——真实统一 AI 调用有 5912 次实据（10-28～10-29 21:51，含两场真实对局完赛）；「练习证据=规则引擎路径」口径仅适用于 10-29 22:00 后的联赛批次。技术报告口径已同步修正（docs/57 §5/§7/§9）。

## 6. 验证命令

- 四轨时间线：`git log --since="2026-10-29T20:00:00+08:00" --date=iso-strict --pretty=format:"%h %ad %s" --reverse`（vrb / iterate-arena / ANALYSIS / log 各自执行）。
- 席位冻结复验：`cd ~/cst && python3 -m unittest tests.practice_tools_test` → 16 tests OK。
- 二进制钉复验：`cd ~/cst && python3 tools/analyze_league192.py`（§3 表钉分布逐格 48/48）。
- key 扫描（声明口径）：提交内容含「密钥扫描通过」者均经全量扫描，当前两分支无真实 key；历史残留已随 baaf97e 移除。
