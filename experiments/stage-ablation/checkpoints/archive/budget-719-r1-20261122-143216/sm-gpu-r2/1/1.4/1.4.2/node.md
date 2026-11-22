# N51: INT8 量化 Qwen3-27B 在 MMLU-Pro 或 GSM8K 等推理基准上的准确率下降百分比，需验证是否低于 2% 阈值以确认其作为 FP8 替代方

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N9

## Claim

INT8 量化 Qwen3-27B 在 MMLU-Pro 或 GSM8K 等推理基准上的准确率下降百分比，需验证是否低于 2% 阈值以确认其作为 FP8 替代方案的可行性，若下降超过 2% 则需重新评估精度选择

## Corrected Claim

INT8 量化 Qwen3-27B 在 MMLU-Pro 或 GSM8K 等推理基准上的准确率下降情况需通过实际基准测试验证，以评估其作为 FP8 替代方案的可行性；若下降幅度超出可接受阈值（如 2%），则需重新评估精度选择。

## Evidence

[质询]该陈述包含具体的经验性阈值（2%）和特定模型（Qwen3-27B）在特定基准（MMLU-Pro/GSM8K）上的量化性能表现，属于经验事实，无法从第一性原理推导，且缺乏来源支持以确认该阈值或具体下降幅度的准确性。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

Qwen3-27B INT8 quantization MMLU-Pro GSM8K accuracy drop percentage
