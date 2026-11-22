# N398: FP8 量化在 Transformer 架构中的精度损失机制：主要源于 KV Cache 的量化误差累积（长上下文下误差随序列长度线性增加）和注意力权重矩阵的离

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N155

## Claim

FP8 量化在 Transformer 架构中的精度损失机制：主要源于 KV Cache 的量化误差累积（长上下文下误差随序列长度线性增加）和注意力权重矩阵的离群值（Outliers）处理不当；对于 32K 上下文，KV Cache FP8 量化可能导致最终生成质量下降 0.5-1.5% [待核验：需参考 SmoothQuant 或 LLM.int8() 论文数据]。

## Corrected Claim

FP8 量化在 Transformer 架构中的精度损失主要源于 KV Cache 的量化误差累积（长上下文下误差随序列长度增加）和注意力权重矩阵的离群值处理不当；对于长上下文（如 32K），KV Cache FP8 量化可能导致最终生成质量出现可测量的下降，具体幅度取决于模型架构、量化策略及评估任务。

## Evidence

[质询]具体数值区间（0.5-1.5%）缺乏直接来源支持，且不同模型、量化方案（如SmoothQuant vs 原生FP8）及评估基准下精度损失差异较大，该数值可能过于具体或仅适用于特定实验条件。 | 先验知识/题面给定，逻辑校验通过：FP8量化误差累积和离群值处理确实是Transformer精度损失的主要机制，但具体百分比为经验事实，因无外部来源支持且存在个体差异，降级为定性表述。

## Search Query

FP8 quantization KV cache error accumulation long context LLM SmoothQuant outlier handling
