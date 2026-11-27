# N266: 近期同品类成交均价 C_ref 的时间窗口设定为 30 天，即 C_ref = (1/30) * Σ P_i * w_i，w_i 为按时间衰减的权重，w_i =

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N88

## Claim

近期同品类成交均价 C_ref 的时间窗口设定为 30 天，即 C_ref = (1/30) * Σ P_i * w_i，w_i 为按时间衰减的权重，w_i = e^(-λ * t_i)，λ = 0.1/天

## Corrected Claim

近期同品类成交均价 C_ref 的时间窗口设定为 30 天，即 C_ref = (1/30) * Σ P_i * w_i，w_i 为按时间衰减的权重，w_i = e^(-λ * t_i)，λ = 0.1/天

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

reference price calculation with time-decay weighting in e-commerce
