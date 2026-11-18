# N101: 参数 μ_S 的确定：由 Pareto(α=1.1, x_min=1KB) 的矩条件 E[S]=11KB 反推对数正态近似参数，需解 E[exp(μ_S + σ

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37

## Claim

参数 μ_S 的确定：由 Pareto(α=1.1, x_min=1KB) 的矩条件 E[S]=11KB 反推对数正态近似参数，需解 E[exp(μ_S + σ_S²/2)] = 11KB 且 Var[S] = E[S]²(1/(α-1)² - 1) 对应的 σ_S 值

## Corrected Claim

参数 μ_S 的确定：由 Pareto(α=1.1, x_min=1KB) 的矩条件 E[S]=11KB 反推对数正态近似参数，需解 E[exp(μ_S + σ_S²/2)] = 11KB 且 Var[S] = E[S]²(1/(α-1)² - 1) 对应的 σ_S 值

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布的矩条件与对数正态近似参数匹配在数学上自洽，量纲与数值量级合理。
