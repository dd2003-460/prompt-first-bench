# N102: 修正 N38 的公式量纲错误：原公式 correction_factor = 1 - (ρ * σ_size * σ_rank) / (μ_size * μ_r

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N38

## Claim

修正 N38 的公式量纲错误：原公式 correction_factor = 1 - (ρ * σ_size * σ_rank) / (μ_size * μ_rank) 中分子为方差量纲（KB^2 * rank^2），分母为均值量纲（KB * rank），导致量纲不一致且数值巨大。正确的负相关对有效容量或命中率的影响应通过联合分布积分或 Copula 模型计算，而非简单的线性修正因子。

## Corrected Claim

修正 N38 的公式量纲错误：原公式 correction_factor = 1 - (ρ * σ_size * σ_rank) / (μ_size * μ_rank) 中分子为方差量纲（KB^2 * rank^2），分母为均值量纲（KB * rank），导致量纲不一致且数值巨大。正确的负相关对有效容量或命中率的影响应通过联合分布积分或 Copula 模型计算，而非简单的线性修正因子。

## Evidence

先验知识/题面给定，逻辑校验通过：原公式分子为方差量纲（KB^2 * rank^2），分母为均值量纲（KB * rank），量纲确实不一致且数值量级不合理；负相关对有效容量的影响确实需通过联合分布或Copula模型计算，而非简单线性修正。

## Search Query

copula model cache hit rate size popularity correlation
