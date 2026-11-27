# N123: Qwen3-27B 在 INT8 (W8A8) 量化下于 HumanEval 数据集上的具体 Pass@1 准确率 (Acc_INT8_HumanEval)，用

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N19

## Claim

Qwen3-27B 在 INT8 (W8A8) 量化下于 HumanEval 数据集上的具体 Pass@1 准确率 (Acc_INT8_HumanEval)，用于量化代码生成能力的退化。

## Corrected Claim

Qwen3.8-27B 在 INT8 (W8A8) 量化下于 GPQA 数据集上的准确率约为 89.9%，基本无损；HumanEval 的具体 Pass@1 数值未在参考来源中明确给出。

## Evidence

[质询]参考来源中提到的模型名称为 'Qwen3.8-27B'，而事实节点声称的是 'Qwen3-27B'，存在版本/命名不一致的嫌疑；且来源仅提供了 GPQA 精度数据，未提供 HumanEval 的具体 Pass@1 数值，无法直接证实该特定指标。 | 来源 [1][2][3] 均指向 'Qwen3.8-27B' 的 W8A8 量化版本，并确认其存在且精度基本无损（GPQA 89.9%），但未提供 HumanEval 的具体 Pass@1 数值，且模型版本号与 claim 中的 'Qwen3-27B' 存在细微差异（3 vs 3.8），属于经验事实且缺乏直接数值支持。

## Search Query

Qwen3-27B INT8 HumanEval pass@1

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_00993/article/details/167267737&rut=2775738823be248463a05848df6d20903333a3014a73c6a243e2965f1018bb7c', 'type': 'ddg', 'title': '一文读懂Qwen3.8-27B-w8a8：W8A8量化多模态大模型的完整入门指南-CSDN博客'}
- {'url': 'https://blog.csdn.net/gitblog_01003/article/details/167275479&rut=2de9f4daf7846e4992840ad86c0bf5875ad5c37ad2c49eb43aa749fc935ce6d7', 'type': 'ddg', 'title': '自己动手量化大模型：基于Qwen3.8-27B-w8a8的msmodelslim w8a8量化完整教程-CSDN博客'}
- {'url': 'https://www.modelscope.cn/models/VerStella/Qwen3.8-27B-W8A8-DCU&rut=ebcfac5ec81f181a33a7c8a9cd1dca2fe2e65678af756cd8b3e190c1ffa5838e', 'type': 'ddg', 'title': 'Qwen3.8-27B-W8A8-DCU · Models'}
