# 首场真实 LLM 对局：设置、流水线、词表映射与第 3 名复盘

更新：2026-10-29。首场真实 LLM 练习对局（session `practice-15465a23820b43d0b277d0f1de7fc655`，stage 2）的完整复盘。数据源为本场练习会话目录（WSL `/home/frank/.rmtc-practice/practice-15465a23820b43d0b277d0f1de7fc655/`）的 score.json（831 行）、frames.jsonl（500 行，行号 = tick）、ai.jsonl（65 行）、communication.jsonl（3971 行）、config.json（425 行）、referee/simulator/scoring/bot 日志，以及 A 席机器人 stdout（`D:\Claude\Temp\claude\D--\550521f2-3d9a-4261-a14e-48ec7be38b55\tasks\b6dyckka3.output`，505 行，tick 行号 = 行号−3；工作树内有同名会话镜像 `practice-15465a23820b43d0b277d0f1de7fc655/bot_A.log`，行号同口径）。全部数字均在本场数据中逐项复算（WSL python3 只读解析）；无法确认的项集中列入第 8 节。单局样本：所有策略修复建议均为假设，标"待测试"，批量对局验证前不改集中参数默认值。

## 1 实验设置

### 1.1 对局与配置

- session：`practice-15465a23820b43d0b277d0f1de7fc655`（score.json 行 18）；stage 2（config.json 行 2）；18×18 四队（config.json 行 57-59 width/height=18；simulator.log 行 1 "simulator ready: 18x18, 4 teams"）；500 tick 完整打完（referee.log 行 5 "match completed at tick 500"；score.json 行 830 `"tick": 500`）；节奏约 500ms/tick（bot stdout 行 3→4 时间戳差 0.506s）。
- 席位与身份：A=Frank（我方机器人，bot stdout 行 1 "seat=A name=Frank"；score.json 行 734 起 team_registry）；B/C/D=原版练习陪练（team_registry 同处；bot_B.log 行 2 `rmtc_test_robot`，AI plan applied goals=[resource_normal,resource_high,reach_target]——本地策略陪练）。出生点 A [1,1]、B [16,1]、C [1,16]、D [16,16]（config.json 行 10/17/24/31）。
- 任务：收集 2 普通 + 1 高价值资源、到达 [9,9]（config.json 行 37 起 missions；score.json 行 731 mission_text）。vision_radius=4、respawn_wait=3、spawn_protection=2（config.json 行 3-5）。
- 模型链路：机器人 AI 配置 model=deepseek-flash、timeout_ms=35000、connect_timeout_ms=5000、max_tokens=2200、thinking=disabled、json_output=1（bot stdout 行 2）；ai.jsonl 65 条全部 `mode: "real"`（ai.jsonl 行 1 起逐条，全文件一致）→ 本局经练习代理转发的都是真实模型请求、非 mock。练习代理与正式网关的时延、配额与默认超时不同，本局延迟分布不可外推（docs/19 第 5 节）。

### 1.2 八事件日程

config.json `events.schedule`（行 382 起；announce_tick 位于行 386/391/396/401/406/411/416/421）；`events` 键起于行 217，其中 enabled=true、announcement_count=8、announcement_delay_ticks=5、base_attack_damage=20、base_defended_damage=10、max_hp=100。开始/结束 tick 取自 score.json `arena_events.announcements` 36 条公告的 start_tick/end_tick 字段（行 103-431），与公告 tick+5 完全一致。

| 事件 | 公告 tick（config 行） | 开始 | 结束 | 关键参数（config.json events.definitions） |
| --- | ---: | ---: | ---: | --- |
| 爆炸 explosion | 10（行 386） | 15 | 16 | 矩形 [3,3]-[7,7]，35 HP（行 233 damage、行 235 rect） |
| 幻术 illusion | 40（行 391） | 45 | 46 | 矩形 [8,3]-[12,7]，12 tick 反向移动（行 255 effect_ticks、行 256 rect） |
| 天使恩泽 angel | 70（行 396） | 75 | 91 | 点位 [[3,9],[14,9]]，8 tick 每 tick +5（行 279 effect_ticks、行 280 heal_per_tick、行 282 points） |
| 天下无双 unrivaled | 100（行 401） | 105 | 129 | 中央 3×3 堡垒，驻留 4 tick，攻击 35 / 防御 7（行 306 stay_ticks、行 308 attack_damage） |
| 世界分裂 world_split | 130（行 406） | 135 | 145 | 交点 [8,8] 十字障碍、线上即死（行 322 point） |
| 火爆辣椒 pepper | 160（行 411） | 165 | 181 | 点位 [[5,6],[12,11]]，火线 30 HP（行 336 points、行 346 damage） |
| 洁身自好 purity | 190（行 416） | 195 | 211 | 攻击防御目标反伤 12（行 359 reflection_damage） |
| 潘潘的神 pan | 220（行 421） | 225 | 243 | 移动窗口 10 tick、易伤 ×2（行 369 movement_window_ticks、行 371 damage_multiplier） |

