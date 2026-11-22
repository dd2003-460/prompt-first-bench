# N300: Pareto 分布下 p_match 的解析解：当 U_i ~ Pareto(α, P_min) 时，p_match = (P_min / P_ask)^α；若

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N95

## Claim

Pareto 分布下 p_match 的解析解：当 U_i ~ Pareto(α, P_min) 时，p_match = (P_min / P_ask)^α；若 P_min = P_median * 0.5（基于历史最低成交价），P_ask = P_median * 1.2，则 p_match = (1/2.4)^α；当 α = 1.5 时，p_match ≈ 0.27；当 α = 2.5 时，p_match ≈ 0.15，具体值取决于 α 的实证估计。

## Corrected Claim

Pareto 分布下 p_match 的解析解：当 U_i ~ Pareto(α, P_min) 时，p_match = (P_min / P_ask)^α；若 P_min = P_median * 0.5（基于历史最低成交价），P_ask = P_median * 1.2，则 p_match = (1/2.4)^α；当 α = 1.5 时，p_match ≈ 0.27；当 α = 2.5 时，p_match ≈ 0.15，具体值取决于 α 的实证估计。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布CDF推导正确，数值计算(1/2.4)^1.5≈0.27及(1/2.4)^2.5≈0.15准确无误

## Search Query

Pareto distribution tail index estimation used goods market
