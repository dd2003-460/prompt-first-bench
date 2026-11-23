# N309: 缓存容量需求 C_cache_req = N_objects_eff * s_avg_weighted * f_hot，其中 s_avg_weighted 为加

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N104

## Claim

缓存容量需求 C_cache_req = N_objects_eff * s_avg_weighted * f_hot，其中 s_avg_weighted 为加权平均对象大小（≈ 0.7*0.5MB + 0.3*5MB ≈ 1.85MB），f_hot 为热点内容占比（假设 20% 内容承载 80% 流量，需缓存全部热点），故 C_cache_req ≈ 7,524,000 * 1.85MB * 0.2 ≈ 27.7TB，需对比 10 个 POP 总缓存容量（假设每点 5TB，共 50TB）以判断是否充足

## Corrected Claim

缓存容量需求 C_cache_req = N_objects_eff * s_avg_weighted * f_hot，其中 s_avg_weighted 为加权平均对象大小（≈ 0.7*0.5MB + 0.3*5MB ≈ 1.85MB），f_hot 为热点内容占比（假设 20% 内容承载 80% 流量，需缓存全部热点），故 C_cache_req ≈ 7,524,000 * 1.85MB * 0.2 ≈ 27.7TB，需对比 10 个 POP 总缓存容量（假设每点 5TB，共 50TB）以判断是否充足

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均大小计算正确（0.7*0.5+0.3*5=1.85MB），容量需求计算正确（7,524,000 * 1.85 * 0.2 ≈ 27.7TB），对比逻辑自洽。
