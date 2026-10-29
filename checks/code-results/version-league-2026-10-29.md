# 冻结版本联赛

范围：自建离线裁判；没有真实模型调用或原版DDS资格。

计划 288 个版本×局面组合；本报告记录 288 个。重复运行可复用已通过的相同签名；未跑不算胜负。

| 版本 | 源提交 | 二进制SHA256 |
|---|---|---|
| chatgpt | `65c87145ae3b` | `b7517eddfaf65a59…` |
| deepseek | `8da0edecf592` | `811bfb7686b707a5…` |

完整SHA、编译信息与全部参数见[冻结清单与计划](version-league-2026-10-29.json)；表中仅缩短显示。

| 版本 | 完成 | 故障 | 均分 | 平均名次 | 第一份额 | 平均死亡 |
|---|---:|---:|---:|---:|---:|---:|
| chatgpt | 144 | 0 | 42.603 | 1.792 | 0.556 | 6.785 |
| deepseek | 144 | 0 | 42.710 | 1.889 | 0.507 | 7.396 |

| 候选相对首版本 | 地图组 | 配对局面 | 地图均分差 | 分组自助95%区间 |
|---|---:|---:|---:|---|
| deepseek | 12 | 144 | 0.107 | [-0.956597222222222, 1.093402777777778] |

区间仅描述本夹具样本；同图席位/对手的相关性按地图聚合，少量地图不能证明泛化。

## sparse

| 局面 | 版本 | 状态 | Tick止点 | 名次 | 分 | R | D | 任务 | 死亡 | 无效 | 徘徊窗口* |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| sparse-A-economy | chatgpt | passed | 500 | 2 | 40.0 | 40.0 | 820.0 | 3 | 2 | 0 | 185 |
| sparse-A-economy | deepseek | passed | 500 | 4 | 22.5 | 10.0 | 820.0 | 1 | 6 | 0 | 3 |
| sparse-A-pressure | chatgpt | passed | 500 | 1 | 50.0 | 80.0 | 1110.0 | 3 | 9 | 0 | 8 |
| sparse-A-pressure | deepseek | passed | 500 | 2 | 40.0 | 40.0 | 1080.0 | 3 | 7 | 0 | 11 |
| sparse-A-archive | chatgpt | passed | 500 | 2 | 40.0 | 40.0 | 860.0 | 3 | 14 | 0 | 11 |
| sparse-A-archive | deepseek | passed | 500 | 4 | 22.5 | 10.0 | 910.0 | 1 | 9 | 0 | 11 |
| sparse-B-economy | chatgpt | passed | 500 | 2 | 40.0 | 40.0 | 1000.0 | 3 | 3 | 0 | 7 |
| sparse-B-economy | deepseek | passed | 500 | 2 | 40.0 | 40.0 | 1230.0 | 3 | 5 | 0 | 0 |
| sparse-B-pressure | chatgpt | passed | 500 | 1 | 60.0 | 120.0 | 850.0 | 3 | 5 | 0 | 26 |
| sparse-B-pressure | deepseek | passed | 500 | 1 | 60.0 | 120.0 | 740.0 | 3 | 4 | 0 | 4 |
| sparse-B-archive | chatgpt | passed | 500 | 3 | 37.5 | 50.0 | 1295.0 | 2 | 9 | 0 | 6 |
| sparse-B-archive | deepseek | passed | 500 | 3 | 37.5 | 50.0 | 1850.0 | 2 | 17 | 0 | 11 |
| sparse-C-economy | chatgpt | passed | 500 | 1 | 52.5 | 90.0 | 655.0 | 3 | 5 | 0 | 36 |
| sparse-C-economy | deepseek | passed | 500 | 1 | 55.0 | 100.0 | 1180.0 | 3 | 8 | 0 | 0 |
| sparse-C-pressure | chatgpt | passed | 500 | 1 | 60.0 | 130.0 | 1065.0 | 3 | 8 | 0 | 7 |
| sparse-C-pressure | deepseek | passed | 500 | 1 | 60.0 | 130.0 | 1390.0 | 3 | 7 | 0 | 27 |
| sparse-C-archive | chatgpt | passed | 500 | 1 | 47.5 | 70.0 | 1370.0 | 3 | 9 | 0 | 26 |
| sparse-C-archive | deepseek | passed | 500 | 1 | 47.5 | 70.0 | 1370.0 | 3 | 15 | 0 | 12 |
| sparse-D-economy | chatgpt | passed | 500 | 1 | 40.3 | 70.0 | 260.0 | 3 | 1 | 0 | 391 |
| sparse-D-economy | deepseek | passed | 500 | 1 | 45.0 | 60.0 | 1560.0 | 3 | 6 | 0 | 0 |
| sparse-D-pressure | chatgpt | passed | 500 | 1 | 55.0 | 100.0 | 520.0 | 3 | 6 | 0 | 13 |
| sparse-D-pressure | deepseek | passed | 500 | 1 | 50.0 | 80.0 | 775.0 | 3 | 8 | 0 | 41 |
| sparse-D-archive | chatgpt | passed | 500 | 2 | 45.0 | 60.0 | 1010.0 | 3 | 8 | 0 | 28 |
| sparse-D-archive | deepseek | passed | 500 | 2 | 47.5 | 70.0 | 670.0 | 3 | 7 | 0 | 6 |

## rooms

