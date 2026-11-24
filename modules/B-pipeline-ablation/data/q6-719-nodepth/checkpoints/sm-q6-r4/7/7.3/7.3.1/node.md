# N369: 单 POP 点有效缓存容量 C_cache_pop = 总存储容量 × (1 - 系统预留比例 10%)，例如若单 POP 配置 100TB 存储，则 C_ca

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N128

## Claim

单 POP 点有效缓存容量 C_cache_pop = 总存储容量 × (1 - 系统预留比例 10%)，例如若单 POP 配置 100TB 存储，则 C_cache_pop ≈ 90TB，该值直接决定单节点可容纳的热门对象数量上限。

## Corrected Claim

单 POP 点有效缓存容量 C_cache_pop = 总存储容量 × (1 - 系统预留比例 10%)，例如若单 POP 配置 100TB 存储，则 C_cache_pop ≈ 90TB，该值直接决定单节点可容纳的热门对象数量上限。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN edge node storage utilization ratio overhead
