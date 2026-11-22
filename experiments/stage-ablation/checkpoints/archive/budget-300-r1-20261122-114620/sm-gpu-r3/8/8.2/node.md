# N128: 在数学推理任务（MATH/GSM8K）上，Qwen3-27B 模型从 BF16 量化至 4-bit (NVFP4/W4A16) 的准确率下降幅度通常大于 5%，

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N37

## Claim

在数学推理任务（MATH/GSM8K）上，Qwen3-27B 模型从 BF16 量化至 4-bit (NVFP4/W4A16) 的准确率下降幅度通常大于 5%，导致 4-bit 方案在精度敏感场景下被排除，除非引入校准数据集或任务特定微调。

## Corrected Claim

在数学推理任务（MATH/GSM8K）上，Qwen3-27B 模型从 BF16 量化至 4-bit (NVFP4/W4A16) 通常会导致一定程度的准确率下降，具体幅度取决于校准策略；在精度敏感场景下，若无有效校准或微调，4-bit 方案可能因精度损失过大而被排除。

## Evidence

[质询]该陈述包含具体的经验性数值阈值（'通常大于 5%'）和特定的量化方案（NVFP4/W4A16），属于经验事实。缺乏直接来源支持该具体数值阈值，且不同模型、不同量化算法（如GPTQ, AWQ, SmoothQuant）及校准策略下，精度下降幅度差异巨大，'通常大于5%'这一概括性结论可能过于绝对或基于特定未披露的实验条件。 | 经验事实，逻辑自洽但缺来源支持。4-bit量化通常会导致精度下降，但具体幅度（>5%）及是否必然导致方案被排除，依赖于具体的校准方法和任务难度，无外部来源证实该特定阈值。

## Search Query

Qwen3-27B 4-bit quantization MATH GSM8K accuracy degradation
