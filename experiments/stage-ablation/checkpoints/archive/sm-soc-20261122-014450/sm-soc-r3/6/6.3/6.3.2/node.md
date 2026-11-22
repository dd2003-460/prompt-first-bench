# N358: 临界阈值推导：将 Q(1.2*P_mkt) = Q(P_mkt) * (1.2)^ε 代入不等式，解得 R_exposure > [(1.2*P_mkt - C

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N114

## Claim

临界阈值推导：将 Q(1.2*P_mkt) = Q(P_mkt) * (1.2)^ε 代入不等式，解得 R_exposure > [(1.2*P_mkt - C) / (P_mkt - C)] * (1.2)^ε，量化右侧数值以确定 R 的最小值。

## Corrected Claim

临界阈值推导：将 Q(1.2*P_mkt) = Q(P_mkt) * (1.2)^ε 代入不等式，解得 R_exposure > [(1.2*P_mkt - C) / (P_mkt - C)] * (1.2)^ε，量化右侧数值以确定 R 的最小值。

## Evidence

先验知识/题面给定，逻辑校验通过：该推导基于标准的需求弹性定义 Q(P) = Q(P0) * (P/P0)^ε 及利润/曝光量不等式的代数变换，量纲与逻辑自洽。
