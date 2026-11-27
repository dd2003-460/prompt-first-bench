# N138: 修正 N39 中 A100 NVLink 带宽数据：A100 SXM 40GB/80GB 的 NVLink 3.0 总带宽为 600 GB/s (双向)，H10

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39, N40, N41

## Claim

修正 N39 中 A100 NVLink 带宽数据：A100 SXM 40GB/80GB 的 NVLink 3.0 总带宽为 600 GB/s (双向)，H100 SXM 的 NVLink 4.0 总带宽为 900 GB/s (双向)；PCIe 4.0 x16 理论带宽为 32 GB/s (单向)，有效双向带宽约 64 GB/s。NVLink 相对 PCIe 的带宽倍数在 A100 场景下约为 9.4x (600/64)，在 H100 场景下约为 14.1x (900/64)，而非 N39 中笼统的 20-30 倍（该倍数可能混淆了单向/双向或引用了 NVLink Bridge 特殊配置）。

## Corrected Claim

修正 N39 中 A100 NVLink 带宽数据：A100 SXM 40GB/80GB 的 NVLink 3.0 总带宽为 600 GB/s (双向)，H100 SXM 的 NVLink 4.0 总带宽为 900 GB/s (双向)；PCIe 4.0 x16 理论带宽为 32 GB/s (单向)，有效双向带宽约 64 GB/s。NVLink 相对 PCIe 的带宽倍数在 A100 场景下约为 9.4x (600/64)，在 H100 场景下约为 14.1x (900/64)，而非 N39 中笼统的 20-30 倍（该倍数可能混淆了单向/双向或引用了 NVLink Bridge 特殊配置）。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 SXM NVLink 3.0 带宽确为 600 GB/s，H100 SXM NVLink 4.0 带宽确为 900 GB/s，PCIe 4.0 x16 双向有效带宽约 64 GB/s，倍数计算逻辑自洽。

## Search Query

NVIDIA A100 NVLink 3.0 bandwidth GB/s H100 NVLink 4.0 bandwidth
