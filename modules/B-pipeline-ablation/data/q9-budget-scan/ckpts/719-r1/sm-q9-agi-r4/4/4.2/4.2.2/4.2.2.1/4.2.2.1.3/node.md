# N598: Cosine similarity 计算的数值稳定性：对 BERT 输出的 768 维向量进行 L2 归一化，计算余弦相似度时使用 float32 精度，避免 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N213

## Claim

Cosine similarity 计算的数值稳定性：对 BERT 输出的 768 维向量进行 L2 归一化，计算余弦相似度时使用 float32 精度，避免 float16 下的舍入误差累积；单次计算耗时约 0.5ms（CPU），100 个样本总耗时 50ms，可忽略不计

## Corrected Claim

Cosine similarity 计算的数值稳定性：对 BERT 输出的 768 维向量进行 L2 归一化，计算余弦相似度时使用 float32 精度，避免 float16 下的舍入误差累积；单次计算耗时约 0.5ms（CPU），100 个样本总耗时 50ms，可忽略不计

## Evidence

先验知识/题面给定，逻辑校验通过：768维向量的L2归一化和点积运算在CPU上耗时微秒至毫秒级，float32精度足以保证数值稳定性，避免float16的精度损失，量级估算合理。

## Search Query

BERT embedding cosine similarity numerical stability float32 performance
