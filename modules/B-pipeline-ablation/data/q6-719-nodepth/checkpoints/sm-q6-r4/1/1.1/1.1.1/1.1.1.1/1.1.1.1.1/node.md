# N429: 上海本地用户访问上海POP的端到端P99延迟 T_P99_local = T_network_rtt + T_processing + T_queueing，其

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N145

## Claim

上海本地用户访问上海POP的端到端P99延迟 T_P99_local = T_network_rtt + T_processing + T_queueing，其中 T_network_rtt 受限于交换机/网卡硬件处理延迟，T_processing 为CDN节点软件栈处理延迟，T_queueing 为队列等待时间

## Corrected Claim

上海本地用户访问上海POP的端到端P99延迟 T_P99_local = T_network_rtt + T_processing + T_queueing，其中 T_network_rtt 受限于交换机/网卡硬件处理延迟，T_processing 为CDN节点软件栈处理延迟，T_queueing 为队列等待时间

## Evidence

先验知识/题面给定，逻辑校验通过：端到端延迟分解为网络往返、处理及排队延迟符合网络通信基本模型，各分量定义准确且量级合理。

## Search Query

CDN edge node P99 latency breakdown network rtt processing queueing
