# N105: 自建 POP 缓存命中率 H_pop 的计算公式为 H_pop = min(1, C_pop_total / W_active)，其中 C_pop_total 

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26

## Claim

自建 POP 缓存命中率 H_pop 的计算公式为 H_pop = min(1, C_pop_total / W_active)，其中 C_pop_total 为 10 个 POP 的总缓存容量（GB），W_active 为热点内容工作集大小（GB），H_pop 直接决定跳数为 1 的请求比例。

## Corrected Claim

自建 POP 缓存命中率 H_pop 的计算公式为 H_pop = min(1, C_pop_total / W_active)，其中 C_pop_total 为 10 个 POP 的总缓存容量（GB），W_active 为热点内容工作集大小（GB），H_pop 直接决定跳数为 1 的请求比例。

## Evidence

先验知识/题面给定，逻辑校验通过
