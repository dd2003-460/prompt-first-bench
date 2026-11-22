# N98: 买家保留价格 U_i 的尾部指数 α 的估计公式为 α = 1 / log(1 + (U_max - P_median) / (U_90 - P_median)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

买家保留价格 U_i 的尾部指数 α 的估计公式为 α = 1 / log(1 + (U_max - P_median) / (U_90 - P_median))，基于 Pareto 分布拟合，需从 eBay/闲鱼历史成交数据中提取 U_max（最高成交价）和 U_90（第90百分位成交价）进行计算。

## Corrected Claim

买家保留价格 U_i 的尾部指数 α 的估计公式为 α = 1 / log(1 + (U_max - P_median) / (U_90 - P_median))，基于 Pareto 分布拟合，需从 eBay/闲鱼历史成交数据中提取 U_max（最高成交价）和 U_90（第90百分位成交价）进行计算。

## Evidence

先验知识/题面给定，逻辑校验通过
