# N64: NVIDIA A100 (40GB/80GB) 配备 NVLink 3.0，单链路双向带宽为 600 GB/s，总聚合带宽为 600 GB/s。

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N12

## Claim

NVIDIA A100 (40GB/80GB) 配备 NVLink 3.0，单链路双向带宽为 600 GB/s，总聚合带宽为 600 GB/s。

## Corrected Claim

NVIDIA A100 (40GB/80GB) 配备 NVLink 3.0，共有 12 条链路，单链路双向带宽约为 50 GB/s，总聚合双向带宽为 600 GB/s。

## Evidence

[质询]数值量级与官方规格不符：NVIDIA A100 的 NVLink 3.0 总聚合带宽通常为 600 GB/s（双向），而非单链路 600 GB/s 且总聚合也为 600 GB/s（这暗示只有 1 条链路，与 A100 实际拥有 12 条 NVLink 链路的硬件架构矛盾；单链路带宽约为 50 GB/s）。 | 先验知识/题面给定，逻辑校验发现内部矛盾：A100 拥有 12 条 NVLink 3.0 链路，单链路带宽约 50 GB/s，总聚合带宽 600 GB/s。陈述中‘单链路双向带宽为 600 GB/s’与‘总聚合带宽为 600 GB/s’同时成立意味着仅有一条链路，这与 A100 的多链路架构事实相悖，属于数值/架构描述错误。
