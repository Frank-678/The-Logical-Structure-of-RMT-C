# docs/48 · 联赛 192 场预注册与 M3 冻结修订（tdc 死参数剔除 + M4 焦点位）· 2026-10-29

**状态**：预注册（开赛前）。本文件先于联赛启动落盘；结果另文分析。
**上游依据**：ChatGPT CG-C-20261029-HANDOFF-FINAL（review.md，2026-10-29 22:59 +0800）第 1/2/5/8 条。
**关联**：docs/46（R2 八轮收口）、docs/47（scale-96 部分批）、summary_ablate9.json（log 分支）。

## 1. 摘要

1. **M3 冻结修订（六参 → 五参）**：代码核查发现 `tactical_search = false`（match_config.hpp:78），
   `tactical_choice` 唯一调用点（strategy.cpp:1438）在该门内 → **tactical_death_cost（tdc）为死参数**。
   第九轮四格消融（grb×tdc）实证：tdc 0.0 与 0.25 在全部 6 组（3 现场 × 2 grb 格）逐 tick 动作序列与终局
   **逐位一致**。tdc 从冻结集剔除；候选行为不变（死参数），docs/46 §6 的"grb/tdc 组合必需"结论修正为
   **grb=0.1 单独贡献**（snake 37.5→47.5）。
2. **M4 焦点位混合新增（144 → 192 场）**：依 HANDOFF 第 1 条——只给 M3 增加对手位不能替代候选作为
   焦点版本与冠军在相同地图/席位/对手池的成对比较。新增 M4：A=candidate、B=champion（席位变体）、
   C/D=原版陪练，与 M1 同 12 图同 A 席位同对手池。
3. **测试器修复**（HANDOFF 第 5 条）：referee 启动重试的 Ready 判定改为每次尝试独立基线（防上一尝试
   残留行误判就绪）；联赛聚合退出码提取为 `batch_exit_code` 并补回归测试（缺局/失败组/空计划 → 1）。
   第 5 条其余项（终局 hp=0 死亡口径、M2 日志勘误、官方排名顺序重核）另文答复，不阻塞联赛。

## 2. tdc 死参数核查与第九轮四格消融

### 2.1 代码证据
- match_config.hpp:78 `tactical_search = false`（本轮训练选中关闭）。
- strategy.cpp:1411 门：`if (stage_ == 2 && parameters_.tactical_search && …)`；:1438 唯一调用
  `rmtc::tactical_choice(input, parameters_)`。
- tdc 唯一使用点 tactics.cpp:170（`value()`，仅被 tactical_choice 内部调用）。
- 结论：候选与全部 R2 变体（tactical_search 未动）中 tdc 均不执行。docs/46 §6 原"grb01/tdc025
  组合必需（rounds 5 vs 6 差分）"归因错误——差分实为 grb01 单独贡献；§6 勘误已追加（见 docs/46）。

### 2.2 第九轮四格消融（build/league/r2_compare9.py；summary_ablate9.json）
基座 = M3 冻结五参数（mev2/pcc0/rmb4/rmv4），四格 = grb{0,0.1} × tdc{0,0.25}。
现场：snake-A-pressure / sparse-A-economy / sparse-A-archive（同 docs/46 口径）。

| 变体 | snake R/D/deaths | sparse-e R/D/deaths | sparse-a R/D/deaths |
|---|---|---|---|
| grb0_tdc0 | 30.0/460.0/7 | 40.0/780.0/2 | 40.0/630.0/0 |
| grb0_tdc025 | 30.0/460.0/7 | 40.0/780.0/2 | 40.0/630.0/0 |
| grb01_tdc0 | 70.0/540.0/9 | 40.0/780.0/2 | 40.0/580.0/0 |
| grb01_tdc025 | 70.0/540.0/9 | 40.0/780.0/2 | 40.0/580.0/0 |

