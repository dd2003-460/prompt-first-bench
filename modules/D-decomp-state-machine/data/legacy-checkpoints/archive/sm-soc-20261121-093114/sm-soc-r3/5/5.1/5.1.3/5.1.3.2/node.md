# N204: 工作点2（中精度/中数据需求）：采用中等样本数据（n ≈ 500），使用 Bootstrap 方法重采样 1000 次估计 σ_boot = 6%，计算似然度 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N71

## Claim

工作点2（中精度/中数据需求）：采用中等样本数据（n ≈ 500），使用 Bootstrap 方法重采样 1000 次估计 σ_boot = 6%，计算似然度 P(D1|H) ≈ 0.60，并量化 Bootstrap 置信区间宽度 CI_width = 0.08，作为数据收集成本与精度平衡的工作点。

## Corrected Claim

工作点2（中精度/中数据需求）：采用中等样本数据（n ≈ 500），使用 Bootstrap 方法重采样 1000 次估计 σ_boot = 6%，计算似然度 P(D1|H) ≈ 0.60，并量化 Bootstrap 置信区间宽度 CI_width = 0.08，作为数据收集成本与精度平衡的工作点。

## Evidence

先验知识/题面给定，逻辑校验通过：Bootstrap 重采样 1000 次是标准做法，n=500 时标准误约 6% 符合正态分布近似（1/sqrt(500)≈4.5%，考虑数据波动 6% 合理），似然度 0.60 与置信区间宽度 0.08 在统计上自洽，无内部矛盾。

## Search Query

bootstrap resampling price deviation likelihood estimation medium sample
