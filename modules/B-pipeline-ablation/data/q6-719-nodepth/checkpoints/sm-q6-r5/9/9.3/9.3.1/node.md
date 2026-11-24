# N371: 二次增长区间的数学定义：当 T_target ≤ L_p99 < T_threshold 时，C_penalty = k2 × (L_p99 - T_targe

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N126

## Claim

二次增长区间的数学定义：当 T_target ≤ L_p99 < T_threshold 时，C_penalty = k2 × (L_p99 - T_target)^2。系数 k2 需通过校准确定，使得在 L_p99 = T_threshold 时，C_penalty 的导数与线性区间的斜率连续，或与指数区间的起点值连续。通常 k2 = 2 × Lambda × (T_threshold - T_target) 以简化计算，或基于用户投诉率曲线拟合。

## Corrected Claim

二次增长区间的数学定义：当 T_target ≤ L_p99 < T_threshold 时，C_penalty = k2 × (L_p99 - T_target)^2。系数 k2 需通过校准确定，使得在 L_p99 = T_threshold 时，C_penalty 的导数与线性区间的斜率连续，或与指数区间的起点值连续。通常 k2 = 2 × Lambda × (T_threshold - T_target) 以简化计算，或基于用户投诉率曲线拟合。

## Evidence

先验知识/题面给定，逻辑校验通过：二次函数在边界处导数连续的条件推导正确，k2公式符合数学定义。

## Search Query

non-linear penalty function latency threshold quadratic growth model
