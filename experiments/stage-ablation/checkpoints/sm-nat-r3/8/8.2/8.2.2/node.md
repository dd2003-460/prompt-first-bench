# N168: 驻留时间 W_i 的迭代求解方程：W_i = 1 / (Σ_{j≠i} λ_j * P(j 在 i 之前被访问且 i 未刷新))，在简化独立到达假设下，W_i 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N73

## Claim

驻留时间 W_i 的迭代求解方程：W_i = 1 / (Σ_{j≠i} λ_j * P(j 在 i 之前被访问且 i 未刷新))，在简化独立到达假设下，W_i ≈ 1 / (λ_i + λ_eviction_rate_i)，其中 λ_eviction_rate_i 由栈中更热门对象的总访问率决定，需通过数值迭代求解 W_i 与 K_eff 的耦合关系。

## Corrected Claim

驻留时间 W_i 的迭代求解方程：W_i = 1 / (Σ_{j≠i} λ_j * P(j 在 i 之前被访问且 i 未刷新))，在简化独立到达假设下，W_i ≈ 1 / (λ_i + λ_eviction_rate_i)，其中 λ_eviction_rate_i 由栈中更热门对象的总访问率决定，需通过数值迭代求解 W_i 与 K_eff 的耦合关系。

## Evidence

先验知识/题面给定，逻辑校验通过
