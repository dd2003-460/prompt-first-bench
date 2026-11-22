# N120: 信号强度 C_signal 的量化定义：C_signal = (Number_of_Recent_Sales_7d / Total_Listings_7d) *

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N38

## Claim

信号强度 C_signal 的量化定义：C_signal = (Number_of_Recent_Sales_7d / Total_Listings_7d) * (1 + β_trust * Seller_Rating_Norm)，其中 β_trust 为信誉系数（通常 0.1-0.3），Seller_Rating_Norm 为归一化卖家评分 [0,1]，该值反映买家对商品真实性的信任度。

## Corrected Claim

信号强度 C_signal 的量化定义：C_signal = (Number_of_Recent_Sales_7d / Total_Listings_7d) * (1 + β_trust * Seller_Rating_Norm)，其中 β_trust 为信誉系数（通常 0.1-0.3），Seller_Rating_Norm 为归一化卖家评分 [0,1]，该值反映买家对商品真实性的信任度。

## Evidence

先验知识/题面给定，逻辑校验通过
