# N217: FP8 (E4M3) 量化对 Qwen3-27B MMLU 分数的具体影响系数：FP8 量化导致的 MMLU 分数下降通常 < 0.5%，在多数子任务上与 BF

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N81

## Claim

FP8 (E4M3) 量化对 Qwen3-27B MMLU 分数的具体影响系数：FP8 量化导致的 MMLU 分数下降通常 < 0.5%，在多数子任务上与 BF16 无统计显著差异，需以具体评测脚本输出为准 [待核验]

## Corrected Claim

FP8 (E4M3) 量化对 Qwen3-27B 的 MMLU 分数影响极小，通常表现为与 BF16 性能几乎一致，具体数值需以实际评测为准。

## Evidence

[质询]来源中提到的模型版本（Qwen3.8/3.6）与事实节点中的 Qwen3-27B 存在版本不一致，且来源仅定性描述“保持几乎相同性能”，未提供具体的 MMLU 分数下降数值（<0.5%）或统计显著性检验结果，属于经验事实缺乏直接数据支持。 | 来源 [1][2][3] 均涉及 Qwen3 系列 27B 模型的 FP8 量化，定性支持性能损失极小（间接支持），但无具体 MMLU 数值证据，且模型版本号存在细微差异，故降级。

## Search Query

Qwen3 FP8 quantization MMLU score drop benchmark

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_29056781/article/details/166022297&rut=90c2b8874e00fe7c65b297d67da0c9b8864d2183e939c714938b3ce2952db9f2', 'type': 'ddg', 'title': 'Qwen3.8-27B FP8量化部署实战：从显存计算到性能调优-CSDN博客'}
- {'url': 'https://blog.csdn.net/lovely_yoshino/article/details/163828474&rut=f6894b90ac7485860ac5f5249184ac86fb627c1a73eb675037becd7558980c4f', 'type': 'ddg', 'title': 'Qwen3.8-27B-FP8 部署实践：从原理到生产 - CSDN博客'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/143005510&rut=26f38960e6230373005b7fbed5496a26ac1208d0db3e2d0cfa1483f31fcc4176', 'type': 'ddg', 'title': 'Qwen3.6-27B-FP8 FP8量化技术深度剖析：如何保持性能的同时减小模型体积？_滑杏舒-智能体开发者社区'}
