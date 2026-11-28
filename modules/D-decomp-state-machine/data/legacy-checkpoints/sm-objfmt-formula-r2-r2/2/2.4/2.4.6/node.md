# N84: A100 对 W4 精度的原生计算支持：SM 8.0 不支持原生 W4 Tensor Core 加速，W4 推理需通过软件模拟或转换为 INT8/FP16 执行

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

A100 对 W4 精度的原生计算支持：SM 8.0 不支持原生 W4 Tensor Core 加速，W4 推理需通过软件模拟或转换为 INT8/FP16 执行，实际加速比低于 INT8，具体性能损耗需实测确定。

## Corrected Claim

A100 对 W4 精度的原生计算支持：SM 8.0 不支持原生 W4 Tensor Core 加速，W4 推理需通过软件模拟或转换为 INT8/FP16 执行，实际加速比低于 INT8，具体性能损耗需实测确定。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 (SM 8.0) 硬件架构确实仅支持 FP16/BF16/TF32/INT8/INT4(仅限特定稀疏或旧代特性，A100主要强调INT8/FP16 Tensor Core) 的原生Tensor Core加速，W4精度通常需软件量化或转换执行，符合硬件规格事实。

## Search Query

A100 W4 quantization inference performance penalty software emulation
