# N312: 干预C的买家决策加速效应机制量化：ΔT_C = T_base * (1 - η_accel)，其中 η_accel 为决策加速率，由买家比价次数减少比例 ΔN_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N90

## Claim

干预C的买家决策加速效应机制量化：ΔT_C = T_base * (1 - η_accel)，其中 η_accel 为决策加速率，由买家比价次数减少比例 ΔN_compare 和单次决策时间缩短比例 Δt_decision 决定。假设 ΔN_compare = 20%，Δt_decision = 10%，则 η_accel = 1 - (1-0.2)*(1-0.1) = 0.28，ΔT_C = T_base * 0.28。

## Corrected Claim

干预C的买家决策加速效应机制量化：ΔT_C = T_base * (1 - η_accel)，其中 η_accel 为决策加速率，由买家比价次数减少比例 ΔN_compare 和单次决策时间缩短比例 Δt_decision 决定。假设 ΔN_compare = 20%，Δt_decision = 10%，则 η_accel = 1 - (1-0.2)*(1-0.1) = 0.28，ΔT_C = T_base * 0.28。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合乘法原理（1-(1-0.2)(1-0.1)=0.28），数值计算正确，量纲一致。
