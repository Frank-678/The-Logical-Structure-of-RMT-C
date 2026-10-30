# 52 · League-192 收批：四混合聚合、二进制完整性证明与 stage2 证据基线

- 身份：DeepSeek
- 时间：2026-10-30 15:05 +0800
- 关联：docs/48（M3 冻结与预注册）、docs/44（16 局试点）、docs/46（R2 离线矩阵）、docs/51（日志诊断）
- 数据：`~/cst/build/league/league-192/`（league_summary.json + 48 × summary_M{mix}_{map}.json + .runs/ 逐局原始）
- 聚合脚本：`tools/analyze_league192.py`（代码仓 vrb 06f3dcd 入库，命令 `cd ~/cst && python3 tools/analyze_league192.py`）

## 1. 批次完整性

- 批次 bslvga5yp：12 图 × 4 席位 × 4 混合 = 192 局。2026-10-29 23:27:50 开跑，2026-10-30 13:51:20 收批，退出码 0。
- planned / completed / returned / failed = **192 / 192 / 192 / 0**；invalid 0（按标签全 0）。
- referee 启动失败自动恢复 8 次（既有重试机制，回归 `test_referee_ready_requires_new_line_per_attempt` 覆盖）。
- 冻结契约（U6）：`verify_frozen` 五二进制全过；钉分布逐格精确（各 48/48）：
  - M1 A / M2 A / M3 A = champion `39557aa16d75`（install 在位钉，sha=eb321df）
  - M2 B = old_champion `bcebb860ae2a`（sha=9bc72a7）
  - M3 B = candidate-B `dd77411fa18e`（sha=38b5d09）
  - M4 A = candidate-A `d76489d8a929`（sha=38b5d09）
  - M4 B = champion-B `98aec3f3c423`（sha=eb321df，original_params=b1efdbc4…）
- 焦点席位 48/48 全部为 A（docs/48 口径）；M3/M4 参战候选 = 五参数版本 38b5d09（mev2.0/pcc0/rmb4/rmv4/grb0.1，tdc 已按 docs/48 §2.2 死参数证据剔除）。

## 2. 四混合聚合（docs/48 §5 口径）

| 混合 | 焦点 | 对手 | 焦点均分 | 对手均分 | Δ | 单局胜过 | 均名次 | rank1% | R | D | M |
|---|---|---|---|---|---|---|---|---|---|---|---|
| M1 基线 | champion | 原版陪练（每局三陪练取最高） | 43.96 | 43.80 | +0.16 | 22/48（平5） | 1.75 | 54% | 61.0 | 1168.6 | 2.8 |
| M2 自战 | champion | old_champion | 44.22 | 41.45 | **+2.77** | **26/48**（平7） | 1.98 | 46% | 60.2 | 1262.6 | 2.8 |
| M3 对手位 | champion | candidate | 43.49 | 42.81 | +0.68 | 22/48（平7） | 2.08 | 42% | 58.1 | 1281.5 | 2.8 |
| M4 焦点位 | candidate | champion | 43.96 | 41.20 | +2.76 | 25/48（平7） | 2.23 | 38% | 60.0 | 828.3 | 2.8 |

- 计分口径 30·min(R/120,1)+15·min(D/500,1)+5·len(completed)（docs/48 §5）。R 全域 58–61/120、D 全域 828–1282（15 分封顶）、M 恒 2.8/3：**四席同场下 RV 是唯一分层变量**，与 docs/51 的 RV 经济学诊断一致。
- **席位效应**（同模型跨席，n=48）：champion A−B = 43.49−41.20 = **+2.29**；candidate A−B = 43.96−42.81 = **+1.15**。A 席优势约 +1.2~2.3。因此 **M4−M1 差值不得作候选增益估计**（docs/48 §5 明令）；同池对照由 **M5** 承担，已于 2026-10-30 14:40 开跑（12 图 48 局，`--mixes M5 --out build/league/league-m5`，预计 18:00 前后收批，分析入 docs/53）。
- rank4 共 **24 局**：M1 4 / M2 5 / M3 6 / M4 9（全部焦点席 A；逐局名单见脚本输出）。M4 的 rank4 最多（9/48）与其 D 828.3 最低相互印证：候选焦点位对池中两席模型的对抗中输出伤害最低。

### 每图×每 mix 焦点均分 / 均名次

