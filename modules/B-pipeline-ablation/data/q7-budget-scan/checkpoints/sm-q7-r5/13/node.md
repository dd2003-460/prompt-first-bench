# N137: HDD+SSD分层方案的扩容异构风险：当冷数据增长超过HDD池容量时，需同时扩容HDD和可能迁移温数据至SSD，扩容成本函数非线性；若冷数据占比从80%上升至9

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

HDD+SSD分层方案的扩容异构风险：当冷数据增长超过HDD池容量时，需同时扩容HDD和可能迁移温数据至SSD，扩容成本函数非线性；若冷数据占比从80%上升至90%，HDD采购成本占比将从~30%上升至~50%，但SSD层可能因温数据减少而缩减，导致整体扩容复杂度增加，运维工时增加20%。

## Corrected Claim

HDD+SSD分层方案的扩容异构风险：当冷数据增长超过HDD池容量时，需同时扩容HDD和可能迁移温数据至SSD，扩容成本函数非线性；若冷数据占比从80%上升至90%，HDD采购成本占比将从~30%上升至~50%，但SSD层可能因温数据减少而缩减，导致整体扩容复杂度增加，运维工时增加20%。

## Evidence

检索失败: no sources from any channel (all 5 failed)
