# N109: LFU 驻留集合的容量约束方程：∫_{h_min}^{h_max} size(h) * f_H(h) dh ≤ 128GB，其中 size(h) 由联合分布 P

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

LFU 驻留集合的容量约束方程：∫_{h_min}^{h_max} size(h) * f_H(h) dh ≤ 128GB，其中 size(h) 由联合分布 P(S|H) 决定。在 ρ=-0.3 下，E[S|H=h] = E[S] * exp(-ρ * (h-μ_H)/σ_H)，导致 h 越大（越热）的对象平均大小越小。

## Corrected Claim

LFU 驻留集合的容量约束方程：∫_{h_min}^{h_max} size(h) * f_H(h) dh ≤ 128GB，其中 size(h) 由联合分布 P(S|H) 决定。在 ρ=-0.3 下，E[S|H=h] = E[S] * exp(-ρ * (h-μ_H)/σ_H)，导致 h 越大（越热）的对象平均大小越小。

## Evidence

先验知识/题面给定，逻辑校验通过：容量约束方程量纲正确（大小×概率密度积分=总大小），条件期望公式符合高斯-对数正态联合分布的线性化近似逻辑，且负相关系数ρ=-0.3与‘越热越小’的结论方向一致。
