# N126: 内在价值波动项 σ_intrinsic² 的计算：由 N33 的 LogNormal 分布参数直接导出，σ_intrinsic² = exp(2μ_log + 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N36

## Claim

内在价值波动项 σ_intrinsic² 的计算：由 N33 的 LogNormal 分布参数直接导出，σ_intrinsic² = exp(2μ_log + σ_log²) * (exp(σ_log²) - 1)；该值代表了商品真实价值因成色、配件缺失等客观因素导致的不可控波动。

## Corrected Claim

内在价值波动项 σ_intrinsic² 的计算：由 N33 的 LogNormal 分布参数直接导出，σ_intrinsic² = exp(2μ_log + σ_log²) * (exp(σ_log²) - 1)；该值代表了商品真实价值因成色、配件缺失等客观因素导致的不可控波动。

## Evidence

先验知识/题面给定，逻辑校验通过：LogNormal分布的方差公式推导正确，且符合内在价值波动的定义。
