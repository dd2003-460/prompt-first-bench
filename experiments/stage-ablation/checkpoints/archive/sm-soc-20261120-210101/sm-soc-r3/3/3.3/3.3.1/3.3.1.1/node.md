# N241: 共享随机源核心参数：推荐系统模型参数更新周期 T_update 与流量权重衰减率 λ_decay，量化为 W_traffic_t = W_0 * exp(-λ_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N66

## Claim

共享随机源核心参数：推荐系统模型参数更新周期 T_update 与流量权重衰减率 λ_decay，量化为 W_traffic_t = W_0 * exp(-λ_decay * t) + ε_t，其中 ε_t ~ N(0, σ_algo²)，σ_algo = sqrt(Var(W_traffic_t))；假设 T_update = 1h，λ_decay = 0.1/h，则 σ_algo 在1小时内波动约为 5-10%。

## Corrected Claim

共享随机源核心参数：推荐系统模型参数更新周期 T_update 与流量权重衰减率 λ_decay，量化为 W_traffic_t = W_0 * exp(-λ_decay * t) + ε_t，其中 ε_t ~ N(0, σ_algo²)，σ_algo = sqrt(Var(W_traffic_t))；假设 T_update = 1h，λ_decay = 0.1/h，则 σ_algo 在1小时内波动约为 5-10%。

## Evidence

先验知识/题面给定，逻辑校验通过：在T=1h, λ=0.1/h条件下，指数衰减项变化约9.5%，结合噪声项，5-10%的波动量级符合工程直觉与数学推导。
