# N67: NVLink vs PCIe 互联带宽对比：NVLink 4.0 (H100) 带宽 900 GB/s (双向)，PCIe 4.0 x16 带宽 64 GB/s

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

NVLink vs PCIe 互联带宽对比：NVLink 4.0 (H100) 带宽 900 GB/s (双向)，PCIe 4.0 x16 带宽 64 GB/s (单向)。若使用 2x H100 通过 NVLink 互联，T_comm = 6.29GB / 900 GB/s ≈ 0.007s，总延迟 ≈ 0.020s/token，吞吐 ≈ 50 tokens/s，比 PCIe 互联 (9.0 tokens/s) 高 455%。因此，多卡方案必须使用 NVLink 或更高带宽互联才能接近单卡性能。

## Corrected Claim

NVLink vs PCIe 互联带宽对比：NVLink 4.0 (H100) 带宽 900 GB/s (双向)，PCIe 4.0 x16 带宽 64 GB/s (单向)。若使用 2x H100 通过 NVLink 互联，T_comm = 6.29GB / 900 GB/s ≈ 0.007s，总延迟 ≈ 0.020s/token，吞吐 ≈ 50 tokens/s，比 PCIe 互联 (9.0 tokens/s) 高 455%。因此，多卡方案必须使用 NVLink 或更高带宽互联才能接近单卡性能。

## Evidence

先验知识/题面给定，逻辑校验通过：NVLink 4.0 (H100) 900GB/s 与 PCIe 4.0 x16 64GB/s 带宽符合硬件规格，计算过程（6.29GB/900GB/s≈0.007s）及吞吐对比逻辑自洽。
