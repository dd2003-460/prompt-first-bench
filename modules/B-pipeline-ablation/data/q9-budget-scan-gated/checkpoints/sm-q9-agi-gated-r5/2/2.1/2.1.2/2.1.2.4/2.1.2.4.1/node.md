# N130: 在 V100 SXM2 的 NVLink 3 拓扑（Full Mesh）下，TP=4 的 Ring-AllReduce 算法实际涉及 2*(4-1)=6 跳传输

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

在 V100 SXM2 的 NVLink 3 拓扑（Full Mesh）下，TP=4 的 Ring-AllReduce 算法实际涉及 2*(4-1)=6 跳传输；单次 AllReduce 的总延迟 T_total = 6 * (T_latency + T_bandwidth)，其中 T_bandwidth 取决于消息大小 M 和有效带宽 B_eff（约 20-25 GB/s per link，受协议开销限制）。

## Corrected Claim

在 V100 SXM2 的 NVLink 3 拓扑（Full Mesh）下，TP=4 的 Ring-AllReduce 算法实际涉及 2*(4-1)=6 跳传输；单次 AllReduce 的总延迟 T_total = 6 * (T_latency + T_bandwidth)，其中 T_bandwidth 取决于消息大小 M 和有效带宽 B_eff（约 20-25 GB/s per link，受协议开销限制）。

## Evidence

先验知识/题面给定，逻辑校验通过：Ring-AllReduce 在 N 节点下确实涉及 2(N-1) 次通信步骤（Reduce-Scatter + All-Gather），V100 SXM2 NVLink 3 单链路带宽约 25GB/s，符合硬件规格。

## Search Query

NVLink 3 ring allreduce latency model V100
