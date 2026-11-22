# N378: 工作点A (高性低成/理论峰值型)：RTX 4090 W4 精度下，若忽略计算延迟和内存碎片，理论峰值 Tokens/s = 1008 GB/s / 13.5 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N143

## Claim

工作点A (高性低成/理论峰值型)：RTX 4090 W4 精度下，若忽略计算延迟和内存碎片，理论峰值 Tokens/s = 1008 GB/s / 13.5 GB ≈ 74.6 Tokens/s，这是带宽限制下的上限，实际性能受限于此值。

## Corrected Claim

工作点A (高性低成/理论峰值型)：RTX 4090 W4 精度下，若忽略计算延迟和内存碎片，理论峰值 Tokens/s = 1008 GB/s / 13.5 GB ≈ 74.6 Tokens/s，这是带宽限制下的上限，实际性能受限于此值。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 显存带宽约 1008 GB/s，W4 精度下模型权重约 13.5 GB，计算 1008/13.5 ≈ 74.6，量纲与数值合理，符合带宽限制下的理论峰值推导。