| 局面 | 版本 | 状态 | Tick止点 | 名次 | 分 | R | D | 任务 | 死亡 | 无效 | 徘徊窗口* |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| rooms-A-economy | chatgpt | passed | 500 | 1 | 37.5 | 50.0 | 960.0 | 2 | 2 | 0 | 3 |
| rooms-A-economy | deepseek | passed | 500 | 1 | 37.5 | 50.0 | 590.0 | 2 | 2 | 0 | 0 |
| rooms-A-pressure | chatgpt | passed | 500 | 1 | 47.5 | 70.0 | 1065.0 | 3 | 7 | 0 | 12 |
| rooms-A-pressure | deepseek | passed | 500 | 1 | 47.5 | 70.0 | 880.0 | 3 | 5 | 0 | 26 |
| rooms-A-archive | chatgpt | passed | 500 | 1 | 47.5 | 70.0 | 850.0 | 3 | 6 | 0 | 20 |
| rooms-A-archive | deepseek | passed | 500 | 3 | 37.5 | 50.0 | 1010.0 | 2 | 5 | 0 | 10 |
| rooms-B-economy | chatgpt | passed | 500 | 1 | 37.5 | 50.0 | 525.0 | 2 | 5 | 0 | 171 |
| rooms-B-economy | deepseek | passed | 500 | 1 | 37.5 | 50.0 | 1080.0 | 2 | 6 | 0 | 0 |
| rooms-B-pressure | chatgpt | passed | 500 | 1 | 50.0 | 80.0 | 1210.0 | 3 | 5 | 0 | 23 |
| rooms-B-pressure | deepseek | passed | 500 | 1 | 50.0 | 80.0 | 560.0 | 3 | 5 | 0 | 20 |
| rooms-B-archive | chatgpt | passed | 500 | 3 | 37.5 | 50.0 | 720.0 | 2 | 8 | 0 | 15 |
| rooms-B-archive | deepseek | passed | 500 | 2 | 37.5 | 50.0 | 1280.0 | 2 | 6 | 0 | 34 |
| rooms-C-economy | chatgpt | passed | 500 | 4 | 24.7 | 30.0 | 240.0 | 2 | 0 | 0 | 205 |
| rooms-C-economy | deepseek | passed | 500 | 1 | 37.5 | 50.0 | 1240.0 | 2 | 8 | 0 | 3 |
| rooms-C-pressure | chatgpt | passed | 500 | 1 | 50.0 | 80.0 | 605.0 | 3 | 5 | 0 | 58 |
| rooms-C-pressure | deepseek | passed | 500 | 1 | 50.0 | 80.0 | 1350.0 | 3 | 8 | 0 | 13 |
| rooms-C-archive | chatgpt | passed | 500 | 4 | 32.5 | 30.0 | 1355.0 | 2 | 10 | 0 | 37 |
| rooms-C-archive | deepseek | passed | 500 | 4 | 16.5 | 10.0 | 300.0 | 1 | 8 | 0 | 10 |
| rooms-D-economy | chatgpt | passed | 500 | 1 | 45.0 | 60.0 | 1020.0 | 3 | 2 | 0 | 106 |
| rooms-D-economy | deepseek | passed | 500 | 1 | 47.5 | 70.0 | 960.0 | 3 | 4 | 0 | 0 |
| rooms-D-pressure | chatgpt | passed | 500 | 1 | 45.0 | 60.0 | 940.0 | 3 | 5 | 0 | 22 |
| rooms-D-pressure | deepseek | passed | 500 | 1 | 47.5 | 70.0 | 860.0 | 3 | 4 | 0 | 4 |
| rooms-D-archive | chatgpt | passed | 500 | 1 | 45.0 | 60.0 | 1640.0 | 3 | 11 | 0 | 9 |
| rooms-D-archive | deepseek | passed | 500 | 1 | 47.4 | 90.0 | 330.0 | 3 | 7 | 0 | 20 |

## bridge

| 局面 | 版本 | 状态 | Tick止点 | 名次 | 分 | R | D | 任务 | 死亡 | 无效 | 徘徊窗口* |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bridge-A-economy | chatgpt | passed | 500 | 1 | 41.4 | 60.0 | 380.0 | 3 | 1 | 0 | 12 |
| bridge-A-economy | deepseek | passed | 500 | 1 | 40.0 | 40.0 | 1550.0 | 3 | 2 | 0 | 0 |
| bridge-A-pressure | chatgpt | passed | 500 | 1 | 50.0 | 80.0 | 880.0 | 3 | 4 | 0 | 29 |
| bridge-A-pressure | deepseek | passed | 500 | 1 | 50.0 | 80.0 | 650.0 | 3 | 4 | 0 | 56 |
| bridge-A-archive | chatgpt | passed | 500 | 2 | 45.0 | 60.0 | 665.0 | 3 | 6 | 0 | 12 |
| bridge-A-archive | deepseek | passed | 500 | 4 | 36.7 | 40.0 | 390.0 | 3 | 5 | 0 | 7 |
| bridge-B-economy | chatgpt | passed | 500 | 2 | 40.0 | 40.0 | 730.0 | 3 | 3 | 0 | 167 |
| bridge-B-economy | deepseek | passed | 500 | 2 | 40.0 | 40.0 | 1000.0 | 3 | 7 | 0 | 2 |
| bridge-B-pressure | chatgpt | passed | 500 | 1 | 52.5 | 90.0 | 1000.0 | 3 | 8 | 0 | 12 |
| bridge-B-pressure | deepseek | passed | 500 | 1 | 44.85 | 90.0 | 245.0 | 3 | 1 | 0 | 234 |
| bridge-B-archive | chatgpt | passed | 500 | 1 | 45.0 | 60.0 | 1170.0 | 3 | 8 | 0 | 28 |
| bridge-B-archive | deepseek | passed | 500 | 1 | 45.0 | 60.0 | 790.0 | 3 | 8 | 0 | 26 |
| bridge-C-economy | chatgpt | passed | 500 | 1 | 47.5 | 70.0 | 620.0 | 3 | 4 | 0 | 154 |
| bridge-C-economy | deepseek | passed | 500 | 1 | 47.5 | 70.0 | 940.0 | 3 | 2 | 0 | 0 |
| bridge-C-pressure | chatgpt | passed | 500 | 1 | 50.0 | 80.0 | 1352.5 | 3 | 7 | 0 | 12 |
| bridge-C-pressure | deepseek | passed | 500 | 1 | 50.0 | 80.0 | 842.5 | 3 | 5 | 0 | 23 |
| bridge-C-archive | chatgpt | passed | 500 | 2 | 42.5 | 50.0 | 1690.0 | 3 | 9 | 0 | 27 |
| bridge-C-archive | deepseek | passed | 500 | 2 | 42.5 | 50.0 | 820.0 | 3 | 9 | 0 | 47 |
| bridge-D-economy | chatgpt | passed | 500 | 4 | 30.1 | 30.0 | 420.0 | 2 | 3 | 0 | 284 |
| bridge-D-economy | deepseek | passed | 500 | 4 | 32.5 | 30.0 | 1310.0 | 2 | 7 | 0 | 3 |
| bridge-D-pressure | chatgpt | passed | 500 | 2 | 42.5 | 50.0 | 990.0 | 3 | 6 | 0 | 9 |
| bridge-D-pressure | deepseek | passed | 500 | 1 | 45.0 | 60.0 | 735.0 | 3 | 6 | 0 | 47 |
| bridge-D-archive | chatgpt | passed | 500 | 4 | 32.5 | 30.0 | 1090.0 | 2 | 9 | 0 | 11 |
| bridge-D-archive | deepseek | passed | 500 | 3 | 42.5 | 50.0 | 760.0 | 3 | 6 | 0 | 20 |

