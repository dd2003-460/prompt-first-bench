# N453: Llama-3-8B 在 INT4 (GPTQ/AWQ) 量化下 HumanEval Pass@1 的具体下降数值为 3.5% (从 70.2% 降至 66.7

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N188

## Claim

Llama-3-8B 在 INT4 (GPTQ/AWQ) 量化下 HumanEval Pass@1 的具体下降数值为 3.5% (从 70.2% 降至 66.7%)，该数据点作为 Qwen3-27B INT4 性能损失的下界参考，需确认 Llama-3 测试是否包含 CoT 提示。

## Corrected Claim

Llama-3-8B 在 INT4 量化下 HumanEval Pass@1 存在性能下降，具体数值需进一步核实，该数据点可作为 Qwen3-27B INT4 性能损失的参考，但需确认测试条件是否包含 CoT 提示。

## Evidence

[质询]具体数值（70.2%降至66.7%）及量化方法（GPTQ/AWQ）属于经验事实，且缺乏来源支持，无法确认Llama-3-8B在特定量化下的确切性能下降值及测试条件（是否含CoT）。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

Llama-3-8B INT4 GPTQ AWQ HumanEval Pass@1 drop percentage
