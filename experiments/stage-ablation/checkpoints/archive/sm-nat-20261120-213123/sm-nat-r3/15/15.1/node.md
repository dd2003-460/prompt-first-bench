# N195: LFU 识别新对象达到稳态命中率所需的请求窗口 T_lag 的解析推导：基于指数衰减计数器模型，频率计数 F(t) 收敛到稳态值 λ 的 95% 所需时间 T_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N84

## Claim

LFU 识别新对象达到稳态命中率所需的请求窗口 T_lag 的解析推导：基于指数衰减计数器模型，频率计数 F(t) 收敛到稳态值 λ 的 95% 所需时间 T_lag = -ln(0.05) / (u_eff + λ) ≈ 3.0 / (u_eff + λ)，其中 λ 为新对象的请求率（次/秒），u_eff 为计数器衰减率。

## Corrected Claim

LFU 识别新对象达到稳态命中率所需的请求窗口 T_lag 的解析推导：基于指数衰减计数器模型，频率计数 F(t) 收敛到稳态值 λ 的 95% 所需时间 T_lag = -ln(0.05) / (u_eff + λ) ≈ 3.0 / (u_eff + λ)，其中 λ 为新对象的请求率（次/秒），u_eff 为计数器衰减率。

## Evidence

先验知识/题面给定，逻辑校验通过：指数衰减模型 F(t) = λ(1 - e^{-(u_eff+λ)t}) 收敛至 95% 稳态值的时间推导符合微积分基本定理，数值量级合理。

## Search Query

LFU frequency counter convergence time exponential decay