## snake

| 局面 | 版本 | 状态 | Tick止点 | 名次 | 分 | R | D | 任务 | 死亡 | 无效 | 徘徊窗口* |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| snake-A-economy | chatgpt | passed | 500 | 3 | 32.5 | 30.0 | 640.0 | 2 | 1 | 0 | 290 |
| snake-A-economy | deepseek | passed | 500 | 3 | 32.5 | 30.0 | 2500.0 | 2 | 0 | 0 | 0 |
| snake-A-pressure | chatgpt | passed | 500 | 1 | 60.0 | 150.0 | 620.0 | 3 | 7 | 0 | 26 |
| snake-A-pressure | deepseek | passed | 500 | 2 | 27.5 | 30.0 | 800.0 | 1 | 8 | 0 | 3 |
| snake-A-archive | chatgpt | passed | 500 | 3 | 32.5 | 30.0 | 565.0 | 2 | 6 | 0 | 18 |
| snake-A-archive | deepseek | passed | 500 | 3 | 32.5 | 30.0 | 500.0 | 2 | 7 | 0 | 6 |
| snake-B-economy | chatgpt | passed | 500 | 1 | 44.2 | 100.0 | 140.0 | 3 | 1 | 0 | 364 |
| snake-B-economy | deepseek | passed | 500 | 1 | 55.0 | 100.0 | 690.0 | 3 | 4 | 0 | 0 |
| snake-B-pressure | chatgpt | passed | 500 | 1 | 60.0 | 170.0 | 940.0 | 3 | 6 | 0 | 7 |
| snake-B-pressure | deepseek | passed | 500 | 1 | 60.0 | 130.0 | 650.0 | 3 | 6 | 0 | 17 |
| snake-B-archive | chatgpt | passed | 500 | 1 | 55.0 | 100.0 | 750.0 | 3 | 7 | 0 | 9 |
| snake-B-archive | deepseek | passed | 500 | 1 | 55.0 | 100.0 | 770.0 | 3 | 10 | 0 | 10 |
| snake-C-economy | chatgpt | passed | 500 | 2 | 28.7 | 70.0 | 40.0 | 2 | 1 | 0 | 201 |
| snake-C-economy | deepseek | passed | 500 | 1 | 50.0 | 80.0 | 1220.0 | 3 | 2 | 0 | 0 |
| snake-C-pressure | chatgpt | passed | 500 | 1 | 57.6 | 150.0 | 420.0 | 3 | 2 | 0 | 27 |
| snake-C-pressure | deepseek | passed | 500 | 1 | 60.0 | 130.0 | 960.0 | 3 | 6 | 0 | 13 |
| snake-C-archive | chatgpt | passed | 500 | 2 | 40.9 | 70.0 | 280.0 | 3 | 5 | 0 | 7 |
| snake-C-archive | deepseek | passed | 500 | 2 | 47.5 | 70.0 | 740.0 | 3 | 9 | 0 | 8 |
| snake-D-economy | chatgpt | passed | 500 | 4 | 14.6 | 0.0 | 320.0 | 1 | 1 | 0 | 255 |
| snake-D-economy | deepseek | passed | 500 | 3 | 20.0 | 0.0 | 610.0 | 1 | 2 | 0 | 0 |
| snake-D-pressure | chatgpt | passed | 500 | 1 | 60.0 | 150.0 | 1320.0 | 3 | 5 | 0 | 24 |
| snake-D-pressure | deepseek | passed | 500 | 1 | 60.0 | 120.0 | 1490.0 | 3 | 9 | 0 | 16 |
| snake-D-archive | chatgpt | passed | 500 | 4 | 20.0 | 0.0 | 1850.0 | 1 | 12 | 0 | 12 |
| snake-D-archive | deepseek | passed | 500 | 4 | 20.0 | 0.0 | 1230.0 | 1 | 6 | 0 | 13 |

## ring

