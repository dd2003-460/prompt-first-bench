# N121: Qwen3-27B 在 INT8 (W8A8) 量化下于 GSM8K 数据集上的具体准确率数值 (Acc_INT8_GSM8K)，用于量化逻辑推理任务的退化程度

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N19

## Claim

Qwen3-27B 在 INT8 (W8A8) 量化下于 GSM8K 数据集上的具体准确率数值 (Acc_INT8_GSM8K)，用于量化逻辑推理任务的退化程度。

## Corrected Claim

Qwen3-27B (或 Qwen3.8-27B) 存在 INT8 (W8A8) 量化版本，但参考来源未提供其在 GSM8K 数据集上的具体准确率数值。

## Evidence

[质询]参考来源仅提供了模型名称、量化方式（W8A8）和硬件需求（~30GB, 2x24GB），并未包含 GSM8K 数据集上的具体准确率数值（Acc_INT8_GSM8K）。此外，来源标题中的模型名为 'Qwen3.8-27B'，与陈述中的 'Qwen3-27B' 存在细微版本差异，且摘要中未提及任何基准测试成绩。 | 来源 [1] 确认了存在 Qwen3.8-27B 的 INT8 (W8A8) 量化版本，但未提供 GSM8K 准确率的具体数值，属于间接支持模型存在性，无法直接支持具体性能指标。

## Search Query

Qwen3-27B INT8 GSM8K accuracy

## Retrieval Sources

- {'url': 'https://huggingface.co/Avesed/Qwen3.8-27B-INT8-W8A8&rut=9b3124eeab0c7d73f385082d587216c4ff250f99642bcd0fc1afbd9c1a2134c2', 'type': 'ddg', 'title': 'Avesed/Qwen3.8-27B-INT8-W8A8 · Hugging Face'}
