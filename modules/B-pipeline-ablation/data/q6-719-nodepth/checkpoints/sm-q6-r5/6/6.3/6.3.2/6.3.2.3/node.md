# N331: 重分配拓扑约束：若故障POP的流量均匀重分配至K个邻近POP，单个邻近POP增加的流量占比为 g_i/K；当K=2时，每个邻近POP增加5%流量，负载率增量 =

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N108

## Claim

重分配拓扑约束：若故障POP的流量均匀重分配至K个邻近POP，单个邻近POP增加的流量占比为 g_i/K；当K=2时，每个邻近POP增加5%流量，负载率增量 = 60% × (5%/40%) = 7.5%，L_neighbor = 67.5%；此拓扑约束决定了最坏情况下的延迟峰值。

## Corrected Claim

重分配拓扑约束：若故障POP的流量均匀重分配至K个邻近POP，单个邻近POP增加的流量占比为 g_i/K；当K=2时，每个邻近POP增加5%流量，负载率增量 = 60% × (5%/40%) = 7.5%，L_neighbor = 67.5%；此拓扑约束决定了最坏情况下的延迟峰值。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 60% * (5%/40%) = 7.5% 正确，60% + 7.5% = 67.5% 正确，拓扑约束逻辑自洽。
