# N24: 全自建策略的控制粒度：控制粒度 G_self 定义为可独立配置的最小单元数量，自建边缘节点的控制粒度为节点级（每个 POP 点可独立配置），单节点可配置参数包括

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

全自建策略的控制粒度：控制粒度 G_self 定义为可独立配置的最小单元数量，自建边缘节点的控制粒度为节点级（每个 POP 点可独立配置），单节点可配置参数包括缓存命中率优化、回源带宽限制、QoS 优先级等，控制粒度数值为 N_POPS = 10，每个 POP 点可独立调整 P99 延迟目标，且可自定义缓存算法（如 LFU vs LRU）。

## Corrected Claim

全自建策略的控制粒度：控制粒度 G_self 定义为可独立配置的最小单元数量，自建边缘节点的控制粒度为节点级（每个 POP 点可独立配置），单节点可配置参数包括缓存命中率优化、回源带宽限制、QoS 优先级等，控制粒度数值为 N_POPS = 10，每个 POP 点可独立调整 P99 延迟目标，且可自定义缓存算法（如 LFU vs LRU）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

self-hosted CDN node level control granularity custom cache algorithm LFU LRU QoS priority
