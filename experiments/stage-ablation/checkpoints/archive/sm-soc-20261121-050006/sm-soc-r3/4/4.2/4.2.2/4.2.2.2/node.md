# N271: 尾部指数 α 的交互效应：当 α < 1.5 时，高估值买家比例 P(U > P_ask) 随 P_ask 下降速度变缓，导致高挂价（>P_median*1.2

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N84, N85, N86

## Claim

尾部指数 α 的交互效应：当 α < 1.5 时，高估值买家比例 P(U > P_ask) 随 P_ask 下降速度变缓，导致高挂价（>P_median*1.2）的匹配概率 p_match > 0.2，此时短周期主要由广泛匹配驱动而非长尾极端值。

## Corrected Claim

在特定尾部指数分布模型中，当 α < 1.5 时，高估值买家比例随挂价下降速度变缓，可能导致高挂价匹配概率维持在较高水平（如 > 0.2），进而影响匹配周期的驱动机制。

## Evidence

[质询]该陈述包含具体的经验性阈值（α < 1.5, P_ask > P_median*1.2, p_match > 0.2）和特定的因果机制（短周期由广泛匹配驱动），这些属于特定市场微观结构模型下的经验事实或模拟结果，无法从第一性原理或通用数学公理中严格推导出来。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该具体阈值与机制非通用物理/数学定律，不适用第一性原理推导条款）

## Search Query

Pareto tail index alpha effect on high price matching probability C2C
