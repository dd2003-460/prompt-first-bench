# N237: Qwen3-27B 在 W4 (INT4/AWQ) 量化下的 MMLU 基准测试得分，需查找独立评测（如 LMSYS Chatbot Arena 或 OpenC

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N69

## Claim

Qwen3-27B 在 W4 (INT4/AWQ) 量化下的 MMLU 基准测试得分，需查找独立评测（如 LMSYS Chatbot Arena 或 OpenCompass）或官方量化版本发布说明中的具体数值，以计算绝对下降值 (Delta Score)。

## Corrected Claim

Qwen3-27B 在 W4 (INT4/AWQ) 量化下的 MMLU 基准测试得分需查阅官方技术报告或独立评测平台（如 OpenCompass）获取具体数值，以计算绝对下降值 (Delta Score)。

## Evidence

[质询]该陈述要求查找具体的MMLU基准测试得分数值，属于经验事实（具体模型在特定量化下的性能指标）。由于检索失败，无法提供具体数值，且不同评测集（如MMLU-Pro vs MMLU-5-shot）或量化实现细节可能导致数值差异，无法从第一性原理推导。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值）

## Search Query

Qwen3-27B AWQ INT4 MMLU score evaluation
