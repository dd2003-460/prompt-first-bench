# N134: 平均浏览商品数 $N_{browse}$ 的估算：$N_{browse}$ 通常受搜索深度和推荐算法影响。若买家平均浏览 10-20 个商品，则 $N_{bro

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N41

## Claim

平均浏览商品数 $N_{browse}$ 的估算：$N_{browse}$ 通常受搜索深度和推荐算法影响。若买家平均浏览 10-20 个商品，则 $N_{browse} \in [10, 20]$。具体数值需基于平台行为数据或 A/B 测试确定。

## Corrected Claim

平均浏览商品数 $N_{browse}$ 受搜索深度和推荐算法影响，具体数值需基于特定平台的行为数据或 A/B 测试确定，通常需通过实证分析获得。

## Evidence

[质询]该陈述中的具体数值范围 [10, 20] 属于经验事实，缺乏通用性，不同平台（如电商 vs 内容社区）差异巨大，且参考来源未提供此具体数据支持。 | 逻辑自洽，但参考来源 [1] 和 [2] 均未提供具体的浏览商品数量数据，属于经验事实且缺来源直接支持。

## Search Query

e-commerce average items browsed per session user behavior data

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/HTTP_cookie', 'type': 'wikipedia', 'title': 'HTTP cookie'}
- {'url': 'https://en.wikipedia.org/wiki/Collaborative_filtering', 'type': 'wikipedia', 'title': 'Collaborative filtering'}
