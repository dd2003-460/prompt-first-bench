# N13: 自建边缘节点架构延迟模型 L_self = RTT_pop + T_queue + T_process_self + T_transfer，其中T_queue为

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

自建边缘节点架构延迟模型 L_self = RTT_pop + T_queue + T_process_self + T_transfer，其中T_queue为排队延迟（受并发影响），T_process_self为自建服务器处理延迟，需评估10个POP点的覆盖半径对RTT的影响

## Corrected Claim

自建边缘节点架构延迟模型 L_self = RTT_pop + T_queue + T_process_self + T_transfer，其中T_queue为排队延迟（受并发影响），T_process_self为自建服务器处理延迟，需评估10个POP点的覆盖半径对RTT的影响

## Evidence

先验知识/题面给定，逻辑校验通过：延迟模型各项（RTT、排队、处理、传输）符合网络通信基本物理规律，量纲一致，无内部矛盾。

## Search Query

self-hosted CDN edge node latency queueing delay POP coverage
