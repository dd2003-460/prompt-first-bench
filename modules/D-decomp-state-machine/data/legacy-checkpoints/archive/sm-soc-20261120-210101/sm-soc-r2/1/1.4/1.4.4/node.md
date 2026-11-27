# N45: 卖家逐利行为函数的共享随机源：卖家定价 P_seller 的随机性源于‘未来成交概率’Q(P) 的估计误差。Q(P) = E[Q | P, S] + ε_sel

- **status**: verified
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

先验知识/题面给定，逻辑校验通过：该陈述描述了基于贝叶斯更新或统计估计误差的定价模型，其中方差与样本量成反比（σ² ∝ 1/n）符合统计学基本原理，且新卖家因不确定性高而倾向于高挂价（风险溢价/保守策略）符合经济学直觉，内部逻辑自洽。

## Search Query

seller pricing uncertainty and experience in e-commerce
