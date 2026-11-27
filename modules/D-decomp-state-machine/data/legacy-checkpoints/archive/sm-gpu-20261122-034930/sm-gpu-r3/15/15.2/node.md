# N436: Qwen3-27B 在 INT8 (AWQ/GPTQ) 精度下的 HumanEval Pass@1 准确率损失具体数值：预计损失为 3.0% ± 1.0% [待

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N157

## Claim

Qwen3-27B 在 INT8 (AWQ/GPTQ) 精度下的 HumanEval Pass@1 准确率损失具体数值：预计损失为 3.0% ± 1.0% [待核验]，即 Pass@1 从 ~68% 降至 ~65%。该损失高于 MMLU 损失 (1-2%)，符合代码生成任务对量化更敏感的规律，需通过本地运行 HumanEval 数据集验证。

## Corrected Claim

Qwen3-27B 在 INT8 (AWQ/GPTQ) 精度下的 HumanEval Pass@1 准确率预计会有所下降，具体损失数值需通过本地运行 HumanEval 数据集验证。

## Evidence

[质询]该陈述包含具体的经验性数值（3.0% ± 1.0% 的损失幅度及 68% 到 65% 的绝对值），属于硬件/模型性能指标，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B INT8 AWQ HumanEval Pass@1 accuracy loss
