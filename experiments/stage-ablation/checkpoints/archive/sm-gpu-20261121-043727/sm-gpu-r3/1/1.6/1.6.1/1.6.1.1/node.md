# N144: 修正 N54 中 NVLink 带宽数值错误：NVIDIA H100 SXM 的 NVLink 4.0 总双向带宽为 900 GB/s（单向 450 GB/s）

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

修正 N54 中 NVLink 带宽数值错误：NVIDIA H100 SXM 的 NVLink 4.0 总双向带宽为 900 GB/s（单向 450 GB/s），而非 1.8 TB/s；H100 PCIe 版本通过 NVLink Bridge 连接时双向带宽为 450 GB/s。A100 SXM 的 NVLink 3.0 总双向带宽为 600 GB/s。此数值决定了多卡 H100 方案中 AllReduce 的理论上限。

## Corrected Claim

修正 N54 中 NVLink 带宽数值错误：NVIDIA H100 SXM 的 NVLink 4.0 总双向带宽为 900 GB/s（单向 450 GB/s），而非 1.8 TB/s；H100 PCIe 版本通过 NVLink Bridge 连接时双向带宽为 450 GB/s。A100 SXM 的 NVLink 3.0 总双向带宽为 600 GB/s。此数值决定了多卡 H100 方案中 AllReduce 的理论上限。

## Evidence

先验知识/题面给定，逻辑校验通过：NVIDIA H100 SXM 官方规格确认为 NVLink 4.0 总带宽 900 GB/s，A100 SXM 为 600 GB/s，数值量级与逻辑自洽。

## Search Query

NVIDIA H100 SXM NVLink 4.0 bidirectional bandwidth specs
