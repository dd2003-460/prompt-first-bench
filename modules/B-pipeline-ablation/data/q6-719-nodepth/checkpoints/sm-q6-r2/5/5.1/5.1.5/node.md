# N108: 自建POP点N-1容忍下的单点故障恢复时间 T_failover 通常为 5-15 分钟（基于 DNS TTL 或 Anycast 路由切换），期间受影响 10

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N27, N28, N29

## Claim

自建POP点N-1容忍下的单点故障恢复时间 T_failover 通常为 5-15 分钟（基于 DNS TTL 或 Anycast 路由切换），期间受影响 10% 流量的 P99 延迟上升至 T_origin + T_failover_queue，量化为 ΔP99_failover = 0.1 × (T_origin + T_failover_queue) + 0.9 × T_cache

## Corrected Claim

自建POP点单点故障恢复时间取决于DNS TTL或Anycast路由切换机制，期间受影响流量的P99延迟会因回源增加而上升，具体数值需根据实际网络配置和流量分布确定。

## Evidence

[质询]该陈述包含具体的经验参数（5-15分钟恢复时间、10%流量占比）及特定的延迟量化公式，属于经验事实而非第一性原理可推导内容；且参考来源[1]讨论的是数仓集群（CM Server）的故障恢复，与CDN/POP点的DNS/Anycast切换机制及延迟模型主题不匹配，缺乏直接外部证据支持。 | 逻辑上自洽（加权平均延迟模型合理），但来源[1]主题无关（数仓vs CDN），且具体数值（5-15min, 10%）为经验事实，无直接来源支持，依据经验事实排除条款降级。

## Search Query

edge node failover time DNS TTL anycast latency impact

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/358001378&rut=d18df473b389e13543189c37d828e345121c16ce253de9ea2a1c31f337c74bdf', 'type': 'ddg', 'title': '数仓集群管理：单节点故障rto机制分析 - 知乎'}