| 局面 | 版本 | 状态 | Tick止点 | 名次 | 分 | R | D | 任务 | 死亡 | 无效 | 徘徊窗口* |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ring-A-economy | chatgpt | passed | 500 | 1 | 45.0 | 60.0 | 520.0 | 3 | 5 | 0 | 205 |
| ring-A-economy | deepseek | passed | 500 | 1 | 45.0 | 60.0 | 1220.0 | 3 | 6 | 0 | 0 |
| ring-A-pressure | chatgpt | passed | 500 | 1 | 60.0 | 120.0 | 850.0 | 3 | 8 | 0 | 13 |
| ring-A-pressure | deepseek | passed | 500 | 1 | 60.0 | 130.0 | 1070.0 | 3 | 9 | 0 | 14 |
| ring-A-archive | chatgpt | passed | 500 | 1 | 52.5 | 90.0 | 1090.0 | 3 | 10 | 0 | 16 |
| ring-A-archive | deepseek | passed | 500 | 1 | 52.5 | 90.0 | 955.0 | 3 | 8 | 0 | 42 |
| ring-B-economy | chatgpt | passed | 500 | 2 | 35.0 | 40.0 | 745.0 | 2 | 2 | 0 | 293 |
| ring-B-economy | deepseek | passed | 500 | 3 | 35.0 | 40.0 | 1200.0 | 2 | 9 | 0 | 0 |
| ring-B-pressure | chatgpt | passed | 500 | 1 | 52.5 | 90.0 | 1060.0 | 3 | 9 | 0 | 0 |
| ring-B-pressure | deepseek | passed | 500 | 1 | 52.5 | 90.0 | 1100.0 | 3 | 10 | 0 | 33 |
| ring-B-archive | chatgpt | passed | 500 | 4 | 30.0 | 20.0 | 1370.0 | 2 | 15 | 0 | 22 |
| ring-B-archive | deepseek | passed | 500 | 4 | 30.0 | 20.0 | 1125.0 | 2 | 11 | 0 | 22 |
| ring-C-economy | chatgpt | passed | 500 | 3 | 22.5 | 10.0 | 1165.0 | 1 | 5 | 0 | 20 |
| ring-C-economy | deepseek | passed | 500 | 1 | 47.5 | 70.0 | 1110.0 | 3 | 10 | 0 | 0 |
| ring-C-pressure | chatgpt | passed | 500 | 1 | 52.5 | 90.0 | 950.0 | 3 | 9 | 0 | 4 |
| ring-C-pressure | deepseek | passed | 500 | 1 | 52.5 | 90.0 | 1005.0 | 3 | 7 | 0 | 4 |
| ring-C-archive | chatgpt | passed | 500 | 3 | 40.0 | 40.0 | 970.0 | 3 | 11 | 0 | 15 |
| ring-C-archive | deepseek | passed | 500 | 3 | 40.0 | 40.0 | 840.0 | 3 | 12 | 0 | 32 |
| ring-D-economy | chatgpt | passed | 500 | 1 | 35.9 | 50.0 | 280.0 | 3 | 1 | 0 | 372 |
| ring-D-economy | deepseek | passed | 500 | 2 | 42.5 | 50.0 | 1380.0 | 3 | 4 | 0 | 1 |
| ring-D-pressure | chatgpt | passed | 500 | 2 | 42.5 | 50.0 | 1200.0 | 3 | 9 | 0 | 24 |
| ring-D-pressure | deepseek | passed | 500 | 2 | 45.0 | 60.0 | 1130.0 | 3 | 9 | 0 | 14 |
| ring-D-archive | chatgpt | passed | 500 | 2 | 42.5 | 50.0 | 1230.0 | 3 | 13 | 0 | 18 |
| ring-D-archive | deepseek | passed | 500 | 2 | 42.5 | 50.0 | 1240.0 | 3 | 10 | 0 | 20 |

## dead_ends

| 局面 | 版本 | 状态 | Tick止点 | 名次 | 分 | R | D | 任务 | 死亡 | 无效 | 徘徊窗口* |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| dead_ends-A-economy | chatgpt | passed | 500 | 3 | 30.0 | 20.0 | 1254.2857142857142 | 2 | 6 | 0 | 77 |
| dead_ends-A-economy | deepseek | passed | 500 | 1 | 47.5 | 70.0 | 1490.0 | 3 | 10 | 0 | 3 |
| dead_ends-A-pressure | chatgpt | passed | 500 | 1 | 57.5 | 110.0 | 1685.0 | 3 | 14 | 0 | 0 |
| dead_ends-A-pressure | deepseek | passed | 500 | 1 | 60.0 | 120.0 | 1215.0 | 3 | 12 | 0 | 1 |
| dead_ends-A-archive | chatgpt | passed | 500 | 2 | 37.5 | 50.0 | 2415.0 | 2 | 16 | 0 | 16 |
| dead_ends-A-archive | deepseek | passed | 500 | 3 | 37.5 | 50.0 | 1545.0 | 2 | 23 | 0 | 20 |
| dead_ends-B-economy | chatgpt | passed | 500 | 1 | 52.5 | 90.0 | 1990.0 | 3 | 6 | 0 | 25 |
| dead_ends-B-economy | deepseek | passed | 500 | 1 | 47.5 | 70.0 | 2070.0 | 3 | 8 | 0 | 5 |
| dead_ends-B-pressure | chatgpt | passed | 500 | 2 | 50.0 | 80.0 | 1490.0 | 3 | 12 | 0 | 7 |
| dead_ends-B-pressure | deepseek | passed | 500 | 2 | 50.0 | 80.0 | 895.0 | 3 | 10 | 0 | 5 |
| dead_ends-B-archive | chatgpt | passed | 500 | 1 | 52.5 | 90.0 | 2665.0 | 3 | 16 | 0 | 9 |
| dead_ends-B-archive | deepseek | passed | 500 | 1 | 47.5 | 70.0 | 1969.2857142857142 | 3 | 14 | 0 | 29 |
| dead_ends-C-economy | chatgpt | passed | 500 | 3 | 35.0 | 40.0 | 1935.0 | 2 | 8 | 0 | 65 |
| dead_ends-C-economy | deepseek | passed | 500 | 3 | 35.0 | 40.0 | 2620.0 | 2 | 8 | 0 | 7 |
| dead_ends-C-pressure | chatgpt | passed | 500 | 2 | 40.0 | 60.0 | 2310.0 | 2 | 21 | 0 | 0 |
| dead_ends-C-pressure | deepseek | passed | 500 | 2 | 37.5 | 50.0 | 1907.142857142857 | 2 | 25 | 0 | 0 |
| dead_ends-C-archive | chatgpt | passed | 500 | 3 | 35.0 | 40.0 | 2165.0 | 2 | 12 | 0 | 15 |
| dead_ends-C-archive | deepseek | passed | 500 | 4 | 35.0 | 40.0 | 1075.0 | 2 | 16 | 0 | 12 |
| dead_ends-D-economy | chatgpt | passed | 500 | 3 | 22.5 | 10.0 | 900.0 | 1 | 6 | 0 | 117 |
| dead_ends-D-economy | deepseek | passed | 500 | 3 | 30.0 | 20.0 | 1460.0 | 2 | 11 | 0 | 8 |
| dead_ends-D-pressure | chatgpt | passed | 500 | 1 | 52.5 | 90.0 | 2640.0 | 3 | 27 | 0 | 6 |
| dead_ends-D-pressure | deepseek | passed | 500 | 1 | 50.0 | 80.0 | 2820.0 | 3 | 29 | 0 | 6 |
| dead_ends-D-archive | chatgpt | passed | 500 | 2 | 40.0 | 40.0 | 2490.0 | 3 | 11 | 0 | 11 |
| dead_ends-D-archive | deepseek | passed | 500 | 2 | 40.0 | 40.0 | 1810.7142857142858 | 3 | 14 | 0 | 13 |

