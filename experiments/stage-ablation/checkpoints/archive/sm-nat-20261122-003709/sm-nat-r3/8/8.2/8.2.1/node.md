# N240: 将N103计算得出的T_res数值代入公式 M_invalidation = 1 - exp(-0.01 * T_res)，计算具体的失效概率百分比，例如若T_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N90

## Claim

将N103计算得出的T_res数值代入公式 M_invalidation = 1 - exp(-0.01 * T_res)，计算具体的失效概率百分比，例如若T_res=10天，则M_invalidation ≈ 9.5%。

## Corrected Claim

将N103计算得出的T_res数值代入公式 M_invalidation = 1 - exp(-0.01 * T_res)，计算具体的失效概率百分比，例如若T_res=10天，则M_invalidation ≈ 9.5%。

## Evidence

先验知识/题面给定，逻辑校验通过：计算 1 - exp(-0.01 * 10) = 1 - exp(-0.1) ≈ 1 - 0.9048 = 0.0952，即 9.52%，与陈述中的 9.5% 一致。

## Search Query

Calculate cache invalidation probability using Poisson update rate and residence time
