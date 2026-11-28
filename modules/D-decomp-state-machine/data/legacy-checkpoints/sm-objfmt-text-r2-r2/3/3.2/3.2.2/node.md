# N68: Qwen3-27B INT8 (W8A8) 量化后的 MMLU、HumanEval、GSM8K 绝对分数，用于实证计算 ΔScore_INT8 = (Score

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N17

## Claim

Qwen3-27B INT8 (W8A8) 量化后的 MMLU、HumanEval、GSM8K 绝对分数，用于实证计算 ΔScore_INT8 = (Score_BF16 - Score_INT8) / Score_BF16 是否严格小于 1%。

## Corrected Claim

Qwen3-27B INT8 (W8A8) 量化模型已发布，但其MMLU、HumanEval、GSM8K的具体绝对分数及相对于BF16版本的性能衰减比例需查阅具体评测报告，当前来源未提供足够数据证实衰减严格小于1%。

## Evidence

[质询]参考来源仅提供了模型的使用说明和链接，未包含具体的MMLU、HumanEval、GSM8K基准测试分数，无法直接验证ΔScore是否小于1%这一具体数值结论。 | 来源[1]确认了Qwen3-27B W8A8 INT8量化模型的存在，但未提供具体的基准测试数据以支持‘分数下降严格小于1%’这一经验性结论，属于经验事实且缺乏直接数据支持。

## Search Query

Qwen3-27B INT8 quantization benchmark evaluation results

## Retrieval Sources

- {'url': 'https://huggingface.co/compute1/Qwen3.8-27B-W8A8-INT8&rut=de5ac1b7ee3ab8f92b5445a6ea50a46189c1d7fe7ee02c50f0ba82ebc96ee0de', 'type': 'ddg', 'title': 'compute1/Qwen3.8-27B-W8A8-INT8 · Hugging Face'}
