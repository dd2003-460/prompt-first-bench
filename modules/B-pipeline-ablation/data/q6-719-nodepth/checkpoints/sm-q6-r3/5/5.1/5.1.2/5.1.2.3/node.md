# N303: P99 延迟上升幅度 ΔP99_scaling 的量化：ΔP99_scaling ≈ T_scaling × (Overflow_Rate / Total_Ra

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N105

## Claim

P99 延迟上升幅度 ΔP99_scaling 的量化：ΔP99_scaling ≈ T_scaling × (Overflow_Rate / Total_Rate) × T_origin_fallback，其中 Overflow_Rate 为超出预置容量的请求比例，T_origin_fallback 为回源延迟，需代入 T_scaling=10-30s 和具体流量模型计算。

## Corrected Claim

P99 延迟上升幅度 ΔP99_scaling 的量化：ΔP99_scaling ≈ T_scaling × (Overflow_Rate / Total_Rate) × T_origin_fallback，其中 Overflow_Rate 为超出预置容量的请求比例，T_origin_fallback 为回源延迟，需代入 T_scaling=10-30s 和具体流量模型计算。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

P99 latency increase during auto scaling delay queueing theory