A 席公告感知：event_text 首次非空于感知 tick 10（communication.jsonl 行 81），末次非空于感知 tick 500（行 3966/3968/3970，各含 36 行公告、无缺失）；预告类 8 条与公告 tick 同 tick 到达，生效/结束/增益类 28 条晚 1 tick 到达（实测规律；机制因果未验证，见第 8 节）。

## 2 结果表

| 席位 | 身份 | R | D(ed) | M | 平台分（score 字段） | 官方公式分 | 终局 hp | invalid_actions | 死亡次数 | 名次 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| A | Frank（我方） | 40 | 845 | 3 | 40.0 | 40.0 | 100 | 0 | 12 | 3 |
| B | 练习陪练B | 60 | 190 | 3 | 35.7 | 35.7 | 20 | 0 | 4 | 4 |
| C | 练习陪练C | 40 | 1128 | 3 | 40.0 | 40.0 | 100 | 0 | 9 | 2 |
| D | 练习陪练D | 60 | 1205 | 3 | 45.0 | 45.0 | 20 | 0 | 7 | 1 |

出处：score.json 行 752-828 的 teams 段（D 块行 753-771：ed 行 755、hp 行 757、invalid 行 758、mc 行 759、rank 行 765、rv 行 766、score 行 768；C 块行 772-790：ed 774、hp 776、invalid 777、rank 784、score 787；A 块行 791-809：ed 793、hp 795、invalid 796、rank 803、score 806；B 块行 810-828：ed 812、hp 814、invalid 815、rank 822、score 825）；frames.jsonl 行 500 teams 同值；scoring.log 行 500 "tick 500 | D=45.00 C=40.00 A=40.00 B=35.70"。平台分 = 练习公开状态的 score 字段（frames.jsonl 行 500 teams[].score 与 score.json 一致，两口径数值相同）；官方公式分 = 30×min(R/120,1)+15×min(D/500,1)+5×M（docs/16-v1.2-rule-migration.md 行 21）复算：A=10+15+15=40.0、B=15+5.7+15=35.7、C=10+15+15=40.0、D=15+15+15=45.0，四席全部吻合。死亡次数按 frames.jsonl 逐 tick 核对（A 12：t20/43/115/186/227/252/315/368/396/435/444/486；B 4：t46/94/142/268；C 9：t24/96/166/204/241/271/390/420/476；D 7：t108/145/193/241/271/348/417）。

## 3 LLM 流水线验证

### 3.1 网关审计（ai.jsonl）

- 65 行全部解析成功；席位分布 A30/B12/C10/D13；status 200×64 + 502×1；success true×64 + false×1；mode real×65、session_id 全文件一致（ai.jsonl 逐条）。
- 修正一处口径：任务描述中"65 调用全 200"在文件层面不成立——ai.jsonl 行 37 是 seat B 的 status=502、success=false、success_count 6/attempt_count 7，为全文件唯一非 200；其余 64 条全部 200/true。
- 行 37 之后 B 的 success_count 永久比 attempt_count 少 1（行 40/47/52/61/64，sc=ac−1），是全文件仅有的 sc≠ac 记录；A/C/D 三席 sc==ac 恒成立。网关在写盘前是否对该次调用做过内部重试，ai.jsonl 无时间戳字段、每条 attempt 只留一条记录，无法判断（不确定）。
- 我方（seat A）：30 条记录全部 success=true、status=200、success_count==attempt_count；attempt_count 1→30 连续、29 个相邻差全部 +1（行 1/5/7/9/13/14/15/20/22/24/25/28/30/31/33/34/35/36/39/41/43/45/46/49/50/53/54/55/57/59）→ 记录层面无重试、无缺号。

### 3.2 客户端调用生命周期（bot stdout，行号 = tick+3）

