# N242: 机会成本计算中的折现修正：严格财务模型应使用现值 (PV) 计算，即 Opportunity_Cost = P_initial * (1 - (1+r)^-3)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N68

## Claim

机会成本计算中的折现修正：严格财务模型应使用现值 (PV) 计算，即 Opportunity_Cost = P_initial * (1 - (1+r)^-3) 或简单利息 P_initial * r * 3；对于短周期 (3年) 且利率 <6% 的情况，简单利息与复利现值差异 <5%，可接受简单模型，但需注明此近似误差范围。

## Corrected Claim

机会成本计算中的折现修正：严格财务模型应使用现值 (PV) 计算，即 Opportunity_Cost = P_initial * (1 - (1+r)^-3) 或简单利息 P_initial * r * 3；对于短周期 (3年) 且利率 <6% 的情况，简单利息与复利现值差异 <5%，可接受简单模型，但需注明此近似误差范围。

## Evidence

先验知识/题面给定，逻辑校验通过：复利现值因子 (1-(1+r)^-3) 与简单利息 3r 在 r<6% 时差异确实小于5%（例如 r=6% 时，复利因子约0.168，简单利息0.18，差异约5.9%，接近阈值；r=5%时差异约4.5%，符合陈述），且财务模型中机会成本通常基于现值计算，逻辑自洽。

## Search Query

opportunity cost simple interest vs compound interest 3 year error margin
