# N13: 自建边缘节点架构延迟模型 L_self = RTT_pop + T_queue + T_process_self + T_transfer，其中T_queue为

- **status**: pending
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

父节点级核验未通过：不完备（子节点正交性良好，分别对应延迟模型中的不同物理/逻辑阶段。但存在完备性缺陷：父节点公式明确包含 'T_transfer'（传输/序列化延迟），且提到需评估覆盖半径对RTT的影响（通常隐含带宽或链路质量因素），但提供的3个子节点仅覆盖了 RTT_pop、T_queue 和 T_process_self，完全缺失了对 T_transfer 的量化分解或说明。）

## Search Query

self-hosted CDN edge node latency queueing delay POP coverage
