# N33: 买家到达率 λ 的价格敏感性函数：λ(D) = λ_0 * exp(-η * D)，其中 η 为价格敏感度系数，需通过历史数据回归估计 η 的取值范围（通常 η

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

买家到达率 λ 的价格敏感性函数：λ(D) = λ_0 * exp(-η * D)，其中 η 为价格敏感度系数，需通过历史数据回归估计 η 的取值范围（通常 η ∈ [0.5, 1.5]）。

## Corrected Claim

买家到达率 λ 的价格敏感性函数：λ(D) = λ_0 * exp(-η * D)，其中 η 为价格敏感度系数，需通过历史数据回归估计 η 的取值范围（通常 η ∈ [0.5, 1.5]）。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点实质上是参数 η 的两个边界取值（0.5 和 1.5）及其对应的业务解释，属于同一参数空间的离散采样，而非正交的概念维度。此外，父节点核心要求是“通过历史数据回归估计 η”，但子节点完全忽略了“数据回归/估计方法”这一关键方面，仅讨论了固定取值下的业务后果，导致完备性不足。）

## Search Query

used goods market price sensitivity coefficient eta demand curve
