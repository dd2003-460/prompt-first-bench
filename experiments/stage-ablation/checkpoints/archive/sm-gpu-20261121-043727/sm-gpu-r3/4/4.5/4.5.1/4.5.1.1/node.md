# N194: 修正 N11/N26 矛盾：NVLink 带宽 900 GB/s 仅存在于 H100 SXM/H200 SXM，RTX 4090 无 NVLink 接口，其最大

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N74

## Claim

修正 N11/N26 矛盾：NVLink 带宽 900 GB/s 仅存在于 H100 SXM/H200 SXM，RTX 4090 无 NVLink 接口，其最大互联带宽为 PCIe 4.0 x16 (64 GB/s 理论，50 GB/s 有效)。N11 中 'NVLink (900GB/s)' 的描述仅适用于数据中心 GPU 对比，不适用于 RTX 4090 多卡方案。N26 中 '相比 NVLink (400GB/s) 低 12.5 倍' 的错误在于 RTX 4090 根本无法使用 NVLink，因此不存在此对比

## Corrected Claim

修正 N11/N26 矛盾：NVLink 带宽 900 GB/s 仅存在于 H100 SXM/H200 SXM，RTX 4090 无 NVLink 接口，其最大互联带宽为 PCIe 4.0 x16 (64 GB/s 理论，50 GB/s 有效)。N11 中 'NVLink (900GB/s)' 的描述仅适用于数据中心 GPU 对比，不适用于 RTX 4090 多卡方案。N26 中 '相比 NVLink (400GB/s) 低 12.5 倍' 的错误在于 RTX 4090 根本无法使用 NVLink，因此不存在此对比

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 确实无 NVLink 接口，H100 SXM 的 NVLink 带宽为 900 GB/s，PCIe 4.0 x16 理论带宽 64 GB/s 均符合硬件规格事实。
