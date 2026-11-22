# N136: 定义‘困惑度增加’的具体计算基准：使用 WikiText2 或 C4 数据集，指标为 Perplexity (PPL)；需明确上下文长度 (Context Le

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

定义‘困惑度增加’的具体计算基准：使用 WikiText2 或 C4 数据集，指标为 Perplexity (PPL)；需明确上下文长度 (Context Length) 固定为 2048 或 4096 tokens 以消除长度偏差，计算公式为 PPL = exp(-1/N * sum(log P(x_i)))。

## Corrected Claim

定义‘困惑度增加’的具体计算基准：使用 WikiText2 或 C4 数据集，指标为 Perplexity (PPL)；需明确上下文长度 (Context Length) 固定为 2048 或 4096 tokens 以消除长度偏差，计算公式为 PPL = exp(-1/N * sum(log P(x_i)))。

## Evidence

先验知识/题面给定，逻辑校验通过：PPL公式定义正确，WikiText2/C4为常用基准，固定上下文长度以消除偏差符合评估规范。
