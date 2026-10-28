# 批量练习赛 batch 2026-10-29（seed 20261029）

程序：`/tmp/batch_practice.py --count 8 --seed 20261029`（WSL，2026-10-29 07:04:41 启动）。
每局：随机墙×6（不挡出生点/中央）、资源重排（12×10+4×20）、席位出生轮换 vid%4、8 事件时间表随机（公告 tick 10-220）、爆炸矩形/伤害与辣椒/天使点位扰动；validate_config 门禁；real 模式 deepseek-flash 经 127.0.0.1:7890 代理。
A = 我们的机器人；B/C/D = 原版练习陪练（实践裁判默认）。4 席位全为同一套 DDS+LLM 流程。

## 结果（4/8 完成；variants 4-7 因构建指纹失效未跑，见下）

| variant | session | A 名次 | A 分数 | A R | A D | A M | A hp | A invalid | 局内最佳 |
|---|---|---|---|---|---|---|---|---|---|
| 0 | practice-7268aa0b | 3/4 | 40.0 | 40 | 755 | 3 | 80 | 0 | D 50.0 (R80) |
| 1 | practice-17d87cb9b | **1/4** | **55.0** | **100** | 835 | 3 | 100 | 0 | A |
| 2 | practice-defcbdf1c | **1/4** | 45.0 | 60 | 750 | 3 | 100 | 0 | A |
| 3 | practice-ddc2e16e | 2/4 | 45.0 | 60 | 890 | 3 | 100 | 0 | D 45.0（D 960 胜 tiebreak） |

四局全 0 无效动作。A 两胜一亚一季；R 全部 ≥40，D 全部 ≥750。对照第一场真实练习赛（A 3/4、R40）明显改善——本批地图/事件均随机化，A 仍稳定在 40-55 分区间，variants 1/2 登顶。R 满值 100（variant 1）证明 A 在部分地图上可以吃掉整张资源饼。

## LLM 网关统计（每局 ai.jsonl）

| variant | A 调用/失败 | B | C | D |
|---|---|---|---|---|
| 0 | 24/0 | 6/1 | 8/1 | 7/0 |
| 1 | 26/0 | 9/0 | 14/0 | 10/1 |
| 2 | 26/0 | 10/0 | 9/1 | 10/1 |
| 3 | 21/0 | 7/1 | 7/0 | 7/2 |

四局合计 201 次真实 LLM 调用，8 次瞬时失败（各局偶发 502/网关抖动，自动重试后全部恢复）；**A 97/97 全成功、0 重试、4 局 0 无效动作**。

## variants 4-7 失败原因（真实故障，非配置问题）

时间线：
- 06:40 build 完成，`build/rmtc_bot/match_config.sha256` 记录当时 `match_config.hpp` 哈希。
- 07:04:41 批量开跑；variants 0-3 正常（07:09-07:22）。
- **07:21:10 在批量进行中编辑了 `src/rmtc_bot/include/rmtc_bot/match_config.hpp`（新增 prepare_fortress_value 参数行，采纳 visible-resource-bfs 的门控杠杆）。** 07:21:19/39 同步编辑 strategy_parameters.hpp / strategy.cpp。
- 07:22:27 variant 4 部署：`run.sh` 的 sha256 门禁（run.sh:16）发现配置已改而未重建 → 打印“当前配置尚未构建。请 bash build.sh…” → A 拒绝启动 → 裁判只注册 B/C/D → 注册等待超时 → variant 4-7 全部同样失败（每次约 100 秒）。

结论：run.sh 的构建指纹门禁按设计工作（防止跑旧二进制），但批量驱动器不知道这一点。教训：**批量进行中不得编辑任何 `match_config.sha256` 覆盖的源文件；编辑后必须先 build.sh 再开新批量**。07:32 已重建（stamp 恢复）；variants 4-7 待用同 seed 重跑（驱动确定性 → 同地图同事件表）。

## 附带事件（与批量无关）

07:33 WSL 发行版重启，/tmp 被清空：`/tmp/batch_summary.json`、`/tmp/batch_practice_20261029/`（config_0..7、botA.log、referee_stdout.log）、驱动器脚本 `/tmp/batch_practice.py` 全部丢失。本目录的 scoreboard 与 ai 统计自任务输出重建；run dir 副本自 `~/.rmtc-practice/` 幸存原件复制。驱动器脚本已重建于 `~`（/tmp 不可再放东西）。

## 文件

- 每局目录：score.json / ai.jsonl / frames.jsonl / referee.log / config.json / communication.jsonl / bot_B|C|D.log
- batch_summary_reconstructed.json：自批量任务输出重建的记分牌（/tmp 原件丢失）。
