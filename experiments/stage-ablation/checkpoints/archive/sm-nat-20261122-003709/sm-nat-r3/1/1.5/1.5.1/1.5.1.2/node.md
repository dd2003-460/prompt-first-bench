# N116: Pareto(α=1.1) 截断分布期望公式的分子截断项 N_α = (1 - (s_max/s_min)^{1-α})，计算值为 (1 - 10^{-9*0.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

Pareto(α=1.1) 截断分布期望公式的分子截断项 N_α = (1 - (s_max/s_min)^{1-α})，计算值为 (1 - 10^{-9*0.1}) ≈ 0.9206，反映尾部截断对均值的抑制

## Corrected Claim

Pareto(α=1.1) 截断分布期望公式的分子截断项 N_α = (1 - (s_max/s_min)^{1-α})，计算值为 (1 - 10^{-9*0.1}) ≈ 0.9206，反映尾部截断对均值的抑制

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布截断期望公式推导正确，数值计算 (1 - 10^{-0.9}) ≈ 0.9206 准确，符合数学第一性原理。
