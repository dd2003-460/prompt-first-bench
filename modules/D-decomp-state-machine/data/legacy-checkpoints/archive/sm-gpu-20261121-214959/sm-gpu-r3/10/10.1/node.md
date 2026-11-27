# N118: Qwen3-27B INT4 (AWQ) 在 MMLU-Pro 基准测试上的准确率从 BF16 的 78.5% 下降至 76.2%，绝对下降 2.3 个百分点，

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N35

## Claim

Qwen3-27B INT4 (AWQ) 在 MMLU-Pro 基准测试上的准确率从 BF16 的 78.5% 下降至 76.2%，绝对下降 2.3 个百分点，相对下降 2.9%，该数值落在 N35 所述的 1-5% 范围内，验证了其在通用知识问答任务上的轻微损失。

## Corrected Claim

Qwen3-27B INT4 (AWQ) 在 MMLU-Pro 基准测试上的准确率相较于 BF16 存在轻微下降，绝对下降约 2-3 个百分点，相对下降约 3%，该数值落在 1-5% 的常见量化损失范围内。

## Evidence

[质询]具体数值（78.5% 和 76.2%）属于特定模型版本在特定基准上的经验测量数据，无法从第一性原理推导，且缺乏来源支持，存在数值不准确或版本混淆的风险。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B AWQ INT4 MMLU-Pro accuracy benchmark
