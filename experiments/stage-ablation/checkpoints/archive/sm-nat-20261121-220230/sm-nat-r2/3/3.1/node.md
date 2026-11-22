# N14: 更新率1%/天对LRU有效命中率的折减系数 = 1 - P_invalid，其中P_invalid为对象在缓存驻留期间被更新的概率。若对象平均驻留时间为T_re

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

更新率1%/天对LRU有效命中率的折减系数 = 1 - P_invalid，其中P_invalid为对象在缓存驻留期间被更新的概率。若对象平均驻留时间为T_resident天，则P_invalid = 1 - (1-0.01)^{T_resident} ≈ 0.01 * T_resident（当T_resident<10时近似成立）。

## Corrected Claim

更新率1%/天对LRU有效命中率的折减系数 = 1 - P_invalid，其中P_invalid为对象在缓存驻留期间被更新的概率。若对象平均驻留时间为T_resident天，则P_invalid = 1 - (1-0.01)^{T_resident} ≈ 0.01 * T_resident（当T_resident<10时近似成立）。

## Evidence

父节点级核验未通过：有冗余（子节点分别对应热度分布的三个互斥区间（Top 10%, Bottom 50%, Middle 10%-50%），在逻辑上是正交的且覆盖了整体分布。然而，这三个子节点本质上是对同一个数学公式 P_invalid = 1 - (1-0.01)^{T_resident} 在不同 T_resident 取值下的具体实例化。从知识分解的角度看，它们属于‘同一参数的不同取值’，而非独立的结构性知识点。如果目标是构建可复用的知识图谱或公式库，将三个案例拆分为独立节点会导致结构冗余，因为核心逻辑完全相同，仅变量 T_resident 不同。）
