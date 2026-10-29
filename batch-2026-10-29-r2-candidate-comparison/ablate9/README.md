# 第九轮四格消融（grb × tdc）——tdc 死参数实证（2026-10-29）

驱动：`r2_compare9.py`（`cd ~/cst && python3 build/league/r2_compare9.py`）。
基座 = M3 冻结五参数（mev2/pcc0/rmb4/rmv4），四格 = grb{0,0.1} × tdc{0,0.25}；
现场 snake-A-pressure / sparse-A-economy / sparse-A-archive。

- `summary_ablate9.json`：12 行结果（R/D/deaths/completed/first_diff 等）。
- `receipt_bitwise.json`：6 对（case × grb）tdc0 vs tdc025 的 500 tick 全 trace 逐位比较 → **6/6 equal**；
  终局 R/D/deaths/completed/hp/invalid 亦全等。tdc 在候选变体中为死参数（代码依据 docs/48 §2.1）。
- `reports/*.json.gz`：12 份场景报告 + 12 份 checkpoint（gzip 原件）。

结论：M3 冻结由六参数修订为五参数（tdc 剔除，行为零漂移）；snake 37.5→47.5 为 grb=0.1 单独贡献。
