# N41: 点击率 CTR 的衰减函数：CTR = CTR_base * exp(-k * ΔP/P_old)，其中 CTR_base 为基线点击率，k 为价格敏感度系数（

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

点击率 CTR 的衰减函数：CTR = CTR_base * exp(-k * ΔP/P_old)，其中 CTR_base 为基线点击率，k 为价格敏感度系数（二手市场通常 k ∈ [0.5, 1.5]），用于量化降价幅度对点击意愿的非线性影响。

## Corrected Claim

点击率 CTR 的衰减函数：CTR = CTR_base * exp(-k * ΔP/P_old)，其中 CTR_base 为基线点击率，k 为价格敏感度系数（二手市场通常 k ∈ [0.5, 1.5]），用于量化降价幅度对点击意愿的非线性影响。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

price sensitivity coefficient click through rate decay model
