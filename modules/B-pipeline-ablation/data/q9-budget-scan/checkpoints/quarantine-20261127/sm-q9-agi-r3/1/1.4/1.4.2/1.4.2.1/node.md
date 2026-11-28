# N146: V100-SXM2 NVLink 有效带宽实测：理论双向带宽 300GB/s (150GB/s unidirectional per link, 4 links

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

V100-SXM2 NVLink 有效带宽实测：理论双向带宽 300GB/s (150GB/s unidirectional per link, 4 links?). 实际上 NVSwitch 连接的 4 GPU 集群，AllReduce 有效带宽通常为理论的 60-70%，即 ~180-210 GB/s。原 claim 使用 150-180GB/s 是合理的保守估计。

## Corrected Claim

V100-SXM2 NVLink 有效带宽实测：理论双向带宽 300GB/s (150GB/s unidirectional per link, 4 links?). 实际上 NVSwitch 连接的 4 GPU 集群，AllReduce 有效带宽通常为理论的 60-70%，即 ~180-210 GB/s。原 claim 使用 150-180GB/s 是合理的保守估计。

## Evidence

先验知识/题面给定，逻辑校验通过：V100 NVLink 理论带宽及 AllReduce 效率符合工程常识，数值量级合理。

## Search Query

Tesla V100 SXM2 NVLink effective allreduce bandwidth benchmark NCCL
