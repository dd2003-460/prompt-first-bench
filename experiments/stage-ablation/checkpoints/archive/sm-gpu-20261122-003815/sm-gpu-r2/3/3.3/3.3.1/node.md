# N114: FP8 精度选择的硬件支持矩阵：明确列出哪些候选 GPU (H100, L40S, A100, RTX 4090) 原生支持 FP8 加速 (Tensor Co

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

FP8 精度选择的硬件支持矩阵：明确列出哪些候选 GPU (H100, L40S, A100, RTX 4090) 原生支持 FP8 加速 (Tensor Cores) 以及哪些仅支持软件模拟，这决定了 FP8 的实际推理速度是否优于 BF16/INT8

## Corrected Claim

FP8 精度选择的硬件支持矩阵：明确列出哪些候选 GPU (H100, L40S, A100, RTX 4090) 原生支持 FP8 加速 (Tensor Cores) 以及哪些仅支持软件模拟，这决定了 FP8 的实际推理速度是否优于 BF16/INT8

## Evidence

先验知识/题面给定，逻辑校验通过：H100 (Hopper架构) 原生支持FP8 Tensor Cores；A100 (Ampere) 和 L40S (Ada Lovelace) 及 RTX 4090 均不支持原生FP8硬件加速，需软件模拟或降精度处理，符合硬件架构演进事实。
