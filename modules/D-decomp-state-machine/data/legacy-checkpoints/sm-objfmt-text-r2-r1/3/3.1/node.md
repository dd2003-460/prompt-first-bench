# N16: 量化质量评估基准：使用 MMLU, HumanEval, GSM8K 等标准数据集，比较 FP16/BF16 基准分数与 INT8, INT4, NVFP4 量

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

量化质量评估基准：使用 MMLU, HumanEval, GSM8K 等标准数据集，比较 FP16/BF16 基准分数与 INT8, INT4, NVFP4 量化后的分数差异，定义相对误差 ΔScore = (Score_base - Score_quant) / Score_base

## Corrected Claim

量化质量评估基准：使用 MMLU, HumanEval, GSM8K 等标准数据集，比较 FP16/BF16 基准分数与 INT8, INT4, NVFP4 量化后的分数差异，定义相对误差 ΔScore = (Score_base - Score_quant) / Score_base

## Evidence

先验知识/题面给定，逻辑校验通过：MMLU/HumanEval/GSM8K 是公认的标准评测集，相对误差公式定义清晰且量纲正确，符合量化评估常规做法。

## Search Query

Qwen3-27B quantization benchmark MMLU HumanEval accuracy drop
