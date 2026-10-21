# 原始代码摘录

摘录保持上游正文；前四行是本次添加的来源/许可/用途说明。1基行号、固定commit、原始正文哈希在manifest.json。不可将这些上下文片段直接当作RMTC实现。

| 片段 | 作用 | 使用限制 |
|---|---|---|
| bomberman-temporal-safety.cppfrag | 时间展开的反向生存筛选 | 将火焰/缩圈替换成RMTC真实事件与行动顺序 |
| tank-restricted-matrix.cppfrag | 双方候选矩阵和虚拟对弈 | 只在已列候选内近似，未知动作和局部信息需适配 |
| warehouse-cache-repair.cppfrag | 路网变化后的增量修复 | 图契约/起点语义/内存所有权必须保留，无法证明时回退 |

其他源码不复制，按固定submodule路径和indexes/upstream-symbols.json查阅。更完整的采用/否决理由见 ../decisions/reuse-register.md。
