# N263: 非线性响应函数的临界阈值：当 ΔRev_seller_high / C_switch < θ_critical 时，Δs_churn ≈ 0；当比值 > θ_c

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N87, N88, N89

## Claim

非线性响应函数的临界阈值：当 ΔRev_seller_high / C_switch < θ_critical 时，Δs_churn ≈ 0；当比值 > θ_critical 时，流失率呈指数上升。θ_critical 的典型值需通过 A/B 测试或历史断点回归估计，通常落在 [0.5, 1.5] 区间。

## Corrected Claim

非线性响应函数的临界阈值：当 ΔRev_seller_high / C_switch < θ_critical 时，Δs_churn ≈ 0；当比值 > θ_critical 时，流失率呈指数上升。θ_critical 的典型值需通过 A/B 测试或历史断点回归估计，通常落在 [0.5, 1.5] 区间。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

churn threshold critical value seller profit impact
