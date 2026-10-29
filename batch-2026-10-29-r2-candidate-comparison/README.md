# batch-2026-10-29-r2-candidate-comparison — R2 候选对照证据归档

I4.2 任务（review.md:358）候选对比步的证据归档。六轮对照，全部在离线竞技场（tests/run_scenarios.py + tests/arena.cpp，stage2 记分 `30*min(R/120,1)+15*min(D/500,1)+5*M`）完成；**不构成联赛证据**，只用于候选筛选。

## 内容

| 文件 | 说明 |
|---|---|
| r2_compare.py | 驱动脚本（第一→四轮；focal→strategy 代理、archive 对手脚本化、until_tick=500、per-variant 报告） |
| r2_compare5.py / r2_compare6.py | 第五轮（snake leave-one-out + rrh 席位复核）/ 第六轮（M3 冻结候选验证）驱动 |
| summary_42.json | 第一轮 42 行（new/old/rrh05/rrh10/pull8/probe0/combo × 6 现场；new 保真 6/6） |
| summary_r2.json | 第二轮 24 行（pull8probe0/oldpull/oldpullprobe0/oldprobe0 × 6 现场） |
| summary_r3.json | 第三轮 21 行（单参数消融 mev2/rmb4/rmv4/grb01/tdc025/etr0/pcc0 × 3 现场） |
| summary_r4.json | 第四轮 12 行（两参交互 mev2rmb4/mev2rmv4/mev2etr0/mev2pcc0 × 3 现场） |
| summary_r5.json | 第五轮 10 行（six_no_mev2/etr0pcc0/mev2etr0pcc0/old7_no_etr0/rrh10 × snake/wide_lanes-archive） |
| summary_r6.json | 第六轮（M3 冻结候选 mev2pcc0rmb4rmv4 验证） |
| r2_compare.log ~ r2_compare6.log | 六轮运行日志（逐格 [done] 行） |
| scenes/<case>-<variant>.json.gz | 第二轮起每变体独立报告（trace+决策+终局）；第一轮 7 变体共享 out_prefix 被末变体覆盖（已知缺陷，以 summary_42.json 为准），仅存 combo 末态 6 份 |
| scenes/*.checkpoint.json | 不归档（世界全量快照，可由报告重放再生） |

## 六轮结论摘要

- 第一轮：new 保真 6/6 位元级；old（7 参）恢复 sparse 双格 40.0 干净、snake 47.5；pull8 恢复 sparse 但 archive 格中止（脚本回放伪影，席位 B）；rrh 翻 wide_lanes T2 动作无分 → 否决；probe0 snake +5 无副作用；wide_lanes 分差参数不可达。
- 第二轮：oldpull 在 snake/wide_lanes 上 ≡ new（"旧版无门槛拉拽"假设证伪）；pull8 5/5 中止 archive 格；oldprobe0 ≡ old。
- 第三轮（消融）：sparse 恢复 = mev2 单独贡献（40.0，archive 格单独时中止）；rmb4/rmv4 单独对两家族均无效；snake +20 无单参来源（etr0 单独 +5、pcc0 单独 +3.8）。
- 第四轮（两参）：snake +20 非任何两参组合；mev2 抵消 etr0 的 +5（轨迹交互）；**mev2pcc0 三格全干净 40/40/40 + snake 31.3**（pcc0 加入后 mev2 的 archive 中止消失）。
- 第五轮（收口）：**snake +20 最小集 = etr0+pcc0 两参（47.5）**；probe 保持开启的等价路径 = pcc0+rmb4+rmv4（grb01/tdc025 为 no-op）——第五轮 old7_no_etr0 47.5 佐证；mev2 再次证实抵消 etr0 系增益；rrh10 中止席位 = **A（脚本回放，非 focal）**——夹具伪影，rrh 否决改由零收益单独支撑。
- 第六轮（冻结验证）：mev2pcc0rmb4rmv4（最小全恢复集，probe 开）× 3 现场，见 summary_r6.json。

## 关联

- 分析报告：The-Logical-Structure-of-RMT-C/docs/46-r2-candidate-comparison-2026-10-29.md（ANALYSIS 分支）。
- 场景源：~/cst/build/league/r2_plan.json + r2_run/（R2 原版计划短现场，与 docs/42 同源）。

