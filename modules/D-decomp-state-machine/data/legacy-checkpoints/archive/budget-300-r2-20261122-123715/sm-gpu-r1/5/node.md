# N23: NVIDIA L40S (48GB GDDR6, ~$8000-10000) 和 L4 (24GB GDDR6, ~$3000-4000) 是介于消费级与H10

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

NVIDIA L40S (48GB GDDR6, ~$8000-10000) 和 L4 (24GB GDDR6, ~$3000-4000) 是介于消费级与H100/A100之间的关键数据中心候选，其FP8支持能力与能效比（~400W TDP for L40S）需纳入性价比排序，特别是对于需要48GB显存但预算低于A100的场景。

## Corrected Claim

NVIDIA L40S (48GB GDDR6) 和 L4 (24GB GDDR6) 是介于消费级与H100/A100之间的关键数据中心候选，其FP8支持能力与能效比需纳入性价比排序，特别是对于需要48GB显存但预算低于A100的场景。

## Evidence

[质询]陈述中包含具体的市场价格（~$8000-10000, ~$3000-4000）和具体功耗数值（~400W TDP），这些属于经验事实。参考来源[1]仅提供了L40S的产品定位和功能描述，未包含任何价格、具体TDP数值或L4 GPU的信息，无法直接支持这些具体参数。 | 来源[1]确认L40S是数据中心GPU，但缺乏价格、TDP及L4 GPU的具体数据支持；作为经验事实，逻辑自洽但缺来源直接支持，故降级。

## Retrieval Sources

- {'url': 'https://www.nvidia.com/en-us/data-center/l40s/&rut=7b7e356de20ff404abfd46444ae0a113cbbeafee16f9b793ca8b17bd72c72b52', 'type': 'ddg', 'title': 'L40S GPU for AI and Graphics Performance | NVIDIA'}
