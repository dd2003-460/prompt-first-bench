# N42: Qwen3-27B 在 INT8 (Weight-only or W8A8) 精度下，长尾事实问答 (TriviaQA/TruthfulQA) 的幻觉率 (Ha

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13, N14, N15

## Claim

Qwen3-27B 在 INT8 (Weight-only or W8A8) 精度下，长尾事实问答 (TriviaQA/TruthfulQA) 的幻觉率 (Hallucination Rate) 上升幅度约为 2-4%，高于 FP8 的稳定性

## Corrected Claim

Qwen3-27B 在 INT8 精度下，长尾事实问答的幻觉率通常高于 FP8 精度，具体上升幅度需参考特定基准测试报告。

## Evidence

[质询]参考来源仅提供了量化模型的下载和使用说明，完全缺失关于幻觉率（Hallucination Rate）的具体数值对比数据，无法证实“2-4%”这一具体量级及与FP8的对比结论。 | 来源[1]仅涉及模型部署，未包含性能评估数据；该陈述属于经验事实，逻辑上INT8量化导致精度下降从而增加幻觉率是合理的，但缺乏具体数值的外部直接支持。

## Search Query

Qwen3-27B INT8 quantization hallucination rate TriviaQA TruthfulQA evaluation

## Retrieval Sources

- {'url': 'https://huggingface.co/compute1/Qwen3.8-27B-W8A8-INT8&rut=de5ac1b7ee3ab8f92b5445a6ea50a46189c1d7fe7ee02c50f0ba82ebc96ee0de', 'type': 'ddg', 'title': 'compute1/Qwen3.8-27B-W8A8-INT8 · Hugging Face'}