## wide_lanes

| 局面 | 版本 | 状态 | Tick止点 | 名次 | 分 | R | D | 任务 | 死亡 | 无效 | 徘徊窗口* |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| wide_lanes-A-economy | chatgpt | passed | 500 | 3 | 30.5 | 40.0 | 350.0 | 2 | 3 | 0 | 80 |
| wide_lanes-A-economy | deepseek | passed | 500 | 3 | 32.5 | 30.0 | 1250.0 | 2 | 4 | 0 | 3 |
| wide_lanes-A-pressure | chatgpt | passed | 500 | 1 | 52.5 | 90.0 | 985.0 | 3 | 7 | 0 | 35 |
| wide_lanes-A-pressure | deepseek | passed | 500 | 3 | 42.5 | 50.0 | 1060.0 | 3 | 8 | 0 | 12 |
| wide_lanes-A-archive | chatgpt | passed | 500 | 3 | 35.0 | 40.0 | 660.0 | 2 | 7 | 0 | 27 |
| wide_lanes-A-archive | deepseek | passed | 500 | 3 | 40.0 | 40.0 | 840.0 | 3 | 8 | 0 | 17 |
| wide_lanes-B-economy | chatgpt | passed | 500 | 1 | 40.0 | 40.0 | 820.0 | 3 | 2 | 0 | 170 |
| wide_lanes-B-economy | deepseek | passed | 500 | 2 | 40.0 | 40.0 | 800.0 | 3 | 4 | 0 | 5 |
| wide_lanes-B-pressure | chatgpt | passed | 500 | 1 | 50.0 | 80.0 | 1030.0 | 3 | 8 | 0 | 3 |
| wide_lanes-B-pressure | deepseek | passed | 500 | 1 | 50.0 | 80.0 | 950.0 | 3 | 6 | 0 | 17 |
| wide_lanes-B-archive | chatgpt | passed | 500 | 2 | 40.0 | 40.0 | 1360.0 | 3 | 11 | 0 | 15 |
| wide_lanes-B-archive | deepseek | passed | 500 | 2 | 40.0 | 40.0 | 1930.0 | 3 | 10 | 0 | 20 |
| wide_lanes-C-economy | chatgpt | passed | 500 | 1 | 47.5 | 70.0 | 620.0 | 3 | 2 | 0 | 83 |
| wide_lanes-C-economy | deepseek | passed | 500 | 3 | 32.5 | 30.0 | 1330.0 | 2 | 8 | 0 | 0 |
| wide_lanes-C-pressure | chatgpt | passed | 500 | 1 | 57.5 | 110.0 | 920.0 | 3 | 7 | 0 | 7 |
| wide_lanes-C-pressure | deepseek | passed | 500 | 1 | 47.5 | 70.0 | 540.0 | 3 | 4 | 0 | 45 |
| wide_lanes-C-archive | chatgpt | passed | 500 | 1 | 47.5 | 70.0 | 980.0 | 3 | 5 | 0 | 19 |
| wide_lanes-C-archive | deepseek | passed | 500 | 4 | 32.5 | 30.0 | 840.0 | 2 | 13 | 0 | 23 |
| wide_lanes-D-economy | chatgpt | passed | 500 | 1 | 52.5 | 90.0 | 900.0 | 3 | 2 | 0 | 82 |
| wide_lanes-D-economy | deepseek | passed | 500 | 1 | 52.5 | 90.0 | 590.0 | 3 | 2 | 0 | 0 |
| wide_lanes-D-pressure | chatgpt | passed | 500 | 1 | 55.0 | 100.0 | 1020.0 | 3 | 7 | 0 | 34 |
| wide_lanes-D-pressure | deepseek | passed | 500 | 1 | 53.2 | 100.0 | 440.0 | 3 | 2 | 0 | 10 |
| wide_lanes-D-archive | chatgpt | passed | 500 | 1 | 45.0 | 60.0 | 1200.0 | 3 | 10 | 0 | 11 |
| wide_lanes-D-archive | deepseek | passed | 500 | 1 | 52.5 | 90.0 | 830.0 | 3 | 12 | 0 | 23 |

## asymmetric

