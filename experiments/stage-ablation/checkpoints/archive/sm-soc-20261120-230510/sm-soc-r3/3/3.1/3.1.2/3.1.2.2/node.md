# N183: 价格敏感度系数 α_price 的量化：在 CTR = CTR_base * exp(-α_price * (P_ask/P_median - 1)) 模型中，

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N56

## Claim

价格敏感度系数 α_price 的量化：在 CTR = CTR_base * exp(-α_price * (P_ask/P_median - 1)) 模型中，α_price 反映价格偏离对点击的边际抑制作用，典型值需通过 A/B 测试回归系数确定（如 α_price ∈ [1.0, 3.0]）。

## Corrected Claim

在 CTR = CTR_base * exp(-α_price * (P_ask/P_median - 1)) 模型中，α_price 反映价格偏离对点击的边际抑制作用，其具体数值需通过 A/B 测试回归系数确定，不同业务场景下取值范围差异显著。

## Evidence

[质询]具体数值范围 [1.0, 3.0] 缺乏通用性，属于特定场景下的经验参数，不同行业、品类及定价策略下该系数差异巨大，直接断言典型值在此区间缺乏普适性证据支持。 | 来源 [1][2][3] 仅提及 A/B 测试用于 CTR 或定价优化，未提供 α_price 的具体数值范围或回归系数典型值，属于经验事实且缺来源直接支持。

## Search Query

price elasticity of click-through rate A/B test regression coefficient marketplace

## Retrieval Sources

- {'url': 'https://fastercapital.com/content/A-B-testing--A-Beginner-s-Guide-to-A-B-Testing-for-Click-Through-Rates.html&rut=7e50d857f9e10c8ad27d54406d02faf57d2b6911144e41f265860cc2ac1c6fd3', 'type': 'ddg', 'title': "A B testing: A Beginner's Guide to A B Testing for Click Through Rates ..."}
- {'url': 'https://fastercapital.com/content/Click-through-rate-optimization--A-B-Testing-for-CTR--How-to-Fine-Tune-Your-Campaigns.html&rut=89bd6c92704c4ccb60d72beed7f0fd5be2af0b6e2106d0107b0758d21712126a', 'type': 'ddg', 'title': 'Click through rate optimization: A B Testing for CTR: How to Fine Tune ...'}
- {'url': 'https://blog.hubspot.com/marketing/price-testing&rut=c6ea952e858227d7e104a13c0dd0ad9ef3bb01b8747bd1776b76b86174bd457a', 'type': 'ddg', 'title': 'How to A/B Test Your Pricing (And Why It Might Be a Bad Idea)'}
