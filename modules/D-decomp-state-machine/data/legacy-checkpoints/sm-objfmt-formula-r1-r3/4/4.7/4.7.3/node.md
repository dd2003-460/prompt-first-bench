# N100: Qwen3-27B 在 NVFP4 量化后，GSM8K 或 HumanEval 等复杂推理/代码生成基准测试相对于 BF16 基线的具体得分下降值（Delta_

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N22

## Claim

Qwen3-27B 在 NVFP4 量化后，GSM8K 或 HumanEval 等复杂推理/代码生成基准测试相对于 BF16 基线的具体得分下降值（Delta_Inference），此类任务对低精度量化更敏感，需查找特定量化仓库的 README 或论文附录中的实证数据（预期范围 1%-5%）

## Corrected Claim

Qwen3-27B 在 NVFP4 量化后，GSM8K 或 HumanEval 等复杂推理/代码生成基准测试相对于 BF16 基线可能存在性能下降，具体幅度需查阅特定量化仓库的 README 或论文附录中的实证数据。

## Evidence

[质询]该陈述包含具体的经验性数值范围（1%-5%）和特定模型/量化组合的性能表现，属于经验事实，无法从第一性原理推导，且缺乏来源支持以确认其准确性。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

Qwen3-27B 4-bit quantization GSM8K HumanEval performance degradation
