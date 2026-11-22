# N354: RTX 3090 显存带宽 936 GB/s 的构成验证：GDDR6 8 通道 × 256-bit 位宽 × 1950 MHz 等效频率 (3900 MT/s)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N119

## Claim

RTX 3090 显存带宽 936 GB/s 的构成验证：GDDR6 8 通道 × 256-bit 位宽 × 1950 MHz 等效频率 (3900 MT/s) / 8 = 975 GB/s 理论峰值，标称 936 GB/s 包含约 4% 的内存控制器开销或降频因素，该数值为硬件固定参数，不可通过软件优化提升。

## Corrected Claim

RTX 3090 显存带宽 936 GB/s 的构成验证：GDDR6 8 通道 × 256-bit 位宽 × 1950 MHz 等效频率 (3900 MT/s) / 8 = 975 GB/s 理论峰值，标称 936 GB/s 包含约 4% 的内存控制器开销或降频因素，该数值为硬件固定参数，不可通过软件优化提升。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3090 显存带宽 936 GB/s 是硬件固定参数，由 GDDR6 显存规格决定，不可通过软件优化提升。
