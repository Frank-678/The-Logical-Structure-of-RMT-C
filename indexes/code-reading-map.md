# 源码阅读定位

全符号索引见 [upstream-symbols.json](upstream-symbols.json)；这里只列核心入口，原始源码以固定submodule为准。

| 集/模块 | 核心文件 | 阅读重点 |
|---|---|---|
| 公共 | [arena/core.py](https://github.com/chen-006/meow-ai-arena/blob/b1893e19d1fe204bbba4e5c36af5b289f2b7b4ad/arena/core.py) | 进程、计时、收发与故障 |
| 评分 | [arena/bt.py](https://github.com/chen-006/meow-ai-arena/blob/b1893e19d1fe204bbba4e5c36af5b289f2b7b4ad/arena/bt.py) | 多人比较、人数等权、地图bootstrap |
| 赛程 | [arena/schedule.py](https://github.com/chen-006/meow-ai-arena/blob/b1893e19d1fe204bbba4e5c36af5b289f2b7b4ad/arena/schedule.py) | 对手和座位平衡 |
| 圈地 | [land/workspace/engine/game.py](https://github.com/chen-006/meow-ai-arena/blob/b1893e19d1fe204bbba4e5c36af5b289f2b7b4ad/land/workspace/engine/game.py) | 移动、死亡、闭环洪泛 |
| 炸弹人 | [bomberman/workspace/engine/engine.py](https://github.com/chen-006/meow-ai-arena/blob/b1893e19d1fe204bbba4e5c36af5b289f2b7b4ad/bomberman/workspace/engine/engine.py) | 缩圈、放弹、统一爆炸快照 |
| 夺旗 | [ctf/workspace/engine.py](https://github.com/chen-006/meow-ai-arena/blob/b1893e19d1fe204bbba4e5c36af5b289f2b7b4ad/ctf/workspace/engine.py) | 复活、碰撞、攻击、拾放/交旗 |
| 夺旗策略 | [ctf/bots/gpt-6-astra.cpp](https://github.com/chen-006/meow-ai-arena/blob/b1893e19d1fe204bbba4e5c36af5b289f2b7b4ad/ctf/bots/gpt-6-astra.cpp) | 任务分配、对手风格、联合微操 |
| 外交 | [diplomacy/referee/arena.py](https://github.com/chen-006/meow-ai-arena/blob/b1893e19d1fe204bbba4e5c36af5b289f2b7b4ad/diplomacy/referee/arena.py) | 验证军令、私信、同时结算 |
| 外交调度 | [diplomacy/referee/scheduler.py](https://github.com/chen-006/meow-ai-arena/blob/b1893e19d1fe204bbba4e5c36af5b289f2b7b4ad/diplomacy/referee/scheduler.py) | 唤醒、去重、消息送达与重试 |
| 仓储基线 | [warehouse/workspace/baseline/sim.cpp](https://github.com/chen-006/meow-ai-arena/blob/b1893e19d1fe204bbba4e5c36af5b289f2b7b4ad/warehouse/workspace/baseline/sim.cpp) | 精确行为与流程顺序 |
| 仓储寻路 | [warehouse/submissions/round3/mimo-v2.6-pro__gpt-6-astra/dist.cpp](https://github.com/chen-006/meow-ai-arena/blob/b1893e19d1fe204bbba4e5c36af5b289f2b7b4ad/warehouse/submissions/round3/mimo-v2.6-pro__gpt-6-astra/dist.cpp) | 缓存契约、增量修复与回退 |
| 坦克引擎 | [tank/workspace/tank.hpp](https://github.com/chen-006/meow-ai-arena/blob/b1893e19d1fe204bbba4e5c36af5b289f2b7b4ad/tank/workspace/tank.hpp) | step、合法命令、弹道、预算 |
| 坦克策略 | [tank/bots/half2/gpt-6-astra.cpp](https://github.com/chen-006/meow-ai-arena/blob/b1893e19d1fe204bbba4e5c36af5b289f2b7b4ad/tank/bots/half2/gpt-6-astra.cpp) | 角色任务、候选矩阵、短期推演 |
| 社区 | [community/check.py](https://github.com/chen-006/meow-ai-arena/blob/b1893e19d1fe204bbba4e5c36af5b289f2b7b4ad/community/check.py) | 结构/编译/评测与参照口径 |
