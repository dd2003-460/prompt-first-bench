# N135: Qwen3-27B INT8 (GPTQ/SmoothQuant) 量化版本在 HumanEval Pass@1 上的准确率相比 BF16 基线通常下降 2-5

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N37

## Claim

Qwen3-27B INT8 (GPTQ/SmoothQuant) 量化版本在 HumanEval Pass@1 上的准确率相比 BF16 基线通常下降 2-5 个百分点，具体数值取决于量化校准数据集的选择，需查阅特定量化库（如 AutoGPTQ, AWQ）的评测报告。

## Corrected Claim

Qwen3-27B INT8 (GPTQ/SmoothQuant) 量化版本在 HumanEval Pass@1 上的准确率相比 BF16 基线通常会有所下降，具体数值取决于量化校准数据集的选择及量化方法，需查阅特定量化库（如 AutoGPTQ, AWQ）的评测报告以获取确切数据。

## Evidence

[质询]该陈述包含具体的经验数值断言（下降2-5个百分点），属于硬件/模型性能经验事实，无法从第一性原理推导，且参考来源中未包含针对Qwen3-27B在HumanEval上量化性能的具体评测数据，存在来源缺失风险。 | 逻辑自洽（量化通常导致精度轻微下降），但属于经验事实，参考来源[1]-[4]均未提供Qwen3-27B INT8量化在HumanEval上的具体性能对比数据，缺乏直接来源支持。

## Search Query

Qwen3-27B INT8 GPTQ HumanEval Pass@1 accuracy drop

## Retrieval Sources

- {'url': 'https://arxiv.org', 'type': None, 'title': 'direct-browser: arxiv.org'}
- {'url': 'https://github.com', 'type': None, 'title': 'direct-browser: github.com'}
- {'url': 'http://arxiv.org/abs/1303.4033v1', 'type': 'arxiv', 'title': 'Two-dimensional magnetic interactions in LaFeAsO'}
- {'url': 'http://arxiv.org/abs/2611.00486v1', 'type': 'arxiv', 'title': 'Integer-Exact Microscaling: Running MXFP4 Language Models on INT8 Matrix Units'}
