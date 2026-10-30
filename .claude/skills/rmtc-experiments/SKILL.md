---
name: rmtc-experiments
description: RMTC 实验操作手册——网关验证、秒级场景批量（2万组方法论）、正式尺寸实跑、联赛批次、LLM 限额纪律、WSL 陷阱
---

# RMTC 实验操作手册

环境：本会话项目 D:\code\The-Logical-Structure-of-RMT-C（doc 仓）+ WSL ~/cst（代码仓 vrb）。目标：stage1 满分（40=200 资源）、stage2 高分（30R+15D+5M）、每局 LLM 调用限额内、低风险进步。

## 0. 铁律（任何操作前必查）

- 密钥形态 `sk-cbc[0-9a-f]{8,}` 永不入库；只许在 WSL 工作区 match_config.hpp 与临时文件；提交文本必须含「密钥扫描通过」；提交前全仓扫描 0 真实 key
- 永不 push main/master（doc main 例外：仅 README 进度矩阵扩充）
- 行为类改动默认关闭 → 竞技场评估 → 有证据才晋升；诊断/工具/配置类可直接采纳
- `~/.rmtc-practice/llm.env` 内容禁读——只由启动器运行时读取
- 比赛可写死就写死（match_config.hpp 编译期常量），不用环境变量猜测
- 实验室成果→ANALYSIS docs 编号递增；比赛→提交映射入 docs/56 台账；review.md 两仓同文回执（CRLF 保留、追加式）

## 1. 网关验证（check_ai 链路）

- 配置唯一来源：WSL `~/cst/src/rmtc_bot/include/rmtc_bot/match_config.hpp`，**编译期注入**。改完必须 `bash build.sh` 重建——0.5s 结束说明 colcon 没检测到变化、未重建
- `bash check_ai.sh`：启动器注入环境变量 → scripts/check_ai.py → requests 继承环境代理
- 判读：`request_ok/200`=链路通；`proxy_error`/`ProxySchemeUnknown: Proxy URL had no scheme`=**启动器二进制停在无 scheme 中间态，重建即可**（不一定是代码 bug）；`http_error 401`=key 空或失效；2ms 无网络动作=requests 解析阶段就失败
- 练习代理端口 8080（practice_port）；占用排查 `ss -tlnp | grep 8080`——占用时用 `RMTC_FORMAL_PORT=8082` 等换端口，**勿杀他人进程**

## 2. 秒级场景批量（2 万组主力路径）

- `bash scenarios.sh` = tests/run_scenarios.py：摆第 200 Tick 局面只跑验证段，**不启 ROS、不调模型**——单次秒级，规模化扫描首选
- 地图族：`python3 tools/formal_size_suite.py` 生成 20×20/24×24 可复现合成图（STYLES=uniform/cluster/edge/center/spread，seed 固定）；practice1/2/config.json 是官方形状基线
- **参数扫描架构**：match_config.hpp 是编译期常量 → 用 build_seat_variants 式**一次构建 K 个变体**（每变体=一组参数组合，并行编译），再短场景批量对打；绝不每组合单独 colcon build（15s×N 不可行）
- 判据纪律（docs/02 + COMPARISON report 02）：同图同席同对手配对、留出图、一机制一改动、记录 AI 资格与异常/失败回放；train 增益≠真实增益（docs/34 实证第二次）

## 3. 正式尺寸实跑（分钟级）

