# N42: 筛选强度量化：定义筛选强度 S = 1 - (N_consult(P_ask) / N_search_total)，其中 N_consult 为发起咨询的买家数

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N9

## Claim

筛选强度量化：定义筛选强度 S = 1 - (N_consult(P_ask) / N_search_total)，其中 N_consult 为发起咨询的买家数，N_search_total 为搜索该商品的总人数；S 与 P_ask 在区间内呈单调递增关系。

## Corrected Claim

筛选强度量化：定义筛选强度 S = 1 - (N_consult(P_ask) / N_search_total)，其中 N_consult 为发起咨询的买家数，N_search_total 为搜索该商品的总人数；S 与 P_ask 在区间内呈单调递增关系。

## Evidence

先验知识/题面给定，逻辑校验通过：S定义为咨询率，P_ask为咨询概率，在独立同分布假设下，S是P_ask的单调递增函数，量纲与逻辑自洽。
