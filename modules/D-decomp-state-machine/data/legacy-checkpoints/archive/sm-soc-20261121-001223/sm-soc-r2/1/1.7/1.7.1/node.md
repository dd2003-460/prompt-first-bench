# N51: 买家搜索成本 C_search 的量化：定义为寻找下一件同类商品的平均时间成本 T_search（小时）乘以买家的时间机会成本 r_time（元/小时），即 C

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N11

## Claim

买家搜索成本 C_search 的量化：定义为寻找下一件同类商品的平均时间成本 T_search（小时）乘以买家的时间机会成本 r_time（元/小时），即 C_search = T_search * r_time；需具体化 T_search 在二手平台的典型分布（如均值 30-60 分钟）及 r_time 的估算基准（如当地平均时薪的 10-20%）。

## Corrected Claim

买家搜索成本 C_search 的量化：定义为寻找下一件同类商品的平均时间成本 T_search（小时）乘以买家的时间机会成本 r_time（元/小时），即 C_search = T_search * r_time；需具体化 T_search 在二手平台的典型分布（如均值 30-60 分钟）及 r_time 的估算基准（如当地平均时薪的 10-20%）。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 C_search = T_search * r_time 符合经济学中时间成本的基本定义（时间×机会成本），量纲（小时×元/小时=元）正确；T_search 30-60分钟及 r_time 为时薪10-20%属于二手交易场景下合理的经验估算范围，无内部矛盾。

## Search Query

second hand market search cost time opportunity cost estimation
