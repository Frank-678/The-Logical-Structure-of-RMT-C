# 从代码仓库迁入的研究文档

按用户2026-10-28本轮要求迁移，保留文件名与原代码基线，不把其他研究内容同步到代码仓库。历史测试报告移至checks/code-results，代码引用固定到原基线，文档之间的相对链接保留。源码目录保留运行教程、源码导读与代码；实测历史和策略研究集中于此。

- [LESSONS.md](LESSONS.md)
- [MATERIALS_CHECK.md](MATERIALS_CHECK.md)
- [NAVIGATION.md](NAVIGATION.md)
- [PLANNING.md](PLANNING.md)
- [REAL_TEST.md](REAL_TEST.md)

迁移前后摘要见[migration.json](migration.json)。后续改动应在本目录维护。

用户后续要求分析类文件统一归此仓库：历史调参结论另见[ARENA_RESULTS.md](ARENA_RESULTS.md)，逐局与实测原始报告存于[迁移清单](migration.json)列出的checks/code-results。selected-parameters.json仍被评测脚本读取，属于代码配置，保留在代码仓库。

- [EVENT_USE.md](EVENT_USE.md)：成功调用如何进入策略、未来抢点修复、日志与实测范围。
- [SCOREBOARD.md](SCOREBOARD.md)：第一阶段38/40回跳30的同场分阶段证据。
