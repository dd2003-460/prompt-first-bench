# N226: 搜索成本节约 ΔSearchCost 的量化公式：ΔSearchCost = T_search_old - T_search_new，其中 T_search_o

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N81

## Claim

搜索成本节约 ΔSearchCost 的量化公式：ΔSearchCost = T_search_old - T_search_new，其中 T_search_old 为信息不透明时的平均搜索时间（分钟），T_search_new 为信息透明后的平均搜索时间，需通过用户行为日志中从进入首页到点击商品的停留时间分布的中位数差值计算。

## Corrected Claim

搜索成本节约 ΔSearchCost 的量化公式：ΔSearchCost = T_search_old - T_search_new，其中 T_search_old 为信息不透明时的平均搜索时间（分钟），T_search_new 为信息透明后的平均搜索时间，需通过用户行为日志中从进入首页到点击商品的停留时间分布的中位数差值计算。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

search cost reduction information transparency e-commerce user behavior
