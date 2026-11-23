# N9: 不同策略下的延迟分布模型：公有云 CDN 延迟服从截断正态分布 N(μ_cdn, σ_cdn²)，其中 μ_cdn ≈ 30ms（国内平均），σ_cdn ≈ 1

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

不同策略下的延迟分布模型：公有云 CDN 延迟服从截断正态分布 N(μ_cdn, σ_cdn²)，其中 μ_cdn ≈ 30ms（国内平均），σ_cdn ≈ 10ms；自建边缘节点延迟服从 N(μ_self, σ_self²)，其中 μ_self ≈ 15ms（核心区域），σ_self ≈ 5ms；混合策略延迟为加权平均：μ_mix = w_self * μ_self + w_cdn * μ_cdn，σ_mix = sqrt(w_self² * σ_self² + w_cdn² * σ_cdn² + 2 * w_self * w_cdn * ρ * σ_self * σ_cdn)，其中 ρ 为相关性系数（假设 0.5）。

## Corrected Claim

不同策略下的延迟分布模型：公有云 CDN 延迟服从截断正态分布 N(μ_cdn, σ_cdn²)，其中 μ_cdn ≈ 30ms（国内平均），σ_cdn ≈ 10ms；自建边缘节点延迟服从 N(μ_self, σ_self²)，其中 μ_self ≈ 15ms（核心区域），σ_self ≈ 5ms；混合策略延迟为加权平均：μ_mix = w_self * μ_self + w_cdn * μ_cdn，σ_mix = sqrt(w_self² * σ_self² + w_cdn² * σ_cdn² + 2 * w_self * w_cdn * ρ * σ_self * σ_cdn)，其中 ρ 为相关性系数（假设 0.5）。

## Evidence

先验知识/题面给定，逻辑校验通过
