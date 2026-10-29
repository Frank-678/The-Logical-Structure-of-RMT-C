# 批量练习赛 batch 2026-10-29（seed 20261103，rrh10：race_reach_holdoff=1.0，仅 3/7 完成）

程序：`python3 -I /home/frank/batch_practice.py --count 7 --seed 20261103`（WSL，2026-10-29 12:49 启动）。
**批次被中断**：battle 1 完赛后（12:59:34），Windows 内存严重不足触发 Claude Code 后台进程回收，批次驱动被杀，battle 3–6 未跑。battle 2 的 practice.py 成为孤儿进程但**打完了整局**（tick 500，score.json 完整落盘），随后停在裁判"暂停"态等待已死的驱动；13:21 核实数据完整后清理孤儿进程，零数据损失。

**A = 冠军策略 + race_reach_holdoff=1.0 临时构建**（杠杠说明同 seed-20261102 批次 README / docs/36）。

## 结果（3/7，2W/1L）

| variant | session | A 名次 | A 分数 | A R | A D | A hp |
|---|---|---|---|---|---|---|
| 0 | practice-9d486e10 | 3/4 | 37.5 | 50 | 1245 | 0 |
| 1 | practice-941ca351 | **1/4** | **60.0** | 120 | 1155 | 100 |
| 2 | practice-202f5d10 | **1/4** | **57.5** | 110 | 1505 | 100 |

（variant 2 中 A 获得「天下无双」并命中输出 1505 有效伤害。）

## LLM 网关统计（每局 ai.jsonl，seat 维度）

| variant | A 调用/失败 | B | C | D |
|---|---|---|---|---|
| 0 | 73/0 | 11/9 | 11/0 | 9/8 |
| 1 | 80/0 | 10/0 | 10/3 | 8/11 |
| 2 | 70/0 | 10/9 | 9/8 | 6/7 |

三局合计 A 223 次真实调用、0 失败。B/C/D 重试偏多与批次期间系统内存压力导致的网关抖动一致（自动重试全部恢复）。

## 预注册指标（docs/35 §5，analyze_batch_race.py，n=3 部分批次）

| 指标 | control(0.0) | rrh10(1.0) | 判据 |
|---|---|---|---|
| A 份额@耗尽 mean | 0.279 | 0.467 | 回升 ✓ |
| 拾取数 mean | 4.4 | 7.0 | 回升 ✓ |
| t30 完成率 mean | 0.257 | 0.383 | 过 0.356 阈值 ✓ |
| deaths mean/median | 8.29/7 | 7.67/8 | 未触发 revert 守卫 |
| score mean | 42.50 | 51.67 | 回升 ✓ |

**注意**：n=3 为部分批次，结论须待 battle 3–6 补齐后再定（docs/37 将汇总）。本目录 batch_summary_reconstructed.json 为从三局 score.json + ai.jsonl 重建（原驱动被杀，未写出 batch_summary.json）。
