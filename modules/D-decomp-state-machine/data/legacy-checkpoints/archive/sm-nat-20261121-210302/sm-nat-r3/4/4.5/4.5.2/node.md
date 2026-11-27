# N54: 热点对象平均大小 S_avg_hot = E[Size | Popularity > F_th]，需通过条件期望计算，F_th 由 N_hot 和 Pareto

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N13

## Claim

热点对象平均大小 S_avg_hot = E[Size | Popularity > F_th]，需通过条件期望计算，F_th 由 N_hot 和 Pareto 分布决定，具体公式为 S_avg_hot = ∫_{F_th}^{F_max} Size * f(Size|Popularity) dSize

## Corrected Claim

热点对象平均大小 S_avg_hot = E[Size | Popularity > F_th]，需通过条件期望计算，F_th 由 N_hot 和 Pareto 分布决定，具体公式为 S_avg_hot = ∫_{F_th}^{F_max} Size * f(Size|Popularity) dSize

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应相关性系数 ρ 的三个关键边界/状态（独立、实际耦合、极端负相关），彼此在参数取值上互斥且覆盖全面，不存在逻辑矛盾或重复。虽然它们本质上是同一公式在不同参数下的计算，但在学术分解中，将基准、实际值和理论极限分开陈述是必要的，以体现不同假设下的物理意义和计算复杂度差异，因此不视为冗余。）
