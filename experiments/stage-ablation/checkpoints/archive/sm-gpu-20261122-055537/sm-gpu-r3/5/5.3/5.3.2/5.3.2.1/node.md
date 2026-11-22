# N281: NVIDIA A10 显存带宽精确值为 600 GB/s (GDDR6)，Qwen3-27B FP8 纯权重解码理论上限 T_max = 600 GB/s / 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N86

## Claim

NVIDIA A10 显存带宽精确值为 600 GB/s (GDDR6)，Qwen3-27B FP8 纯权重解码理论上限 T_max = 600 GB/s / 27 GB ≈ 22.22 tokens/s；N86 原陈述 66.67 tokens/s 错误地将带宽视为 1800 GB/s 或模型大小视为 9 GB，正确计算应基于 600 GB/s 带宽与 27 GB FP8 权重。

## Corrected Claim

NVIDIA A10 显存带宽精确值为 600 GB/s (GDDR6)，Qwen3-27B FP8 纯权重解码理论上限 T_max = 600 GB/s / 27 GB ≈ 22.22 tokens/s；N86 原陈述 66.67 tokens/s 错误地将带宽视为 1800 GB/s 或模型大小视为 9 GB，正确计算应基于 600 GB/s 带宽与 27 GB FP8 权重。

## Evidence

先验知识/题面给定，逻辑校验通过：NVIDIA A10 显存带宽确为 600 GB/s，Qwen3-27B FP8 权重约 27 GB，计算 600/27 ≈ 22.22 tokens/s 符合算术逻辑，原陈述 66.67 tokens/s 确实存在数量级错误。

## Search Query

NVIDIA A10 datasheet memory bandwidth GDDR6
