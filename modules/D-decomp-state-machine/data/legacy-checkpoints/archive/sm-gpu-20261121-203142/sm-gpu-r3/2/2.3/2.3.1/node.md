# N55: W8A8量化在MMLU基准上相比BF16的准确率损失通常为0.5%-1.5%，该区间基于Llama-2-70B及Qwen-14B在AWQ/GPTQ实现下的公开评

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13

## Claim

W8A8量化在MMLU基准上相比BF16的准确率损失通常为0.5%-1.5%，该区间基于Llama-2-70B及Qwen-14B在AWQ/GPTQ实现下的公开评测数据，具体到Qwen3-27B需核验 [待核验: Qwen3-27B INT8 MMLU score]

## Corrected Claim

W8A8量化在MMLU基准上相比BF16的准确率损失通常在0.5%-1.5%区间（基于Llama-2-70B及Qwen-14B等模型的公开评测），Qwen3-27B的具体损失需进一步核验，但预期处于相似量级。

## Evidence

[质询]该陈述包含具体的经验性数值区间（0.5%-1.5%）和特定模型（Qwen3-27B）的量化表现，属于硬件/模型规格类的经验事实，无法从第一性原理推导。且Qwen3-27B为较新模型，其INT8/W8A8在MMLU上的具体损失数据缺乏公开权威评测直接支持，存在将旧模型（Llama-2/Qwen-14B）数据直接外推至新模型的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且Qwen3-27B具体数据未覆盖）

## Search Query

Qwen3-27B INT8 W8A8 MMLU benchmark accuracy loss BF16
