# N355: 曝光倍数计算：基于 W(P) 计算 R_exposure = W(1.2*P_mkt)/W(P_mkt) = (1.2)^θ，需验证当 θ ∈ [1, 2] 时

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N113

## Claim

曝光倍数计算：基于 W(P) 计算 R_exposure = W(1.2*P_mkt)/W(P_mkt) = (1.2)^θ，需验证当 θ ∈ [1, 2] 时，R_exposure 是否大于 1.15（例如 θ=1 时 R=1.2>1.15）。

## Corrected Claim

曝光倍数计算：基于 W(P) 计算 R_exposure = W(1.2*P_mkt)/W(P_mkt) = (1.2)^θ，需验证当 θ ∈ [1, 2] 时，R_exposure 是否大于 1.15（例如 θ=1 时 R=1.2>1.15）。

## Evidence

先验知识/题面给定，逻辑校验通过：幂函数性质推导成立，θ∈[1,2]时(1.2)^θ≥1.2>1.15
