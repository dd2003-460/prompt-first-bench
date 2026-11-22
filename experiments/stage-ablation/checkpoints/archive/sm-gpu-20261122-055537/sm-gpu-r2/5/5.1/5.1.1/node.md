# N80: Q_score (质量得分) 的计算基准：Q_score = (Score_quantized / Score_BF16)，其中 Score 为在特定基准测试 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N24

## Claim

Q_score (质量得分) 的计算基准：Q_score = (Score_quantized / Score_BF16)，其中 Score 为在特定基准测试 (如 MMLU, HumanEval) 上的准确率。对于 Qwen3-27B，BF16 基线得分需通过实测获取，作为分母。

## Corrected Claim

Q_score (质量得分) 的计算基准：Q_score = (Score_quantized / Score_BF16)，其中 Score 为在特定基准测试 (如 MMLU, HumanEval) 上的准确率。对于 Qwen3-27B，BF16 基线得分需通过实测获取，作为分母。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Qwen3-27B MMLU HumanEval baseline score BF16
