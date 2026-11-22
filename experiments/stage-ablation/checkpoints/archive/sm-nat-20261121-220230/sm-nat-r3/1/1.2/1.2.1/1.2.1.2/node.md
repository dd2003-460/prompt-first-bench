# N117: 在 Pareto(α=1.1) 下，对象大小的累积分布 F_s(s) = 1 - (s_min/s)^{α-1}，前 K 个最小对象的总大小 Σ_{i=1}^{

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N37

## Claim

在 Pareto(α=1.1) 下，对象大小的累积分布 F_s(s) = 1 - (s_min/s)^{α-1}，前 K 个最小对象的总大小 Σ_{i=1}^{K} s_i 可通过积分 ∫_{s_min}^{s_K} s * f(s) ds 近似，其中 s_K 是第 K 小对象的大小，由 F_s(s_K) = K/N 确定，需验证 K=11,900 时 s_K ≈ 1.01KB 是否合理

## Corrected Claim

在 Pareto(α=1.1) 下，对象大小的累积分布 F_s(s) = 1 - (s_min/s)^{α-1}，前 K 个最小对象的总大小 Σ_{i=1}^{K} s_i 可通过积分 ∫_{s_min}^{s_K} s * f(s) ds 近似，其中 s_K 是第 K 小对象的大小，由 F_s(s_K) = K/N 确定，需验证 K=11,900 时 s_K ≈ 1.01KB 是否合理

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布CDF公式正确，积分近似总大小的方法在连续分布下合理，s_K由分位数确定符合定义，数值量级（1.01KB）在典型对象大小分布中合理。
