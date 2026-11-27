# N72: 有限总体 $N=10^5$ 下Pareto分布的归一化常数 $C_N = \sum_{i=1}^{N} i^{-\beta}$ 需通过积分近似 $C_N \ap

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N24

## Claim

有限总体 $N=10^5$ 下Pareto分布的归一化常数 $C_N = \sum_{i=1}^{N} i^{-\beta}$ 需通过积分近似 $C_N \approx \frac{N^{1-\beta}}{1-\beta} + \zeta(\beta)$ 计算，其中 $\zeta(0.9)$ 为黎曼zeta函数值，需查表或数值计算

## Corrected Claim

有限总体 $N=10^5$ 下Pareto分布的归一化常数 $C_N = \sum_{i=1}^{N} i^{-\beta}$ 需通过积分近似 $C_N \approx \frac{N^{1-\beta}}{1-\beta} + \zeta(\beta)$ 计算，其中 $\zeta(0.9)$ 为黎曼zeta函数值，需查表或数值计算

## Evidence

先验知识/题面给定，逻辑校验通过：该近似公式基于Euler-Maclaurin展开或积分近似，量纲与数学推导自洽，属于knowledge范畴。

## Search Query

Riemann zeta function value at 0.9
