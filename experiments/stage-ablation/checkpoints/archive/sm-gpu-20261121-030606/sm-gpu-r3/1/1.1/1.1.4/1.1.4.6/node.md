# N203: RTX 5090 显存带宽 1792 GB/s 的构成：GDDR7 频率 28 Gbps × 512-bit 位宽 / 8 = 1792 GB/s，N85 数值

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N83, N84, N85

## Claim

RTX 5090 显存带宽 1792 GB/s 的构成：GDDR7 频率 28 Gbps × 512-bit 位宽 / 8 = 1792 GB/s，N85 数值正确，带宽提升幅度修正为 1792/672 - 1 = 166.7%（基于修正后的 4090 带宽 672 GB/s），而非 N85 声称的 78%

## Corrected Claim

RTX 5090 显存带宽 1792 GB/s 的构成：GDDR7 频率 28 Gbps × 512-bit 位宽 / 8 = 1792 GB/s，N85 数值正确，带宽提升幅度修正为 1792/672 - 1 = 166.7%（基于修正后的 4090 带宽 672 GB/s），而非 N85 声称的 78%

## Evidence

先验知识/题面给定，逻辑校验通过：28 Gbps × 512 bit / 8 = 1792 GB/s 计算正确；1792/672 - 1 ≈ 166.7% 计算正确；RTX 4090 带宽 672 GB/s 为公认事实。
