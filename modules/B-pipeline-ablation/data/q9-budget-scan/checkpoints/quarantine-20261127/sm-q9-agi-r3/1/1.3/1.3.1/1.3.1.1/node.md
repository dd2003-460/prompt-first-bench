# N135: Tesla V100-SXM2 物理互联采用 NVLink 3.0 点对点链路（每卡 6 条链路，每条 25 GB/s，单向总带宽 150 GB/s，双向 30

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42

## Claim

Tesla V100-SXM2 物理互联采用 NVLink 3.0 点对点链路（每卡 6 条链路，每条 25 GB/s，单向总带宽 150 GB/s，双向 300 GB/s），并非 NVSwitch（NVSwitch 仅在 V100 DGX 或 A100/H100 SXM 中常见，V100 SXM2 通常通过 PCIe 或直连 NVLink 连接，无中央交换芯片）。

## Corrected Claim

Tesla V100-SXM2 物理互联采用 NVLink 3.0 点对点链路（每卡 6 条链路，每条 25 GB/s，单向总带宽 150 GB/s，双向 300 GB/s），并非 NVSwitch（NVSwitch 仅在 V100 DGX 或 A100/H100 SXM 中常见，V100 SXM2 通常通过 PCIe 或直连 NVLink 连接，无中央交换芯片）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Tesla V100 SXM2 NVLink topology bandwidth specifications
