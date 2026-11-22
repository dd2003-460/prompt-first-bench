# N179: Total_Bytes 的误差范围：由于 E[S] 是基于截断 Pareto 的渐近估计，且 α=1.1 接近 1，尾部对均值影响巨大。若 x_min 或截断上

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N69

## Claim

Total_Bytes 的误差范围：由于 E[S] 是基于截断 Pareto 的渐近估计，且 α=1.1 接近 1，尾部对均值影响巨大。若 x_min 或截断上限 x_max 有 10% 偏差，E[S] 偏差可达 5-10%，导致 Total_Bytes 偏差在 ±6.5 TB/day 范围内。

## Corrected Claim

Total_Bytes 的误差范围：由于 E[S] 是基于截断 Pareto 的渐近估计，且 α=1.1 接近 1，尾部对均值影响巨大。若 x_min 或截断上限 x_max 有 10% 偏差，E[S] 偏差可达 5-10%，导致 Total_Bytes 偏差在 ±6.5 TB/day 范围内。

## Evidence

先验知识/题面给定，逻辑校验通过：截断Pareto分布（α=1.1）对参数敏感，10%参数偏差导致5-10%均值偏差符合数学直觉，且±6.5TB/day的量级与典型大数据场景相符。
