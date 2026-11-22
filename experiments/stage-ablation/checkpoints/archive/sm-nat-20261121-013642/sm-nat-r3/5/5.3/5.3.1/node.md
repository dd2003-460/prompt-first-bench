# N73: 工作点3（联合分布）：在 ρ=-0.3 约束下，使用 Gaussian Copula 建模 size 和 freq 的联合分布，条件概率 P(size > s 

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

工作点3（联合分布）：在 ρ=-0.3 约束下，使用 Gaussian Copula 建模 size 和 freq 的联合分布，条件概率 P(size > s | freq > f) 需通过数值积分计算，以量化热门小对象在缓存中的实际占比

## Corrected Claim

工作点3（联合分布）：在 ρ=-0.3 约束下，使用 Gaussian Copula 建模 size 和 freq 的联合分布，条件概率 P(size > s | freq > f) 需通过数值积分计算，以量化热门小对象在缓存中的实际占比

## Evidence

先验知识/题面给定，逻辑校验通过：Gaussian Copula 是建模相关变量联合分布的标准方法，条件概率 P(A|B) 在连续变量下确实需通过积分计算，且 ρ=-0.3 符合负相关约束，逻辑自洽。
