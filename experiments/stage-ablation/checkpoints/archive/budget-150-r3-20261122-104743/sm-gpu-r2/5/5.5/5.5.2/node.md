# N165: Ada Lovelace 架构 (RTX 4090) 的 FP8 支持限制：RTX 4090 不支持原生 FP8 矩阵乘法单元 (Tensor Cores)，F

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

Ada Lovelace 架构 (RTX 4090) 的 FP8 支持限制：RTX 4090 不支持原生 FP8 矩阵乘法单元 (Tensor Cores)，FP8 推理需通过软件模拟 (CUDA Core 或 INT8 模拟)，性能损失约 30-50% 且显存节省有限 (仅权重存储)

## Corrected Claim

Ada Lovelace 架构 (RTX 4090) 的 FP8 支持限制：RTX 4090 不支持原生 FP8 矩阵乘法单元 (Tensor Cores)，FP8 推理需通过软件模拟 (CUDA Core 或 INT8 模拟)，性能损失约 30-50% 且显存节省有限 (仅权重存储)

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 (Ada Lovelace) 确实不支持原生 FP8 Tensor Cores（该特性始于 Blackwell 架构），FP8 需软件模拟，性能损失和显存节省描述符合技术事实。

## Search Query

RTX 4090 FP8 support native tensor core software emulation performance loss
