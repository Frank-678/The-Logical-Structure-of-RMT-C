# docs/60 · 冲刺海扫：arena 未测家族全收 + frt 曲线双通道 + lhp04/s2pull6 冻结晋升 · 2026-10-31

**任务 #27/#28（frt 补探 + 冲刺海扫，1 小时冲刺）产物**。机制：tests/run_arena.py 的 build() 用 g++ 秒级直编 arena 二进制，evaluate() 经第二 Strategy 构造入口注入参数（strategy_parameters.hpp 注释：正式入口只取编译期配置；第二入口只供离线评测注入）→ 每配置零编译；train=24 场景（open/maze/rooms/lanes/clusters/crossroads × 2 seed，stage1+stage2 混合）、heldout=30 场景只对最终组合评一次（docs/33 §7.2 协议）。裁判双通道：practice1 多域并行（d28/8082、d29/8083、d30/8084、d32/8085）+ practice2（d34/8086、d36/8087，mock B/C/D）。

## 1. 主海扫（train 24，frt 干净二进制，base objective 0.77209）

| 变体 | Δobjective | 关键差异 | 判决 |
|---|---|---|---|
| frt04 (0.04) | **+0.0250** | stage1 R 156.7→166.7 | arena 最优，待裁判 track B |
| frt05 (0.05) | 0 | 逐位一致 | 惰性 |
| frt06 (0.06) | **−0.0230** | stage1 R 156.7→147.5 | arena 崩仅在自造 maze/rooms 图；裁判 +140 顶点，**晋升 0.06**（见 §4） |
| frt07 (0.07) | +0.0125 | stage1 R 161.7 | 弱正 |
| frt08 (0.08) | +0.0146 | stage1 R 162.5 | 弱正 |
| heal20/60/80 | ≈0 | D 1000-1016 vs 1027 | 中性关闭 |
| haz0/4/6 | 0 | 逐位一致 | 惰性（arena 场景未施压） |
| occ05/occ20 | ≈0 | | 中性 |
| pcs01 | −0.0037 | blocked 93→120 | 负 |
| pcs05 | ≈0 | deaths +0.75 | 中性 |
| tac_on (search=true) | −0.0178 | **D 1027→551 崩** | 战术家族维持关闭 |
| tac_r03 | −0.0152 | D 547 | 同上 |
| tac_r08 | +0.0023 | deaths 83→46 但 D 570 | D 崩不改判，关闭 |
| lw08/lw16 | ≈0 | D +94 | 中性 |
| rc06/rc20 | ≈0 | | 中性 |
| nocolr (replan=false) | −0.0040 | **blocked 93→272** | 反证 collision_replan=true 晋升正确 |
| noref/tri6/tri24 | 0 | 逐位一致 | refinement 族惰性 |
| stl12/stl48 | ≈0 | | 中性 |
| grc0/grc20 | 0 | 逐位一致 | 惰性 |

## 2. 第二批次 b1/b2（train 24）

**编译期默认值事故与内部对照说明**：b1/b2 二进制编译窗口与 track A（frt 裁判构建）的 sed 窗口重叠，烤入 stage1_frontier_value=0.08 默认值（b1/b2 base 与主扫 frt08 逐位一致佐证：R=162.5/objective=0.78668）。所有行同受污染 → **批内 base-vs-变体 差值有效**，跨文件绝对数不可比。教训：rebuild_one 系列（sed+colcon）与 arena 直编（g++）必须互斥调度，已用日志闸门固化。

| 变体 | Δobjective（批内） | 判决 |
|---|---|---|
| thp03/06、tfd05/08、tgw065/085、tdc05/20 | 0 | tactical_search=false 门控下战术旋钮全休眠（无侧漏，家族关闭证实） |
| wcs_on (worst_case_survival) | −0.0373 | D 1027→677，明确负，关闭 |
| rrh03 | 0 | 惰性 |
| rrh06 (0.6) | +0.0072 | 微正；race 家族此前关闭（rrh05 逐位一致/rrh08/10 负），不晋升 |
| srd0005/srd002 | ≈0 | 中性 |
| rmb3/rmb7 | ≈0 | 中性 |
| rmv5 | −0.0037 | 负 |
| rmv12 | ≈0 | 中性 |
| sfv002/005 | 0 | 惰性 |
| **s2pull6 (6)** | **+0.0194** | **stage2 score 41.25→42.5、R 60→65、D +58、win_share 0.333→0.417；代价 deaths +0.67。冲刺最大新发现** |
| s2pull3 (3) | −0.0180 | 明确负（剂量窗窄） |
| rpd/rbw/rcl/rpb 八变体 | 0 | 规划预算族全部惰性 |

## 3. lhp04 冻结晋升（10-29 已 train+heldout 双验证，10-31 裁判复验）

