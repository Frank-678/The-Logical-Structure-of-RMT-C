# docs/40：版本联赛启动 + 试点预注册（2026-10-29）

> 状态：**完成**（2026-10-29 17:25 +0800 开跑 → 18:37 全部 16 局完成，16/16 ok、invalid 全 0；设计与承诺见 §3，执行记录见 §4，结果入 docs/44）。
> 前情：docs/38 冻结联赛规格（144 场/版本 = 12 图 × 4 席位 × 3 混合，U6/C7 双方接受条款）。docs/39 关闭第 16/17 家族后，待评估队列清空、无候选版本 —— M3 自战·候选推迟，先跑 M1（vs 原版）与 M2（自战·旧冠军）。
> 依据：用户指令"短时间多测"（review.md 8da0ede）；U6 承诺 tools/ 入库。

## §1 工具链入库（U6 承诺兑现，tools/ 六件套）

| 文件 | 职责 |
|---|---|
| `tools/batch_practice.py` | 去密钥多席位批量驱动：`--our SEAT:INSTALL_BASE` 可重复（自战两席），席位日志由 run_seat.sh 管；新增 `--map-locked` 模式（同图同事件日程、4 局仅轮换出生席位，实现 docs/38"按初始地图成组"） |
| `tools/run_seat.sh` | 席位启动器：`bash tools/run_seat.sh <base> <seat> <log>`，节点名重映射 `rmtc_bot_<seat>` 解决双实例 ROS 命名冲突（不动源码、不重建冠军二进制） |
| `tools/build_seat_variants.sh` | 席位变体构建：临时改 match_config.hpp team/token → colcon 独立底座 → 还原 + sha256 校验 → 清单记录 |
| `tools/archive_batch.py` | 批次归档：10 件套拷贝 + 密钥形状扫描（sk-cbc+≥8hex，命中即中止）+ README 战报表 |
| `tools/versions.json` | 冻结清单：12 图 seed、版本身份（sha/params_digest/binary_sha256）、席位变体记录 |
| `tests/version_league.py` | 联赛调度器：逐 (图, 混合) 驱动 --map-locked --count 4；开赛前冻结契约校验（参战二进制 sha256 与清单不符即中止） |

密钥管理：驱动只读 `PRACTICE_LLM_KEY` 环境变量或 `~/.rmtc-practice/llm.env`（仓库外、600 权限），仓库内零密钥。

## §2 冻结身份（2026-10-29 实测）

| 版本 | SHA | params_digest（match_config.hpp） | 参战二进制 |
|---|---|---|---|
| champion | eb321df | b1efdbc4…07c7 | install/ bot sha256 39557aa1…9052（位元钉，此前 4 次逐位复现） |
| old_champion | 9bc72a7（= d795e16^，post_cap 晋升前冠军） | d9cd2a2f…4962 | install-v-old_champion-B bot sha256 bcebb860…9bf1e（team="B"/practice-B 席位变体，构建时 header 还原校验一致） |
| candidate | —（17 家族全关，无候选） | — | — |

12 张联赛图 = seed 20261201…20261212（随清单一次性冻结）。old_champion 源树 = `git worktree add --detach /home/frank/cst-league-old 9bc72a7`，worktree 头文件 digest 与清单逐位一致。

## §3 试点预注册（24 场规格的 M3 推迟版 = 16 局）

**执行**：M1 + M2 × 前 2 张图（seed 20261201、20261202）× 每 (图,混合) 4 局席位轮换 = **16 局真实对局**（deepseek-flash，约 90 分钟）。每局约 5 分钟、500 tick。

| 混合 | A | B | C | D | 证据类型 |
|---|---|---|---|---|---|
| M1 原版 | champion | 原版陪练 | 原版陪练 | 原版陪练 | vs 原版（stage-2 要求） |
| M2 自战·旧冠军 | champion | old_champion（冻结二进制） | 原版陪练 | 原版陪练 | self-play 不同模型 |

