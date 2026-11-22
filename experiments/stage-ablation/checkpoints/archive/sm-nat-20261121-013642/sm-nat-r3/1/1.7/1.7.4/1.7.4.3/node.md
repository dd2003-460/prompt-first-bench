# N156: LFU 相比 LRU 的最大字节命中率提升下界 ΔH_min = (B_lfu_tail - B_lru_hot) / R_bytes_total，在 B_lf

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N52

## Claim

LFU 相比 LRU 的最大字节命中率提升下界 ΔH_min = (B_lfu_tail - B_lru_hot) / R_bytes_total，在 B_lfu_tail < B_lru_hot 时为负值，表明 LFU 在此参数下可能劣于 LRU，需验证符号

## Corrected Claim

LFU 相比 LRU 的最大字节命中率提升下界 ΔH_min = (B_lfu_tail - B_lru_hot) / R_bytes_total，在 B_lfu_tail < B_lru_hot 时为负值，表明 LFU 在此参数下可能劣于 LRU，需验证符号

## Evidence

先验知识/题面给定，逻辑校验通过
