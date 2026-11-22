# N45: 卖家逐利行为函数的共享随机源：卖家定价 P_seller 的随机性源于‘未来成交概率’Q(P) 的估计误差。Q(P) = E[Q | P, S] + ε_sel

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N9, N10, N11

## Claim

卖家逐利行为函数的共享随机源：卖家定价 P_seller 的随机性源于‘未来成交概率’Q(P) 的估计误差。Q(P) = E[Q | P, S] + ε_seller，其中 ε_seller ~ N(0, σ_seller²)，σ_seller² 与卖家的历史成交数据量 n_seller 成反比（σ_seller² = σ_base² / n_seller）。新卖家（n_seller < 5）的 σ_seller 大，倾向于高挂价以覆盖不确定性溢价；老卖家（n_seller > 50）的 σ_seller 小，定价更接近市场清算价。

## Corrected Claim

卖家逐利行为函数的共享随机源：卖家定价 P_seller 的随机性源于‘未来成交概率’Q(P) 的估计误差。Q(P) = E[Q | P, S] + ε_seller，其中 ε_seller ~ N(0, σ_seller²)，σ_seller² 与卖家的历史成交数据量 n_seller 成反比（σ_seller² = σ_base² / n_seller）。新卖家（n_seller < 5）的 σ_seller 大，倾向于高挂价以覆盖不确定性溢价；老卖家（n_seller > 50）的 σ_seller 小，定价更接近市场清算价。

## Evidence

父节点级核验未通过：不完备（子节点在逻辑上分别处理了基准参数量化、风险溢价计算和下游后果投影，彼此正且不重复。但是，父节点明确定义了σ_seller²与n_seller的反比关系（σ_seller² = σ_base² / n_seller），并以此作为核心机制解释新/老卖家行为差异。子节点中虽然使用了该公式进行数值举例，但缺乏一个专门解释或验证该‘方差-数据量反比关系’本身合理性的子节点（例如：为什么是反比？是否有理论依据如贝叶斯收缩或中心极限定理的变体？）。因此，父节点中的核心数学关系未被独立分解或充分论证，导致完备性不足。）

## Search Query

seller pricing uncertainty and experience in e-commerce
