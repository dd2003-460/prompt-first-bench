# N58: 大小加权修正项 W_s = (∑_{i=1}^K s_i h_i) / (∑_{i=1}^K s_i) / E[S]，用于修正热度分布与大小分布不一致导致的命中

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

大小加权修正项 W_s = (∑_{i=1}^K s_i h_i) / (∑_{i=1}^K s_i) / E[S]，用于修正热度分布与大小分布不一致导致的命中率偏差；在 ρ=0 假设下，W_s 接近 1，但需通过数值积分精确计算

## Corrected Claim

大小加权修正项 W_s = (∑_{i=1}^K s_i h_i) / (∑_{i=1}^K s_i) / E[S]，用于修正热度分布与大小分布不一致导致的命中率偏差；在 ρ=0 假设下，W_s 接近 1，但需通过数值积分精确计算

## Evidence

先验知识/题面给定，逻辑校验通过
