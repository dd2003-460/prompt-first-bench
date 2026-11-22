# N142: 热度阈值 F_th 的选取标准：为使 K_ρ 反映'热门对象'对缓存容量的净效应，F_th 应取使得 P(F > F_th) = 0.1（即 Top 10% 热

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N54

## Claim

热度阈值 F_th 的选取标准：为使 K_ρ 反映'热门对象'对缓存容量的净效应，F_th 应取使得 P(F > F_th) = 0.1（即 Top 10% 热度）的分位数，对应 Pareto(β=0.9) 的 CDF 反函数 F_th = x_min_F * (0.1)^(-1/(β-1))，该阈值决定了条件期望的积分下限。

## Corrected Claim

热度阈值 F_th 的选取标准：为使 K_ρ 反映'热门对象'对缓存容量的净效应，F_th 应取使得 P(F > F_th) = 0.1（即 Top 10% 热度）的分位数，对应 Pareto(β=0.9) 的 CDF 反函数 F_th = x_min_F * (0.1)^(-1/(β-1))，该阈值决定了条件期望的积分下限。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布CDF反函数公式正确，Top 10%分位数定义与积分下限逻辑自洽
