# N22: 不确定性量化：Hit_base 的 95% 置信区间为 [Hit_base - 1.96*σ, Hit_base + 1.96*σ]，其中 σ 由蒙特卡洛模拟 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

不确定性量化：Hit_base 的 95% 置信区间为 [Hit_base - 1.96*σ, Hit_base + 1.96*σ]，其中 σ 由蒙特卡洛模拟 1000 次请求序列得到

## Corrected Claim

不确定性量化：Hit_base 的 95% 置信区间为 [Hit_base - 1.96*σ, Hit_base + 1.96*σ]，其中 σ 由蒙特卡洛模拟 1000 次请求序列得到

## Evidence

先验知识/题面给定，逻辑校验通过：基于中心极限定理，大样本下正态分布近似成立，95%置信区间公式正确，蒙特卡洛模拟1000次为合理实验设计。
