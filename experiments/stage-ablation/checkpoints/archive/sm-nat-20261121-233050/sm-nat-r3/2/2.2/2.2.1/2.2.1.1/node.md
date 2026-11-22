# N97: 在 ρ=-0.3 的负相关约束下，基于频率排名 Top-K 对象的总大小 Sum_{i=1}^K S_i 的数值积分表达式：Sum_{i=1}^K S_i = 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

在 ρ=-0.3 的负相关约束下，基于频率排名 Top-K 对象的总大小 Sum_{i=1}^K S_i 的数值积分表达式：Sum_{i=1}^K S_i = N * E[S] * ∫_0^{K/N} Q_S(u | u_F ≤ K/N) du，其中 Q_S 为条件分位数函数，需通过 Gaussian Copula 求解。

## Corrected Claim

在 ρ=-0.3 的负相关约束下，基于频率排名 Top-K 对象的总大小 Sum_{i=1}^K S_i 的数值积分表达式：Sum_{i=1}^K S_i = N * E[S] * ∫_0^{K/N} Q_S(u | u_F ≤ K/N) du，其中 Q_S 为条件分位数函数，需通过 Gaussian Copula 求解。

## Evidence

先验知识/题面给定，逻辑校验通过：该表达式基于条件期望与积分定义，在负相关约束下通过Copula建模条件分布是标准且逻辑自洽的数学推导。
