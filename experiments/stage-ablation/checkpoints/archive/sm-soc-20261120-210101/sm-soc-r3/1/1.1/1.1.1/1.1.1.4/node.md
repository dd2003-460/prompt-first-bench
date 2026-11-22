# N122: 下游投影3：信息不对称噪声项 Var(I_asym) 的量化公式，定义为 Var(I_asym) = k_info * Var(ε_market) * (1 -

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N30

## Claim

下游投影3：信息不对称噪声项 Var(I_asym) 的量化公式，定义为 Var(I_asym) = k_info * Var(ε_market) * (1 - μ_credit)，其中 k_info 为信息不对称系数（假设 k_info=0.4），μ_credit 为卖家信用分均值（来自 N108）。

## Corrected Claim

下游投影3：信息不对称噪声项 Var(I_asym) 的量化公式，定义为 Var(I_asym) = k_info * Var(ε_market) * (1 - μ_credit)，其中 k_info 为信息不对称系数（假设 k_info=0.4），μ_credit 为卖家信用分均值（来自 N108）。

## Evidence

先验知识/题面给定，逻辑校验通过
