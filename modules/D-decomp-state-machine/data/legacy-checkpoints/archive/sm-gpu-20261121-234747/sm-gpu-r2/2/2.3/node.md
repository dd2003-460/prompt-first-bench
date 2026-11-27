# N12: 硬件-精度兼容性矩阵：各候选GPU对FP8/INT8/NVFP4/W4的原生支持情况（如H100支持FP8 Tensor Core，RTX 4090不支持原生F

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

硬件-精度兼容性矩阵：各候选GPU对FP8/INT8/NVFP4/W4的原生支持情况（如H100支持FP8 Tensor Core，RTX 4090不支持原生FP8需软件模拟），需标注不支持时的性能惩罚系数（如INT8在4090上相对BF16的吞吐比）

## Corrected Claim

硬件-精度兼容性矩阵：各候选GPU对FP8/INT8/NVFP4/W4的原生支持情况（如H100支持FP8 Tensor Core，RTX 4090不支持原生FP8需软件模拟），需标注不支持时的性能惩罚系数（如INT8在4090上相对BF16的吞吐比）

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

RTX 4090 FP8 support H100 FP8 tensor core INT8 performance penalty
