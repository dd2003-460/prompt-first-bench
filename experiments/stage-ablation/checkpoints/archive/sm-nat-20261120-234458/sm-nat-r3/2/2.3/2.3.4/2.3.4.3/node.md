# N137: LRU 驱逐大冷对象造成的字节损失占比公式应为 (S_tail90% - S_top10%) / S_total_avg，而非 (S_tail90% - S_t

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N42

## Claim

LRU 驱逐大冷对象造成的字节损失占比公式应为 (S_tail90% - S_top10%) / S_total_avg，而非 (S_tail90% - S_top10%) / S_tail90%，需明确分母定义

## Corrected Claim

LRU 驱逐大冷对象造成的字节损失占比公式应为 (S_tail90% - S_top10%) / S_total_avg，而非 (S_tail90% - S_top10%) / S_tail90%，需明确分母定义

## Evidence

先验知识/题面给定，逻辑校验通过：LRU驱逐大冷对象造成的字节损失占比，其分母应为总平均大小（S_total_avg）以反映整体影响，而非仅尾部大小（S_tail90%），公式定义在逻辑上自洽且符合缓存分析常规口径。
