# N238: N86 未评估 INT8 量化对质量的影响：参考 N148/N149，INT8 下 MMLU 下降 1-2 个百分点，HumanEval Pass@1 下降 0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N86

## Claim

N86 未评估 INT8 量化对质量的影响：参考 N148/N149，INT8 下 MMLU 下降 1-2 个百分点，HumanEval Pass@1 下降 0.5-1.5 个百分点，需将质量损失系数 Q_norm=0.98-0.99 纳入 CPR 计算，导致实际性价比下降 1-2%。

## Corrected Claim

N86 未评估 INT8 量化对质量的影响：参考 N148/N149，INT8 下 MMLU 下降 1-2 个百分点，HumanEval Pass@1 下降 0.5-1.5 个百分点，需将质量损失系数 Q_norm=0.98-0.99 纳入 CPR 计算，导致实际性价比下降 1-2%。

## Evidence

先验知识/题面给定，逻辑校验通过
