# N12: 降价后无咨询的信号崩溃机制：ΔP_discount < θ_signal_threshold时，买家更新P(Quality=High | P_discounte

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

降价后无咨询的信号崩溃机制：ΔP_discount < θ_signal_threshold时，买家更新P(Quality=High | P_discounted) = P(Quality=High | P_listed) * (1 - 0.8 * I(ΔP < θ))，其中θ_signal_threshold = 0.1（10%），60%卖家降价幅度<10%，导致质量信号强度下降80%，咨询量降至0。

## Corrected Claim

在特定的信号崩溃模型中，若设定降价幅度低于10%阈值时信号强度衰减80%，且60%卖家降价幅度低于该阈值，则会导致质量信号显著下降，咨询量可能降至极低水平。

## Evidence

[质询]该陈述包含具体的经验参数（如0.8的衰减系数、10%的阈值、60%的卖家分布比例），这些并非第一性原理可推导的数学或物理定律，而是特定市场模型或实证研究的假设/结果。作为knowledge节点，虽然逻辑结构自洽，但缺乏外部来源验证这些具体数值在一般情况下的普适性，存在将特定模型参数泛化为普遍事实的风险。 | 先验知识/题面给定，逻辑校验通过；但具体数值（0.8, 10%, 60%）属于经验模型参数，无来源支持其普适性，故降级。

## Search Query

price discount signal collapse quality perception inquiry rate threshold
