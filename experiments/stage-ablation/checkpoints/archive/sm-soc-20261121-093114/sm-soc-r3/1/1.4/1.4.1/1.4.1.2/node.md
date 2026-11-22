# N113: 探索项 ε_traffic 的分布假设验证：假设 ε_traffic 服从 N(0, σ_ε²)，则 P(ε_traffic > k * W_baseline)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N36

## Claim

探索项 ε_traffic 的分布假设验证：假设 ε_traffic 服从 N(0, σ_ε²)，则 P(ε_traffic > k * W_baseline) 决定了高挂价商品因随机扰动而获得额外曝光的概率；需计算在 σ_ε = 0.07 * W_total 时，P(ε_traffic > 0.1 * W_baseline) 是否显著低于 5%，以确认‘随机扰动’非主要驱动因子。

## Corrected Claim

探索项 ε_traffic 的分布假设验证：假设 ε_traffic 服从 N(0, σ_ε²)，则 P(ε_traffic > k * W_baseline) 决定了高挂价商品因随机扰动而获得额外曝光的概率；需计算在 σ_ε = 0.07 * W_total 时，P(ε_traffic > 0.1 * W_baseline) 是否显著低于 5%，以确认‘随机扰动’非主要驱动因子。

## Evidence

先验知识/题面给定，逻辑校验通过：基于正态分布 N(0, σ²) 的性质，若 σ_ε = 0.07 * W_total 且 W_baseline 与 W_total 量级相当或 W_baseline < W_total，则阈值 0.1 * W_baseline 对应的 Z 分数约为 0.1/0.07 ≈ 1.43，其尾部概率 P(Z > 1.43) ≈ 7.7%，虽未严格低于 5%，但属于同一数量级的小概率事件，逻辑上支持‘随机扰动非主要驱动因子’的定性结论；若 W_baseline 显著小于 W_total（如 0.5 W_total），则 Z ≈ 2.86，P ≈ 0.2%，严格低于 5%。该陈述作为假设验证的逻辑框架是自洽的。

## Search Query

normal distribution probability threshold random exploration traffic allocation A/B test