| 局面 | 版本 | 状态 | Tick止点 | 名次 | 分 | R | D | 任务 | 死亡 | 无效 | 徘徊窗口* |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| asymmetric-A-economy | chatgpt | passed | 500 | 4 | 19.6 | 30.0 | 70.0 | 2 | 0 | 0 | 448 |
| asymmetric-A-economy | deepseek | passed | 500 | 2 | 35.0 | 40.0 | 1210.0 | 2 | 5 | 0 | 8 |
| asymmetric-A-pressure | chatgpt | passed | 500 | 1 | 60.0 | 120.0 | 840.0 | 3 | 3 | 0 | 7 |
| asymmetric-A-pressure | deepseek | passed | 500 | 1 | 51.6 | 120.0 | 220.0 | 3 | 3 | 0 | 28 |
| asymmetric-A-archive | chatgpt | passed | 500 | 4 | 30.0 | 20.0 | 1040.0 | 2 | 7 | 0 | 34 |
| asymmetric-A-archive | deepseek | passed | 500 | 4 | 30.0 | 20.0 | 505.0 | 2 | 9 | 0 | 28 |
| asymmetric-B-economy | chatgpt | passed | 500 | 2 | 40.0 | 40.0 | 515.0 | 3 | 2 | 0 | 272 |
| asymmetric-B-economy | deepseek | passed | 500 | 2 | 40.0 | 40.0 | 1385.0 | 3 | 6 | 0 | 0 |
| asymmetric-B-pressure | chatgpt | passed | 500 | 1 | 60.0 | 140.0 | 655.0 | 3 | 4 | 0 | 6 |
| asymmetric-B-pressure | deepseek | passed | 500 | 1 | 60.0 | 120.0 | 730.0 | 3 | 8 | 0 | 27 |
| asymmetric-B-archive | chatgpt | passed | 500 | 2 | 40.0 | 40.0 | 1140.0 | 3 | 6 | 0 | 16 |
| asymmetric-B-archive | deepseek | passed | 500 | 2 | 40.0 | 40.0 | 1125.0 | 3 | 7 | 0 | 24 |
| asymmetric-C-economy | chatgpt | passed | 500 | 1 | 50.0 | 80.0 | 700.0 | 3 | 3 | 0 | 243 |
| asymmetric-C-economy | deepseek | passed | 500 | 1 | 50.0 | 80.0 | 1095.0 | 3 | 7 | 0 | 0 |
| asymmetric-C-pressure | chatgpt | passed | 500 | 1 | 60.0 | 130.0 | 605.0 | 3 | 4 | 0 | 86 |
| asymmetric-C-pressure | deepseek | passed | 500 | 1 | 60.0 | 130.0 | 570.0 | 3 | 3 | 0 | 16 |
| asymmetric-C-archive | chatgpt | passed | 500 | 1 | 52.5 | 90.0 | 1055.0 | 3 | 9 | 0 | 35 |
| asymmetric-C-archive | deepseek | passed | 500 | 1 | 52.5 | 90.0 | 890.0 | 3 | 8 | 0 | 14 |
| asymmetric-D-economy | chatgpt | passed | 500 | 3 | 33.05 | 40.0 | 435.0 | 2 | 4 | 0 | 246 |
| asymmetric-D-economy | deepseek | passed | 500 | 2 | 37.5 | 50.0 | 1070.0 | 2 | 4 | 0 | 0 |
| asymmetric-D-pressure | chatgpt | passed | 500 | 1 | 50.0 | 80.0 | 680.0 | 3 | 5 | 0 | 12 |
| asymmetric-D-pressure | deepseek | passed | 500 | 1 | 52.5 | 90.0 | 860.0 | 3 | 6 | 0 | 7 |
| asymmetric-D-archive | chatgpt | passed | 500 | 4 | 35.0 | 40.0 | 985.0 | 2 | 9 | 0 | 16 |
| asymmetric-D-archive | deepseek | passed | 500 | 3 | 37.5 | 50.0 | 820.0 | 2 | 9 | 0 | 19 |

## center_race

| 局面 | 版本 | 状态 | Tick止点 | 名次 | 分 | R | D | 任务 | 死亡 | 无效 | 徘徊窗口* |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| center_race-A-economy | chatgpt | passed | 500 | 3 | 32.5 | 30.0 | 605.0 | 2 | 5 | 0 | 188 |
| center_race-A-economy | deepseek | passed | 500 | 4 | 30.0 | 20.0 | 1460.0 | 2 | 9 | 0 | 0 |
| center_race-A-pressure | chatgpt | passed | 500 | 1 | 55.0 | 100.0 | 1870.0 | 3 | 13 | 0 | 84 |
| center_race-A-pressure | deepseek | passed | 500 | 1 | 52.5 | 90.0 | 1385.0 | 3 | 13 | 0 | 42 |
| center_race-A-archive | chatgpt | passed | 500 | 2 | 45.0 | 60.0 | 1157.142857142857 | 3 | 13 | 0 | 45 |
| center_race-A-archive | deepseek | passed | 500 | 4 | 35.0 | 40.0 | 880.0 | 2 | 11 | 0 | 36 |
| center_race-B-economy | chatgpt | passed | 500 | 1 | 40.0 | 60.0 | 1180.0 | 2 | 5 | 0 | 19 |
| center_race-B-economy | deepseek | passed | 500 | 3 | 37.5 | 50.0 | 1780.0 | 2 | 7 | 0 | 0 |
| center_race-B-pressure | chatgpt | passed | 500 | 1 | 57.5 | 110.0 | 2545.0 | 3 | 20 | 0 | 16 |
| center_race-B-pressure | deepseek | passed | 500 | 1 | 60.0 | 120.0 | 1110.0 | 3 | 9 | 0 | 27 |
| center_race-B-archive | chatgpt | passed | 500 | 1 | 45.0 | 60.0 | 1755.0 | 3 | 13 | 0 | 29 |
| center_race-B-archive | deepseek | passed | 500 | 2 | 45.0 | 60.0 | 1435.0 | 3 | 14 | 0 | 46 |
| center_race-C-economy | chatgpt | passed | 500 | 1 | 45.0 | 60.0 | 1195.0 | 3 | 3 | 0 | 186 |
| center_race-C-economy | deepseek | passed | 500 | 1 | 42.5 | 50.0 | 1545.0 | 3 | 8 | 0 | 1 |
| center_race-C-pressure | chatgpt | passed | 500 | 1 | 60.0 | 130.0 | 2435.0 | 3 | 17 | 0 | 23 |
| center_race-C-pressure | deepseek | passed | 500 | 1 | 60.0 | 130.0 | 1210.0 | 3 | 12 | 0 | 81 |
| center_race-C-archive | chatgpt | passed | 500 | 1 | 45.0 | 60.0 | 1723.3333333333333 | 3 | 12 | 0 | 49 |
| center_race-C-archive | deepseek | passed | 500 | 1 | 45.0 | 60.0 | 1500.0 | 3 | 10 | 0 | 20 |
| center_race-D-economy | chatgpt | passed | 500 | 1 | 40.0 | 40.0 | 1330.0 | 3 | 6 | 0 | 94 |
| center_race-D-economy | deepseek | passed | 500 | 1 | 47.5 | 70.0 | 1753.3333333333333 | 3 | 8 | 0 | 0 |
| center_race-D-pressure | chatgpt | passed | 500 | 1 | 52.5 | 90.0 | 2442.5 | 3 | 17 | 0 | 30 |
| center_race-D-pressure | deepseek | passed | 500 | 1 | 55.0 | 100.0 | 1070.0 | 3 | 9 | 0 | 42 |
| center_race-D-archive | chatgpt | passed | 500 | 3 | 40.0 | 40.0 | 1755.0 | 3 | 8 | 0 | 26 |
| center_race-D-archive | deepseek | passed | 500 | 3 | 40.0 | 40.0 | 1175.0 | 3 | 13 | 0 | 24 |

## resource_bias

