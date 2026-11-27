# N432: FP8权重的量化元数据（Scale/Zero-point）存储开销计算公式：Overhead_FP8 = (27e9 / group_size) * sizeo

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N140

## Claim

FP8权重的量化元数据（Scale/Zero-point）存储开销计算公式：Overhead_FP8 = (27e9 / group_size) * sizeof(scale_dtype) + (27e9 / group_size) * sizeof(zero_dtype)，其中group_size通常为128或512，scale/zero_dtype通常为FP16或FP32，需具体量化算法（如FP8-LM或SmoothQuant）确定参数

## Corrected Claim

FP8权重的量化元数据（Scale/Zero-point）存储开销计算公式：Overhead_FP8 = (27e9 / group_size) * sizeof(scale_dtype) + (27e9 / group_size) * sizeof(zero_dtype)，其中group_size通常为128或512，scale/zero_dtype通常为FP16或FP32，需具体量化算法（如FP8-LM或SmoothQuant）确定参数

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合分组量化（Group-wise Quantization）的元数据开销计算逻辑（总参数量/组大小 * 元数据元素数 * 字节数），量纲与数值量级合理。

## Search Query

FP8 quantization metadata overhead formula group size scale zero point storage
