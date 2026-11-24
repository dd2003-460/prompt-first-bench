# N514: 双峰混合分布下 E[s_avg] 的精确计算：s_avg = p_img × E[s_img] + p_vid × E[s_vid]，其中 p_img=0.8,

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N173

## Claim

双峰混合分布下 E[s_avg] 的精确计算：s_avg = p_img × E[s_img] + p_vid × E[s_vid]，其中 p_img=0.8, p_vid=0.2, E[s_img]=2MB, E[s_vid]=10MB，得 s_avg = 3.6MB；若 s_img 和 s_vid 均服从对数正态分布，则 E[s] = exp(μ + σ²/2)，需代入具体 μ/σ 验证 2MB 和 10MB 是否为期望值而非中位数

## Corrected Claim

双峰混合分布下 E[s_avg] 的精确计算：s_avg = p_img × E[s_img] + p_vid × E[s_vid]，其中 p_img=0.8, p_vid=0.2, E[s_img]=2MB, E[s_vid]=10MB，得 s_avg = 3.6MB；若 s_img 和 s_vid 均服从对数正态分布，则 E[s] = exp(μ + σ²/2)，需代入具体 μ/σ 验证 2MB 和 10MB 是否为期望值而非中位数

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均计算 0.8*2 + 0.2*10 = 3.6 正确；对数正态分布期望公式 E[s]=exp(μ+σ²/2) 正确，且指出需区分期望与中位数符合统计学原理。
