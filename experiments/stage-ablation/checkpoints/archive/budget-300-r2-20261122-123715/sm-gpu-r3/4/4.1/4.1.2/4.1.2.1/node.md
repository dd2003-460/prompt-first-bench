# N292: Qwen3-27B 在 W4 (GPTQ/AWQ) 精度下的实测质量基准数据：需获取 HuggingFace 官方量化模型仓库或第三方评测报告中的 MMLU 准

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N85, N86, N87

## Claim

Qwen3-27B 在 W4 (GPTQ/AWQ) 精度下的实测质量基准数据：需获取 HuggingFace 官方量化模型仓库或第三方评测报告中的 MMLU 准确率下降幅度（预期 5-10%）及 HumanEval 代码通过率下降幅度（预期 >10%），以判定其是否满足 Quality_Sensitivity=Medium 的约束。

## Corrected Claim

Qwen3-27B 在 W4 (GPTQ/AWQ) 精度下的实测质量基准数据需通过 HuggingFace 官方仓库或第三方评测报告获取，以确认 MMLU 和 HumanEval 的具体下降幅度是否满足 Quality_Sensitivity=Medium 约束，具体数值需实测验证。

## Evidence

[质询]该陈述包含具体的经验性数值预期（MMLU下降5-10%，HumanEval下降>10%），属于特定模型在特定量化方案下的实测数据，无法从第一性原理推导，且当前无可用来源支持这些具体数值。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法验证具体量化损失幅度）

## Search Query

Qwen3-27B W4 GPTQ AWQ perplexity MMLU HumanEval benchmark accuracy drop
