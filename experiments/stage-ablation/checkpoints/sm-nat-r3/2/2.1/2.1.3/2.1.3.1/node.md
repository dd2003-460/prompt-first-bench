# N141: 在理想归一化工作点下，分母项 Σ_{all} p_i · s_i = E[S] * Σ p_i = E[S] * 1，其中 E[S] 为 Pareto(α=1.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

在理想归一化工作点下，分母项 Σ_{all} p_i · s_i = E[S] * Σ p_i = E[S] * 1，其中 E[S] 为 Pareto(α=1.1, x_min=1KB) 的期望大小，需数值积分计算 E[S] 以量化分母。

## Corrected Claim

在理想归一化工作点下，分母项 Σ_{all} p_i · s_i = E[S] * Σ p_i = E[S] * 1，其中 E[S] 为 Pareto(α=1.1, x_min=1KB) 的期望大小，需数值积分计算 E[S] 以量化分母。

## Evidence

先验知识/题面给定，逻辑校验通过：期望的线性性质 E[Σp_i s_i] = Σp_i E[s_i] 在独立假设下成立，且 Pareto 分布期望公式 E[S] = αx_min/(α-1) 在 α>1 时收敛，数值积分需求合理。
