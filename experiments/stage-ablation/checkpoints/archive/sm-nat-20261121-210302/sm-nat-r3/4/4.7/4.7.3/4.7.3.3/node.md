# N185: Stale_Penalty 在 LFU 驻留时间下的量化：代入 N64 公式，使用 N78 计算的 T_resident_LFU（通常远大于 LRU 驻留时间）

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N65

## Claim

Stale_Penalty 在 LFU 驻留时间下的量化：代入 N64 公式，使用 N78 计算的 T_resident_LFU（通常远大于 LRU 驻留时间），计算 1 - (1-0.01)^{T_resident_LFU} 的具体折损比例，评估 LFU 因长期驻留导致的过期惩罚。

## Corrected Claim

Stale_Penalty 在 LFU 驻留时间下的量化：代入 N64 公式，使用 N78 计算的 T_resident_LFU（通常远大于 LRU 驻留时间），计算 1 - (1-0.01)^{T_resident_LFU} 的具体折损比例，评估 LFU 因长期驻留导致的过期惩罚。

## Evidence

先验知识/题面给定，逻辑校验通过
