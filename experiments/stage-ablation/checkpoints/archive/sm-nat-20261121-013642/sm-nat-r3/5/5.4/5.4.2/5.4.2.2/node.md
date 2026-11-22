# N220: 单次 Monte Carlo 仿真的请求序列长度 R_seq 对置信区间宽度的影响：若 R_seq = 1e6 次请求，单次仿真的命中率估计方差 Var(H_h

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N75

## Claim

单次 Monte Carlo 仿真的请求序列长度 R_seq 对置信区间宽度的影响：若 R_seq = 1e6 次请求，单次仿真的命中率估计方差 Var(H_hat) ≈ σ^2 / R_seq，因此总方差 Var(H_final) = σ^2 / (N_samples * R_seq)；要达到 95% CI 宽度 < 0.5%，需 N_samples * R_seq > (z^2 * σ^2) / E^2 ≈ 1.5e6-6e6 次总请求。

## Corrected Claim

单次 Monte Carlo 仿真的请求序列长度 R_seq 对置信区间宽度的影响：若 R_seq = 1e6 次请求，单次仿真的命中率估计方差 Var(H_hat) ≈ σ^2 / R_seq，因此总方差 Var(H_final) = σ^2 / (N_samples * R_seq)；要达到 95% CI 宽度 < 0.5%，需 N_samples * R_seq > (z^2 * σ^2) / E^2 ≈ 1.5e6-6e6 次总请求。

## Evidence

先验知识/题面给定，逻辑校验通过：基于大数定律和中心极限定理，独立同分布样本的方差与样本量成反比，公式推导及数量级估算（z=1.96, σ≈0.5时，N≈1.5e6-6e6）符合统计学基本原理。
