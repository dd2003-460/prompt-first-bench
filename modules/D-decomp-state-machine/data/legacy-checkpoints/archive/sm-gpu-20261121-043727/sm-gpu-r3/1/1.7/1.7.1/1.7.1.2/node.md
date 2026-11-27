# N149: 定义质量损失的可接受阈值量化标准：通常认为 Delta_PPL < 5% 或 MMLU 下降 < 2% 为“可接受”，Delta_PPL < 10% 为“边缘可

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57

## Claim

定义质量损失的可接受阈值量化标准：通常认为 Delta_PPL < 5% 或 MMLU 下降 < 2% 为“可接受”，Delta_PPL < 10% 为“边缘可接受”，>10% 为“不可接受”。需将此阈值应用于 N80 (INT8) 和 N81 (FP8) 的预测值，判断其在 32K 长上下文下的实际退化是否超出阈值，特别是长文本生成任务对 PPL 更敏感，阈值可能需收紧至 3%。

## Corrected Claim

定义质量损失的可接受阈值量化标准：通常认为 Delta_PPL < 5% 或 MMLU 下降 < 2% 为“可接受”，Delta_PPL < 10% 为“边缘可接受”，>10% 为“不可接受”。需将此阈值应用于 N80 (INT8) 和 N81 (FP8) 的预测值，判断其在 32K 长上下文下的实际退化是否超出阈值，特别是长文本生成任务对 PPL 更敏感，阈值可能需收紧至 3%。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LLM quantization quality degradation threshold perplexity acceptable loss benchmark