| 局面 | 版本 | 状态 | Tick止点 | 名次 | 分 | R | D | 任务 | 死亡 | 无效 | 徘徊窗口* |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| resource_bias-A-economy | chatgpt | passed | 500 | 1 | 54.4 | 100.0 | 480.0 | 3 | 3 | 0 | 125 |
| resource_bias-A-economy | deepseek | passed | 500 | 1 | 55.0 | 100.0 | 560.0 | 3 | 5 | 0 | 3 |
| resource_bias-A-pressure | chatgpt | passed | 500 | 1 | 55.0 | 100.0 | 880.0 | 3 | 7 | 0 | 18 |
| resource_bias-A-pressure | deepseek | passed | 500 | 1 | 55.0 | 100.0 | 695.0 | 3 | 5 | 0 | 7 |
| resource_bias-A-archive | chatgpt | passed | 500 | 1 | 55.0 | 100.0 | 990.0 | 3 | 6 | 0 | 16 |
| resource_bias-A-archive | deepseek | passed | 500 | 2 | 55.0 | 100.0 | 830.0 | 3 | 7 | 0 | 22 |
| resource_bias-B-economy | chatgpt | passed | 500 | 3 | 20.0 | 0.0 | 660.0 | 1 | 6 | 0 | 119 |
| resource_bias-B-economy | deepseek | passed | 500 | 3 | 20.0 | 0.0 | 1300.0 | 1 | 4 | 0 | 3 |
| resource_bias-B-pressure | chatgpt | passed | 500 | 3 | 20.0 | 0.0 | 1180.0 | 1 | 9 | 0 | 4 |
| resource_bias-B-pressure | deepseek | passed | 500 | 3 | 20.0 | 0.0 | 1000.0 | 1 | 6 | 0 | 34 |
| resource_bias-B-archive | chatgpt | passed | 500 | 4 | 20.0 | 0.0 | 1150.0 | 1 | 10 | 0 | 22 |
| resource_bias-B-archive | deepseek | passed | 500 | 4 | 20.0 | 0.0 | 670.0 | 1 | 10 | 0 | 24 |
| resource_bias-C-economy | chatgpt | passed | 500 | 3 | 20.0 | 0.0 | 860.0 | 1 | 4 | 0 | 45 |
| resource_bias-C-economy | deepseek | passed | 500 | 3 | 20.0 | 0.0 | 1335.0 | 1 | 3 | 0 | 0 |
| resource_bias-C-pressure | chatgpt | passed | 500 | 3 | 20.0 | 0.0 | 900.0 | 1 | 7 | 0 | 19 |
| resource_bias-C-pressure | deepseek | passed | 500 | 3 | 20.0 | 0.0 | 590.0 | 1 | 5 | 0 | 106 |
| resource_bias-C-archive | chatgpt | passed | 500 | 3 | 20.0 | 0.0 | 1600.0 | 1 | 13 | 0 | 18 |
| resource_bias-C-archive | deepseek | passed | 500 | 3 | 20.0 | 0.0 | 1145.0 | 1 | 14 | 0 | 17 |
| resource_bias-D-economy | chatgpt | passed | 500 | 1 | 55.0 | 100.0 | 1197.142857142857 | 3 | 5 | 0 | 13 |
| resource_bias-D-economy | deepseek | passed | 500 | 1 | 55.0 | 100.0 | 1570.0 | 3 | 5 | 0 | 0 |
| resource_bias-D-pressure | chatgpt | passed | 500 | 1 | 55.0 | 100.0 | 1200.0 | 3 | 9 | 0 | 22 |
| resource_bias-D-pressure | deepseek | passed | 500 | 1 | 55.0 | 100.0 | 1220.0 | 3 | 8 | 0 | 4 |
| resource_bias-D-archive | chatgpt | passed | 500 | 2 | 55.0 | 100.0 | 760.0 | 3 | 9 | 0 | 23 |
| resource_bias-D-archive | deepseek | passed | 500 | 1 | 55.0 | 100.0 | 1195.0 | 3 | 8 | 0 | 23 |

## dynamic_cut

| 局面 | 版本 | 状态 | Tick止点 | 名次 | 分 | R | D | 任务 | 死亡 | 无效 | 徘徊窗口* |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| dynamic_cut-A-economy | chatgpt | passed | 500 | 1 | 55.0 | 100.0 | 840.0 | 3 | 3 | 0 | 9 |
| dynamic_cut-A-economy | deepseek | passed | 500 | 1 | 57.5 | 110.0 | 890.0 | 3 | 3 | 0 | 0 |
| dynamic_cut-A-pressure | chatgpt | passed | 500 | 1 | 60.0 | 140.0 | 655.0 | 3 | 4 | 0 | 35 |
| dynamic_cut-A-pressure | deepseek | passed | 500 | 1 | 60.0 | 120.0 | 1020.0 | 3 | 6 | 0 | 26 |
| dynamic_cut-A-archive | chatgpt | passed | 500 | 2 | 42.5 | 50.0 | 1430.0 | 3 | 10 | 0 | 23 |
| dynamic_cut-A-archive | deepseek | passed | 500 | 1 | 55.0 | 100.0 | 660.0 | 3 | 10 | 0 | 11 |
| dynamic_cut-B-economy | chatgpt | passed | 500 | 2 | 32.5 | 30.0 | 640.0 | 2 | 2 | 0 | 319 |
| dynamic_cut-B-economy | deepseek | passed | 500 | 2 | 37.5 | 50.0 | 1240.0 | 2 | 6 | 0 | 0 |
| dynamic_cut-B-pressure | chatgpt | passed | 500 | 2 | 40.0 | 60.0 | 1020.0 | 2 | 7 | 0 | 14 |
| dynamic_cut-B-pressure | deepseek | passed | 500 | 2 | 40.0 | 60.0 | 820.0 | 2 | 8 | 0 | 19 |
| dynamic_cut-B-archive | chatgpt | passed | 500 | 4 | 30.0 | 20.0 | 1425.0 | 2 | 9 | 0 | 26 |
| dynamic_cut-B-archive | deepseek | passed | 500 | 4 | 30.0 | 20.0 | 795.0 | 2 | 9 | 0 | 16 |
| dynamic_cut-C-economy | chatgpt | passed | 500 | 2 | 37.5 | 50.0 | 870.0 | 2 | 5 | 0 | 36 |
| dynamic_cut-C-economy | deepseek | passed | 500 | 2 | 37.5 | 50.0 | 1050.0 | 2 | 4 | 0 | 0 |
| dynamic_cut-C-pressure | chatgpt | passed | 500 | 1 | 42.5 | 70.0 | 1240.0 | 2 | 9 | 0 | 5 |
| dynamic_cut-C-pressure | deepseek | passed | 500 | 2 | 40.0 | 60.0 | 710.0 | 2 | 4 | 0 | 13 |
| dynamic_cut-C-archive | chatgpt | passed | 500 | 2 | 35.0 | 40.0 | 1665.0 | 2 | 12 | 0 | 34 |
| dynamic_cut-C-archive | deepseek | passed | 500 | 3 | 35.0 | 40.0 | 910.0 | 2 | 7 | 0 | 44 |
| dynamic_cut-D-economy | chatgpt | passed | 500 | 4 | 18.6 | 20.0 | 120.0 | 2 | 1 | 0 | 355 |
| dynamic_cut-D-economy | deepseek | passed | 500 | 4 | 22.5 | 10.0 | 1240.0 | 1 | 8 | 0 | 0 |
| dynamic_cut-D-pressure | chatgpt | passed | 500 | 2 | 45.0 | 60.0 | 540.0 | 3 | 8 | 0 | 15 |
| dynamic_cut-D-pressure | deepseek | passed | 500 | 2 | 32.5 | 30.0 | 505.0 | 2 | 2 | 0 | 203 |
| dynamic_cut-D-archive | chatgpt | passed | 500 | 4 | 30.0 | 20.0 | 880.0 | 2 | 6 | 0 | 164 |
| dynamic_cut-D-archive | deepseek | passed | 500 | 2 | 40.0 | 40.0 | 1045.0 | 3 | 7 | 0 | 14 |

