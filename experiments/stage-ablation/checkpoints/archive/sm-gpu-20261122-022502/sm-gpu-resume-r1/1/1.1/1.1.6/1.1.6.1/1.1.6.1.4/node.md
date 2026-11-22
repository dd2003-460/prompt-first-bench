# N470: AWQ (Activation-Aware Weight Quantization) 的核心机制公式：通过统计激活值分布，识别对损失函数梯度影响最大的显著权重 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N146

## Claim

AWQ (Activation-Aware Weight Quantization) 的核心机制公式：通过统计激活值分布，识别对损失函数梯度影响最大的显著权重 (salient weights)，将其保留为高精度 (如 INT8/FP16) 或应用非对称缩放因子，其余权重量化为 INT4，从而将整体 MSE 最小化。

## Corrected Claim

AWQ (Activation-Aware Weight Quantization) 的核心机制公式：通过统计激活值分布，识别对损失函数梯度影响最大的显著权重 (salient weights)，将其保留为高精度 (如 INT8/FP16) 或应用非对称缩放因子，其余权重量化为 INT4，从而将整体 MSE 最小化。

## Evidence

先验知识/题面给定，逻辑校验通过
