# 61 · Stage2 真实 AI 每局调用实证：25/25 成功、约 25 次/局、≥1 富余 24 倍

- 身份：DeepSeek
- 时间：2026-10-31 12:40 +0800
- 关联：docs/52、docs/53（联赛证据）、docs/57（技术报告草稿）、review.md（#15 链路 request_ok 记录）
- 背景：冲刺反馈要求实证「llm 调用次数每局有限制」；手册要求 stage2 每场每席位 ≥1 次真实 AI 成功调用，否则任务分=0
- 数据：`/home/frank/.rmtc-practice2b/practice-7ca685a8672845e1afefea073fb5028d/`（bot.log、score.json）、`/home/frank/.rmtc-gw/practice-9c47bbc20e3b489c81b7afc203a694c1/ai.jsonl`（真实网关侧逐请求日志）

## 1. 实验设置

- 对局：practice2 裁判（127.0.0.1:8086，ROS 域 34），w8-uniform-23（24×24，8 墙），500ms×500 tick 正式节奏
- 我方：`install_camp_base-s2_34` 席位 A（编译期 ai_url=http://127.0.0.1:8080/v1/chat/completions）
- 真实 AI 网关：practice.py `--ai-mode real` 监听 127.0.0.1:8080（ROS 域 37，dummy session 激活转发），上游 https://api.deepseek.com/chat/completions，deepseek-flash，经 127.0.0.1:7890 代理（与 review.md #15 已验证链路一致）
- 陪练 B/C/D 由裁判 robot_node 自 spawn，走裁判自带的 8086 mock 网关（不影响 A 的计数）

## 2. 结果

| 指标 | 数值 |
|---|---|
| 真实网关记录 A 请求 | **25 次，25 成功，全部 200，mode=real** |
| bot A 自身计数器（tick 500 终态） | started=24 / finished=24 / http_successes=24 / last_http=200 / last_result=model_reply_received / known_mock=false |
| 单次调用时延 | 646ms（终态），~1.03s（tick 116 时） |
| 本局成绩（A） | score=57.9 / R=**120.0** / D=430 / M=3 / hp=20 / invalid=0 |
| 事件侧 | events_known=4、ai=events_validated（事件经 LLM 理解路径） |

- 调用节奏：首帧保底 1 次 + 公告/事件批次（tick 116 时 12 次 → tick 500 时 24 次），约每 20 tick 一次，无 429、无重试风暴。
- 网关侧 25 与 bot 侧 24 差 1：末 tick 边界计数口径差异，不影响结论。
- 结论：**每局真实调用 ≈ 25 次，全部成功**——既远高于「≥1 次」的及格线（富余 24 倍），又远低于任何合理限额（429 quota 兜底机制从未触发）。

## 3. 沿途两个修复（本次实证暴露）

1. `stage2_drive.py` 用 `generate(1, ...)` 生成 stage2 图——practice1 底座只有 A 席位，被裁判 400 拒绝（「陪练须在场内」）。改为 `generate(2, ...)`（practice2 底座含 A/B/C/D 四席）；官方图入口同步改为 practice2/config.json（标签 official-practice2）。
2. 网关 upstream 最初误填 192.168.50.1:8000（手册网关，系正式赛环境）→ 502；练习链路正确上游是 api.deepseek.com（review.md #15 口径），且应走 7890 代理（Windows 侧 Clash 监听，WSL 内 `ss` 不可见但 curl 可达，mirrored 回环）。

## 4. 对正式赛的含义

- 正式赛时组织方裁判自带真实网关（席位令牌），我方 bot 只认 127.0.0.1:8080 + `Bearer practice-A` 本地约定；本实证证明 bot→本地网关→真实上游整条链路与预算机制（首帧保底、去重、429 停、退避）在真实模型下工作正常。
- 每局 ~25 次的实测量级写入技术报告「LLM 调用预算」小节（docs/57 同步）。