**设计承诺（先冻结）**：
1. 同图同日程只轮席位（--map-locked）：同图内 4 局差异仅出生席位，消出生位置偏差；跨混合同 seed 同图（rng 消耗一致）。
2. 开赛前冻结契约校验：champion 与 old_champion-B 二进制 sha256 必须等于清单值，不符即中止（U6 条款）。
3. 报告字段（U6 条款 + review.md:58）：每局 session_id、AI 模式、最终名次、score/R/D/M/hp/invalid；版本级按初始地图成组，保留最差样本。
4. 全部归档 log 分支（10 件套 + README），分析入 docs/42。
5. 预注册判定规则：champion vs 原版的每局名次与得分分布 = stage-2"原版证据"第一手数据；champion vs old_champion 的 R/D/名次差分 = post_cap 晋升（+0.02 combat weight）在真实对局尺度的验证。**试点目的只验证调度器与双选手同场**，不做任何晋升裁决（放量 144 场才做）。

## §4 执行记录

- **smoke（开跑前）**：M2 双席位同场冒烟通过——champion 与 old_champion-B 两 ROS 节点同场注册（节点名重映射 `rmtc_bot_<seat>`，不动源码）、旧二进制与现行裁判 API 兼容、invalid 0；修复 run_seat.sh 管道孤儿进程问题（4a69bad，进程组回收）。
- **冻结契约校验**：17:25:34 两参战二进制 sha256 与清单逐位一致（champion 39557aa1…9052 / old_champion-B bcebb860…9bf1e）。
- **开跑**：2026-10-29 17:25 +0800，16 局（M1 原版 + M2 自战·旧冠军 × seed 20261201/20261202 × 4 席位轮换，--map-locked 同图同日程），deepseek-flash。
- 进度快照（17:39）：3/16 完成。M1×20261201 前三局 champion（A 席）：score 40.0 / 40.0 / 50.0，名次第 3 / 3 / 1，hp 100 / 100 / 20，D 875 / 1340 / 1110，invalid 全 0。
- **结果汇总与裁决分析：docs/44（2026-10-29 完成；docs/42/43 已被 ChatGPT 占用，路径由 docs/42 改为 docs/44，勘误如下）**；归档：log 分支（tools/archive_batch.py 10 件套 + 密钥扫描，提交 7aa8076）。
- **收尾（18:36:57 rc=0）**：16/16 完成，invalid 全 0，唯一死亡 = 01·M2 v3 D 席原版陪练（hp0）。champion 16 局均分 45.9375、rank1 6/16；vs 原版（M1）均分 47.1875；vs old_champion（M2）头对头 4 胜 2 负 2 平、总分 0——无晋升主张（详见 docs/44）。赛后复核参战二进制 sha256 与清单一致（champion 39557aa1…9052）。
- **路径勘误（追加，不改写预注册原文）**：§3 第 4 点承诺"分析入 docs/42"——因 docs/42/43 被 ChatGPT 占用（其 288 局离线报告），试点分析实际入 **docs/44**（2f98fc2 C9 已声明）。§1 表内 archive_batch.py"密钥形状扫描（sk-cbc+≥8hex）"为早期口径，现行 tools/archive_batch.py 已升级为通用 KEY_RE 形状扫描并覆盖单文件。
- **本批身份边界（I4.1 采纳）**：本批为旧驱动（tests/version_league.py 合并前状态）产物；正式证据按新路径 `bash practice_league.sh --maps 20261201,20261202 --mixes M1,M2 --out build/practice-league/pilot-new` 重跑（执行中）。
- **位元钉口径勘误（追加）**：§2 表"位元钉，此前 4 次逐位复现"——bot 二进制嵌入 `__DATE__`/`__TIME__`（bot.cpp Ready 行，8fc7c65 起），跨秒全量重建 sha 必变（仅时间字符串差异，源码/params 逐位一致）；重跑前实测干净重建 789f333d… ≠ 39557aa1…，详情见 docs/44 §6 勘误。U6 冻结契约按在场 sha 校验，不受影响。
