# N39: 在 λ=0.01/day 且假设 T_res=10 days 的条件下，失效概率 P_invalid 的精确计算值：P_invalid = 1 - exp(-0

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

在 λ=0.01/day 且假设 T_res=10 days 的条件下，失效概率 P_invalid 的精确计算值：P_invalid = 1 - exp(-0.01 * 10) ≈ 0.09516，即 9.516%。

## Corrected Claim

在 λ=0.01/day 且假设 T_res=10 days 的条件下，失效概率 P_invalid 的精确计算值：P_invalid = 1 - exp(-0.01 * 10) ≈ 0.09516，即 9.516%。

## Evidence

先验知识/题面给定，逻辑校验通过：计算 1 - exp(-0.1) ≈ 0.09516258，与陈述中的 0.09516 一致，符合指数分布失效概率公式。
