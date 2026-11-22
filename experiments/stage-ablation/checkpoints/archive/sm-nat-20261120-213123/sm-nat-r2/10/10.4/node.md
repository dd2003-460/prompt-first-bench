# N79: 线性近似失效的边界条件：当 ρ * σ_logS * σ_logH < -0.5 时，线性近似 B_corr ≈ B_indep * (1 + ρ * σ_lo

- **status**: degraded
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

[质询]该陈述包含具体的经验性阈值（-0.5）和特定的数值预测（0.60-0.68），属于金融工程中的经验事实或特定模型参数，无法仅从第一性原理严格推导，且缺乏外部来源支持其具体数值的准确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Copula cache hit rate accuracy linear approximation error
