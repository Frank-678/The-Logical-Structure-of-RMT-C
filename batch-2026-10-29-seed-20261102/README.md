# 批量练习赛 batch 2026-10-29（seed 20261102，rrh08：race_reach_holdoff=0.8）

程序：`python3 -I /home/frank/batch_practice.py --count 7 --seed 20261102`（WSL，2026-10-29 12:17 前后启动，12:49 完成 7/7）。
每局：随机墙×6、资源重排（200 R 一次性地图）、席位出生轮换 vid%4、8 事件时间表随机；real 模式 deepseek-flash 经 127.0.0.1:7890 代理。

**A = 冠军策略 + race_reach_holdoff=0.8 临时构建**（match_config.hpp 手改后编译，批次后已还原 0.0）。杠杠只作用于 stage2 且仅当自身感知到已知可收集资源存在时下调 reach_mission 权重 —— 见 docs/36（D:\code\The-Logical-Structure-of-RMT-C）。

## 结果（7/7 完成，4W/3L）

| variant | session | A 名次 | A 分数 | A R | A D | A hp |
|---|---|---|---|---|---|---|
| 0 | practice-5b85143d | **1/4** | **60.0** | 120 | 1563 | 100 |
| 1 | practice-c26e8f7 | **1/4** | **47.5** | 70 | 1290 | 60 |
| 2 | practice-6b35cade | **1/4** | **50.0** | 80 | — | — |
| 3 | practice-08887c3f | 3/4 | 40.0 | 40 | — | — |
| 4 | practice-132d4959 | 3/4 | 37.5 | 50 | — | — |
| 5 | practice-d1fac3c7 | **1/4** | **50.0** | 80 | — | — |
| 6 | practice-5d69ef83 | 3/4 | 32.5 | 30 | — | — |

细节与每局 LLM 网关统计见 batch_summary.json（A 全程 0 失败）。

## 预注册指标（docs/35 §5，analyze_batch_race.py）

| 指标 | control(0.0) | rrh08(0.8) | 判据 |
|---|---|---|---|
| A 份额@耗尽 mean | 0.279 | 0.336 | 回升 ✓ |
| 拾取数 mean | 4.4 | 5.4 | 回升 ✓ |
| t30 完成率 mean | 0.257 | 0.293 | 未过 0.356 阈值 |
| deaths mean/median | 8.29/7 | 8.71/9 | 未触发 revert 守卫（需 mean≥9 且 median≥8） |
| score mean | 42.50 | 45.36 | 回升 ✓ |

注：批次级 config_0..4 已被驱动清理，仅保留 config_5/config_6；每局有效配置见各 practice 目录内 config.json。