- 30 次完成调用（started/finished 最大均为 30）；每次完成 last_result=model_reply_received（仅 tick 0-1 为启动态空值）、known_mock 恒 false、last_http 全 200（last_http=0 仅 tick 0-1 首次请求前）→ 无超时（timeout_ms=35000 未触发，行 2）。
- 延迟（elapsed_ms，按"finished 首次递增的完成行"取值，30 次）：min 438ms（call 6，tick 47，行 50）/ max 2129ms（call 16，tick 141，行 144）/ 均值 895.7 / p50 840.5 / p90 1190.4。均值/p50/p90 对取值口径敏感（较早一版抽取得 834.7/754/1174，min/max 与逐调用值一致），本文件以完成行口径为准。
- 校验异常 2 次，均为全局长耗时前两名：call 16（2129ms）→ tick 141-142 ai=invalid_model_reply（行 144-145）；call 21（1693ms）→ tick 186-187 ai=events_incomplete（行 189-190）。两次均重试后通过：call 17 于 tick 145 完成（行 148）、call 22 于 tick 190 完成（行 193）。ai 状态全程分布（行 3-503 重算）：events_validated 428 tick、requesting 65、queued 4、invalid_model_reply 2、events_incomplete 2 → seat A 除 4 个瞬态 tick 外全部 events_validated，无公告被永久忽略。"两次长耗时伴随校验失败"指向响应截断风险，但日志无截断的直接证据——待测试。
- 陪练网关：C 10 条、D 13 条全 200；B 1×502（行 37）。bot_B.log 17 条 "AI unavailable, invalid or stale" 警告 vs ai.jsonl 仅 1 次 502 → 其余警告应属 invalid/stale 或本地策略路径（推断，不确定）；bot_C.log 18 条 warn/3 条 plan applied，bot_D.log 18/2。

## 4 官方词表映射逐事件裁决

官方 8 个中文事件词（爆炸/幻术/天使恩泽/天下无双/世界分裂/火爆辣椒/洁身自好/潘潘的神）由 LLM 按系统提示中的内部词表解码为 enum（explosion/illusion/heal/fortress/split/chili/reflect/vulnerability，bot 仓库 events.hpp）。本局 8/8 词名映射全部通过、无公告被永久忽略；唯一疑点是火爆辣椒的坐标参数解码。逐事件裁决：

| 事件 | 解码通过（bot 行/tick） | 行为证据 | 裁决 |
| --- | --- | --- | --- |
| 爆炸 | t12 events_validated（行 15） | t15 A 在 [9,8] hp 100 未受伤（frames 行 15），t8-14 reason=reach_mission 行军恰好离开爆炸矩形（行 11-17）——解码通过、行为不可观测，无忽略证据 | 通过 |
| 幻术 | t43（行 46，call 5） | t45 A 已死亡且不在矩形 [8,3]-[12,7] 内（frames 行 45）→ 不适用 | 通过（不可观测） |
| 天使恩泽 | t73（行 76，call 8） | A 全程满血未入点：策略仅在 hp<healing_below_hp 时启用 seek_healing（bot 仓库 strategy.cpp L645-647，词汇验证已核对）→ 策略门限而非词汇失败；对照 D 入点得 8×5=40 回血（frames t84-91 D hp 30→70；score.json 行 180-193 id 9/10） | 通过 |
| 天下无双 | t103（行 106，call 12） | 行为铁证：t108 sent=defend reason=hold_fortress（行 111；堡垒专属分支 strategy.cpp L648-652）→ t108 获得增益（score.json 行 226-230 id 14；驻留 4 tick=config 行 306）→ t113/t115 两次 35 伤害（frames C hp 100→65→30 = config 行 308 attack_damage=35） | 通过（解码+占领+使用闭环） |
| 世界分裂 | 预告 t133（行 136，call 15）；start 批次 t141-142 首次回复被本地校验拒绝（行 144-145）→ 重试 → t145 通过（行 148） | t135-145 A 全程 x≤7、不在行 8/列 8 死亡区（frames）；t146 首次跨入列 8（事件 end 145 后 1 tick）；与 split_wall 路径过滤一致 | 通过（含一次重试） |
| 火爆辣椒 | 预告 t163（行 166，call 19）；start t167（行 170，call 20） | t166/168/171/173 reason=trigger_chili（行 169/171/174/176，chili 专属分支 strategy.cpp L654-664）→ 词名映射成功；但官方点位 [[5,6],[12,11]]（config 行 336）的火线（行 6/11、列 5/12）在决策时点无可击杀敌人（B 最后目击 t163 (17,4) hp20；D (16,5)/(16,7)/(16,10) hp30；C 已死/出生保护）→ 收益恒 0、按 L661-663 分支不应产生计划 → 解码出的点位参数偏离官方公告坐标（本地校验只核对 source 子串与字段类型、不验证坐标语义）。最终未触发（score.json 无 trigger 记录；frames t165-180 A 沿列 15-16 行动） | 词名通过；坐标参数级疑点（待测试） |
| 洁身自好 | t198（行 201，call 24） | A 窗口内零攻击（frames t194-212 A ed 冻结 455）→ 不可观测；12 反噬在 D/C 上确认（frames t198 D hp 100→88、t199 C 80→68 = config 行 359 reflection_damage=12） | 通过 |
| 潘潘的神 | t223（行 226，call 26） | A t230 复活后移动获得易伤（score.json 行 383-387 id 31），窗口内零战斗伤害 → 不可观测；×2 在 D 上确认（frames t241 C 名义 20×2 打 D 剩余 28 hp、C ed 530→558=+28） | 通过 |

