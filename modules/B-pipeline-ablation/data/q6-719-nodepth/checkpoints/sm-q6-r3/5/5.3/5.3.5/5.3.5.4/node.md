# N305: 边缘节点本地处理延迟 L_edge_self = L_queue + L_read，其中 L_queue 为队列等待时间（与负载率 L_util 呈非线性关系，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N99, N100, N101

## Claim

边缘节点本地处理延迟 L_edge_self = L_queue + L_read，其中 L_queue 为队列等待时间（与负载率 L_util 呈非线性关系，L_util > 80% 时 L_queue > 10ms），L_read 为 NVMe 读取延迟（<1ms）；需结合 N108 的负载重分配模型，计算故障期间 L_edge_self 的峰值。

## Corrected Claim

边缘节点本地处理延迟 L_edge_self = L_queue + L_read，其中 L_queue 为队列等待时间（与负载率 L_util 呈非线性关系，L_util > 80% 时 L_queue > 10ms），L_read 为 NVMe 读取延迟（<1ms）；需结合 N108 的负载重分配模型，计算故障期间 L_edge_self 的峰值。

## Evidence

先验知识/题面给定，逻辑校验通过：边缘节点本地处理延迟由队列等待和存储读取组成，NVMe读取延迟<1ms符合硬件特性，高负载下队列延迟非线性增长符合排队论基本规律，整体逻辑自洽且数值量级合理。
