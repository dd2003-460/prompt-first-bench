# N138: FP8量化对Qwen3-27B的perplexity损失约为0.5-1.5%（基于WikiText2数据集），而INT4量化损失约为3-8%（取决于校准集大小，

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N28

## Claim

FP8量化对Qwen3-27B的perplexity损失约为0.5-1.5%（基于WikiText2数据集），而INT4量化损失约为3-8%（取决于校准集大小，通常需200-500个样本），具体数值需参考HuggingFace量化模型卡片或arXiv论文。

## Corrected Claim

FP8量化对Qwen3-27B的perplexity损失通常较小（约0.5-1.5%），而INT4量化损失相对较大（约3-8%），具体数值取决于量化算法、校准集大小及数据集，需参考具体模型卡片或论文。

## Evidence

[质询]具体数值范围（0.5-1.5% 和 3-8%）属于经验事实，缺乏直接来源支持，且不同量化实现（如GPTQ, AWQ, SmoothQuant）及校准策略下结果差异较大，单一区间可能具有误导性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B FP8 INT4 perplexity loss benchmark WikiText2
