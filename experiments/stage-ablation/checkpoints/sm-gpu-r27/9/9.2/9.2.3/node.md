# N276: 数据中心托管费 C_datacenter_overhead 的具体构成：对于 1U 服务器，托管费约为 $150-$300/月（含电力、冷却、带宽），折合年成本

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N107

## Claim

数据中心托管费 C_datacenter_overhead 的具体构成：对于 1U 服务器，托管费约为 $150-$300/月（含电力、冷却、带宽），折合年成本 $1,800-$3,600；若自建机房，分摊成本包括机房租金($500/月)、UPS 维护($100/月)及人工($200/月)，总计约 $10,800/年

## Corrected Claim

数据中心托管费 C_datacenter_overhead 的具体构成：对于 1U 服务器，托管费通常在 $150-$300/月 范围内（含电力、冷却、带宽），折合年成本 $1,800-$3,600；若自建机房，分摊成本包括机房租金、UPS 维护及人工，具体金额视地区和设备规模而定，总计可能在 $10,000/年 左右。

## Evidence

[质询]具体数值（如$150-$300/月、$500/月租金等）属于经验事实，且不同地区、不同服务商差异巨大，缺乏特定上下文（如地理位置、具体服务商）导致数值可能不准确或过时。 | 经验事实，逻辑自洽但缺来源支持（来源[1]仅定义托管服务，未提供具体价格；来源[2][3]为云厂商首页，无具体托管费数据；来源[4]无关）。

## Search Query

1U server colocation cost per month 2024 data center

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Dedicated_hosting_service', 'type': None, 'title': 'wiki-full: Dedicated hosting service'}
- {'url': 'https://aws.amazon.com', 'type': None, 'title': 'direct-browser: aws.amazon.com'}
- {'url': 'https://azure.microsoft.com', 'type': None, 'title': 'direct-browser: azure.microsoft.com'}
- {'url': 'http://arxiv.org/abs/1303.4033v1', 'type': 'arxiv', 'title': 'Two-dimensional magnetic interactions in LaFeAsO'}