## 5 排名第 3 原因分析（前三主因，按证据强度排序）

主因① tick 8 后停止采集 492 tick（证据最强、直接观测）。A 的 resource_value 序列仅 (1,10)→(4,20)→(8,40)，tick 8-500 恒 40（frames 行 1/4/8/500）；与 D 的 20 分差 = practice_9@t22 + practice_7@t30，两次采集时 A 分别是尸体躺 [9,8]（行 22，曼哈顿 5）与 [8,1]（行 30，曼哈顿 19 > vision_radius=4，config 行 3）——均非竞争所得。按公式 20 R = 5.0 分，恰为 45.0−40.0 对 D 的全部分差。

主因② t15-19 站桩对射 + t20 首死。t15 A 到 [9,8] 时 C 已占 [9,9]（frames 行 15 C [9,9]、同 tick C mission_completed=3）；5 tick 换血被杀（行 16-20 A hp 100→0；行 20 ed 80→20 净 −60 = 死亡扣减，docs/02-rulebook.md 行 17）；死亡 3 tick（config 行 4 respawn_wait）加复活赶路 16 tick，t39 才登上 [9,9]（比 C 首达晚 24 tick）；死亡窗口（t20-22）正值 B/D 扫空地图余下 7 份普通资源的时期（行 8 起 map_view.resources，B t12/15/25/33、D t12/22/30 采完），A 零参与。

主因③ 40.0 平分时输同分裁决。规则"有效伤害超过 500 的部分用于同分比较"（docs/16 行 21）：A ed 845 < C 1128（score.json 行 793/774）→ C 第 2、A 第 3。ed 赤字直接账：12 次死亡各扣 60（各死亡 tick ed 净变化 −60/−50/−25/−40×2 均与同 tick 攻击入账互洽）；且被 C/D 反复击杀刷分——C 杀 A：t20 ed 80→160、t252 638→718、t368 848→918、t444 1088→1168；D 杀 A：t186 405→485、t315 745→825、t396 815→885、t435 895→965、t486 1125→1205（frames 各行）。

纠错一条：此前对手轨迹分析称"t390 C 杀 A"与 frames 实况相反——行 390 是 A ed 685→755（+70）且 C hp 0、alive=false、C ed 978→918（净 −60，C 自己死亡）→ t390 是 A 击杀 C；行 420 同理 A 杀 C。因此 C 杀 A 实为 4 次（t20/252/368/444），A 全场击杀 9 次（t94/108/142/145/166/271/348/390/420）。

结论：对 D 输 5 分（停止采集）、对 C 输同分（ed 赤字）——三者叠加完整解释第 3 名。

## 6 发现的问题清单（A/Frank 视角；A=直接观测，B=推断待验证）

A1 任务完成后停止采集（最大失分）：t8 后 492 tick 零采集，地图余 7 份普通资源（frames 行 8）全被 B/D 拿走。
A2 站桩对射致死：12 次死亡全部落在 ≥3 tick 静止段内（frames 位置表 19 段，死亡 tick 全落在段内），死前 reason=approach_enemy 7/12，defend_lethal_threat 全程仅 6 tick；尤其 t363-371 在出生点 [1,1] 静止 9 tick 被 C 隔 2 格点死（frames 行 363-371）。
A3 无双利用率极低：t108 获得、仅 t113/115 用出 2 次 35 攻击即 t115 死亡（frames；config 行 308）。
A4 天使恩泽错过：t72-73 距点位 [14,9] 仅 1 格未入（frames），D 捡走 8×5 回血（t84-91 D hp 30→70）。
A5 不感知身后：t364-368 追 B 时被身后 C（[3,1]→[1,1]）无还手打至死（frames 行 364-368）。
A6 复生即死循环：t435 死、t438 复活于 [1,0]（出生点被 C 占、按规则位移）、t444 仅 9 tick 后再死（frames 行 438-444）。
A7 E_BLOCKED 后不撤离：t364-365 出生点撞墙（行 367-368 last_action error=E_BLOCKED）、t366 defend、t367 又 approach_enemy、t368 死（行 369-371）。
A8 长时间停滞：bot 内部 stagnant_ticks 全程 36 段、5 段 ≥17 tick，最长 272-314 共 43 tick（行 317 stagnant_ticks=43）；两次 navigation recovery（t305 recoveries 0→1，行 308；t384 1→2，行 387）后均在 ~10 tick 内死亡（t315、t396，行 318/399）。
A9 方向抖动：t313 实际右移、t314 命令左移（行 317 sent=left、effective_direction=right）后 t315 死亡；t483-485 上下往返后 t486 死亡（行 486-488）。
A10 通信层干净：四席 invalid_actions 全 0（score.json 行 758/777/796/815）；A 网关 30/30 成功（ai.jsonl）。

