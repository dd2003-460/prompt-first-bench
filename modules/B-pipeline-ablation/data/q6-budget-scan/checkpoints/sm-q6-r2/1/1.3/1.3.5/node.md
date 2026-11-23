# N45: P99超标的临界条件量化：P99_latency = P50_hit + (1-H) * P99_origin，当H=0.845时，P99_latency = 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

P99超标的临界条件量化：P99_latency = P50_hit + (1-H) * P99_origin，当H=0.845时，P99_latency = 50ms + 0.155 * 73.26ms = 61.35ms；需计算不同H值下P99_latency与T的差距，确定H的最低阈值（H_min = 1 - (T - P50_hit)/P99_origin）

## Corrected Claim

P99超标的临界条件量化：P99_latency = P50_hit + (1-H) * P99_origin，当H=0.845时，P99_latency = 50ms + 0.155 * 73.26ms = 61.35ms；需计算不同H值下P99_latency与T的差距，确定H的最低阈值（H_min = 1 - (T - P50_hit)/P99_origin）

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 50 + 0.155 * 73.26 ≈ 61.35 正确，公式推导 H_min = 1 - (T - P50_hit)/P99_origin 符合代数逻辑。

## Search Query

CDN P99 latency threshold cache hit rate minimum requirement
