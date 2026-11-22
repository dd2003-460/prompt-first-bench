# N46: Stale Fraction P_stale 的边界条件修正：当更新率 u 与驻留时间 T_avg_residency 的乘积 u*T_avg_residenc

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

Stale Fraction P_stale 的边界条件修正：当更新率 u 与驻留时间 T_avg_residency 的乘积 u*T_avg_residency < 0.1 时，P_stale ≈ u * T_avg_residency（线性近似）；在 u=0.01/天 和 T_avg_residency=1 小时（1/24 天）时，u*T_avg_residency = 0.0004，P_stale ≈ 0.04%，远低于 0.5%-1.5% 的估算值，表明在短驻留时间下缓存污染比例极低。

## Corrected Claim

Stale Fraction P_stale 的边界条件修正：当更新率 u 与驻留时间 T_avg_residency 的乘积 u*T_avg_residency < 0.1 时，P_stale ≈ u * T_avg_residency（线性近似）；在 u=0.01/天 和 T_avg_residency=1 小时（1/24 天）时，u*T_avg_residency = 0.0004，P_stale ≈ 0.04%，远低于 0.5%-1.5% 的估算值，表明在短驻留时间下缓存污染比例极低。

## Evidence

父节点级核验未通过：不完备（子节点之间存在逻辑依赖但主题正交（一个关注模型适用性/边界验证，另一个关注最终性能量化）。然而，完备性不足：父节点的核心论断是“在短驻留时间下缓存污染比例极低”，但子节点1直接指出该前提（T_avg=1小时）与另一节点（N68）矛盾，导致父节点结论被推翻，子节点2则基于推翻后的结论进行计算。分解未能涵盖“如何裁决 N46 与 N68 关于 T_avg 的矛盾”这一关键决策点，也未明确说明父节点结论在何种条件下才成立，导致逻辑链条断裂。）
