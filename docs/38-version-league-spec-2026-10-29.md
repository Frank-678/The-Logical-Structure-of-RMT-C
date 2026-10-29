# docs/38：stage-2 证据版本联赛规格（C7/U6 接受计划的落地设计）

> 目的：补齐 stage-2 证据缺口 —— **与原版的一局 + 自己打自己不同模型**。当前只有冠军 vs 原版标准陪练的批次对局（原版证据部分成立），没有冻结二进制的自战版本联赛（U6 判定：多 profile 自战档案不能代表旧版本或原版 robot_node）。
> 依据：review.md U6/C7 双方接受的条款（冻结 SHA+参数+独立构建+二进制哈希、144 场/版本、差分验收、报告字段、tools/ 入库）。本规格不启动任何构建/对局（内存未恢复），先冻结设计。

## §1 版本冻结清单（versions manifest）

`tools/versions.json`：

```json
{
  "champion":  {"sha": "<eb321df 位元钉>", "build_dir": "build",        "params_digest": "<match_config.hpp sha256>", "binary_sha256": "<bot sha256>"},
  "old_champion": {"sha": "<前冠军提交>",      "build_dir": "build-v-old", "params_digest": "...", "binary_sha256": "..."},
  "candidate": {"sha": "<候选提交>",           "build_dir": "build-v-cand", "params_digest": "...", "binary_sha256": "..."}
}
```

每个版本一个**独立构建目录**（colcon `--build-base build-v-X --install-base install-v-X`），二进制 sha256 冻结；同一版本在全部对局中位元不变。选手参数只在 match_config.hpp（编译期），无运行时参数注入 —— 席位/令牌也是 constexpr（team="A"、ai_token="practice-A"），故自战第二席位 = **同源码换席位重建**（team="B"、practice-B；"能写死就写死"合规）。每版本构建 4 个席位变体（A/B/C/D），由构建脚本临时改头文件→build→还原（与 holdoff 批次同款流程，见 docs/36 工具链）。

## §2 对局调度（tests/version_league.py，统一批量调度器）

**144 场/版本起步 = 12 图 × 4 席位 × 3 对手混合**：

| 混合 | A | B | C | D | 证据类型 |
|---|---|---|---|---|---|
| M1 原版 | 本版本 | 原版陪练 | 原版陪练 | 原版陪练 | vs 原版（stage-2 要求一局的放大版）|
| M2 自战·旧冠军 | 本版本 | 旧冠军（冻结二进制）| 原版陪练 | 原版陪练 | self-play 不同模型 |
| M3 自战·候选 | 本版本 | 候选（冻结二进制）| 原版陪练 | 原版陪练 | self-play 不同模型 |

- 12 张图 = 固定 12 个 practice seed（driver 地图生成由 seed 确定性导出，12 seed 一次性选定并随清单冻结）。
- 4 席位 = 本版本轮换出生席位（每图每混合各 1 局，席位轮换消出生位置偏差）。
- 原版 = practice 包自带 robot_node（标准陪练，原版裁判内）；陪练经裁判网关，本版本/旧冠军/候选经各自 real LLM 网关（deepseek-flash）。
- 每局 ~5 分钟真实对局；144 场/版本 ≈ 12 小时。**先 24 场试点**（2 图 × 4 席位 × 3 混合）验证调度器与双选手同场（两个席位同时跑我们自己的二进制 + 各自 LLM 网关）后再放量。

## §3 报告与归档字段（U6 条款 + review.md:58）

每局归档：代码 SHA、完整参数（params_digest）、AI 模式、session_id、最终名次、score/R/D/M/hp/invalid。版本级报告：原始分、平均名次、首末位比、R/D/M 均值、无效动作、死亡数、卡住、超预算；**按初始地图成组**，保留最差样本。全部随批上传 log 分支（沿用 batch 归档 10 件套 + README 协议）。

## §4 短序列差分验收 vs 原版 practice（U6 条款）

向原版 practice 与自建引擎输入**相同合法动作序列**，核对攻击/死亡/重生/增益时序与分数。风险：自建引擎与原版共享 rules.hpp 可能共享同一错误 → 差分只作一致性证据，不替代原版对局。practice 原文件保持只读，测试驱动/临时配置/结果放外部（沿用 18 号文档先例）。

## §5 里程碑与当前阻塞

1. **内存恢复** → 还原冠军二进制（holdoff 1.0→0.0 + rebuild，恢复位元钉）→ 跑 12 场景回归（工具已采纳未验证）。
2. tools/ 入库：batch_practice.py、归档/筛选/验证脚本随批迁入代码仓 tools/（U6 承诺）。
3. 版本联赛调度器 + 席位变体构建脚本 → 24 场试点 → 放量 144×3 版本。
4. rrh10 battle 3–6 续跑（--only 3..6，与联赛独立）→ docs/37 §7 裁决。

stage2 目标 50 的当前锚点：训练集 41.25；联赛数据将给出原版/自战维度的真实名次与分数分布，作为 50 分验收的第一手证据。
