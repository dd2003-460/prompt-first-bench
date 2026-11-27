# N293: 在混合更新工作点下，D_update = 1 - (Σ p_i s_i (1 - exp(-λ_i * T_i))) / (Σ p_i s_i)，其中 λ_i 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N103

## Claim

在混合更新工作点下，D_update = 1 - (Σ p_i s_i (1 - exp(-λ_i * T_i))) / (Σ p_i s_i)，其中 λ_i ∝ r_i^0.9，需通过数值积分计算加权平均失效概率，估计 D_update 介于 0.9963 与 0.99959 之间。

## Corrected Claim

在混合更新工作点下，D_update = 1 - (Σ p_i s_i (1 - exp(-λ_i * T_i))) / (Σ p_i s_i)，其中 λ_i ∝ r_i^0.9，需通过数值积分计算加权平均失效概率，估计 D_update 介于 0.9963 与 0.99959 之间。

## Evidence

先验知识/题面给定，逻辑校验通过
