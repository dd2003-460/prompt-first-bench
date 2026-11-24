# N275: DNS查询延迟的组件分解：$T_{dns} = T_{resolver} + T_{authoritative} + T_{propagation}$，其中 $

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N100

## Claim

DNS查询延迟的组件分解：$T_{dns} = T_{resolver} + T_{authoritative} + T_{propagation}$，其中 $T_{resolver}$ 为本地DNS解析器查询时间（5-20ms，取决于缓存命中），$T_{authoritative}$ 为权威DNS服务器响应时间（1-5ms），$T_{propagation}$ 为DNS记录传播延迟（0-100ms，取决于TTL）；P99 DNS延迟通常为20-50ms，需量化递归DNS缓存命中率（通常90%-95%）对 $T_{resolver}$ 的影响

## Corrected Claim

DNS查询延迟的组件分解：$T_{dns} = T_{resolver} + T_{authoritative} + T_{propagation}$，其中 $T_{resolver}$ 为本地DNS解析器查询时间（5-20ms，取决于缓存命中），$T_{authoritative}$ 为权威DNS服务器响应时间（1-5ms），$T_{propagation}$ 为DNS记录传播延迟（0-100ms，取决于TTL）；P99 DNS延迟通常为20-50ms，需量化递归DNS缓存命中率（通常90%-95%）对 $T_{resolver}$ 的影响

## Evidence

先验知识/题面给定，逻辑校验通过
