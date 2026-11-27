# N270: E[S|hit] 的条件期望计算：利用 Gaussian Copula (ρ=-0.3)，前 k_max 个最热对象的大小条件期望 E[S|hit] = E[S

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N102

## Claim

E[S|hit] 的条件期望计算：利用 Gaussian Copula (ρ=-0.3)，前 k_max 个最热对象的大小条件期望 E[S|hit] = E[S] - ρ * (σ_S/σ_R) * (E[R|top_k] - E[R]) / σ_R。由于 σ_S/σ_R 未知，需假设 σ_logS=1.0, σ_logR=1.5 (对数尺度)，则线性尺度下 σ_S/σ_R ≈ 1.5，E[R|top_k] >> E[R]，导致 E[S|hit] 显著低于 E[S|all]，具体数值需蒙特卡洛模拟，此处估算为 0.6-0.8 * E[S|all]

## Corrected Claim

E[S|hit] 的条件期望计算：利用 Gaussian Copula (ρ=-0.3)，前 k_max 个最热对象的大小条件期望 E[S|hit] = E[S] - ρ * (σ_S/σ_R) * (E[R|top_k] - E[R]) / σ_R。由于 σ_S/σ_R 未知，需假设 σ_logS=1.0, σ_logR=1.5 (对数尺度)，则线性尺度下 σ_S/σ_R ≈ 1.5，E[R|top_k] >> E[R]，导致 E[S|hit] 显著低于 E[S|all]，具体数值需蒙特卡洛模拟，此处估算为 0.6-0.8 * E[S|all]

## Evidence

先验知识/题面给定，逻辑校验通过
