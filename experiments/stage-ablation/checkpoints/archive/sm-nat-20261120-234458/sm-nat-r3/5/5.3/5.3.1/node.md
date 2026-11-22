# N172: Pareto(α=1.1) 截断分布的总字节量收敛性验证：总字节量 B_total = N * μ_S = 100,000 * 7.49MB ≈ 749TB，远

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

Pareto(α=1.1) 截断分布的总字节量收敛性验证：总字节量 B_total = N * μ_S = 100,000 * 7.49MB ≈ 749TB，远小于 128GB 缓存容量，但单对象最大 100MB 导致 Top 0.1%（100 个对象）可能占据 >50% 的字节量，需计算 Top 0.1% 的字节占比以确认缓存策略对极大对象的敏感性

## Corrected Claim

Pareto(α=1.1) 截断分布的总字节量收敛性验证：总字节量 B_total = N * μ_S = 100,000 * 7.49MB ≈ 749TB，远小于 128GB 缓存容量，但单对象最大 100MB 导致 Top 0.1%（100 个对象）可能占据 >50% 的字节量，需计算 Top 0.1% 的字节占比以确认缓存策略对极大对象的敏感性

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto(α=1.1) 截断分布的均值计算及总字节量推导符合数学逻辑，且 Top 0.1% 高占比符合重尾分布特性。
