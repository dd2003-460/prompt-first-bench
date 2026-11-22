# N71: 卖家临界干预强度计算：当平台展示真实成交价导致卖家挂价下调 ΔP 时，卖家剩余变化 ΔSS_seller = -ΔP * Prob(Sale) - C_wait

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N26

## Claim

卖家临界干预强度计算：当平台展示真实成交价导致卖家挂价下调 ΔP 时，卖家剩余变化 ΔSS_seller = -ΔP * Prob(Sale) - C_wait_reduction。设定 Threshold_seller = 5% 利润下降，则临界干预强度对应于使 ΔSS_seller / Initial_Profit = -0.05 的 ΔP 值，该值与当前平均溢价率 (20%) 和成交概率弹性相关。

## Corrected Claim

卖家临界干预强度计算：当平台展示真实成交价导致卖家挂价下调 ΔP 时，卖家剩余变化 ΔSS_seller = -ΔP * Prob(Sale) - C_wait_reduction。设定 Threshold_seller = 5% 利润下降，则临界干预强度对应于使 ΔSS_seller / Initial_Profit = -0.05 的 ΔP 值，该值与当前平均溢价率 (20%) 和成交概率弹性相关。

## Evidence

父节点级核验未通过：不完备（子节点覆盖了父节点公式中的主要变量（Initial_Profit, ε_prob, C_wait_reduction），但存在关键逻辑缺失。父节点明确提到临界强度与‘当前平均溢价率 (20%)’相关，但在子节点中未体现溢价率如何作为边界条件或参数输入影响临界值的计算（例如，溢价率决定了ΔP的最大可能空间或基准参考）。此外，C1中的Prob(Sale|P_ask)与C2中的弹性定义在逻辑上是紧密耦合的，虽然不重复，但C2作为弹性系数应更明确地关联到C1中的基准概率，目前表述略显割裂。最核心的缺失是‘平均溢价率’这一父节点中强调的关键上下文未在子节点中落地。）

## Search Query

seller surplus loss threshold price transparency intervention 5 percent
