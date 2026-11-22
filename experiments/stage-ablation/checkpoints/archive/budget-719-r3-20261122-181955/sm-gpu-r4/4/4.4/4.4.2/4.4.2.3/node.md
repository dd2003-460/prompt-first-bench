# N332: INT4 量化下 HumanEval 的损失分布：代码生成任务对量化更敏感，建议采用正态分布 $N(2.0\%, 1.0\%^2)$ 或均匀分布 $U(1.0\

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N109

## Claim

INT4 量化下 HumanEval 的损失分布：代码生成任务对量化更敏感，建议采用正态分布 $N(2.0\%, 1.0\%^2)$ 或均匀分布 $U(1.0\%, 3.0\%)$ 建模，该分布比 MMLU 的损失分布更宽，反映了任务类型的差异性。

## Corrected Claim

INT4 量化下 HumanEval 的损失分布：代码生成任务对量化更敏感，建议采用正态分布 $N(2.0\%, 1.0\%^2)$ 或均匀分布 $U(1.0\%, 3.0\%)$ 建模，该分布比 MMLU 的损失分布更宽，反映了任务类型的差异性。

## Evidence

先验知识/题面给定，逻辑校验通过
