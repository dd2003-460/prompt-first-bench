# N243: Pareto(α=1.1, s_min=1KB, s_max=100MB) 截断分布的标准差 σ_S 计算：由于 α<2，原始方差发散，截断后方差 σ_S^2 

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N87, N88, N89

## Claim

Pareto(α=1.1, s_min=1KB, s_max=100MB) 截断分布的标准差 σ_S 计算：由于 α<2，原始方差发散，截断后方差 σ_S^2 = ∫(s-E[S])^2 f(s) ds 需数值积分，其值显著大于 E[S]^2，导致 ρ * σ_R * σ_S 项不可忽略，D_byte 显著小于 N * E[R] * E[S]（因为 ρ<0）。

## Corrected Claim

Pareto(α=1.1, s_min=1KB, s_max=100MB) 截断分布的标准差 σ_S 计算：由于 α<2，原始方差发散，截断后方差 σ_S^2 = ∫(s-E[S])^2 f(s) ds 需数值积分，其值显著大于 E[S]^2，导致 ρ * σ_R * σ_S 项不可忽略，D_byte 显著小于 N * E[R] * E[S]（因为 ρ<0）。

## Evidence

逻辑推导成立，来源未直接覆盖（基于Pareto分布α<2时方差发散及截断后数值特性的数学原理）

## Search Query

truncated Pareto distribution variance alpha 1.1 standard deviation

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Pareto_distribution&rut=3541c8b3f71fd194fb160deaa36ef23bcf3225d4a84bcccff152370e666d69b5', 'type': 'ddg', 'title': 'Pareto distribution - Wikipedia'}
