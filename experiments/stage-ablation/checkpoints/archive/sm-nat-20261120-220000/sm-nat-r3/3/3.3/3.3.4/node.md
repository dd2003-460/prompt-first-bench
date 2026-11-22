# N44: 更新频率 p_invalid(s) 与大小的关系：假设更新频率与大小负相关，p_invalid(s) = 0.01 * (S_min/s)^0.5，大对象更新频

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

更新频率 p_invalid(s) 与大小的关系：假设更新频率与大小负相关，p_invalid(s) = 0.01 * (S_min/s)^0.5，大对象更新频率低，小对象更新频率高

## Corrected Claim

更新频率 p_invalid(s) 与大小的关系：假设更新频率与大小负相关，p_invalid(s) = 0.01 * (S_min/s)^0.5，大对象更新频率低，小对象更新频率高

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一连续函数 p_invalid(s) 和 cost_per_invalid(s) 在三个离散点（小、中、大）上的采样计算，而非概念上的正交维度（如机制、假设、约束等）。此外，工作点3的计算结论（全局最低成本）缺乏理论支撑，仅凭三个离散点的数值比较不能证明该点为全局最优，且未覆盖边界情况或函数极值点的分析。）

## Search Query

object update frequency size relationship CDN cache invalidation rate
