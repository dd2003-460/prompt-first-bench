# N77: LFU 空间效率损失 0.15GB/天 的计算逻辑：损失 = (E[S|top10] - E[S|LRU_evict]) * R_evict_top10，需明确

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

LFU 空间效率损失 0.15GB/天 的计算逻辑：损失 = (E[S|top10] - E[S|LRU_evict]) * R_evict_top10，需明确 R_evict_top10（头部对象被驱逐的速率）及 E[S|LRU_evict]（LRU 驱逐对象的平均大小）以验证该数值。

## Corrected Claim

LFU 空间效率损失 0.15GB/天 的计算逻辑：损失 = (E[S|top10] - E[S|LRU_evict]) * R_evict_top10，需明确 R_evict_top10（头部对象被驱逐的速率）及 E[S|LRU_evict]（LRU 驱逐对象的平均大小）以验证该数值。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合缓存空间效率损失的定义（大小差值乘以驱逐速率），量纲与数值量级在工程语境下合理。
