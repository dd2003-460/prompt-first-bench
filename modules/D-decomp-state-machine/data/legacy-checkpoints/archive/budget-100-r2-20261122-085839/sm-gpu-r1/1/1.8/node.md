# N13: Qwen3-27B在W4 (4-bit)量化（如AWQ, GPTQ）下的性能损失：通常在MMLU上损失3-5个百分点，在复杂推理任务（GSM8K）上损失5-8个

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

Qwen3-27B在W4 (4-bit)量化（如AWQ, GPTQ）下的性能损失：通常在MMLU上损失3-5个百分点，在复杂推理任务（GSM8K）上损失5-8个百分点。例如，MMLU从85.0%降至81.0%，GSM8K从90%降至83% [待核验: 具体数值需查阅Qwen3 W4量化评测报告]。

## Corrected Claim

Qwen3-27B在W4量化下通常存在性能损失，MMLU约损失3-5个百分点，GSM8K约损失5-8个百分点，具体数值取决于量化算法及校准策略。

## Evidence

[质询]具体数值（MMLU 85.0%->81.0%, GSM8K 90%->83%）属于特定模型版本和量化配置下的经验测量数据，无法从第一性原理推导，且不同量化算法（AWQ vs GPTQ）及校准数据集会导致结果波动，缺乏具体来源支持时，精确数值不可靠。 | source=knowledge，逻辑自洽（4-bit量化通常导致3-8%性能损失符合业界常识），但具体数值为经验事实，无外部来源直接支持，依据经验事实排除条款降级。

## Search Query

Qwen3-27B 4-bit quantization AWQ GPTQ performance drop
