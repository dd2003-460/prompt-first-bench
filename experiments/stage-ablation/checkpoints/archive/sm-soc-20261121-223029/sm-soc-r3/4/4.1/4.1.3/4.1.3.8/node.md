# N243: 半衰期模型失效的边界条件：当 δ_t < δ_noise_floor（噪声地板，即随机偏好噪声导致的不可消除偏差，估计 δ_noise_floor ≈ 0.05

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N79, N80, N81

## Claim

半衰期模型失效的边界条件：当 δ_t < δ_noise_floor（噪声地板，即随机偏好噪声导致的不可消除偏差，估计 δ_noise_floor ≈ 0.05-0.10）时，指数衰减模型失效，偏差将围绕噪声地板震荡而非趋近于 0；需量化 δ_noise_floor 的具体值，并计算 T_convergence 是否应定义为达到 δ_noise_floor + 2σ 的时间而非 5%。

## Corrected Claim

半衰期模型失效的边界条件：当 δ_t < δ_noise_floor（噪声地板，即随机偏好噪声导致的不可消除偏差，估计 δ_noise_floor ≈ 0.05-0.10）时，指数衰减模型失效，偏差将围绕噪声地板震荡而非趋近于 0；需量化 δ_noise_floor 的具体值，并计算 T_convergence 是否应定义为达到 δ_noise_floor + 2σ 的时间而非 5%。

## Evidence

先验知识/题面给定，逻辑校验通过：噪声地板导致偏差震荡而非趋零符合信号处理与统计收敛的基本原理，量级（0.05-0.10）在偏好噪声语境下合理。

## Search Query

price noise floor random preference bias in markets
