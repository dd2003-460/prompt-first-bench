# N508: P99 图片大小具体数值：基于 μ_img=0.69 (ln(2MB)), σ_img=0.5，计算得 P99_img = exp(0.69 + 2.326×0

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N171

## Claim

P99 图片大小具体数值：基于 μ_img=0.69 (ln(2MB)), σ_img=0.5，计算得 P99_img = exp(0.69 + 2.326×0.5) ≈ exp(1.853) ≈ 6.38 MB，用于确定回源带宽峰值需求。

## Corrected Claim

P99 图片大小具体数值：基于 μ_img=0.69 (ln(2MB)), σ_img=0.5，计算得 P99_img = exp(0.69 + 2.326×0.5) ≈ exp(1.853) ≈ 6.38 MB，用于确定回源带宽峰值需求。

## Evidence

先验知识/题面给定，逻辑校验通过：对数正态分布P99计算公式正确，数值推导 exp(0.69 + 2.326*0.5) = exp(1.853) ≈ 6.38 准确无误。
