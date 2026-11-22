# N58: FP8 精度下 Qwen3-27B 的质量损失量化指标：在 MMLU 基准上准确率下降幅度约为 0.5%-1.0%，在 HumanEval 代码生成基准上 Pa

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13

## Claim

FP8 精度下 Qwen3-27B 的质量损失量化指标：在 MMLU 基准上准确率下降幅度约为 0.5%-1.0%，在 HumanEval 代码生成基准上 Pass@1 下降幅度约为 1.0%-2.0%。

## Corrected Claim

FP8 精度下 Qwen3-27B 在 MMLU 和 HumanEval 基准上通常表现出轻微的质量损失，具体下降幅度取决于量化算法和校准策略，一般在 1%-2% 左右。

## Evidence

[质询]具体数值区间（0.5%-1.0% 和 1.0%-2.0%）缺乏特定实验数据支持，不同量化方法（如 GPTQ, AWQ, SmoothQuant）和校准数据集会导致结果显著差异，直接断言固定区间可能以偏概全。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体量化损失幅度属于经验数据，无法从第一性原理推导）。

## Search Query

Qwen3-27B FP8 quantization accuracy drop MMLU HumanEval benchmark
