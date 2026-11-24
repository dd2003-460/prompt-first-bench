# N314: 缓存淘汰策略对 CHR 的修正因子：ΔCHR_algorithm = CHR_LFU - CHR_LRU ≈ 0.03 (3%)，基于 N117；最终 CHR_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N100, N101, N102

## Claim

缓存淘汰策略对 CHR 的修正因子：ΔCHR_algorithm = CHR_LFU - CHR_LRU ≈ 0.03 (3%)，基于 N117；最终 CHR_final = CHR_Zipf × (1 + ΔCHR_algorithm)，需区分核心 POP (LFU) 和长尾 POP (LRU) 的不同算法配置对总命中率的影响

## Corrected Claim

缓存淘汰策略对 CHR 的修正因子：ΔCHR_algorithm = CHR_LFU - CHR_LRU ≈ 0.03 (3%)，基于 N117；最终 CHR_final = CHR_Zipf × (1 + ΔCHR_algorithm)，需区分核心 POP (LFU) 和长尾 POP (LRU) 的不同算法配置对总命中率的影响

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LFU vs LRU cache hit ratio improvement benchmark
