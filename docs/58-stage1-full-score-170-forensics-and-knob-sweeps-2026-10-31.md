# Stage1 满分专项：170 伪影验尸 + 修正重建链 + 三旋钮 relaxed 扫描

日期：2026-10-31。任务 #22（stage1 满分专项）。本文记录三件事：①三个变体扫描出的 170 伪影的完整验尸与修复；②修正后 stage=1 重建链的验证门结果；③三旋钮（ring/flood/tour）31 图 relaxed 扫描结果与对比基线 19/31 的结论。另附正式赛两阶段切换的协议核实（P0 决议）。

## 1. 170 伪影验尸（stage 编译期漏 sed）

### 1.1 现象

- 基线 install_stage1（stage1 专项构建）官方练习图 R=200 满分。
- 10-31 00:16 建成的三变体（ring 1.0 / flood 0.1 / tour 0.06，install_stage1_*）在官方图上全部 R=170；控制组（新构建、默认参数、install_stage1_control）同样 R=170。
- 基线-now（同一 install_stage1）与 control（同一源码新构建）间隔数分钟先后跑官方图：200 vs 170。

### 1.2 判别链（三路对照）

| 局 | 二进制 | 官方图 R | 结论 |
|---|---|---|---|
| probe/ring | install_stage1_ring（新构建） | 170 | 伪影与旋钮无关 |
| baseline-now | install_stage1（旧构建） | 200 | 基线无退化 |
| control | install_stage1_control（新构建，默认参数） | 170 | 伪影=构建过程，非参数 |

构建标志对照：Debug vs 空 build type 仅差 `-g` 编译标志（flags.make 逐行 diff），排除。

### 1.3 验尸三件套定位根因

同一官方图两局 bot.log 的 mode 行：

| 局 | mode | ai |
|---|---|---|
| 基线（200） | `mode=collecting` | `ai=disabled_missing_url_and_token` |
| control（170） | `mode=combat_ready` | `ai=requesting/timeout` |

`mode=combat_ready` 说明 bot 以 **stage2 战斗逻辑**运行。代码链：match_config.hpp:8 `inline constexpr int stage = 2` 是编译期值 → bot.cpp:33 `const int stage = cfg::stage` → session.cpp:8 `Session(int stage, AiConfig config) : strategy_(stage), ai_(stage == 2 ? ... : AiConfig{})`。R(t) 曲线分叉（rtrace.py）：基线 t51→t88 稳步 130→200；control t63 后停滞 170 直到终局（21 tick 零拾取）——stage2 的资源串策略在 stage1 图（只有 move/wait、任务分 40 上限）下放弃继续采集。

**根因**：重建脚本只 sed 了域号和三个旋钮数值，**漏 sed `stage = 2`→`= 1`**。install_stage1 是 stage1 专项构建（当时 sed 了 stage），四个新构建全是 stage=2。旋钮（ring/flood/tour）无罪；三变体此前扫描数据（全部 170）作废。

### 1.4 修复与验证门

/tmp/rebuild_variants_28.sh 增加 stage sed（及 trap 反向还原），重建 4 个 install_stage1_*（stage=1 + 域 28）。验证链（全 && + 探针闸，链 bhuw6svdb）：

1. **probe（ring 二进制，官方图）**：我的裁判见注册 ✓、用户日志零增量（delta=0）✓、first_own_tick=2 ✓、**R=200 FULL** ✓。
2. **mode 门**：bot.log 两帧 `mode=collecting ai=disabled_missing_url_and_token` ✓（stage1 确认编译进去）。
3. **control 门（官方图）**：`control RESULT R=200 invalid=0 FULL` ✓——**新构建与基线等价坐实，170 伪影彻底关闭**。

## 2. 三旋钮 relaxed 扫描（31 图：official + w8/w12 × 5 styles × seeds 11/23/47）

扫描器 /tmp/sweep_hyg2.py（卫生驱动，双向门，无 official 中止护栏）。基线参照：19/31 FULL（18/30 formal + official，弱图 spread 0/6、edge-47、w8-uniform 三图 190、w12-uniform-23 170）。