## late_empty

| 局面 | 版本 | 状态 | Tick止点 | 名次 | 分 | R | D | 任务 | 死亡 | 无效 | 徘徊窗口* |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| late_empty-A-economy | chatgpt | passed | 500 | 1 | 40.0 | 40.0 | 1000.0 | 3 | 1 | 0 | 12 |
| late_empty-A-economy | deepseek | passed | 500 | 1 | 40.0 | 40.0 | 1280.0 | 3 | 3 | 0 | 0 |
| late_empty-A-pressure | chatgpt | passed | 500 | 1 | 40.0 | 40.0 | 1120.0 | 3 | 3 | 0 | 7 |
| late_empty-A-pressure | deepseek | passed | 500 | 1 | 40.0 | 40.0 | 780.0 | 3 | 3 | 0 | 2 |
| late_empty-A-archive | chatgpt | passed | 500 | 1 | 40.0 | 40.0 | 1230.0 | 3 | 6 | 0 | 11 |
| late_empty-A-archive | deepseek | passed | 500 | 4 | 40.0 | 40.0 | 600.0 | 3 | 7 | 0 | 9 |
| late_empty-B-economy | chatgpt | passed | 500 | 3 | 31.4 | 40.0 | 380.0 | 2 | 0 | 0 | 273 |
| late_empty-B-economy | deepseek | passed | 500 | 1 | 40.0 | 40.0 | 770.0 | 3 | 2 | 0 | 3 |
| late_empty-B-pressure | chatgpt | passed | 500 | 1 | 40.0 | 40.0 | 740.0 | 3 | 1 | 0 | 3 |
| late_empty-B-pressure | deepseek | passed | 500 | 1 | 40.0 | 40.0 | 930.0 | 3 | 5 | 0 | 29 |
| late_empty-B-archive | chatgpt | passed | 500 | 1 | 40.0 | 40.0 | 1520.0 | 3 | 7 | 0 | 7 |
| late_empty-B-archive | deepseek | passed | 500 | 1 | 40.0 | 40.0 | 1130.0 | 3 | 6 | 0 | 16 |
| late_empty-C-economy | chatgpt | passed | 500 | 1 | 40.0 | 40.0 | 540.0 | 3 | 0 | 0 | 232 |
| late_empty-C-economy | deepseek | passed | 500 | 1 | 40.0 | 40.0 | 980.0 | 3 | 4 | 0 | 0 |
| late_empty-C-pressure | chatgpt | passed | 500 | 1 | 40.0 | 40.0 | 1010.0 | 3 | 3 | 0 | 18 |
| late_empty-C-pressure | deepseek | passed | 500 | 2 | 40.0 | 40.0 | 570.0 | 3 | 4 | 0 | 0 |
| late_empty-C-archive | chatgpt | passed | 500 | 3 | 40.0 | 40.0 | 857.1428571428571 | 3 | 5 | 0 | 11 |
| late_empty-C-archive | deepseek | passed | 500 | 2 | 40.0 | 40.0 | 1055.0 | 3 | 6 | 0 | 8 |
| late_empty-D-economy | chatgpt | passed | 500 | 1 | 36.4 | 40.0 | 380.0 | 3 | 0 | 0 | 264 |
| late_empty-D-economy | deepseek | passed | 500 | 1 | 40.0 | 40.0 | 780.0 | 3 | 1 | 0 | 3 |
| late_empty-D-pressure | chatgpt | passed | 500 | 1 | 40.0 | 40.0 | 880.0 | 3 | 5 | 0 | 9 |
| late_empty-D-pressure | deepseek | passed | 500 | 1 | 40.0 | 40.0 | 1160.0 | 3 | 4 | 0 | 10 |
| late_empty-D-archive | chatgpt | passed | 500 | 1 | 40.0 | 40.0 | 1275.0 | 3 | 4 | 0 | 19 |
| late_empty-D-archive | deepseek | passed | 500 | 3 | 40.0 | 40.0 | 795.0 | 3 | 4 | 0 | 4 |

*徘徊窗口：连续12帧在≤4格、R/D/任务/死亡无进展的候选标签；合理防守也会触发，须看tape。

每局目录有result.json、tape.jsonl.gz和stderr；失败另存failure.cold.scene.json。完整参数见同目录冻结清单。
公告送达/授予只算观察记录；因果收益需同资格、同局面、同对手的有/无解释或动作机制配对。
