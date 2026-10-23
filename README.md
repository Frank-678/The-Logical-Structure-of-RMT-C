# RMTC · COMPARISON

2026-10-23新增：[v1.1迁移影响](reports/04-v1.1-transfer-update.md) · [Prompt与分层harness](reports/05-prompt-harness-review.md)。六集原游戏数据不变，RMTC计分依据已更新。

外部项目的规则、实现、实验、可借鉴方法与否决理由。当前参考覆盖 meow-ai-arena 的全部六集和公共平台，不只截图中的夺旗。

阅读顺序：[总索引](INDEX.md) → [六集总报告](reports/01-six-episodes.md) → [迁移与否决](decisions/reuse-register.md) → [代码摘录](snippets/README.md) → [数据核查](checks/README.md)。

上游以 submodule 固定在 b1893e19d1fe204bbba4e5c36af5b289f2b7b4ad；[版本锁定](sources.lock.json)、[全文件索引](indexes/upstream-inventory.json)、[阅读边界](indexes/reading-coverage.md)。克隆本分支后执行 git submodule update --init --recursive 即可取得完整上游；上游目录Gitlink与.gitmodules配对，不是源码缺失。

六集入口：[圈地](episodes/01-land.md) · [炸弹人](episodes/02-bomberman.md) · [夺旗](episodes/03-ctf.md) · [外交](episodes/04-diplomacy.md) · [仓储](episodes/05-warehouse.md) · [坦克](episodes/06-tank.md)。

RMTC原始材料与设计在 [ANALYSIS](https://github.com/Frank-678/The-Logical-Structure-of-RMT-C/tree/ANALYSIS)。所有策略迁移均需在RMTC验证；当前没有宣称已实现参赛bot。没有另外研究的相近仓库，不列成已读来源。保留 [原协作规范](governance/original-collaboration-guidelines.md)，不改main。

**私密预备资料：** 本分支不进入其他分支或公开导航；未来公开使用干净历史导出，见 [私密预备约定](governance/private-preparation.md)。
