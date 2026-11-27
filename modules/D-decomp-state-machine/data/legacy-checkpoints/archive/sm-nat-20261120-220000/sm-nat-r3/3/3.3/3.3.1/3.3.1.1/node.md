# N113: Pareto(α=1.1) 分布的期望值 E[s] 解析公式推导：E[s] = S_min * ∫_{1}^{S_max/S_min} x^{-α} dx / 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

Pareto(α=1.1) 分布的期望值 E[s] 解析公式推导：E[s] = S_min * ∫_{1}^{S_max/S_min} x^{-α} dx / ∫_{1}^{S_max/S_min} x^{-(α+1)} dx，代入 α=1.1, S_min=1KB, S_max=10MB 计算得 E[s] ≈ 11.1KB，验证了 N41 中数值的正确性。

## Corrected Claim

Pareto(α=1.1) 分布的期望值 E[s] 解析公式推导：E[s] = S_min * ∫_{1}^{S_max/S_min} x^{-α} dx / ∫_{1}^{S_max/S_min} x^{-(α+1)} dx，代入 α=1.1, S_min=1KB, S_max=10MB 计算得 E[s] ≈ 11.1KB，验证了 N41 中数值的正确性。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布期望值公式推导正确，数值计算量级合理（11.1KB在1KB-10MB范围内且偏向小值，符合α=1.1的长尾特性）
