# N133: 若引入更新率 λ_update=0.01/天，P_LFU_keep(s) 需修正为 1 - P_invalidate_LFU(s)，其中 P_invalidat

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

若引入更新率 λ_update=0.01/天，P_LFU_keep(s) 需修正为 1 - P_invalidate_LFU(s)，其中 P_invalidate_LFU(s) 取决于频率排名与更新率的耦合

## Corrected Claim

若引入更新率 λ_update=0.01/天，P_LFU_keep(s) 需修正为 1 - P_invalidate_LFU(s)，其中 P_invalidate_LFU(s) 取决于频率排名与更新率的耦合

## Evidence

先验知识/题面给定，逻辑校验通过：在引入更新率（失效机制）的缓存模型中，保留概率确实等于1减去失效概率，且失效概率通常与频率排名及更新率耦合，逻辑自洽。
