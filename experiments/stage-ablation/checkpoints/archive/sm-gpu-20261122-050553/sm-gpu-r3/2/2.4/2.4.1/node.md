# N62: W4 (4-bit) 精度下 Qwen3-27B 的质量损失量化指标：在 MMLU 基准上准确率下降幅度约为 3.0%-5.0%，在 HumanEval 代码生

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N15

## Claim

W4 (4-bit) 精度下 Qwen3-27B 的质量损失量化指标：在 MMLU 基准上准确率下降幅度约为 3.0%-5.0%，在 HumanEval 代码生成基准上 Pass@1 下降幅度约为 5.0%-10.0%，通常显著高于 FP8 和 INT8 量化。

## Corrected Claim

W4 (4-bit) 精度下 Qwen3-27B 的质量损失通常显著高于 FP8 和 INT8 量化，在 MMLU 和 HumanEval 等基准上会出现可测量的准确率下降，具体幅度取决于量化算法和校准策略。

## Evidence

[质询]具体数值区间（MMLU 3-5%, HumanEval 5-10%）属于经验事实，不同量化算法（如GPTQ, AWQ, SmoothQuant）和校准数据集会导致结果差异巨大，且Qwen3-27B的具体量化基准数据可能随模型版本更新而变化，缺乏特定来源支持该精确区间。 | 经验事实，逻辑自洽（4-bit量化损失通常高于8-bit）但缺来源支持

## Search Query

Qwen3-27B W4 4-bit quantization accuracy drop MMLU HumanEval benchmark
