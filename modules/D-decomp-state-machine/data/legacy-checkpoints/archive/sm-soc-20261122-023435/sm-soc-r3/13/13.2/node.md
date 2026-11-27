# N261: 临界时间 T_critical 的推导：T_critical = σ_random / k_t。当 t > T_critical 时，Var(P_dir) > 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N85

## Claim

临界时间 T_critical 的推导：T_critical = σ_random / k_t。当 t > T_critical 时，Var(P_dir) > Var(ε_random)，挂价分布由随机噪声主导转为定向压力主导。以 σ_random ≈ 0.15 * P_ref 和 k_t ≈ 0.01 * P_ref /天 为例，T_critical ≈ 15 天。若市场流动性高（k_t 大），T_critical 缩短，意味着卖家更快被迫降价。

## Corrected Claim

临界时间 T_critical 的推导：T_critical = σ_random / k_t。当 t > T_critical 时，Var(P_dir) > Var(ε_random)，挂价分布由随机噪声主导转为定向压力主导。以 σ_random ≈ 0.15 * P_ref 和 k_t ≈ 0.01 * P_ref /天 为例，T_critical ≈ 15 天。若市场流动性高（k_t 大），T_critical 缩短，意味着卖家更快被迫降价。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 T_critical = σ_random / k_t 量纲一致（价格/价格速率=时间），数值代入 0.15/0.01=15 正确，且高流动性（k_t大）导致临界时间缩短符合经济直觉。

## Search Query

critical time price convergence variance ratio stochastic model
