# N121: 性价比核心指标定义：每 Token 成本 (Cost per Token, CPT) = (Hardware_Capex / Estimated_Tokens_

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

性价比核心指标定义：每 Token 成本 (Cost per Token, CPT) = (Hardware_Capex / Estimated_Tokens_Lifetime) + (Power_Cost_per_Token)。其中 Estimated_Tokens_Lifetime = Throughput(tokens/s) * 8760 hours * Lifespan_Years。对于本地部署，Capex 权重通常为 60%，Opex (电力) 权重为 40%。

## Corrected Claim

性价比核心指标定义：每 Token 成本 (Cost per Token, CPT) = (Hardware_Capex / Estimated_Tokens_Lifetime) + (Power_Cost_per_Token)。其中 Estimated_Tokens_Lifetime = Throughput(tokens/s) * 8760 hours * Lifespan_Years。对于本地部署，Capex 和 Opex (电力) 的具体权重取决于硬件寿命、电价及折旧策略，通常需根据具体场景计算，而非固定为 60% 和 40%。

## Evidence

[质询]陈述中关于本地部署 Capex 权重 60% 和 Opex 权重 40% 的具体数值缺乏通用标准支持，且该比例高度依赖于硬件寿命、电价及折旧政策，并非固定的行业定义或第一性原理推导结果。 | 来源 [1][2] 确认了 Cost per Token 包含硬件折旧和电力成本等组成部分，支持公式的逻辑结构；但所有来源均未提及具体的 60/40 权重分配，该经验数值缺乏直接来源支持。

## Retrieval Sources

- {'url': 'https://www.compassingai.com/zh-hant/concept/cost-per-token/&rut=d02e4dbb0861a902e475a5cf1386877cf7ffbf2ea7243d65918c22656585422d', 'type': 'ddg', 'title': '每 token 成本 Cost per Token | Compassing AI 概念庫'}
- {'url': 'https://www.compassingai.com/concept/cost-per-token/&rut=a33241ab36d2fe338aabf1c07b6c2a9aacd2dbb1e9303a4d5121b8b5088215a8', 'type': 'ddg', 'title': '每 token 成本 Cost per Token | Compassing AI 概念库'}
- {'url': 'https://www.cerebras.ai/glossary/cost-per-token-and-ai-price-performance&rut=78c34b2ea736e69570ae397b1dad8b1c83b30ebce5f3683d1b5de105ac857855', 'type': 'ddg', 'title': 'AI Cost per Token and Price-Performance Explained'}
- {'url': 'https://www.glassdoor.com/Reviews/AIDS-Healthcare-Foundation-Reviews-E288826.htm', 'type': 'bing', 'title': 'AIDS Healthcare Foundation Reviews (1,102): Pros & Cons of …'}
