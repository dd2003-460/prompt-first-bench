# N131: 热度 Top-10% 对象的平均访问频率 f_avg_top10 的计算：f_avg_top10 = R_total * (Σ_{i=1}^{0.1N} i^{

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N55

## Claim

热度 Top-10% 对象的平均访问频率 f_avg_top10 的计算：f_avg_top10 = R_total * (Σ_{i=1}^{0.1N} i^{-β}) / (Σ_{j=1}^{N} j^{-β})，代入 R_total=5e7, β=0.9, N=1e5，计算得 f_avg_top10 ≈ 5e7 * (H_{10000, 0.9} - H_{100000, 0.9}) / H_{100000, 0.9}，其中 H_{n, β} 为广义调和数。

## Corrected Claim

热度 Top-10% 对象的平均访问频率 f_avg_top10 的计算：f_avg_top10 = R_total * (Σ_{i=1}^{0.1N} i^{-β}) / (Σ_{j=1}^{N} j^{-β})，代入 R_total=5e7, β=0.9, N=1e5，计算得 f_avg_top10 ≈ 5e7 * (H_{10000, 0.9} - H_{100000, 0.9}) / H_{100000, 0.9}，其中 H_{n, β} 为广义调和数。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Pareto distribution average frequency top percentile calculation
