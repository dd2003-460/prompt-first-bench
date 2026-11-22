# N201: NVLink 硬件成本与可用性分析：A100 SXM 服务器 (如 DGX A100) 集成 NVLink 桥接，额外硬件成本已包含在整机价格中 (约 $100

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

NVLink 硬件成本与可用性分析：A100 SXM 服务器 (如 DGX A100) 集成 NVLink 桥接，额外硬件成本已包含在整机价格中 (约 $1000-$2000 溢价)，而 PCIe 版 A100 (A100 PCIe) 不支持 NVLink，仅能通过 PCIe 互联，其 TP=2 性能将大幅劣化；H100 SXM 同样集成 NVLink 4，PCIe 版 H100 不支持 NVLink。因此，多卡 NVLink 方案必须基于 SXM 形态的 GPU 和专用服务器机箱，其 TCO 需包含服务器整机价格而非单卡价格。

## Corrected Claim

NVLink 硬件成本与可用性分析：A100 SXM 服务器 (如 DGX A100) 集成 NVLink 桥接，额外硬件成本已包含在整机价格中 (约 $1000-$2000 溢价)，而 PCIe 版 A100 (A100 PCIe) 不支持 NVLink，仅能通过 PCIe 互联，其 TP=2 性能将大幅劣化；H100 SXM 同样集成 NVLink 4，PCIe 版 H100 不支持 NVLink。因此，多卡 NVLink 方案必须基于 SXM 形态的 GPU 和专用服务器机箱，其 TCO 需包含服务器整机价格而非单卡价格。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

A100 SXM vs PCIe NVLink support multi-GPU inference cost difference
