# N31: Gaussian Copula 下，给定边缘分布 F_S, F_R 和 Pearson 相关系数 ρ=-0.3，联合 CDF 为 C(u,v) = Φ_2(u,

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

Gaussian Copula 下，给定边缘分布 F_S, F_R 和 Pearson 相关系数 ρ=-0.3，联合 CDF 为 C(u,v) = Φ_2(u, v; ρ)，其中 Φ_2 是二元标准正态 CDF，该结构允许直接计算联合概率密度 f(S,R) = f_S(S) * f_R(R) * c(F_S(S), F_R(R))

## Corrected Claim

Gaussian Copula 下，给定边缘分布 F_S, F_R 和 Pearson 相关系数 ρ=-0.3，联合 CDF 为 C(u,v) = Φ_2(u, v; ρ)，其中 Φ_2 是二元标准正态 CDF，该结构允许直接计算联合概率密度 f(S,R) = f_S(S) * f_R(R) * c(F_S(S), F_R(R))

## Evidence

父节点级核验未通过：不完备（子节点1关注联合密度函数的具体数学表达式及系数量化，子节点2关注条件概率偏移对策略的影响，两者角度不同（密度函数 vs 条件概率/策略影响），故正交且无冗余。但父节点核心是描述Gaussian Copula结构及其允许直接计算联合概率密度（f(S,R)），子节点1虽然给出了密度公式，但遗漏了Copula函数C(u,v)本身的定义或性质（如Sklar定理的应用前提），且子节点2偏向应用层（缓存策略），未完全覆盖父节点中关于“联合CDF结构”这一基础数学定义的完整性。）

## Search Query

Gaussian Copula joint distribution formula Pearson correlation
