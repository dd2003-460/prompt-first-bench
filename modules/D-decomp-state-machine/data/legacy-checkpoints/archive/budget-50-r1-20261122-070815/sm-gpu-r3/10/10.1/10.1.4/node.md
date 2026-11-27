# N419: H100 上 FP8 推理的内存带宽利用率修正：由于 FP8 权重体积减半，decode 阶段的内存访问模式可能从 compute-bound 转向 memor

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N145

## Claim

H100 上 FP8 推理的内存带宽利用率修正：由于 FP8 权重体积减半，decode 阶段的内存访问模式可能从 compute-bound 转向 memory-bound，需计算实际带宽利用率 U_mem = (Throughput_FP8 * Weights_Size_FP8) / 3350 GB/s，以判断是否达到硬件理论上限。

## Corrected Claim

H100 上 FP8 推理的内存带宽利用率修正：由于 FP8 权重体积减半，decode 阶段的内存访问模式可能从 compute-bound 转向 memory-bound，需计算实际带宽利用率 U_mem = (Throughput_FP8 * Weights_Size_FP8) / 3350 GB/s，以判断是否达到硬件理论上限。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8权重体积减半导致算术强度降低，decode阶段易转为memory-bound，带宽利用率公式量纲正确（GB/s），符合H100硬件特性。
