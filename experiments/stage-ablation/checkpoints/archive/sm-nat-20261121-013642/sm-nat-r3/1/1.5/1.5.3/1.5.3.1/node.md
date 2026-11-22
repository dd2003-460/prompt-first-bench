# N133: 条件期望 E[r_i | s_i < s_threshold] 的解析表达式：在 Pareto 大小分布截断 s_max 下，E[r_i | s_i < s_t

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

条件期望 E[r_i | s_i < s_threshold] 的解析表达式：在 Pareto 大小分布截断 s_max 下，E[r_i | s_i < s_threshold] = ∫_{s_min}^{s_threshold} ∫_{r_min}^{∞} r * f_{r|s}(r|s) * f_s(s) dr ds / P(s_i < s_threshold)，其中 f_{r|s} 由 Copula 偏导数 ∂C(u,v)/∂v 给出。

## Corrected Claim

条件期望 E[r_i | s_i < s_threshold] 的解析表达式：在 Pareto 大小分布截断 s_max 下，E[r_i | s_i < s_threshold] = ∫_{s_min}^{s_threshold} ∫_{r_min}^{∞} r * f_{r|s}(r|s) * f_s(s) dr ds / P(s_i < s_threshold)，其中 f_{r|s} 由 Copula 偏导数 ∂C(u,v)/∂v 给出。

## Evidence

先验知识/题面给定，逻辑校验通过：条件期望的定义式正确，Copula 偏导数 ∂C(u,v)/∂v 确实给出条件密度 f_{r|s}，数学推导自洽。

## Search Query

conditional expectation given truncation Gaussian copula