B1 火爆辣椒坐标参数解码偏差（第 4 节）——修复假设待测试。
B2 call 16/21 两次长耗时伴随校验失败（第 3 节）——响应截断为疑似，公告上下文缩减/去重后复测待测试。
B3 威胁评估偏低：贴脸连续攻击多 tick 不致死（t15-18、t439-442）仍不撤（行 18-21、442-445）。
B4 陪练 B 网关 502（ai.jsonl 行 37）不影响本队流水线；bot_B 17 条 warn 与该 502 的对应关系不确定。
B5 随包 rules.txt 与 v1.2 裁判行为不一致（rules.txt L289/L380 旧口径，README.md L35 声明旧文作废）——按随包文本读回放会误判。
B6 复活后直冲热点：每次复活直返 [9,9] 或敌方出生点缠斗，未利用 2 tick 出生保护换路线（frames 复活后路径）。

## 7 下一步：批量对局与回放驱动修复

用户已明确授权"跑大量局，不同地图不同对手，轮番检测看回放找问题"。计划：

- 批量对局矩阵：地图 × 对手 × 参数。地图候选：stage2 默认 18×18、stage1 采集图、自编辑地图（docs/15）；对手候选：原版陪练（B/C/D）、参考车、多风格自对弈（docs/24）。每组合跑多局，每局完整留存 ai.jsonl/score/frames/四 bot 日志与回放。
- 轮番检测：每局按本文件第 2-6 节口径自动产出核对表（R/D/M/分数、LLM 审计、词表裁决、问题清单），逐 tick 比对回放，不只看终局分数；把 A2/A8 类"静止段-死亡"模式作为批量统计指标。
- 回放驱动修复候选（全部标"待测试"，批量验证前不改集中参数默认值）：
  1. 任务完成后继续采普通资源的收益阈值与路线规划——待测试（本局直接失分 5.0）。
  2. 站桩对射的撤退/防御 hp 阈值与威胁评估——待测试（12 死主模式）。
  3. 辣椒公告坐标的几何校验（解码后核对点位与火线可达性）——待测试（唯一词表级疑点）。
  4. 无双获得后的利用窗口取舍——待测试。
  5. 身后隔格攻击源纳入致命判定——待测试。
  6. 长耗时回复/截断风险：公告上下文缩减后延迟与校验失败率复测——待测试。

## 8 未验证边界

- ai.jsonl 无时间戳/tick 字段：记录与公告 tick 的对应只能靠顺序；网关写盘前是否内部重试不可观察。
- bot_B.log 17 条 warn 与 ai.jsonl 行 37 的 502 对应关系不确定；"多数警告属 invalid/stale"是推断。
- frames.jsonl 无 effects 字段（练习公开状态有意过滤）：天使回血、易伤等只能由 hp/ed 与公告参数间接推断。
- 击杀奖励（+60 多人分摊）与死亡扣减 60 是"规则文档 + 本局数据拟合"的组合结论；+70/+80/+45/+40/+28/+35 等增量均已由事件参数解释、无未解释异常——但计分实现在原版 ELF 中、源码不可审，公式的完全验证以裁判输出为准。
- 公告生效类条目比公告 tick 晚 1 tick 出现在 A 感知快照（28 条无例外，communication.jsonl）是实测规律；机制未在公开字段中说明、因果未验证。
- 练习代理时延/配额 ≠ 正式网关（docs/19 第 5 节）：本局延迟分布不可外推。
- 本局 bot 构建于 2026-10-29 06:38（bot stdout 行 1），晚于公告去重修复 50b18b2（docs/19 第 8 节，2026-10-28）——推测已包含该修复，未单独验证，不确定。
- 单局样本：全部策略结论基于 1 局、1 地图、原版陪练对手；第 7 节全部修复假设在批量局验证前保持"待测试"。
