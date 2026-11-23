# N320: 阿里云95分位计费的实际有效峰值溢价率计算：Peak_Premium_effective = (BWP_95 - BWP_avg) / BWP_avg × (P

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N102

## Claim

阿里云95分位计费的实际有效峰值溢价率计算：Peak_Premium_effective = (BWP_95 - BWP_avg) / BWP_avg × (Price_per_Mbps_95 / Price_per_Mbps_traffic)，其中BWP_95/BWP_avg = K_peak_95（典型1.2-1.5，低于K_peak=2.0因95分位截断极端峰值），Price比约为1:1.5（95分位单价低于流量单价），综合有效溢价率约20%-40%，非显式但隐含在分位截断中。

## Corrected Claim

阿里云95分位计费的实际有效峰值溢价率受95分位截断影响，通常低于基于绝对峰值的溢价率，具体数值取决于业务流量分布特征及当时定价策略，典型区间可能在20%-40%之间，但需以实际账单数据为准。

## Evidence

[质询]该陈述包含具体的经验参数（如K_peak_95典型值1.2-1.5、价格比1:1.5、综合溢价率20%-40%），这些数值并非第一性原理可推导，且缺乏来源支持，属于经验事实。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Alibaba Cloud CDN 95th percentile bandwidth billing vs traffic based pricing effective premium rate
