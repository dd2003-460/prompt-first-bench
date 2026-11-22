# N255: 卖家调整滞后时间 τ 的中位数 τ_median 由指数分布参数 λ_τ 决定，公式为 τ_median = ln(2)/λ_τ；若假设平均调整时间为 5 天，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

卖家调整滞后时间 τ 的中位数 τ_median 由指数分布参数 λ_τ 决定，公式为 τ_median = ln(2)/λ_τ；若假设平均调整时间为 5 天，则 λ_τ = 0.2，τ_median ≈ 3.47 天。

## Corrected Claim

卖家调整滞后时间 τ 的中位数 τ_median 由指数分布参数 λ_τ 决定，公式为 τ_median = ln(2)/λ_τ；若假设平均调整时间为 5 天，则 λ_τ = 0.2，τ_median ≈ 3.47 天。

## Evidence

先验知识/题面给定，逻辑校验通过：指数分布中位数公式 τ_median = ln(2)/λ 正确，且 λ=1/5=0.2 时，ln(2)/0.2 ≈ 0.693/0.2 ≈ 3.465 ≈ 3.47，数值计算无误。