- tdc 0.0 vs 0.25：6/6 组动作序列逐位相等且终局逐位相等 → **死参实证**。
- grb01_tdc0 复现第 6~8 轮 old7_no_etr0 全部结果（snake 47.5 / sparse 40+40 竞技场分）→
  五参数集与六参数集行为一致，冻结修订零行为漂移。
- grb 0.0 → 0.1：snake 竞技场分 37.5 → 47.5（R 30→70），sparse 不变（40/40，archive D 630→580 同分）。

## 3. M3 冻结修订后的参数集（五参数）

```
mission_explore_value 2.0 / post_cap_combat_weight 0.0 / resource_mission_bonus 4.0
/ reach_mission_value 4.0 / goal_retention_bonus 0.1
```
探针 explore_toward_resource_value 0.5 不动；tactical_search 不动（false）。
行为类默认关闭：不进入默认配置，仅在联赛 M3/M4 席位以参数集形态上场。

## 4. 席位变体与冻结契约

| 席位 | 二进制 sha256 | params_sha256 | 源 |
|---|---|---|---|
| champion-A（install） | 39557aa1…（在位钉，逐局校验） | b1efdbc4… | eb321df |
| champion-B | 98aec3f3… | 5df1b351…（original=b1efdbc4…） | eb321df worktree + 仅 team/token 改写 |
| candidate-B（M3 对手位） | dd77411f… | bca6f974… | 当前源码 + 五参数覆盖 |
| candidate-A（M4 焦点位） | d76489d8… | 903ec32b… | 当前源码 + 五参数覆盖 |

开赛前 `verify_frozen` 逐席位校验在场 sha = 清单，不符即中止。

## 5. 联赛预注册：192 场

`bash practice_league.sh --maps 20261201..20261212 --mixes M1,M2,M3,M4`
12 seed × 4 席位轮换 × 4 混合 = **192 场**（M1 48 / M2 48 / M3 48 / M4 48）。
- M1 原版基线：A=champion vs 原版陪练。
- M2 自战旧冠军：A=champion vs B=old_champion。
- M3 自战候选·对手位：A=champion vs B=candidate。
- M4 自战候选·焦点位：A=candidate vs B=champion（与 M1 同图同席位同对手池的成对比较）。
评估口径（stage2）：`30*min(R/120,1)+15*min(D/500,1)+5*len(completed)`；全部对局以 M1 为基线、
M2 为自战参照、M3+M4 为候选证据（对手位+焦点位成对）。失败组/缺局聚合退出码非零并如实记录。
route A（etr0+pcc0+探针关）保留为 R2 离线对照臂，不进入本轮联赛席位（HANDOFF 第 1 条"作为对照保留"
以离线矩阵形式兑现，见 docs/46 与后续消融）。

## 6. 工具修复清单（本文件对应提交）

1. tools/batch_practice.py：Ready 判定每次尝试独立基线（referee_ready_since）。
2. tests/practice_version_league.py：M4 混合 + batch_exit_code 提取。
3. tools/build_seat_variants.py：冻结树补 tests/（BUILD_TESTING 引用 ../../tests）+ colcon 显式
   source ROS（login shell 不保证环境）。
4. tests/practice_tools_test.py：+3 回归（聚合退出码 6 断言、Ready 独立基线 4 断言、colcon 调用形态）。
   全部 14 测试通过。

## 7. 已知未决（不阻塞本轮联赛）

- wide_lanes 代码层定位（HANDOFF 第 3 条：旧侧 65c87145…，tick-10 前缀二分，比较驱动迁 tools/）。
- 原版 ROS 脚本差分适配器（HANDOFF 第 4 条）。
- 终局 hp=0 而死亡 0 的口径核对、旧 16 局 M2 日志勘误、官方排名顺序重核（HANDOFF 第 5 条）。
- 贵方 log 批次 batch-2026-10-29-chatgpt-offline/ 尚未见于 log 分支（截至本文件 fetch）。

---

*密钥扫描通过（本文件不含密钥；扫描命令输出另存于 log 批次）。*
