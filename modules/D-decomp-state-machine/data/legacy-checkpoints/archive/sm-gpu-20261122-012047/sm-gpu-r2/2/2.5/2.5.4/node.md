# N89: H100 NVLink 4.0 提供 900 GB/s 双向带宽，单方向有效带宽约 450 GB/s，相比 PCIe 4.0 x16 的 25 GB/s 有效带

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

H100 NVLink 4.0 提供 900 GB/s 双向带宽，单方向有效带宽约 450 GB/s，相比 PCIe 4.0 x16 的 25 GB/s 有效带宽，加速比约为 18 倍，因此在高通信频率的 TP 场景中，H100 多卡效率损失可忽略（<5%），而 PCIe 多卡效率损失可达 20-40%（修正 N18 中 900 GB/s 为双向峰值，需区分单向有效值）。

## Corrected Claim

H100 NVLink 4.0 提供 900 GB/s 双向带宽，单方向有效带宽约 450 GB/s，相比 PCIe 4.0 x16 的 25 GB/s 有效带宽，加速比约为 18 倍，因此在高通信频率的 TP 场景中，H100 多卡效率损失可忽略（<5%），而 PCIe 多卡效率损失可达 20-40%（修正 N18 中 900 GB/s 为双向峰值，需区分单向有效值）。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 NVLink 4.0 双向带宽 900 GB/s 及 PCIe 4.0 x16 带宽 25 GB/s 均为标准硬件规格，18 倍加速比计算正确，且符合高带宽互联降低通信开销的工程直觉。