### 2.1 ring（stage1_ring_value 0.0→1.0，近出生点环加成）

结果（31 图，每图 1 局）：**18/31 FULL（17 formal + official）**，基线 19/31。逐图对照：30 图与基线逐位一致，唯一变化 **w12-edge-23 200→190（−10）**；全部 12 个弱图无一提升（w8-uniform 三图仍 190、w12-uniform-23 仍 170、spread 六图仍 140-170、edge-47 仍 140/160）。

**结论：ring=1.0 零增益、一图退化 → 维持默认 0.0（关闭），不晋升。** 近出生点环加成在 relaxed 图集上没有兑现 rooms-195 的修复预期。

### 2.2 flood（stage1_flood_value 0.0→0.1，最近边界洪泛）

结果：**19/31 FULL**（与基线同数），7 图提升 vs 4 图受损：

| 图 | 基线 | flood 0.1 | 差 |
|---|---|---|---|
| w8-uniform-23 | 190 | **200** | +10 |
| w8-uniform-47 | 190 | **200** | +10 |
| w8-edge-47 | 140 | 170 | +30 |
| w8-spread-11 | 150 | 180 | +30 |
| w8-spread-23 | 160 | 170 | +10 |
| w8-spread-47 | 140 | 180 | +40 |
| w12-uniform-23 | 170 | **200** | +30 |
| w8-edge-23 | 200 | 180 | **−20** |
| w12-edge-11 | 200 | 110 | **−90** |
| w12-edge-23 | 200 | 190 | −10 |
| w12-edge-47 | 160 | 150 | −10 |

**0.1 剂量不可晋升**：spread 全家（3/6）+3 弱图显著受益，但 edge 系列受损（w12-edge-11 直接崩到 110，w8-edge-23 丢满分）。**剂量响应跟进**：0.05 / 0.02 同 11 图扫描（链 b30c6vain）——洪泛过强会把边界空档拖离 edge 图的资源走廊，找"只赢不亏"的剂量。

### 2.3 tour（explore_tour_value 0.03→0.06，边界巡回）

结果：**20/31 FULL（+1）**，唯一变化 **w12-uniform-23 170→200**，其余 30 图与基线逐位一致，**零损失**。单局噪声风险：w12-uniform-23 ×3 复验进行中（tour_rep1/2/3）；若三局全 200 → 晋升 0.03→0.06。

### 2.4 对比与组合结论

（收批中：tour 复验×3 + flood 0.05/0.02 剂量 11 图扫描，链 b30c6vain。当前中间结论：ring 不晋升；flood 0.1 不晋升；tour 待复验。若某 flood 剂量"只赢不亏"且 tour 复验通过 → 组合变体（tour 0.06 + 该剂量）跑全 31 图再终审；行为类改动默认关 → 有晋升证据才写回默认值）

## 3. 正式赛两阶段切换核实（P0 决议）

- 协议 v1.2 §3 感知字段表：无 stage 字段（tick/session_id/vision_radius/self/visible_entities/score/mission_text/missions/map/event_text）——程序无法从感知判定阶段。
- 规则 v1.2 §2.3：每个正式阶段开始前确认代码版本；「第一阶段全部结束后设置统一调整窗口，可修改参数、Prompt 和任务解析逻辑；窗口结束后重新确认第二阶段版本」。
- 结论：**编译期 stage 是官方预期设计**。已落地：README「两阶段切换」章节 + tools/build_stage.sh 1|2（一键 sed+重建，build/rmtc_bot/match_config.sha256 供版本确认）+ docs/57 功能表更新。启动始终 `bash run.sh`，裁判由主办方按 --stage 启动；阶段间窗口内执行 `bash tools/build_stage.sh 2`。
- decision_type 登记（§2.3，可选）：决定不实现不使用，技术报告注明。原因：行为类改动临近截止日风险大于现场人工切换收益；每场最多 2 次人工切换为可选能力而非义务。
