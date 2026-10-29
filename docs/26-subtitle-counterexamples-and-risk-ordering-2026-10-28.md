# 七份字幕与假设风险逃路修复

2026-10-28。按用户要求先完成导航修复，再逐行阅读七份字幕及遗漏段。区分来源叙述与可运行证据，逐项记录采纳/已有/暂缓/不适用，不转载原字幕或模型思考内容。

炸弹人05:50/11:52/20:20的“不确定风险封唯一生路”在4ba9dcd生产核心确实复现：本车40HP、三墙单出口、次Tick爆炸80，因敌车可能踩辣椒50而删除逃路，旧策略DEFEND后死亡。改为风险排序/HP比例收益折扣，保留墙/当前敌车占位/已解释公告时序。只执行本Tick首步。

每版32例是4席位×4旋转×2固定敌方动作，不是32独立地图。对手不踩点旧16死→新0死；实际踩点仍各16死，未伪造无风险保证。四席位各自身份/坐标/成绩隔离新增契约，未发现同类观测复用缺陷。Prompt澄清原公告时间锚和另一辣椒火线可命中当前触发点，未改JSON schema或冒称真实模型理解率已提高。

固定六风格NPC、新种子49009组、每版6采集+24对抗，权重未重调。它们使用公开局部观测及公告后延迟oracle，不是官方标准车、LLM调用或正式资格证明。核心/HTTP/原Handler/规则通过ASan/UBSan（LSan关闭），真实ROS手工链接通过，practice18原件不变。致命守卫长期防御、用户原地图和原版DDS完整对局仍未验收。

[实际取舍和验证](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/826c4da5afa74d038b7ffad032da570e682d31a1/LESSONS.md)、[最小配对](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/826c4da5afa74d038b7ffad032da570e682d31a1/tests/results/risk-2026-10-28.json)、[新地图](https://github.com/Frank-678/RoboMaster-Turing-Competition-BeyondControl/blob/826c4da5afa74d038b7ffad032da570e682d31a1/tests/results/risk-maps-2026-10-28.json)。

下一步有证据需求的方向：原版裁判具体僵局、公开输入下有界counterkill/多阵营预测、短预告与HTTP完成的时效。以上均是待试，不标已实现。

新地图实测：采集均分32.67不变；对抗37.77、获胜份额45.8%、死亡79、受阻87均不变，无效动作0，24局逐局分数相同。该修复针对确定反例，不能宣称普遍提高分数。

本轮代码按两次提交发布：24774f4修复/契约，826c4da夹具/来源取舍/结果；既有PR保持开放未合并。main矩阵按已有授权扩至R45，仅README。
