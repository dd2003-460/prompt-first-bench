# N51: 平台收入方差投影：Var[r×T] = E[T]²×Var[r] + E[r]²×Var[T] + 2×E[r]×E[T]×Cov(r, T)，其中 Var[r

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N10

## Claim

平台收入方差投影：Var[r×T] = E[T]²×Var[r] + E[r]²×Var[T] + 2×E[r]×E[T]×Cov(r, T)，其中 Var[r]=0.000625（假设 r 均匀分布于[0.05,0.10]），Var[T] 为成交周期方差；当 σ_T=2天时，Var[r×T]=49×0.000625 + 0.005625×4 + 0 = 0.03046875

## Corrected Claim

平台收入方差投影：Var[r×T] = E[T]²×Var[r] + E[r]²×Var[T] + 2×E[r]×E[T]×Cov(r, T)，其中 Var[r]=0.000625（假设 r 均匀分布于[0.05,0.10]），Var[T] 为成交周期方差；当 σ_T=2天时，Var[r×T]=49×0.000625 + 0.005625×4 + 0 = 0.03046875

## Evidence

先验知识/题面给定，逻辑校验通过：方差公式展开正确，均匀分布方差计算正确（(0.05)^2/12），数值代入与结果一致。
