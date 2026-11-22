# N174: 卖家伤害投影的共享随机源为曝光量下降 ΔE_seller，其标准误 SE_E 取决于对照组样本量 n_control 及曝光量的原始波动率 σ_E，计算公式为 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N58

## Claim

卖家伤害投影的共享随机源为曝光量下降 ΔE_seller，其标准误 SE_E 取决于对照组样本量 n_control 及曝光量的原始波动率 σ_E，计算公式为 SE_E = σ_E / sqrt(n_control)，用于确定 ΔE_seller 的置信区间。

## Corrected Claim

卖家伤害投影的共享随机源为曝光量下降 ΔE_seller，其标准误 SE_E 取决于对照组样本量 n_control 及曝光量的原始波动率 σ_E，计算公式为 SE_E = σ_E / sqrt(n_control)，用于确定 ΔE_seller 的置信区间。

## Evidence

先验知识/题面给定，逻辑校验通过：标准误公式 SE = σ/√n 符合统计学基本原理，量纲与逻辑自洽。
