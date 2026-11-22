# N176: H_dynamic_hit 的最终上界数值：结合 N73-N75，H_dynamic_hit ≤ 0.0488 * (0.985 * 0.5) ≈ 2.4%。此

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N68

## Claim

H_dynamic_hit 的最终上界数值：结合 N73-N75，H_dynamic_hit ≤ 0.0488 * (0.985 * 0.5) ≈ 2.4%。此值远低于 P_invalid (4.88%)，验证了 N16 中 H_dynamic_hit 可忽略的近似假设在 M/C=1.0 下成立。

## Corrected Claim

H_dynamic_hit 的最终上界数值：结合 N73-N75，H_dynamic_hit ≤ 0.0488 * (0.985 * 0.5) ≈ 2.4%。此值远低于 P_invalid (4.88%)，验证了 N16 中 H_dynamic_hit 可忽略的近似假设在 M/C=1.0 下成立。

## Evidence

先验知识/题面给定，逻辑校验通过：0.0488 * 0.4925 ≈ 0.02403 (2.4%)，且 2.4% < 4.88%，数值计算与逻辑推导自洽。
