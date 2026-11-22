# N162: 在 ρ=0（独立假设）下，W_s 的解析近似为 W_s ≈ E[S | S ≤ S_K] / E[S]，由于 Pareto(α=1.1) 均值发散，需截断至 S

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N58

## Claim

在 ρ=0（独立假设）下，W_s 的解析近似为 W_s ≈ E[S | S ≤ S_K] / E[S]，由于 Pareto(α=1.1) 均值发散，需截断至 S_max，若 S_K << S_max，则 W_s 显著小于 1，反映缓存中对象平均大小小于全局平均大小。

## Corrected Claim

在 ρ=0（独立假设）下，W_s 的解析近似为 W_s ≈ E[S | S ≤ S_K] / E[S]，由于 Pareto(α=1.1) 均值发散，需截断至 S_max，若 S_K << S_max，则 W_s 显著小于 1，反映缓存中对象平均大小小于全局平均大小。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto(α=1.1) 均值发散需截断，条件期望 E[S|S≤S_K] 在 S_K << S_max 时显著小于全局截断均值，推导自洽。
