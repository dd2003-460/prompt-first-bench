# N528: N172 工作点下，热点内容预加载策略导致的源站额外读取负载 Cost_preload = N_hot_objects * s_avg * R_reload_f

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N172

## Claim

N172 工作点下，热点内容预加载策略导致的源站额外读取负载 Cost_preload = N_hot_objects * s_avg * R_reload_freq，假设 N_hot_objects = 10,000, s_avg = 1MB, R_reload_freq = 1次/小时，源站 IOPS 增量需评估是否触发源站扩容成本。

## Corrected Claim

N172 工作点下，热点内容预加载策略导致的源站额外读取负载 Cost_preload = N_hot_objects * s_avg * R_reload_freq，假设 N_hot_objects = 10,000, s_avg = 1MB, R_reload_freq = 1次/小时，源站 IOPS 增量需评估是否触发源站扩容成本。

## Evidence

先验知识/题面给定，逻辑校验通过
