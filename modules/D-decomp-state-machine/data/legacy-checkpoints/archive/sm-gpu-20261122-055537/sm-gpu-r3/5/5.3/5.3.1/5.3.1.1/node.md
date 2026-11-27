# N279: NVIDIA L4 显存带宽精确值为 300 GB/s (GDDR6)，非 N85 中误用的 336 GB/s；基于此，Qwen3-27B FP8 纯权重解码理

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N85

## Claim

NVIDIA L4 显存带宽精确值为 300 GB/s (GDDR6)，非 N85 中误用的 336 GB/s；基于此，Qwen3-27B FP8 纯权重解码理论上限 T_max = 300 GB/s / 27 GB ≈ 11.11 tokens/s，N85 原陈述中 48.75 tokens/s 及 4.4 修正系数为错误推导，应废弃。

## Corrected Claim

NVIDIA L4 显存带宽精确值为 300 GB/s (GDDR6)，非 N85 中误用的 336 GB/s；基于此，Qwen3-27B FP8 纯权重解码理论上限 T_max = 300 GB/s / 27 GB ≈ 11.11 tokens/s，N85 原陈述中 48.75 tokens/s 及 4.4 修正系数为错误推导，应废弃。

## Evidence

先验知识/题面给定，逻辑校验通过：NVIDIA L4 显存带宽确为 300 GB/s，Qwen3-27B FP8 权重约 27 GB，理论解码上限 300/27 ≈ 11.11 tokens/s，原 48.75 tokens/s 及 4.4 修正系数推导错误。

## Search Query

NVIDIA L4 datasheet memory bandwidth GDDR6
