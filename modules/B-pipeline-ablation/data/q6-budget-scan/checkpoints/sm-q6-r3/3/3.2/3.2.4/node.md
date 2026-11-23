# N71: 缓存失效导致的额外P99延迟贡献 ΔT_cache_miss = (1-H) * (T_origin - T_hit)；若 H=0.845, T_origin=

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N17

## Claim

缓存失效导致的额外P99延迟贡献 ΔT_cache_miss = (1-H) * (T_origin - T_hit)；若 H=0.845, T_origin=200ms, T_hit=50ms，则 ΔT_cache_miss = 0.155 * 150ms = 23.25ms，需计入P99延迟预算。

## Corrected Claim

缓存失效导致的额外P99延迟贡献 ΔT_cache_miss = (1-H) * (T_origin - T_hit)；若 H=0.845, T_origin=200ms, T_hit=50ms，则 ΔT_cache_miss = 0.155 * 150ms = 23.25ms，需计入P99延迟预算。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 ΔT = (1-H)*(T_origin - T_hit) 符合缓存未命中惩罚的标准定义，数值计算 0.155 * 150 = 23.25 准确无误。
