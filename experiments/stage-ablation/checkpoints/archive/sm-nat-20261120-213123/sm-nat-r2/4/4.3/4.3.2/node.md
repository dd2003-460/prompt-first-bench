# N57: LFU 在动态更新场景下的失效概率：当对象更新率 u=1%/天 时，LFU 频率计数器的重置机制导致其失效概率 P_lfu_invalidate = 1 - e

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19

## Claim

LFU 在动态更新场景下的失效概率：当对象更新率 u=1%/天 时，LFU 频率计数器的重置机制导致其失效概率 P_lfu_invalidate = 1 - e^(-T_counter/T_obj)，其中 T_counter 为计数器半衰期（通常设为 1 天），T_obj=100 天，故 P_lfu_invalidate ≈ 1%。

## Corrected Claim

LFU 在动态更新场景下的失效概率：当对象更新率 u=1%/天 时，LFU 频率计数器的重置机制导致其失效概率 P_lfu_invalidate = 1 - e^(-T_counter/T_obj)，其中 T_counter 为计数器半衰期（通常设为 1 天），T_obj=100 天，故 P_lfu_invalidate ≈ 1%。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 P = 1 - e^(-T_counter/T_obj) 在 T_counter=1, T_obj=100 时，P ≈ 1 - e^(-0.01) ≈ 0.00995 ≈ 1%，数值量级与逻辑自洽。

## Search Query

LFU counter reset mechanism dynamic update invalidation probability
