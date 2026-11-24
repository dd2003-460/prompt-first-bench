# N26: 全自建10 POP策略的路由逻辑采用基于IP地理库的静态映射，单请求跳数为 1（用户->自建POP）或 2（用户->POP->源站，当POP未命中时），其中PO

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

全自建10 POP策略的路由逻辑采用基于IP地理库的静态映射，单请求跳数为 1（用户->自建POP）或 2（用户->POP->源站，当POP未命中时），其中POP未命中率取决于缓存命中率 H_pop。

## Corrected Claim

全自建10 POP策略的路由逻辑采用基于IP地理库的静态映射，单请求跳数为 1（用户->自建POP）或 2（用户->POP->源站，当POP未命中时），其中POP未命中率取决于缓存命中率 H_pop。

## Evidence

先验知识/题面给定，逻辑校验通过
