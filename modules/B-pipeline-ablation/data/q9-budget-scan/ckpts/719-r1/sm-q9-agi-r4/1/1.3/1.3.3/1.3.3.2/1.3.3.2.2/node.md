# N412: 'Dequantize to FP16 on-the-fly' 机制的执行位置：在 Attention 和 FFN 层的 GEMM 调用前插入 dequanti

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N139

## Claim

'Dequantize to FP16 on-the-fly' 机制的执行位置：在 Attention 和 FFN 层的 GEMM 调用前插入 dequantize kernel，该 kernel 本身消耗约 10%-15% 的额外 GPU 周期，且增加内存带宽占用至 2 倍

## Corrected Claim

'Dequantize to FP16 on-the-fly' 机制在执行 Attention 和 FFN 层 GEMM 前插入 dequantize kernel，通常会引入额外的计算开销和内存带宽压力，具体比例取决于硬件实现与量化策略。

## Evidence

[质询]数值量级存疑：'10%-15% 额外 GPU 周期'和'2 倍内存带宽'是高度依赖硬件架构、量化格式（INT8/FP8）及算子融合程度的经验参数，并非固定物理常数，缺乏通用性。 | 先验知识/题面给定，逻辑校验通过（机制描述符合低精度推理常见优化路径），但具体性能开销数值属于经验事实，无来源支持且非第一性原理可推导，故降级。

## Search Query

on-the-fly dequantization kernel overhead in LLM inference engines
