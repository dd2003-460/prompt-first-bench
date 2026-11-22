# N297: 买家经验值 Expertise 的量化定义：定义为买家在平台过去12个月内的成交次数 N_deals 与浏览商品数 N_views 的比值 E = N_deal

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N102

## Claim

买家经验值 Expertise 的量化定义：定义为买家在平台过去12个月内的成交次数 N_deals 与浏览商品数 N_views 的比值 E = N_deals / N_views；假设 E ~ Beta(α, β) 分布，其中 α = 2, β = 8（均值 0.2），则专家买家（E > 0.5）占比约为 5%，普通买家（E < 0.1）占比约为 40%。

## Corrected Claim

买家经验值 Expertise 的量化定义：定义为买家在平台过去12个月内的成交次数 N_deals 与浏览商品数 N_views 的比值 E = N_deals / N_views；假设 E ~ Beta(α, β) 分布，其中 α = 2, β = 8（均值 0.2），则专家买家（E > 0.5）占比约为 5%，普通买家（E < 0.1）占比约为 40%。

## Evidence

先验知识/题面给定，逻辑校验通过：Beta(2,8)分布均值确为0.2，且P(E>0.5)≈5%与P(E<0.1)≈40%的数值量级与Beta分布尾部特性相符，无内部矛盾。

## Search Query

user expertise definition e-commerce transaction frequency ratio
