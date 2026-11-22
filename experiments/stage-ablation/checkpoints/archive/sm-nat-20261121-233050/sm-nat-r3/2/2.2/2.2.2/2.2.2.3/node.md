# N102: K 值的渐近估计修正项：K ≈ N * (C / (N * E[S]))^{α/(1-ρ*σ)}，其中 σ 为大小分布的对数标准差，在 α=1.1 和 ρ=-0

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N37

## Claim

K 值的渐近估计修正项：K ≈ N * (C / (N * E[S]))^{α/(1-ρ*σ)}，其中 σ 为大小分布的对数标准差，在 α=1.1 和 ρ=-0.3 下，该修正使 K 估计值比独立情况高约 5-10%。

## Corrected Claim

K 值的渐近估计修正项公式为 K ≈ N * (C / (N * E[S]))^{α/(1-ρ*σ)}，其中 σ 为大小分布的对数标准差。在 α=1.1 和 ρ=-0.3 的参数设定下，该修正项会使 K 估计值高于独立情况，具体增幅需依据特定负载模型确定（原陈述称约为 5-10%，但缺乏直接来源支持）。

## Evidence

[质询]该陈述包含具体的经验性数值结论（'高约 5-10%'）和特定的参数组合（α=1.1, ρ=-0.3），这属于经验事实而非纯数学推导。参考来源仅提供了关于静态频率缓存渐近最优性的理论框架，并未提供针对该特定参数组合下的具体数值模拟结果或修正幅度数据，因此无法从现有来源直接验证该具体百分比范围。 | 来源 [1] 和 [2] 讨论了请求相关性对缓存性能的影响，支持了存在修正项的逻辑背景，但未提供具体的 5-10% 数值支持；该数值属于经验事实，逻辑自洽但缺来源直接支持。

## Search Query

asymptotic cache size estimation with correlated size and frequency distributions

## Retrieval Sources

- {'url': 'https://arxiv.org/html/0903.4898v1&rut=61b307c0401c2d0d994be551598c811f5487c83c6967dd2cfc2c4b6e4d1323ea', 'type': 'ddg', 'title': 'Asymptotic Optimality of the Static Frequency Caching in the Presence ...'}
- {'url': 'https://arxiv.org/abs/0903.4898&rut=c5095972379c41f2d79bf84d652816d00f9f7f31cd3cd9127bdee4bd32d3a683', 'type': 'ddg', 'title': 'Asymptotic Optimality of the Static Frequency Caching in the Presence ...'}
