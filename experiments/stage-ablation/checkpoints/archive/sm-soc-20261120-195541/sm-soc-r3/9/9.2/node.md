# N200: 筛选效应导致的成交周期缩短量 ΔT_shorten 的计算：ΔT_shorten = T_base * [1 - exp(-k_filter * σ_quali

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N67

## Claim

筛选效应导致的成交周期缩短量 ΔT_shorten 的计算：ΔT_shorten = T_base * [1 - exp(-k_filter * σ_quality)]，其中 k_filter 为筛选强度系数（假设 k_filter=0.5），σ_quality 为商品质量离散度；该公式表明筛选效应对周期缩短的贡献随质量离散度增加而递减。

## Corrected Claim

筛选效应导致的成交周期缩短量 ΔT_shorten 的计算：ΔT_shorten = T_base * [1 - exp(-k_filter * σ_quality)]，其中 k_filter 为筛选强度系数（假设 k_filter=0.5），σ_quality 为商品质量离散度；该公式表明筛选效应对周期缩短的贡献随质量离散度增加而递减。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合饱和增长模型，数学性质（随σ增加边际贡献递减）推导正确

## Search Query

matching speed quality dispersion filtering effect exponential decay model
