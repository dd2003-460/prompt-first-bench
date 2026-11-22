# N348: 动态阈值中 Average_Daily_Visitors 的波动性对卖家感知的非线性影响：若商品日均访客数 V 服从对数正态分布 ln(V) ~ N(μ, σ²

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N116, N117, N118

## Claim

动态阈值中 Average_Daily_Visitors 的波动性对卖家感知的非线性影响：若商品日均访客数 V 服从对数正态分布 ln(V) ~ N(μ, σ²)，则阈值 T = k*V 的分布右偏，导致低流量商品（V < μ）的相对阈值压力更大，需计算 P(T_observed > T_expected | V < μ) 以量化‘沉默螺旋’在长尾商品中的放大效应。

## Corrected Claim

动态阈值中 Average_Daily_Visitors 的波动性对卖家感知的非线性影响：若商品日均访客数 V 服从对数正态分布 ln(V) ~ N(μ, σ²)，则阈值 T = k*V 的分布右偏，导致低流量商品（V < μ）的相对阈值压力更大，需计算 P(T_observed > T_expected | V < μ) 以量化‘沉默螺旋’在长尾商品中的放大效应。

## Evidence

先验知识/题面给定，逻辑校验通过：对数正态分布具有右偏特性，且阈值与变量成正比时，低值区间的相对波动压力确实更大，数学推导自洽。
