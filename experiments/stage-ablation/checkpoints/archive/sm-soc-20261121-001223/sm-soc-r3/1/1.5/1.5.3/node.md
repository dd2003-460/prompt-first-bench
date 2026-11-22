# N44: 成交周期T_deal的计算：T_deal = 1 / (k_consult * k_deal)，其中k_deal为咨询到成交的转化率（基准值0.3-0.5），用

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N9

## Claim

成交周期T_deal的计算：T_deal = 1 / (k_consult * k_deal)，其中k_deal为咨询到成交的转化率（基准值0.3-0.5），用于量化高挂价通过提升k_consult缩短成交周期的机制。

## Corrected Claim

成交周期T_deal的计算：T_deal = 1 / (k_consult * k_deal)，其中k_deal为咨询到成交的转化率（基准值0.3-0.5），用于量化高挂价通过提升k_consult缩短成交周期的机制。

## Evidence

父节点级核验未通过：有冗余（子节点在逻辑上是正交的（分别代表最优、基准、最差三种状态），且覆盖了公式的两个变量（k_consult, k_deal）的极端与中间情况。然而，从学术分解的角度看，这三个子节点本质上是同一个双变量函数 T_deal(k_consult, k_deal) 在参数空间中的三个特定采样点（工作点），而非对‘成交周期计算机制’这一父节点的不同维度分解。它们属于‘参数敏感性分析’或‘情景模拟’，而非结构性分解。因此，存在冗余，因为它们可以被压缩为对 k_consult 和 k_deal 参数范围的定义，或合并为一个‘参数影响分析’节点。）
