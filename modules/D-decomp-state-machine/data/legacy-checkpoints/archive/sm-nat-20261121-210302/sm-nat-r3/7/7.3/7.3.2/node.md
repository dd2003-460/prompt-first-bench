# N206: 在 MissRate_LRU=0.5 且 P_hot_bytes=0.5 的工作点下，Δ% 的上界计算为 (S_LRU_evict / S_LFU_hot - 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N77

## Claim

在 MissRate_LRU=0.5 且 P_hot_bytes=0.5 的工作点下，Δ% 的上界计算为 (S_LRU_evict / S_LFU_hot - 1) * 0.5 * 0.5，量化了高失效率与中等热点覆盖下的最大提升空间，此时 LFU 优势最显著。

## Corrected Claim

在 MissRate_LRU=0.5 且 P_hot_bytes=0.5 的工作点下，Δ% 的上界计算为 (S_LRU_evict / S_LFU_hot - 1) * 0.5 * 0.5，量化了高失效率与中等热点覆盖下的最大提升空间，此时 LFU 优势最显著。

## Evidence

先验知识/题面给定，逻辑校验通过
