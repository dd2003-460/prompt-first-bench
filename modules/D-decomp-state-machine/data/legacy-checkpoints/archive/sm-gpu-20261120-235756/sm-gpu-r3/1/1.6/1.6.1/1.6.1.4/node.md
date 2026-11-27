# N176: W4A16量化在32K长上下文下，由于KV Cache保持BF16精度，其质量退化主要源于权重量化误差在解码过程中的累积，而非KV Cache精度损失；幻觉率增

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N51, N52, N53

## Claim

W4A16量化在32K长上下文下，由于KV Cache保持BF16精度，其质量退化主要源于权重量化误差在解码过程中的累积，而非KV Cache精度损失；幻觉率增幅需通过Perplexity对比量化，预期较BF16增加2-5% [待核验]。

## Corrected Claim

W4A16量化在32K长上下文下，由于KV Cache保持BF16精度，其质量退化主要源于权重量化误差在解码过程中的累积，而非KV Cache精度损失；幻觉率增幅需通过Perplexity对比量化，具体增幅取决于模型与评估设置，通常表现为一定程度的性能下降。

## Evidence

[质询]「预期较BF16增加2-5%」这一具体数值范围缺乏通用理论支持，属于高度依赖具体模型、数据集和评估协议的实证经验值，无法从第一性原理推导，且不同文献中报告的提升幅度差异较大，该具体区间可能不准确或仅适用于特定实验条件。 | 先验知识/题面给定，逻辑校验通过：W4A16量化中KV Cache保持BF16精度是常见工程实践，权重量化误差累积导致质量退化符合逻辑；但具体幻觉率增幅2-5%为经验事实，无来源支持且非第一性原理可推导，故降级。

## Search Query

W4A16 long context hallucination rate increase perplexity comparison
