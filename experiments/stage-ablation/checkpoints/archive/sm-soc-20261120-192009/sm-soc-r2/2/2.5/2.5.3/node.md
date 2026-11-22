# N59: 买家筛选放大系数：算法将高挂价商品的曝光时长乘以系数 k_exposure，导致单位时间内接触该商品的买家数量 N_buyers = k_exposure * 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N15, N16, N17

## Claim

买家筛选放大系数：算法将高挂价商品的曝光时长乘以系数 k_exposure，导致单位时间内接触该商品的买家数量 N_buyers = k_exposure * N_base；筛选效应使得成交转化率 Conv_rate = Conv_base * (1 + α_filter * Price_Deviation)，其中 α_filter 需实证估计。

## Corrected Claim

买家筛选放大系数：算法将高挂价商品的曝光时长乘以系数 k_exposure，导致单位时间内接触该商品的买家数量 N_buyers = k_exposure * N_base；筛选效应使得成交转化率 Conv_rate = Conv_base * (1 + α_filter * Price_Deviation)，其中 α_filter 需实证估计。

## Evidence

先验知识/题面给定，逻辑校验通过
