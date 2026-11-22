# N57: LRU 稳态字节命中率下界 H_LRU_lower 的计算：H_LRU_lower = 1 - (1 - p_hit_cold_start) * (1 - H_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N16

## Claim

LRU 稳态字节命中率下界 H_LRU_lower 的计算：H_LRU_lower = 1 - (1 - p_hit_cold_start) * (1 - H_steady)，其中 p_hit_cold_start 为冷启动后首次访问的命中率，H_steady 为稳态命中率，需分离冷启动效应

## Corrected Claim

LRU 稳态字节命中率下界 H_LRU_lower 的计算：H_LRU_lower = 1 - (1 - p_hit_cold_start) * (1 - H_steady)，其中 p_hit_cold_start 为冷启动后首次访问的命中率，H_steady 为稳态命中率，需分离冷启动效应

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LRU cache steady state hit rate lower bound cold start
