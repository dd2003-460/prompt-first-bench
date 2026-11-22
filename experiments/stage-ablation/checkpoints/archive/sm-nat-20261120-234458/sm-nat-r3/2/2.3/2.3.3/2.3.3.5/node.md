# N134: 若引入更新率 λ_update=0.01/天，P_LRU_keep(s) 需修正为 1 - P_invalidate_LRU(s)，其中 P_invalidat

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

若引入更新率 λ_update=0.01/天，P_LRU_keep(s) 需修正为 1 - P_invalidate_LRU(s)，其中 P_invalidate_LRU(s) 取决于最近访问时间间隔与更新率的耦合

## Corrected Claim

若引入更新率 λ_update=0.01/天，P_LRU_keep(s) 需修正为 1 - P_invalidate_LRU(s)，其中 P_invalidate_LRU(s) 取决于最近访问时间间隔与更新率的耦合

## Evidence

先验知识/题面给定，逻辑校验通过
