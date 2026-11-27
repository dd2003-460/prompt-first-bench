# N338: Qwen3-27B INT4 量化在 MMLU 基准上的具体准确率数值，用于验证其是否满足 N107 设定的 >70% 通用任务阈值。

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N107, N108, N109

## Claim

Qwen3-27B INT4 量化在 MMLU 基准上的具体准确率数值，用于验证其是否满足 N107 设定的 >70% 通用任务阈值。

## Corrected Claim

Qwen3-27B INT4 量化在 MMLU 基准上的准确率通常维持在较高水平（约70%-80%区间），具体数值取决于量化算法与评测配置，需查阅特定技术报告确认是否严格大于70%。

## Evidence

[质询]具体数值属于经验事实，且不同量化方案（如GPTQ, AWQ, GGUF）及评测设置（如few-shot数量）会导致准确率波动，缺乏具体来源无法确定唯一数值。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B INT4 MMLU accuracy
