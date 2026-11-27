# N65: LFU 提升上限的最终约束：ΔH_max <= P_hot_bytes * (1 - Stale_Penalty) * MissRate_LRU，其中 Miss

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N15

## Claim

LFU 提升上限的最终约束：ΔH_max <= P_hot_bytes * (1 - Stale_Penalty) * MissRate_LRU，其中 MissRate_LRU 为 LRU 基础未命中率

## Corrected Claim

LFU 提升上限的最终约束：ΔH_max <= P_hot_bytes * (1 - Stale_Penalty) * MissRate_LRU，其中 MissRate_LRU 为 LRU 基础未命中率

## Evidence

先验知识/题面给定，逻辑校验通过
