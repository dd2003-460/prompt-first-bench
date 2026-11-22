# N183: 筛选效应系数 ε_filter 的微观基础量化：假设买家支付意愿 V 服从截断正态分布 N(μ, σ², V_min, V_max)。无筛选时需求 Q_base

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N56

## Claim

筛选效应系数 ε_filter 的微观基础量化：假设买家支付意愿 V 服从截断正态分布 N(μ, σ², V_min, V_max)。无筛选时需求 Q_base 对应 V ≥ P_market 的买家比例。筛选后，高挂价 P_list 不仅过滤掉 V < P_list 的买家，还通过信号机制吸引 V > V_signal_threshold 的高意愿买家。ε_filter 应等于 (dQ_unfiltered/dP - dQ_filtered/dP) / (dQ_unfiltered/dP)，需通过估计 V 的分布参数 μ, σ 及信号阈值 V_signal_threshold 来计算具体数值。

## Corrected Claim

筛选效应系数 ε_filter 的微观基础量化：假设买家支付意愿 V 服从截断正态分布 N(μ, σ², V_min, V_max)。无筛选时需求 Q_base 对应 V ≥ P_market 的买家比例。筛选后，高挂价 P_list 不仅过滤掉 V < P_list 的买家，还通过信号机制吸引 V > V_signal_threshold 的高意愿买家。ε_filter 应等于 (dQ_unfiltered/dP - dQ_filtered/dP) / (dQ_unfiltered/dP)，需通过估计 V 的分布参数 μ, σ 及信号阈值 V_signal_threshold 来计算具体数值。

## Evidence

先验知识/题面给定，逻辑校验通过