- `bash practice1/run.sh`（stage1 单席 20×20）、`bash practice2/run.sh`（stage2 24×24）：原版裁判+校验器；`RMTC_FORMAL_CONFIG/RMTC_FORMAL_PORT/RMTC_FORMAL_DATA_DIR` 环境可覆盖
- **run.sh 只起裁判（暂停态等 A 席）——bot 必须单独启动**：`bash tools/run_seat.sh <install_base> <A|B|C|D> <logfile>`；开赛需 `curl -X POST -d '{}' http://127.0.0.1:8082/api/resume`（缺 JSON body 会 400）
- **域隔离铁律**：bot main() 强制 `setenv(ROS_DOMAIN_ID, cfg::ros_domain_id, 覆盖)`——外层 export 对 bot 无效，域号是编译期值；裁判(start_referee.sh)尊重环境变量。变体构建必须把目标域编进二进制：`sed stage/ros_domain_id → colcon build --build-base build_stage1 --install-base install_stage1 → 复原 → build.sh`。**仓库默认域=27（用户会话占用中）**：任何变体构建第一步必须 `sed 's/ros_domain_id = "27"/ros_domain_id = "28"/'`，否则 bot 注册会打到用户暂停对局里污染其 referee.log（10-31 实测 ring/flood 变体 REG-FAIL + 用户裁判日志多 3 行 Frank 注册）；构建脚本用 trap EXIT 兜底还原源码
- practice.py 是**双参与者**：公开节点=env 域，内部组织者=域+1（internal_ros.py）；referee_node 公开面在 env 域。同机已有会话占 27 时必须用 28（裁判 env 28 + bot 编译 28），端口换 8082，否则 /team_A/perception 等席位话题串线、bot 注册还会污染他人会话
- **换图零重启**：`POST /api/start` 接受完整 config 正文（stage/tick_ms/max_ticks/config），同一个 practice.py 可以循环跑任意地图（formal_size_suite.generate 产出）；`/api/reset` 复用原 settings 重新部署
- **循环换图基建坑（2026-10-30/31 实测）**：① 上一场 tick 刚满就 /api/start → 上一场子进程未退、同域 FastDDS participant 创建冲突 → 500「部署失败」；每场结束必须 /api/stop 等完全停止再开下一场。② **`/api/reset` 是重新部署（app.start(settings) 会 spawn 全新三件套），不是停止**——严禁在换图 stop 序列里调用；跨图间只发 /api/stop，500 重试也只重发 stop。③ **驱动级 bug 实录（2026-10-31 破案）**：`launch_bot` 只 `return subprocess.Popen(...)` 未给全局赋值 → `kill_bot` 全局永远 None 全程空转 → 每图 bot 全部存活成孤儿、抢先注册下一局并代打（真 bot 迟到整场）→ invalid_actions 随图序爬升 6→79 + R 崩塌、bot.log 只见外局 session 行即确诊；修复 = `bot = subprocess.Popen(...)` 赋值全局 + 每图 kill 后 /proc 扫 rmtc_bot 审计孤儿。④ **长命 bot 对新生 referee_node 的 DDS 重发现不可靠**：新会话的感知可能晚到几十 tick 甚至整场为零（R=30/R=0 伪影，bot 日志该会话无 tick 行即确诊）——批量扫描必须**每图重启 bot**，不能复用一个长命进程跑多图
- **注册门是单向的**（证明裁判收到 bot 注册，不证明 bot 收到裁判感知）：resume 后必须加**双向门**——轮询 bot.log 出现「session=<本局sid> tick=≤5」行，15s 内未出现或首 tick>5 → 判定 MAP-BAD，stop+kill 后整图重跑一次；批量驱动的 bot.log 用 bash `>` 打开、进程死前 ~3s 缓冲粒度
- DDS 域诊断：UDP 端口 = 7400+250×domain（`ss -uanp`）；**WSL 下 /proc/PID/environ 是 exec 快照、不反映 setenv，不可信**
- stage1 无 LLM（launcher：real = `--check-ai` || `--batch` || stage==2）；stage2 强制 real 模式
- **practice2/run.sh 硬编码 `--ai-mode mock`**——stage2 真实 AI 实跑必须追加 `--ai-mode real`（argparse 后者覆盖前者）；real 模式要求裁判进程环境含 `PRACTICE_LLM_URL`（完整 completions 地址）+`PRACTICE_LLM_KEY`，上游请求由 requests 继承 `http_proxy`/`https_proxy`（7890），陪练 robot_node 若不带 model 还需 `PRACTICE_MODEL`。绕过 launcher 自起裁判时全部手动 export
- 量化口径：会话目录 ai.jsonl 字段 seat/session_id/mode/status/success/success_count/attempt_count；success==(status==200) 恒等

