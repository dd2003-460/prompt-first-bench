# N33: 黑盒参数的先验分布假设：T 的先验分布为均匀分布 U(100ms, 500ms)，s 的先验分布为对数正态分布 LogNormal(μ=ln(500KB), σ

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

黑盒参数的先验分布假设：T 的先验分布为均匀分布 U(100ms, 500ms)，s 的先验分布为对数正态分布 LogNormal(μ=ln(500KB), σ=0.5)，geo_share 的先验分布为 Dirichlet 分布 Dir(α_1, α_2, ..., α_N)，其中 α_i 反映区域流量不确定性，通过蒙特卡洛采样 1000 次，计算每种策略的成本均值和 95% 置信区间，用于量化不确定性对最终决策的影响。

## Corrected Claim

黑盒参数的先验分布假设：T 的先验分布为均匀分布 U(100ms, 500ms)，s 的先验分布为对数正态分布 LogNormal(μ=ln(500KB), σ=0.5)，geo_share 的先验分布为 Dirichlet 分布 Dir(α_1, α_2, ..., α_N)，其中 α_i 反映区域流量不确定性，通过蒙特卡洛采样 1000 次，计算每种策略的成本均值和 95% 置信区间，用于量化不确定性对最终决策的影响。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

prior distribution assumption T s geographic distribution Dirichlet Monte Carlo sampling 1000 iterations confidence interval
