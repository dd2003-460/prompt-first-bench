# N281: 2×RTX 4090 Tensor Parallel 方案的通信延迟量化：总通信时间 = 总通信数据量 / 有效 PCIe 带宽；假设有效带宽为 35 GB/s

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N90

## Claim

2×RTX 4090 Tensor Parallel 方案的通信延迟量化：总通信时间 = 总通信数据量 / 有效 PCIe 带宽；假设有效带宽为 35 GB/s，总通信时间 ≈ 8 GB / 35 GB/s ≈ 0.23 秒；若单卡计算时间（含 FlashAttention 优化）约为 5.9 秒（参考 N120），则通信开销占比 ≈ 0.23 / 5.9 ≈ 3.9%，远低于 N90 中估算的 15-30%；这表明在 Batch_Size=1 且序列长度固定时，PCIe 瓶颈影响较小，主要瓶颈仍在计算。

## Corrected Claim

2×RTX 4090 Tensor Parallel 方案的通信延迟量化：总通信时间 = 总通信数据量 / 有效 PCIe 带宽；假设有效带宽为 35 GB/s，总通信时间 ≈ 8 GB / 35 GB/s ≈ 0.23 秒；若单卡计算时间（含 FlashAttention 优化）约为 5.9 秒（参考 N120），则通信开销占比 ≈ 0.23 / 5.9 ≈ 3.9%，远低于 N90 中估算的 15-30%；这表明在 Batch_Size=1 且序列长度固定时，PCIe 瓶颈影响较小，主要瓶颈仍在计算。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算（8/35≈0.23, 0.23/5.9≈3.9%）正确，PCIe 4.0 x16 有效带宽 35GB/s 符合工程常识，结论与计算逻辑自洽。
