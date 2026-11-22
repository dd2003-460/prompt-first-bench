# N361: 3个月（12周）后 C_intervention > 0.5 的临界条件：若 δc(12) = δc_0 * e^(-12*λ_decay) > 0.5 * δ

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N123

## Claim

3个月（12周）后 C_intervention > 0.5 的临界条件：若 δc(12) = δc_0 * e^(-12*λ_decay) > 0.5 * δc_0，则要求 λ_decay < ln(2)/12 ≈ 0.0577/周；若 λ_decay 估计值超过此阈值，则长期可信度失效。

## Corrected Claim

3个月（12周）后 C_intervention > 0.5 的临界条件：若 δc(12) = δc_0 * e^(-12*λ_decay) > 0.5 * δc_0，则要求 λ_decay < ln(2)/12 ≈ 0.0577/周；若 λ_decay 估计值超过此阈值，则长期可信度失效。

## Evidence

先验知识/题面给定，逻辑校验通过：不等式 δc_0 * e^(-12λ) > 0.5 * δc_0 等价于 e^(-12λ) > 0.5，取对数得 -12λ > ln(0.5) = -ln(2)，即 λ < ln(2)/12 ≈ 0.0577，推导严谨且数值正确。
