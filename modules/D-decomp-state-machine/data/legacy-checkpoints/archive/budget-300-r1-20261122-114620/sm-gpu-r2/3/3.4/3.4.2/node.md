# N96: Qwen3-27B 在 4-bit 量化下，GSM8K (数学推理) 的 Pass@1 准确率下降幅度通常比 HumanEval 更大，预计从 BF16 的 ~

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N21

## Claim

Qwen3-27B 在 4-bit 量化下，GSM8K (数学推理) 的 Pass@1 准确率下降幅度通常比 HumanEval 更大，预计从 BF16 的 ~50-60% 下降至 ~40-50%，下降幅度达 10-20 个百分点；这是因为 4-bit 量化对中间推理步骤的数值精度损失累积效应更明显。

## Corrected Claim

Qwen3-27B 在 4-bit 量化下，GSM8K (数学推理) 的 Pass@1 准确率通常会出现一定程度的下降，且由于数学推理涉及多步数值计算，其精度损失累积效应往往比代码生成（HumanEval）更明显，但具体下降幅度取决于量化算法和校准数据。

## Evidence

[质询]具体数值区间（BF16 ~50-60% 降至 4-bit ~40-50%）及下降幅度（10-20个百分点）属于特定模型版本（Qwen3-27B）在特定量化方案下的经验数据，缺乏通用性，且不同量化算法（如GPTQ, AWQ, GGUF）对精度的影响差异巨大，该具体数值范围可能不准确或仅适用于特定配置。 | 经验事实，逻辑自洽（数学推理对精度更敏感符合直觉）但缺来源支持，且具体数值无法从第一性原理推出。

## Search Query

Qwen3-27B 4-bit quantization GSM8K math reasoning accuracy drop
