# N30: 公有云CDN三线及以下城市P99延迟构成：网络传输延迟_P99 ≈ 120-200ms（最近节点距离150-500km），边缘处理延迟_P99 ≈ 5-10ms

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

公有云CDN三线及以下城市P99延迟构成：网络传输延迟_P99 ≈ 120-200ms（最近节点距离150-500km），边缘处理延迟_P99 ≈ 5-10ms，回源延迟_P99 ≈ 150-250ms（命中率90%时加权后贡献≈15-25ms）

## Corrected Claim

公有云CDN在三线及以下城市的P99延迟通常由网络传输（约100-200ms）、边缘处理（约5-10ms）及回源贡献（命中率90%时约15-25ms）构成，具体数值受节点分布与网络状况影响。

## Evidence

[质询]该陈述包含具体的经验性数值（如120-200ms传输延迟、5-10ms处理延迟等），属于特定场景下的工程经验数据，无法从第一性原理严格推导，且参考来源中未提供针对'公有云CDN三线及以下城市'这一特定细分场景的P99延迟构成数据，存在来源缺失风险。 | 逻辑上各分量延迟量级符合物理直觉（光速限制下的传输延迟、服务器处理耗时、回源加权计算正确），但参考来源[1][2][3]仅讨论P99定义或通用延迟概念，未提供该特定场景的具体数值支持，属于经验事实且缺直接来源支持。

## Search Query

Alibaba Cloud CDN P99 latency tier-3 cities China

## Retrieval Sources

- {'url': 'https://blog.csdn.net/liuxiao723846/article/details/109036203&rut=43d7003da649df40effc071f67f042ac1213a0676859e220404157c2e84b50d2', 'type': 'ddg', 'title': '服务响应时间与分布（p99指标） - CSDN博客'}
- {'url': 'https://blog.openresty.com/cn/p99-latency/&rut=233dd5c3a18a3791af688572afb0f24354b8415ef888957190725cafc9e9c8eb', 'type': 'ddg', 'title': 'P99 延迟：为什么平均值会骗人，以及如何诊断最慢的 1% - OpenResty 官方博客'}
- {'url': 'https://blog.csdn.net/weixin_30225755/article/details/167196370&rut=8d8c4d19aa0402821bebd334cd51db3c0415b51e03ca538a8ef1e9e2e2db026e', 'type': 'ddg', 'title': '实时云渲染延迟的真相：端到端链路、P95/P99指标与选型避坑指南-csdn博客'}
