# N111: Qwen3-27B INT8 量化版本在 GSM8K 上的实测得分，用于评估 INT8 量化对逻辑链推理任务的特定影响。

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N41

## Claim

Qwen3-27B INT8 量化版本在 GSM8K 上的实测得分，用于评估 INT8 量化对逻辑链推理任务的特定影响。

## Corrected Claim

Qwen3-27B INT8 量化版本在 GSM8K 上的表现通常接近 FP16 基线，具体得分取决于量化算法（如 GPTQ/AWQ）及评测提示策略，需查阅特定技术报告获取精确数值。

## Evidence

[质询]该陈述声称存在具体的“实测得分”，但缺乏任何数据来源支持，且不同量化实现（如GPTQ, AWQ, SmoothQuant）及评测设置（CoT vs Direct）会导致分数显著差异，无法确定具体数值。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值）

## Search Query

Qwen3-27B INT8 W8A8 quantized GSM8K score
