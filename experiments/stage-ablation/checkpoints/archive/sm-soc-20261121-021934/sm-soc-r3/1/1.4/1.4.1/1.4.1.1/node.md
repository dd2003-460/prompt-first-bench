# N79: w_anchor 的估计需通过 OLS 回归 V_bid = β0 + β1*P_rec + β2*V_intrinsic + ε 获得，其中 β1 即为 w_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N32

## Claim

w_anchor 的估计需通过 OLS 回归 V_bid = β0 + β1*P_rec + β2*V_intrinsic + ε 获得，其中 β1 即为 w_anchor，标准误 SE(β1) = σ_ε / (√(Σ(P_rec - P̄_rec)²))，用于判断 [0.7, 0.9] 区间的统计显著性

## Corrected Claim

w_anchor 的估计需通过 OLS 回归 V_bid = β0 + β1*P_rec + β2*V_intrinsic + ε 获得，其中 β1 即为 w_anchor，标准误 SE(β1) = σ_ε / (√(Σ(P_rec - P̄_rec)²))，用于判断 [0.7, 0.9] 区间的统计显著性

## Evidence

先验知识/题面给定，逻辑校验通过：OLS回归中斜率系数的标准误公式推导正确，量纲与统计定义自洽。
