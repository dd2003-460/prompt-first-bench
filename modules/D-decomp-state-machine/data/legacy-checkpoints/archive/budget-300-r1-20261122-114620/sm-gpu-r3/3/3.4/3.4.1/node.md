# N95: Qwen3-27B 在 NVFP4 (或 GPTQ-INT4) 量化下，WikiText2 Perplexity 增加幅度通常为 5-15%，绝对值可能从 BF

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N21

## Claim

Qwen3-27B 在 NVFP4 (或 GPTQ-INT4) 量化下，WikiText2 Perplexity 增加幅度通常为 5-15%，绝对值可能从 BF16 的 ~5.6 升至 ~6.0-6.5；在 MMLU 综合基准上，准确率下降幅度约为 3-8 个百分点，显著高于 INT8 水平。

## Corrected Claim

Qwen3-27B 在 NVFP4 (或 GPTQ-INT4) 量化下，WikiText2 Perplexity 和 MMLU 准确率通常会有一定程度的下降，具体幅度取决于量化方法和校准策略，但通常显著高于 INT8 量化带来的性能损失。

## Evidence

[质询]具体数值范围（如PPL从5.6升至6.0-6.5，MMLU下降3-8%）属于经验事实，缺乏通用基准数据支持，且不同量化实现（如GPTQ vs AWQ vs NVFP4）及校准集差异可能导致结果波动较大，该具体区间可能过于精确或仅适用于特定实验条件。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B 4-bit quantization NVFP4 INT4 MMLU perplexity degradation
