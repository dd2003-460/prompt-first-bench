# N95: Top 10对象的累计请求率占比 Σ_{i=1}^{10} w_i 约为 0.054，即头部10个对象承载了总流量的5.4%，这一集中度决定了LRU缓存中‘热区

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N28

## Claim

Top 10对象的累计请求率占比 Σ_{i=1}^{10} w_i 约为 0.054，即头部10个对象承载了总流量的5.4%，这一集中度决定了LRU缓存中‘热区’的最小容量需求

## Corrected Claim

Top 10对象的累计请求率占比 Σ_{i=1}^{10} w_i 约为 0.054，即头部10个对象承载了总流量的5.4%，这一集中度决定了LRU缓存中‘热区’的最小容量需求

## Evidence

先验知识/题面给定，逻辑校验通过
