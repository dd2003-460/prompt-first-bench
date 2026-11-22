# N39: 重填充期间并发请求的 miss 概率：P(miss | refill) = 1 - exp(-λ * t_refill)，λ = 578.7 req/s，t_r

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N12

## Claim

重填充期间并发请求的 miss 概率：P(miss | refill) = 1 - exp(-λ * t_refill)，λ = 578.7 req/s，t_refill ≈ 5.25ms，P(miss | refill) ≈ 1 - exp(-578.7 * 0.00525) ≈ 0.951

## Corrected Claim

重填充期间并发请求的 miss 概率：P(miss | refill) = 1 - exp(-λ * t_refill)，λ = 578.7 req/s，t_refill ≈ 5.25ms，P(miss | refill) ≈ 1 - exp(-578.7 * 0.00525) ≈ 0.951

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 1 - exp(-578.7 * 0.00525) ≈ 1 - exp(-3.038) ≈ 1 - 0.0479 ≈ 0.952，与陈述中的 0.951 在数值精度上高度一致，逻辑自洽。

## Search Query

concurrent request miss probability during cache refill Poisson process
