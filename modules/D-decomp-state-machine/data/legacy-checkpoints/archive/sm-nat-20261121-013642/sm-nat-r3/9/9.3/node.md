# N89: ΔH = H_LFU - H_LRU 的上界公式：ΔH_max ≈ (1 - H_LRU) * (1 - P_LFU_miss_on_hot) * (P_LRU

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

ΔH = H_LFU - H_LRU 的上界公式：ΔH_max ≈ (1 - H_LRU) * (1 - P_LFU_miss_on_hot) * (P_LRU_miss_on_hot - P_LFU_miss_on_hot)，其中 P_LRU_miss_on_hot 为 LRU 对热门对象的 miss 率，需通过仿真获取

## Corrected Claim

ΔH = H_LFU - H_LRU 的上界公式：ΔH_max ≈ (1 - H_LRU) * (1 - P_LFU_miss_on_hot) * (P_LRU_miss_on_hot - P_LFU_miss_on_hot)，其中 P_LRU_miss_on_hot 为 LRU 对热门对象的 miss 率，需通过仿真获取

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LFU LRU hit rate difference upper bound formula hot object miss rate
