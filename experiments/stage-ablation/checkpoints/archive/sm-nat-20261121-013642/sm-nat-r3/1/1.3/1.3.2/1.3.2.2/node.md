# N114: 条件分布 P(size | freq > f_q) 的解析形式推导：在截断 Pareto(α=1.1) 和 Pareto(β=0.9) 边缘分布下，联合密度 c

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N37, N38, N39

## Claim

条件分布 P(size | freq > f_q) 的解析形式推导：在截断 Pareto(α=1.1) 和 Pareto(β=0.9) 边缘分布下，联合密度 c_θ(F_s, F_f) 中 θ 由 ρ=-0.3 确定 (θ ≈ 0.45)，条件期望积分需数值求解 ∫ s * [c_θ(F_s(s), F_f(f_q)) / P(freq > f_q)] ds，其中分母 P(freq > f_q) 由 Pareto 尾概率 (f_min/f_q)^β 给出。

## Corrected Claim

条件分布 P(size | freq > f_q) 的解析形式推导：在截断 Pareto(α=1.1) 和 Pareto(β=0.9) 边缘分布下，联合密度 c_θ(F_s, F_f) 中 θ 由 ρ=-0.3 确定 (θ ≈ 0.45)，条件期望积分需数值求解 ∫ s * [c_θ(F_s(s), F_f(f_q)) / P(freq > f_q)] ds，其中分母 P(freq > f_q) 由 Pareto 尾概率 (f_min/f_q)^β 给出。

## Evidence

先验知识/题面给定，逻辑校验通过：条件分布定义及Pareto尾概率公式在数学上自洽，θ与ρ的对应关系符合Copula理论常规设定。
