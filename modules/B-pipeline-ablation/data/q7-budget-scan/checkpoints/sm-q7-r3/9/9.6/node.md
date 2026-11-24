# N108: 云归档存储 5年取回/请求费 = (500TB × 1024GB × 1次/年 × 5年 × ¥0.06/GB) / 500TB = ¥307/TB（假设每年全

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N26

## Claim

云归档存储 5年取回/请求费 = (500TB × 1024GB × 1次/年 × 5年 × ¥0.06/GB) / 500TB = ¥307/TB（假设每年全量取回1次，取回单价¥0.06/GB）

## Corrected Claim

云归档存储5年取回/请求费约为¥307/TB（基于假设：每年全量取回1次，取回单价¥0.06/GB，具体价格需以实际云厂商最新报价为准）

## Evidence

[质询]取回单价¥0.06/GB属于特定云厂商（如阿里云OSS归档存储）的经验性定价参数，并非通用物理常数或数学公理，且参考来源均为AWS S3 Glacier（美元计价），无法直接支持该具体数值。 | 逻辑推导自洽（500TB*1024GB*5*0.06/500TB=307.2≈307），但参考来源[1][2]涉及AWS美元定价，与本题人民币及具体单价无关，属经验事实缺直接来源支持。

## Search Query

AWS S3 Glacier retrieval cost per GB standard retrieval 2024

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Amazon_S3_Glacier', 'type': 'wikipedia', 'title': 'Amazon S3 Glacier'}
- {'url': 'https://en.wikipedia.org/wiki/Timeline_of_Amazon_Web_Services', 'type': 'wikipedia', 'title': 'Timeline of Amazon Web Services'}
