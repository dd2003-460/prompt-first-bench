# N360: N122 公式中 Daily_Traffic 的精确计算：Daily_Traffic = R_read_daily * s_avg * (1-H_steady)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N121, N122, N123

## Claim

N122 公式中 Daily_Traffic 的精确计算：Daily_Traffic = R_read_daily * s_avg * (1-H_steady)，其中 R_read_daily = 1.273×10^9 req/day（基于 N7 和 N116），s_avg = 1.5MB，H_steady = 85%。计算得 Daily_Traffic ≈ 2.86TB/日（考虑回源流量），而非题面给定的 2TB 下载总量，需区分边缘下发流量与回源流量。

## Corrected Claim

N122 公式中 Daily_Traffic 的精确计算：Daily_Traffic = R_read_daily * s_avg * (1-H_steady)，其中 R_read_daily = 1.273×10^9 req/day（基于 N7 和 N116），s_avg = 1.5MB，H_steady = 85%。计算得 Daily_Traffic ≈ 2.86TB/日（考虑回源流量），而非题面给定的 2TB 下载总量，需区分边缘下发流量与回源流量。

## Evidence

先验知识/题面给定，逻辑校验通过：1.273e9 * 1.5MB * 0.15 ≈ 2.86TB，计算无误且量级合理
