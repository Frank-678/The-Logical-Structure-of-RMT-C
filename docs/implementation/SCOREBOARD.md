# 第一阶段吃空后为什么网页显示30分

2026-10-29，只读核对用户上传日志，固定来源`log@b6a4818fdb751bad0491be3fc532d1622df02b43`。原版practice文件未改，没有把观赛记录作为参赛程序输入。

截图场次`practice-036ac763cdd14b26bef321a277b6e013`的正确结果是40分。配置为stage1，资源总价值200；score.json为stage1、Tick100、A资源200、score40、无效动作0。scoring.log末尾也明确A=40.00。

真正问题是同场同Tick的计分消息混用了两个阶段。frames.jsonl有200行，却只有100个(session_id,tick)：每个Tick各一份stage1和stage2消息；不是前次读取其他场次时发现的完全相同重复。

| Tick / 资源R | stage1消息 | stage2消息 |
| --- | ---: | ---: |
| 1 / 10 | 2 | 2.5 |
| 66–68 / 190 | 38 | 30 |
| 100 / 200 | 40 | 30 |

这直接复现了用户看到“曾经38，后来降到30”。按v1.2 §9，第一阶段为40×R/200；R190得38、R200得40。stage2消息套入第二阶段资源分30×min(R/120,1)，R达到120后便显示30。第一阶段没有敌车攻击或死亡扣分造成这种下降。

原版practice.py的on_board订阅/referee/scoreboard，只检查session_id相同便覆盖board；index.html显示最近board里的score，没有重新按阶段计算。原始启动器给scoring_node传入stage1，scoring.log也正确；现场同时收到stage2消息，说明还有一条计分发布路径与它冲突。仅凭这些记录不能精确断言冲突消息属于哪个进程，不能把原因归为已经证实的旧进程残留或某个具体二进制错误。

另外两场`practice-f13056a4d2e54a08b1f4052791f524b1`、`practice-f2a9b769609b4dc2bf7647c693462784`也各有100组不同stage的同Tick消息，正确score.json均为40分。

不修改原裁判，不让机器人发布或覆盖成绩。验收时同时核对场次、阶段、Tick、R和scoring.log/score.json；页面的最后一帧30不能据此当成机器人少拿了资源。

[逐场证据、来源摘要](../../checks/phase-and-event-audit-2026-10-29.json)。原始数据仍在用户log分支对应场次目录；具体网页帧来自哪次发布的进程级溯源，需裁判维护方进一步检查。
