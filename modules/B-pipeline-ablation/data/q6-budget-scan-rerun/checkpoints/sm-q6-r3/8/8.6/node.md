# N301: 延迟分布长尾对 P99 的敏感度分析：假设核心用户延迟服从正态分布 $N(50, 10^2)$ ms，长尾用户延迟服从正态分布 $N(400, 50^2)$ m

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N99, N100, N101

## Claim

延迟分布长尾对 P99 的敏感度分析：假设核心用户延迟服从正态分布 $N(50, 10^2)$ ms，长尾用户延迟服从正态分布 $N(400, 50^2)$ ms。若长尾用户占比 $w_{tail}=0.2$，则整体 P99 延迟主要由长尾分布的上分位数决定。计算混合分布的 P99 需解方程 $0.8 * F_{core}(t) + 0.2 * F_{tail}(t) = 0.99$。

## Corrected Claim

延迟分布长尾对 P99 的敏感度分析：假设核心用户延迟服从正态分布 $N(50, 10^2)$ ms，长尾用户延迟服从正态分布 $N(400, 50^2)$ ms。若长尾用户占比 $w_{tail}=0.2$，则整体 P99 延迟主要由长尾分布的上分位数决定。计算混合分布的 P99 需解方程 $0.8 * F_{core}(t) + 0.2 * F_{tail}(t) = 0.99$。

## Evidence

先验知识/题面给定，逻辑校验通过：混合分布的分位数定义正确，方程 0.8*F_core(t) + 0.2*F_tail(t) = 0.99 符合概率论中混合分布CDF的性质，且P99确实由长尾分布主导（因长尾均值高且方差大，其上分位数远高于核心分布）。

## Search Query

mixed distribution percentile calculation
