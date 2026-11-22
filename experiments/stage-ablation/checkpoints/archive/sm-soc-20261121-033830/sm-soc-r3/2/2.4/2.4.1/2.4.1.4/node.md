# N170: 边界条件：当 λ_b(P_high) * E[t_response] < 0.1 时，积分近似为 λ_b(P_high) * E[t_response]，此时响

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

边界条件：当 λ_b(P_high) * E[t_response] < 0.1 时，积分近似为 λ_b(P_high) * E[t_response]，此时响应速度 v_high 对成交概率的边际贡献趋近于线性，非线性效应可忽略。

## Corrected Claim

边界条件：当 λ_b(P_high) * E[t_response] < 0.1 时，积分近似为 λ_b(P_high) * E[t_response]，此时响应速度 v_high 对成交概率的边际贡献趋近于线性，非线性效应可忽略。

## Evidence

先验知识/题面给定，逻辑校验通过：当泊松过程参数 λt 远小于 1 时，概率 P(N≥1) = 1 - e^(-λt) ≈ λt，符合泰勒展开一阶近似原理，非线性项 (λt)^2/2 可忽略。

## Search Query

small lambda response time linear approximation boundary condition
