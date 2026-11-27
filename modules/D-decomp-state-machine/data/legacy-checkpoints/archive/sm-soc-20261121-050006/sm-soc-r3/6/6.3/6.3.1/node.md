# N312: 在 Pareto 重尾分布假设下，p_match = 1 - F_U(P_ask) 的具体计算形式为 (P_min / P_ask)^α，其中 P_min 为市

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N100

## Claim

在 Pareto 重尾分布假设下，p_match = 1 - F_U(P_ask) 的具体计算形式为 (P_min / P_ask)^α，其中 P_min 为市场最低可接受价格，α 为尾部指数；当 P_ask 位于第 80-90 百分位时，需结合 α ∈ [1.5, 2.5] 区间计算具体的匹配概率范围。

## Corrected Claim

在 Pareto 重尾分布假设下，p_match = 1 - F_U(P_ask) 的具体计算形式为 (P_min / P_ask)^α，其中 P_min 为市场最低可接受价格，α 为尾部指数；当 P_ask 位于第 80-90 百分位时，需结合 α ∈ [1.5, 2.5] 区间计算具体的匹配概率范围。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布的生存函数（Complementary CDF）在尾部确实表现为 (x_m/x)^α 的形式，其中 x_m 为最小值（此处对应 P_min），α 为形状参数（尾部指数）。当 P_ask 位于高分位时，匹配概率 p_match 即为该生存函数值，逻辑与数学定义自洽。
