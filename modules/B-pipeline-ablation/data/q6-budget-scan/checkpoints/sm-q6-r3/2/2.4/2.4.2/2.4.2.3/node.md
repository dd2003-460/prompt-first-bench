# N200: 跨区回源对 P99 延迟的边际影响：若 H_cache 从 90% 降至 85%，跨区回源延迟贡献从 2.5ms 升至 3.75ms，P99 增加 1.25ms

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

跨区回源对 P99 延迟的边际影响：若 H_cache 从 90% 降至 85%，跨区回源延迟贡献从 2.5ms 升至 3.75ms，P99 增加 1.25ms；若 H_cache 从 95% 降至 90%，延迟贡献从 1.25ms 升至 2.5ms，P99 增加 1.25ms。表明跨区回源的 P99 敏感度与核心区域相近（约 0.25-0.5ms/1% 命中率降低），但绝对值更高，需在混合策略中优先保障核心区域的缓存命中率。

## Corrected Claim

跨区回源对 P99 延迟的边际影响：若 H_cache 从 90% 降至 85%，跨区回源延迟贡献从 2.5ms 升至 3.75ms，P99 增加 1.25ms；若 H_cache 从 95% 降至 90%，延迟贡献从 1.25ms 升至 2.5ms，P99 增加 1.25ms。表明跨区回源的 P99 敏感度与核心区域相近（约 0.25-0.5ms/1% 命中率降低），但绝对值更高，需在混合策略中优先保障核心区域的缓存命中率。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算自洽（2.5-1.25=1.25, 3.75-2.5=1.25），敏感度推导合理（1.25ms/5%=0.25ms/1%），符合缓存命中率与延迟贡献的线性关系直觉。

## Search Query

cross-region cache hit rate sensitivity P99 latency marginal impact