## 4. 联赛批次（小时级）

- `tools/league.sh freeze old/current --ref SHA → suite --versions → run --limit`；冻结钉=tools/versions.json（二进制 sha256 + params_digest）
- 混合口径（docs/48 §5）：M1 基线（champion vs 原版陪练）、M2 自战（vs old_champion）、M5 同池对照；计分 30·min(R/120,1)+15·min(D/500,1)+5·len(completed)
- 勘误口径（引用前必读）：docs/44/45 死亡列=终局存活态误读（用 docs/55：16 局实际 122 死）；M3=五参数（tdc 死参数，docs/48）；40/50 目标以离线竞技场为准、league 原版裁判分为另一口径

## 5. LLM 每局限额（stage2 命门）

- 每场每席 ≥1 次真实统一 AI 成功，否则任务分=0；每局调用次数有限额 → 只对高价值事件调用、公告批次包含去重、连续 3 坏回复暂停重试（生命周期 Idle→Queued→Requesting→Validate→Backoff/Stopped）
- max_tokens=512（2026-10-30 手册）；截断=finish_reason "length" → 压缩 prompt/减少重复上下文（REAL_TEST 5977ms 教训）；不靠关键词/正则/时间表替代 LLM 语义理解

## 6. WSL 陷阱（实测踩过）

- wsl.exe 命令中禁 `$()`；PowerShell 外层双引号会吞 `$N`/`$?`——外层用单引号最稳
- bash -lc 内层用单引号写 bash 语法；避免 awk print $6 这类组合
- **WSL 构建脚本禁 `set -u`**：`/opt/ros/humble/setup.bash` 引用未设变量（AMENT_TRACE_SETUP_FILES）→ nounset 下 source 即崩、静默失败（10-31 变体重建脚本只输出零行、二进制未重建、旧域二进制照跑再污染）——只用 `set -eo pipefail` + trap EXIT 兜底还原
- **链式命令禁 `;` 串失败步骤**：`重建脚本; 三 sweep` 让重建失败后旧二进制无条件照扫（第二次污染）——依赖步骤一律 `&&`，且探针闸探测脚本用 `sys.exit(1)` 断链（域验证探针 /tmp/probe_domain28.py：我的裁判见注册 ∧ 用户日志零增量 ∧ bot.log 本局 sid tick≤5，任一不满足即退出）
- **变体构建必须同时 sed `stage`**：`match_config.hpp` 的 stage 是编译期值（bot.cpp:33 `const int stage = cfg::stage`），感知消息无阶段字段。10-31 惨案：重建脚本只 sed 域+旋钮、漏 sed `stage = 2`→`= 1`，4 个新构建全是 stage2 战斗逻辑打 stage1 图（官方图 R=170 vs 基线 200，bot.log `mode=combat_ready ai=requesting` 而非 `mode=collecting ai=disabled_missing_url_and_token`）。修复后 stage1+域28 重建链全绿（probe/control 官方图均 200）。**验尸三件套**：mode 行 + R 值 + 与基线 install 对照；正式赛两阶段切换用 `tools/build_stage.sh 1|2`（README 两阶段切换章节），官方流程=每阶段前确认代码版本+阶段间 10min 调整窗口可改参数

## 7. 收尾清单

- 结论入 ANALYSIS docs（编号递增）并推送；doc main 只碰 README 矩阵
- 两仓 review.md 同文回执块（CG-R- 编号、DeepSeek 身份、Asia/Shanghai 时间戳、完整 SHA、验证命令+正反结果）
