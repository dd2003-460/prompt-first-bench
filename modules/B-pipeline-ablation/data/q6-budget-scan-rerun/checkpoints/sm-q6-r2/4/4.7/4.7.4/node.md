# N124: 混合策略故障域耦合风险：若核心自建POP故障，流量回退至公有云长尾节点，此时P99延迟 = max(Self_POP_P99, Cloud_Fallback_P

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

混合策略故障域耦合风险：若核心自建POP故障，流量回退至公有云长尾节点，此时P99延迟 = max(Self_POP_P99, Cloud_Fallback_P99)，且回退瞬间缓存未命中导致Origin_Latency占比激增，需计算回退场景下的最坏P99值

## Corrected Claim

混合策略故障域耦合风险：若核心自建POP故障，流量回退至公有云长尾节点，此时P99延迟 = max(Self_POP_P99, Cloud_Fallback_P99)，且回退瞬间缓存未命中导致Origin_Latency占比激增，需计算回退场景下的最坏P99值

## Evidence

先验知识/题面给定，逻辑校验通过：在混合架构中，故障回退路径的延迟确实由原路径与回退路径的最大值决定，且缓存失效导致源站延迟占比增加符合CDN/边缘计算的基本原理。
