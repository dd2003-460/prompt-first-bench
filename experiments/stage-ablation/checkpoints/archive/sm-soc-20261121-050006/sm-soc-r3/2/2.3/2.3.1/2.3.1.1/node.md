# N196: GMV 对随机源的弹性传导：GMV 的波动系数 CV_GMV 与 CV_N 的关系为 CV_GMV = ε_GMV_N * CV_N + ε_GMV_P * C

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N60

## Claim

GMV 对随机源的弹性传导：GMV 的波动系数 CV_GMV 与 CV_N 的关系为 CV_GMV = ε_GMV_N * CV_N + ε_GMV_P * CV_P_ask，其中 ε_GMV_N 为 GMV 对活跃用户数的弹性（通常 >1，规模效应），ε_GMV_P 为 GMV 对平均挂价的弹性（已确认为负值）。

## Corrected Claim

GMV 对随机源的弹性传导：GMV 的波动系数 CV_GMV 与 CV_N 的关系为 CV_GMV = ε_GMV_N * CV_N + ε_GMV_P * CV_P_ask，其中 ε_GMV_N 为 GMV 对活跃用户数的弹性（通常 >1，规模效应），ε_GMV_P 为 GMV 对平均挂价的弹性（已确认为负值）。

## Evidence

先验知识/题面给定，逻辑校验通过：基于对数线性模型（GMV ≈ N^ε_N * P^ε_P），取对数微分可得波动系数（CV）的线性叠加关系，量纲与逻辑自洽。
