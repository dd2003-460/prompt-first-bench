# N254: 锚点展示对成交周期 T 的边际影响量化：假设展示中位数锚点导致卖家挂价下调 ΔP_anchor = k_used * (P_list - P_median)，进

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N81

## Claim

锚点展示对成交周期 T 的边际影响量化：假设展示中位数锚点导致卖家挂价下调 ΔP_anchor = k_used * (P_list - P_median)，进而导致买家搜索时间缩短 ΔT_search = -ζ * ΔP_anchor / P_median，其中 ζ 为搜索效率系数（ζ ≈ 0.5-1.0 天/10% 价差）；需验证 ΔT_search 是否足以抵消因价格降低导致的买家犹豫时间增加。

## Corrected Claim

锚点展示对成交周期 T 的边际影响需通过实证数据量化：假设展示中位数锚点导致卖家挂价下调 ΔP_anchor，进而影响买家搜索时间 ΔT_search；需验证 ΔT_search 的缩短是否足以抵消因价格降低导致的买家犹豫时间增加，具体系数 ζ 需基于历史交易数据回归分析确定。

## Evidence

[质询]该陈述包含具体的经验参数（ζ ≈ 0.5-1.0 天/10% 价差）和特定的因果机制假设（锚点导致挂价下调进而缩短搜索时间），这些属于市场行为经验事实，无法从第一性原理严格推导，且缺乏外部数据支持其量级和方向的正确性。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该参数非数学/物理公理可推导范畴）

## Search Query

price anchor display impact on transaction time search efficiency second-hand market
