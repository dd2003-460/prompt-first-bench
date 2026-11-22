# N241: 分析M_invalidation对最终命中率的非线性影响：若T_res较小（<5天），M_invalidation近似线性（≈1-λ*T_res）；若T_res

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N90

## Claim

分析M_invalidation对最终命中率的非线性影响：若T_res较小（<5天），M_invalidation近似线性（≈1-λ*T_res）；若T_res较大（>50天），需使用精确指数公式，并计算两种近似下的误差范围。

## Corrected Claim

分析M_invalidation对最终命中率的非线性影响：若T_res较小（<5天），M_invalidation近似线性（≈1-λ*T_res）；若T_res较大（>50天），需使用精确指数公式，并计算两种近似下的误差范围。

## Evidence

先验知识/题面给定，逻辑校验通过：指数衰减函数在自变量较小时可用一阶泰勒展开近似为线性，在自变量较大时需使用精确指数公式，符合数学原理。

## Search Query

Analyze linear approximation error of cache invalidation probability for small versus large residence times
