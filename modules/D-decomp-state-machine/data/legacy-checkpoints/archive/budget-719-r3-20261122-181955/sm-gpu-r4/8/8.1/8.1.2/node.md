# N346: Qwen3-27B INT4 (AWQ) 量化后 MMLU 准确率需从第三方评测平台（如 OpenCompass, LMSYS Arena）或模型作者发布的量化

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N117

## Claim

Qwen3-27B INT4 (AWQ) 量化后 MMLU 准确率需从第三方评测平台（如 OpenCompass, LMSYS Arena）或模型作者发布的量化评测表中获取，若缺失则通过本地运行 lm-eval-harness 在 RTX 4090 上实测（耗时约 2-4 小时）。

## Corrected Claim

Qwen3-27B INT4 (AWQ) 量化后 MMLU 准确率需从第三方评测平台（如 OpenCompass, LMSYS Arena）或模型作者发布的量化评测表中获取，若缺失则通过本地运行 lm-eval-harness 在 RTX 4090 上实测（耗时视具体配置而定）。

## Evidence

[质询]该陈述包含具体的经验性参数（如RTX 4090上运行lm-eval-harness耗时2-4小时），这属于经验事实而非第一性原理可推导内容，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B INT4 AWQ MMLU benchmark OpenCompass
