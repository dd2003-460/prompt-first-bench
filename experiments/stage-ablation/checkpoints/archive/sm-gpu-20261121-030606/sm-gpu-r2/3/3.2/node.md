# N16: FP8精度下，Qwen3-27B在MMLU基准上得分降至84.7%（-0.5%），GSM8K降至81.5%（-0.6%），HumanEval降至67.8%（-0

- **status**: pending
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

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 9 column 5 (char 714)

## Search Query

Qwen3 27B FP8 quantization benchmark loss
