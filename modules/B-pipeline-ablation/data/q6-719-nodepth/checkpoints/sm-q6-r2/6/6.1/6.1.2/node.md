# N161: P99 延迟计算中的回源概率修正项：实际 P99 需考虑缓存未命中导致的长尾延迟，公式为 P99_actual = P99_hit + (1 - H_cache

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

P99 延迟计算中的回源概率修正项：实际 P99 需考虑缓存未命中导致的长尾延迟，公式为 P99_actual = P99_hit + (1 - H_cache) * P99_miss_penalty，其中 H_cache 为缓存命中率，P99_miss_penalty 为回源额外耗时（通常 50-200ms），低命中率场景下 P99 会显著高于平均延迟

## Corrected Claim

P99 延迟计算中的回源概率修正项：实际 P99 需考虑缓存未命中导致的长尾延迟，公式为 P99_actual = P99_hit + (1 - H_cache) * P99_miss_penalty，其中 H_cache 为缓存命中率，P99_miss_penalty 为回源额外耗时（通常 50-200ms），低命中率场景下 P99 会显著高于平均延迟

## Evidence

先验知识/题面给定，逻辑校验通过