| map | M1 | M2 | M3 | M4 |
|---|---|---|---|---|
| 20261201 | 43.12 / r2.0 | 42.50 / r1.8 | 43.75 / r2.0 | 42.50 / r3.2 |
| 20261202 | 52.50 / r1.0 | 46.25 / r1.5 | 43.75 / r1.5 | 43.75 / r1.5 |
| 20261203 | 44.38 / r1.0 | 43.75 / r2.0 | 43.75 / r2.2 | 43.75 / r2.0 |
| 20261204 | 38.12 / r2.5 | 41.88 / r1.8 | 39.38 / r2.5 | 40.62 / r2.5 |
| 20261205 | 45.65 / r1.5 | 47.50 / r1.8 | 45.62 / r2.0 | 46.88 / r1.8 |
| 20261206 | 41.25 / r2.0 | 43.75 / r2.0 | 41.88 / r2.0 | 44.38 / r2.2 |
| 20261207 | 39.38 / r2.2 | 45.62 / r2.0 | 45.62 / r2.0 | 43.12 / r2.0 |
| 20261208 | 43.12 / r2.0 | 45.62 / r2.5 | 45.62 / r2.5 | 45.62 / r2.5 |
| 20261209 | 48.12 / r1.5 | 45.62 / r1.5 | 46.25 / r1.5 | 46.25 / r1.8 |
| 20261210 | 48.12 / r1.0 | 40.00 / r2.5 | 42.50 / r2.0 | 41.25 / r2.5 |
| 20261211 | 40.62 / r2.5 | 42.50 / r2.5 | 40.00 / r2.8 | 42.50 / r2.8 |
| 20261212 | 43.12 / r1.8 | 45.62 / r2.0 | 43.75 / r2.0 | 46.88 / r2.0 |

## 3. 与 docs/44 旧试点交叉验证

| 证据 | 试点（docs/44，8 局 2 图） | League-192（48 局 12 图） |
|---|---|---|
| M2 自战 champion vs old_champion | 44.6875 vs 44.6875；4 胜 2 负 2 平；总分差 0；bootstrap 95% CI [−4.06, +3.75] → **无晋升主张** | 44.22 vs 41.45；**Δ+2.77；26/48 胜过**（平 7） |

样本从 8 局扩大到 48 局后，champion 对 old_champion 由试点平局转为**稳定正差**：26/48 单局胜过、均分差 +2.77。试点 CI 跨 0 的结论按其自身样本成立（docs/44 裁决不变），本批为其后续扩展证据。old_champion 席位定义两批一致（9bc72a7，二进制 bcebb860ae2a 冻结）。

M1 试点 8 局 47.1875（仅 20261201/02 两图）与本批 12 图 43.96 地图集不同，不作数值比较。

## 4. 二进制完整性证明（M4 的 champion-B 对手席位契约合规）

1. **四钉复验**：收批后对五参战二进制逐一 sha256，全部与 tools/versions.json 冻结钉一致。
2. **champion/B 清单**：install-v-champion-B/frozen.json 记录 20 个源文件逐一与 eb321df 树比对，**20/20 一致**，仅 match_config.hpp 席位烘焙（[BAKED]）；original_params_sha256 = `b1efdbc4d869a53c` = sha256(eb321df match_config.hpp) = champion params_digest。
3. **candidate A/B**：20/20 与 38b5d09 一致（original_params=33ac5ca9=sha256(38b5d09 match_config.hpp)）。
4. **champion A vs B 逐字节分析**：.text 差异 3285 字节 = 1659 处 RIP 相对位移立即数，全部 ≤3 字节、全部正向平移（1588 处恰为 +288，其余 35–248），**零指令差异** → 同一程序，仅字符串布局平移（B .rodata 180288 vs A 180000 字节）。
5. **编译身份**：两者均 -O0；A 实际编译于 2026-10-29 15:57:26（.rodata __TIME__），晚于 eb321df 提交（10-29 12:09）→ 早前"二进制早于提交 3.5 天"疑虑解除（10-25 21:33 的 mtime 是 cp 保留伪影）。

结论：M2/M4 的 champion-B 席位与其 A 席位是同一 eb321df 程序，仅席位/团队字段烘焙差异；候选席位为 38b5d09（eb321df + 4 项行为中性改动 3a37703）。全部对比有效。

## 5. AI 调用告警（练习证据的重大 caveat，如实声明）

- 本批 **3640/3640 次 AI 调用全部失败**（M1–M3 各 960、M4 760），bot 日志每 tick `ai=http_502 http_success=0`；**联赛批次口径成立，但「历史抽查 0/200」「LLM 精化路径从未实际生效」表述有误——勘误见文末 §8**。全部联赛批次练习证据（docs/44/46/48 及本批）度量的是规则引擎路径。
- 机制（已逐环实证）：
  1. practice_launcher.cpp 对 stage2 强制 real 模式，并把 match_config.hpp 的 practice_llm_key（**提交态为空串**，按"用后即还原并重建、绝不提交"纪律）以覆盖方式写入环境；
  2. 原版代理 practice.py forward_ai 直连上游，携带 `Authorization: Bearer `（空）；
  3. 上游返回 401 纯文本（"Authentication Fails (auth header format should be Bearer sk-...)"，content-type 空，无重定向——2026-10-30 实测）；
  4. 代理 `response.json()` 抛 ValueError → 映射 502「上游模型调用失败」（practice.py:450；重定向分支 :446）。
