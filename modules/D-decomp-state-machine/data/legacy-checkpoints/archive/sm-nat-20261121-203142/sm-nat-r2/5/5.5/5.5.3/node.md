# N77: Pareto 参数恒定假设的时效性：在 7 天观测窗口内，Pareto(α=1.1, β=0.9) 参数的漂移幅度（标准差）通常 <5%，若漂移 >10%，则命

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N25

## Claim

Pareto 参数恒定假设的时效性：在 7 天观测窗口内，Pareto(α=1.1, β=0.9) 参数的漂移幅度（标准差）通常 <5%，若漂移 >10%，则命中率公式需引入参数修正项 H = H_0 * (1 + ε_α * Δα + ε_β * Δβ)，其中 ε_α, ε_β 为敏感度系数，需通过敏感性分析确定 [待核验]

## Corrected Claim

在 7 天观测窗口内，若 Pareto 参数漂移幅度较小（通常认为 <5%），可假设参数恒定；若漂移显著（如 >10%），则命中率公式需引入参数修正项 H = H_0 * (1 + ε_α * Δα + ε_β * Δβ)，其中敏感度系数需通过敏感性分析确定。

## Evidence

[质询]该陈述包含具体的经验性阈值（<5%、>10%）和特定的参数组合（α=1.1, β=0.9），这些属于经验事实而非第一性原理可推导的数学性质。在缺乏具体数据集或行业基准来源支持的情况下，无法验证这些具体数值阈值的普适性或准确性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体数值阈值无法从第一性原理严格推出）

## Search Query

Pareto distribution parameter drift time series CDN workload sensitivity analysis cache hit rate
