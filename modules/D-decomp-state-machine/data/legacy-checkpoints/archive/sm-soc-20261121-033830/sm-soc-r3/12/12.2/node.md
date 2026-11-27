# N357: 最优策略价格 P*_i 的估计误差 δ_P* 对 σ_noise 计算的影响：P*_i 并非已知常数，而是通过回归模型估计得到，存在估计误差 δ_P*。观测到的

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N113

## Claim

最优策略价格 P*_i 的估计误差 δ_P* 对 σ_noise 计算的影响：P*_i 并非已知常数，而是通过回归模型估计得到，存在估计误差 δ_P*。观测到的噪声 σ_obs = std(P_i - P*_i_est) 包含真实随机噪声 σ_true 和估计误差 δ_P*，即 σ_obs^2 ≈ σ_true^2 + Var(δ_P*)。需通过交叉验证估计 Var(δ_P*)，从而分离出真实的随机偏好噪声强度 σ_true，避免高估噪声水平导致错误判断定向压力主导。

## Corrected Claim

最优策略价格 P*_i 的估计误差 δ_P* 对 σ_noise 计算的影响：P*_i 并非已知常数，而是通过回归模型估计得到，存在估计误差 δ_P*。观测到的噪声 σ_obs = std(P_i - P*_i_est) 包含真实随机噪声 σ_true 和估计误差 δ_P*，即 σ_obs^2 ≈ σ_true^2 + Var(δ_P*)。需通过交叉验证估计 Var(δ_P*)，从而分离出真实的随机偏好噪声强度 σ_true，避免高估噪声水平导致错误判断定向压力主导。

## Evidence

先验知识/题面给定，逻辑校验通过：基于误差传播定律，观测方差确实等于真实方差与估计误差方差之和，分离噪声的逻辑自洽且符合统计学基本原理。

## Search Query

estimation error in optimal pricing model impact on noise variance decomposition
