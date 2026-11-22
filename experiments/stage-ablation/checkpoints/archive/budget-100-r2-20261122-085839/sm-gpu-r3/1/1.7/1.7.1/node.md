# N48: Qwen3-27B 在 GPTQ (INT8, 1024校准样本) 量化下，MMLU 分数从 BF16 基线 85.0% 降至 83.8% (Δ=-1.2%)，

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N12

## Claim

Qwen3-27B 在 GPTQ (INT8, 1024校准样本) 量化下，MMLU 分数从 BF16 基线 85.0% 降至 83.8% (Δ=-1.2%)，HumanEval (Pass@1) 从 70.0% 降至 68.2% (Δ=-1.8%) [待核验: 需检索 Qwen3 官方量化报告或 HuggingFace 社区具体 benchmark 数据]

## Corrected Claim

Qwen3-27B 在 GPTQ (INT8) 量化下，MMLU 和 HumanEval 分数通常会出现轻微下降（约1-2%），具体数值取决于校准样本数量及量化实现细节。

## Evidence

[质询]具体数值（85.0%, 83.8%, 70.0%, 68.2%）及特定量化配置（GPTQ INT8, 1024校准样本）属于经验事实，缺乏来源支持，且不同量化实现（如GPTQ vs AWQ）及校准集大小可能导致结果波动，无法确认这些精确数值为官方或社区公认标准。 | 经验事实，逻辑自洽（量化通常导致性能轻微下降，量级合理）但缺来源支持，且检索无可用来源。

## Search Query

Qwen3-27B GPTQ INT8 MMLU HumanEval benchmark score degradation
