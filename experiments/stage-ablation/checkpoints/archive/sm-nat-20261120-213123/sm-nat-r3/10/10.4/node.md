# N79: 线性近似失效的边界条件：当 ρ * σ_logS * σ_logH < -0.5 时，线性近似 B_corr ≈ B_indep * (1 + ρ * σ_lo

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N28

## Claim

线性近似失效的边界条件：当 ρ * σ_logS * σ_logH < -0.5 时，线性近似 B_corr ≈ B_indep * (1 + ρ * σ_logS * σ_logH) 误差超过 10%，需使用 Copula 精确积分。在本例中 ρ * σ_logS * σ_logH = -0.353，接近边界，建议用 Clayton Copula 数值积分验证，预期修正因子在 0.60-0.68 之间。

## Corrected Claim

线性近似在强负相关下可能失效，当 ρ * σ_logS * σ_logH 接近 -0.353 时，建议通过 Copula 数值积分（如 Clayton Copula）验证修正因子，具体数值需根据实际分布参数计算。

## Evidence

父节点级核验未通过：不完备（子节点之间存在逻辑矛盾（父节点建议Clayton，子节点2指出Clayton不适用），且子节点1的数学推导与子节点2的参数求解结果在数值上不一致（0.647 vs 预期0.60-0.68的边界），导致分解内部不协调。此外，父节点提到的'边界条件'和'误差超过10%'的判定标准未在子节点中充分展开或验证，仅停留在近似计算。）

## Search Query

Copula cache hit rate accuracy linear approximation error
