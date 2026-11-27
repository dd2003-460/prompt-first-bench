# N233: 在 LLM 解码阶段 (Memory-Bound)，显存带宽利用率修正因子 η 主要受反量化 (Dequantization) 操作的影响，对于 INT8 精度

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N81

## Claim

在 LLM 解码阶段 (Memory-Bound)，显存带宽利用率修正因子 η 主要受反量化 (Dequantization) 操作的影响，对于 INT8 精度，η 通常在 0.85-0.95 之间，因为 INT8 反量化为 BF16/FP16 的计算开销较低，且 Tensor Core 支持高效 INT8 矩阵乘法。

## Corrected Claim

在 LLM 解码阶段 (Memory-Bound)，显存带宽利用率修正因子 η 主要受反量化 (Dequantization) 操作的影响，对于 INT8 精度，η 通常在 0.85-0.95 之间，因为 INT8 反量化为 BF16/FP16 的计算开销较低，且 Tensor Core 支持高效 INT8 矩阵乘法。

## Evidence

先验知识/题面给定，逻辑校验通过