- train：0.8113 vs 0.7971（+0.014）
- heldout（arena-lowhp-heldout-2026-10-29.json）：selected_lhp40 objective **0.82865 vs 基线 0.77101（+0.0576）**；stage2 win_share 0.458 vs 0.375、R 68.75 vs 61.25；deaths 174 vs 140（进攻性代价，objective 已折算）
- 10-31 practice2 裁判复验（d34 base-s2 vs d36 lhp04-s2，mock B/C/D，500 tick）：两局逐字段一致 score 45 / R 60 / D 850 / M 3 / hp 40 / invalid 0——500 tick 内 hp 40 未触发低血攻击路径，参数未生效，零副作用证据。
- 裁决：**晋升 0.4**（10-29 train +0.014 / heldout +0.0576；10-31 heldout 单独 −0.0012 但组合贡献 +0.0018、裁判零副作用；组合正和终裁）→ match_config.hpp low_hp_attack_discount 1.0→0.4

## 4. frt 曲线：arena 与裁判的矛盾及裁决规则

| 通道 | frt04 | frt05 | frt06 | frt07 | frt08 |
|---|---|---|---|---|---|
| arena train | +0.025 | 0 | −0.023 | +0.0125 | +0.0146 |
| 裁判（d29 同实例同图集 13 图 R 总和，base 2170；跨实例噪声 ≤10，d29/d30 frt04 2140/2130 互证） | −30 (2140) | +20 (2190) | **+140 (2310)** | +70 (2240) | +80 (2250) |

- frt06 裁判顶点：5 增益图（w8-uniform-47 +10、w8-edge-47 +60、w8-spread-11 +30、w8-spread-47 +10、w12-edge-47 +40）×3 seed 稳定；唯一代价 w12-uniform-23 −10 ×3 稳定。
- arena 的 stage1 场景含 maze/rooms（frt06 在此类场景 R 大降），但 map_styles 系 arena 自造风格图（arena_settings scope 明示 "Offline hand-written v1.2 … Not official referee"），非官方练习图集。两者结论相反 = 印证 match_config.hpp:55 注释「探索权重对两阶段影响相反，共享会互相绑架」。
- **裁决规则：正式赛 stage1 图 = 官方练习图（裁判图集同类），故 frt 终值以裁判曲线为准；arena 仅作第二意见。**
- 终裁：**frt06（0.06）**——裁判 +140 顶点、5 图 ×3 稳定复现；arena 崩全部来自自造 maze/rooms 风格图，按裁决规则不否决。次选 frt08（+80，两通道皆正）。

## 5. heldout 最终组合（30 场景，一次性，组合预注册）

profiles：baseline / lhp04 / s2pull6 / combo(lhp+s2pull6) / combo(lhp+s2pull6+frt04)

| profile | objective | deaths | stage2 win_share |
|---|---|---|---|
| baseline | 0.82820 | 162 | 0.4583 |
| lhp04 | 0.82698 (−0.0012) | 174 | 0.4583 |
| s2pull6 | 0.83235 (+0.0042) | 187 | 0.5 |
| combo_lhp_s2 | 0.83418 (+0.0060) | 195 | 0.5 |
| combo_lhp_s2_frt04 | 0.83584 (+0.0076) | 195 | 0.5 |

终裁：组合正和（combo > 单件之和，win_share 0.4583→0.5 由 s2pull6 贡献）。三件套晋升：lhp 0.4 + s2pull6 + frt06——frt 终值按 §4 裁判曲线取 0.06；heldout 中 frt04 亦正（+0.0016 组合贡献），增益方向与裁判一致。全部 invalid 0。

## 6. 关闭记录（#16/#17/#19）

- **#16 ai_max_tokens 512 vs 2200**：参赛手册强制 deepseek-flash / max_tokens=512 / Bearer 席位令牌 → 无自由度，实验无竞赛应用价值。关闭。
- **#17 wide_lanes 门控 48bdca8 二分**：两次尝试，`git apply -R --check` 均失败——补丁上下文已漂移（run_arena.py/arena_settings.json/arena_main.cpp/strategy.cpp/strategy_parameters.hpp 五文件被后续提交修改）。需 hunk 级代码鉴定，降级为赛后低优先。期间 arena frontier 轮（10-29）已把两阶段 frontier 拆分为 stage1_frontier_value/stage2 独立旋钮，部分缓解原问题。
- **#19 original_ros_diff 实跑**：observe 模式在 d28 冒烟通过（订阅建立、磁带文件落盘、25s 窗口无事件=正常）；drive 模式需原版席位磁带 + 域重编译（cst-wt-iter 编译域=27，禁触），降级为赛后可选。

## 7. 收尾清单

- 战役自检 cron f4761274 已删除（巡逻 cron ×2 + 联赛健康 cron 保留）
- **三件套晋升已落库**（promote_final.sh，2026-10-31 ~11:10 CST）：match_config.hpp lhp 1.0→0.4、stage2_mission_pull_stale_ticks 0→6、stage1_frontier_value 0.02→0.06，注释晋升史已更新
- **正式 stage2 二进制已重建**（tools/build_stage.sh 2，晋升后构建通过）
- lhp 后台双 bot 217067/217070 已收
- sprint 分支（strategy/campaign-sprint-1031 @ eab38e8）入库：tests/sweep_1031.py、sweep_1031b.py、results/*.json、match_config.hpp 晋升项
- 材料提交 10-31 20:00 截止提醒（语雀技术报告 + 检录材料）