- 上游网络本身可达（2026-10-30 实测直连 401 即证明链路通）。根因是**配置层**（空 key），非网络/接口。
- 对 stage2 的影响：官方赛 AI 调用为官方端点 + 席位令牌（手册事实：deepseek-flash / max_tokens 512 / Bearer 席位令牌），与练习配置不同；「模型调用成功时」的行为在练习档案中已有实据（90 会话 5912 次真实 200，含 EVENT_USE 两局完赛——勘误见文末 §8），技术报告按勘误口径声明。
- 修复路线（联赛后、诊断/工具类，行为类默认关）：practice_launcher 环境变量优先（setenv 覆盖=0）→ 密钥置于 ~/.rmtc-practice/llm.env（不入库）→ `--check-ai` 单次验证 → 重建席位变体 + 重新冻结钉 → 小批次 AI-real 验证 http_success>0，之后 AI 行为证据才成立。

## 6. stage2 证据满足性

- **与原版比拼**：M1 48 局，同场三原版陪练（官方原版机器人 practice 树 3c352b3f，服务器内置）——满足手册"与原版的一局"且远多于要求。
- **与自己的其他模型比拼**：M2 champion vs old_champion 48 局（Δ+2.77、26/48）+ M3/M4 候选成对 96 局（无晋升主张，待 M5 同池裁定）——满足"和自己的其他模型比拼"。
- 全部在 0 invalid、冻结契约逐格验证、焦点席位固定的条件下成立。

## 7. 下一步（联赛后队列，顺序执行）

1. **M5 同池对照**（运行中）：收批后按同口径分析 → docs/53；M5 vs M1 同池同席位比较给出候选（五参数）对原版陪练池的净效应裁定。
2. wide_lanes 门控 hunk 二分（48bdca8 优先，独立快照口径按 docs/50；含 maze/spiral 图）。
3. CHASE 真实墙角失败提取（docs/49，需 Frank 实际失败局记录）。
4. 复杂地图三实验（race_reach_holdoff / low_hp_attack_discount 0.3~0.5 / high-value early racing，全部默认关）。
5. original_ros_diff 适配器实跑（c416ecd 身份）。
6. AI 上游修复（§5 路线）→ AI-real 小批次验证。
7. 10-31 20:00 材料提交：语雀技术报告（含 AI 协同开发与测试截图）、前置检录截图、max_tokens 512/2200 决策、docs/02 手册事实更新。

## 验证命令

- 聚合：`cd ~/cst && python3 tools/analyze_league192.py`（本表全部数值来源）
- 冻结复验：`cd ~/cst && python3 -m unittest tests.practice_tools_test` → 16 tests OK（R2 1→1 / R3 空格 / R4 入口注入 / 批次退出码 / Ready 逐次基线）
- 上游连通性（无 key 探测，不读 key）：`curl -sS -X POST https://api.deepseek.com/chat/completions -H 'Authorization: Bearer ' -d '{...}'` → 401 纯文本
- 二进制比对：objcopy 逐段抽取 + chk_disp.py 位移分类（1659 处全部正向平移、零指令差异）

## 8. 勘误（2026-10-30 深夜，观赛量化）

§5 的「历史抽查 0/200」「模型调用成功时的行为未经练习验证」**不成立**：抽查只覆盖 bot 日志且多为空 key 时代样本，未核对练习代理侧的 ai.jsonl。全库复核（`/home/frank/.rmtc-practice/`，419 会话、382 份 ai.jsonl，success 与 status 逐条一致）：

- **90 个会话 real 模式 HTTP 200 共 5912 次**（10-28 21:21～10-29 21:51；82 个会话同时含 200/502 记录；四席 A/B/C/D 均有真实成功记录）；
- 含 EVENT_USE 真实对局 dfcef97（45 分第一，A 席 26/26）与 178b15（55 分第一，A 席 29/29）；
- 6 个早期会话 200 条 mock 模式记录（非真实调用，不计入）；
- 其余 26594 条 502 集中在 10-29 22:00 后空 key 联赛批次——**本批 3640/3640 全败口径不变**。

修正结论：练习历史有 5912 次真实统一 AI 调用实据；「练习证据=规则引擎路径」仅适用于 10-29 22:00 后的联赛批次。技术报告（docs/57）已按此修正。
