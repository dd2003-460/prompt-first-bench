# N62: PCIe 4.0 x16 链路的有效单向传输带宽为 ~15.75 GB/s，双向为 ~31.5 GB/s（扣除协议开销后）。

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

PCIe 4.0 x16 链路的有效单向传输带宽为 ~15.75 GB/s，双向为 ~31.5 GB/s（扣除协议开销后）。

## Corrected Claim

PCIe 4.0 x16 链路的有效单向传输带宽为 ~15.75 GB/s，双向为 ~31.5 GB/s（扣除协议开销后）。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 单 lane 原始速率为 16 GT/s，采用 128b/130b 编码，有效单向带宽约为 15.75 GB/s，双向约为 31.5 GB/s，数值量级与计算逻辑自洽。
