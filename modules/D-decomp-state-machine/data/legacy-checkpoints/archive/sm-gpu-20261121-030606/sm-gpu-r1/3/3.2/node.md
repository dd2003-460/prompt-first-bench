# N16: FP8精度下，Qwen3-27B在MMLU基准上得分降至84.7%（-0.5%），GSM8K降至81.5%（-0.6%），HumanEval降至67.8%（-0

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N3

## Claim

FP8精度下，Qwen3-27B在MMLU基准上得分降至84.7%（-0.5%），GSM8K降至81.5%（-0.6%），HumanEval降至67.8%（-0.7%），质量损失<1%，在大多数应用场景下可接受，尤其对于非数学/代码密集任务。

## Corrected Claim

FP8精度下，Qwen3-27B在MMLU、GSM8K和HumanEval等基准上的得分通常会有轻微下降（通常<1%），具体数值需参考官方技术报告或独立评测，但整体质量损失在大多数应用场景下可接受。

## Evidence

[质询]具体数值（84.7%, 81.5%, 67.8%）及特定模型（Qwen3-27B）的基准测试结果为经验事实，无法从第一性原理推导，且缺乏外部来源直接支持或交叉验证，存在数值虚构或混淆不同量化方案（如FP8 vs INT8）的风险。 | 经验事实，逻辑自洽（FP8量化通常导致<1%的性能损失符合业界共识），但缺来源支持，无法验证具体数值。

## Search Query

Qwen3 27B FP8 quantization benchmark loss
