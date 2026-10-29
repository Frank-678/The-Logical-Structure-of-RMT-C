# 34. lowhp 轮：低血量攻击折扣（low_hp_attack_discount，2026-10-29）

> review.md T5 处方："先找一条明确损失路径，再写一个小改进与一组配对反例。" 损失路径 = docs/33 §5-7（53 死亡中 40 例最后动作为攻击且 hp<60、12 例死亡 tick 存在一步安全方向、8 例可撤退，配对反例见 docs/33 §6）。本档案 = 那个小改进（杠杆）的 train 证据与预注册 heldout 判据；heldout 结果与裁决在判据之后补写。

## 1. 杠杆设计

- `low_hp_attack_discount`（match_config.hpp 默认 **1.0** = 旧行为，冠军逐位一致）。
- 语义：**自身 hp < 60 且本 tick 未被火力波及（incoming==0）时，攻击估值乘此值**；还手不折扣（不白挨打，与 pie 折扣同型）；hp≥60 与 incoming>0 完全不受影响。
- 两处落点（同口径）：
  1. strategy.cpp §6 攻击估值：`utility *= parameters_.low_hp_attack_discount`（pie 折扣之后、致命检查之前）；
  2. tactics.cpp 束搜索：深度 0 的 attack 分支 `child.utility *= p.low_hp_attack_discount`。
- 配套：strategy_parameters.hpp（成员 + competition() + validate() 0..1 范围）；arena_main.cpp（PARAMETER + competition_dump）；eval_levers.py 新组 `lowhp`。
- 逐位一致保证：默认 1.0 → 两处 `if` 永不触发。train 结果中 stage-1 四个 profile 逐位相同（33.33 / R166.67 / 0 死，见 §5）即直接证据（stage-1 无对手、杠杆 stage-2 门控，兼作冠军一致性探针）。

## 2. 扫描规模

sweep {0.7, 0.4, 0.1} + base_off（冠军基线）；train 全量 24 场景（12 stage-1 + 12 stage-2），协议同前（selection_guards：invalid==0、stage1 ≥ baseline_stage1−1；heldout 仅对选中者评估一次）。

## 3. 预注册判据（写于 heldout 运行前，heldout 正在后台运行）

1. **train 选择**：满足 selection_guards 的候选中取 train objective 最高者。
2. **heldout 晋升判据**：选中者的 heldout objective ≥ **冠军封存 0.8299**（arena-postcap-heldout-2026-10-29，同 30 场景；docs/32 §7.3 参考系）。冻结 baseline 行必须逐位复现 **0.7710073**（确定性钉），否则本次 heldout 作废重跑。
3. 不达标 → 家族关闭，保持 1.0，不作第二次 heldout。

## 4. train 结果（tests/results/levers-lowhp-2026-10-29.json）

| profile | objective | invalid | deaths | blocked | stage1 score | stage2 score | stage2 R | stage2 D | stage2 deaths | stage2 win_share |
|---|---|---|---|---|---|---|---|---|---|---|
| base_off（冠军） | 0.7971 | 0 | 83 | 93 | 33.33 | 41.25 | 60.0 | 1026.7 | 6.92 | 0.333 |
| lhp07（0.7） | 0.7933 | 0 | 87 | 100 | 33.33 | 40.83 | 58.3 | 1015.8 | 7.25 | 0.333 |
| lhp04（0.4） | **0.8113** | 0 | 86 | 160 | 33.33 | 41.88 | 64.2 | 912.1 | 7.17 | 0.417 |
| lhp01（0.1） | 0.8042 | 0 | 76 | 181 | 33.33 | 41.06 | 64.2 | 750.0 | 6.33 | 0.417 |

- **stage-1 四 profile 逐位一致**：杠杆未触及 stage-1，冠军一致性探针通过。
- **lhp04 最优**（+0.0142）：win_share 0.333→0.417（名次翻转）、stage2 R +4.2、score +0.63；代价 D −114.6、deaths +0.25、blocked +67。
- **lhp01**（+0.0071）：win_share 0.417、deaths 6.33（低于冠军 6.92）、R +4.2；但 D 750、blocked 181 最高。
- **lhp07 微负**（−0.0038）：轻微折扣只把攻击换成走动，没换来名次。
- 形状：折扣强度与 deaths/D 反相关，0.4 为 train 平衡点。**收益机制不是存活**（lhp04 deaths 反升）——是低血量弃战→转采集（R +4.2）与名次翻转。
- 既往提醒：L-c 的 train +0.0113 在 heldout 上为噪声（−0.039 vs 冠军封存）；本轮 +0.0142 同量级，**由 heldout 一次性裁决**，train 数字不作结论。

## 5. heldout 与裁决

（heldout 运行中；结果与裁决按 §3 判据补写，不回头改判据。）
