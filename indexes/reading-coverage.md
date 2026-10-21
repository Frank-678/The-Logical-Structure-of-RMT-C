# 阅读覆盖与边界

全仓1078文件逐字节读取、哈希和按类型解析；991份不同内容。C++建立符号索引，Python做AST，JSON/JSONL/CSV完整解析，8个gzip完整解码，42个HTML扫描脚本及可解析数据。详见 upstream-scan_summary.json。

语义精读重点是六集规则/条件、公共core/schedule/tournament/bt、land/game.py、bomberman/engine.py、ctf/engine.py、diplomacy/arena.py和scheduler关键流程、warehouse基线与CHANGE/缺陷归类/重点终版交接及距离修复、tank/step与核心接口及Astra/Sol终版；各章指向具体来源。

全量读取/结构化处理不等于所有历史源文件逐行人工审查，不能声称每条外交私信、每个回放帧、每个权重数字都已语义核验。没有模型原始完整会话、未公开官方外交PDF或封闭源码，不能补造。当前未重新执行全部98780局对战。

所有JSON/CSV解析通过不等于功能正确；程序作者NOTES、模型复盘是自述而不是独立验证。后续若新增精读或运行实验，更新此页和检查结果。
