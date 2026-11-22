# N364: PCIe 4.0 x16 的有效带宽为 32 GB/s，理论最大通信延迟为 0.5 MB / 32 GB/s = 0.0156 ms/Step；若使用 NVLi

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N122

## Claim

PCIe 4.0 x16 的有效带宽为 32 GB/s，理论最大通信延迟为 0.5 MB / 32 GB/s = 0.0156 ms/Step；若使用 NVLink (900 GB/s)，延迟为 0.5 MB / 900 GB/s = 0.00056 ms/Step；PCIe 通信延迟比 NVLink 高 27.8x，但在 27B 模型推理中，计算时间 (约 10-20 ms/Token) 远大于通信时间，故通信开销占比 <5%。

## Corrected Claim

PCIe 4.0 x16 的有效带宽为 32 GB/s，理论最大通信延迟为 0.5 MB / 32 GB/s = 0.0156 ms/Step；若使用 NVLink (900 GB/s)，延迟为 0.5 MB / 900 GB/s = 0.00056 ms/Step；PCIe 通信延迟比 NVLink 高 27.8x，但在 27B 模型推理中，计算时间 (约 10-20 ms/Token) 远大于通信时间，故通信开销占比 <5%。

## Evidence

先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16 双向带宽约 32 GB/s，NVLink 带宽量级正确，延迟计算及占比推导符合逻辑。

## Search Query

PCIe 4.0 x16 bandwidth NVLink bandwidth comparison
