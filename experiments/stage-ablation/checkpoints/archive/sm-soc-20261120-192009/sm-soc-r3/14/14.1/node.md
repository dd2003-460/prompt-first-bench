# N355: 卖家策略偏离度 S_seller 的量化定义：S_seller = (Average_Listing_Price - Median_Recent_Transac

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N121

## Claim

卖家策略偏离度 S_seller 的量化定义：S_seller = (Average_Listing_Price - Median_Recent_Transaction_Price) / Median_Recent_Transaction_Price；在观测数据中，S_seller 的均值应为 0.20（对应 15-25% 溢价的中值）。

## Corrected Claim

卖家策略偏离度 S_seller 的量化定义：S_seller = (Average_Listing_Price - Median_Recent_Transaction_Price) / Median_Recent_Transaction_Price；在观测数据中，S_seller 的均值应为 0.20（对应 15-25% 溢价的中值）。

## Evidence

先验知识/题面给定，逻辑校验通过
