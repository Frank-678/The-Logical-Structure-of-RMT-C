# 来源完整性与后续研究边界

上游由真实gitlink mode160000固定commit，.gitmodules给出公开地址。不要只复制某个README然后称完整上游已归档；本分支同时保存全仓哈希、结构化索引和原始数据核查，可初始化submodule恢复全部1078个文件。

来源链：sources.lock.json → upstream固定提交 → indexes文件哈希/符号 → episodes与总报告 → decisions采用/否决 → snippets具体片段 → checks可复算证据。

当前没有完成的事项：所有历史bot逐行审查、每条外交消息语义复核、全部比赛重跑、RMTC迁移策略实现和实测、其他相近repo的独立调查。后续有必要增加参考对象时，用新来源ID、固定提交、许可、读取范围和独立对照；不能用未经读取的项目补充榜单。

用户提供的B站截图原图已恢复并保存在 [bilibili-ctf-screenshot.jpg](../references/bilibili-ctf-screenshot.jpg)，仅用于记录参考repo的发现来源；视频本体未完整观看，不声称完成视频核验或转写。
