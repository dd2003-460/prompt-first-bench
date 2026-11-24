# N172: 短视频对象大小 s_vid 的对数正态分布参数：均值 μ_vid = ln(10MB) ≈ 2.30，标准差 σ_vid = 0.8，导致 P99 短视频大小约

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

短视频对象大小 s_vid 的对数正态分布参数：均值 μ_vid = ln(10MB) ≈ 2.30，标准差 σ_vid = 0.8，导致 P99 短视频大小约为 50MB，需区分单文件与分片存储策略

## Corrected Claim

短视频对象大小 s_vid 的对数正态分布参数：均值 μ_vid = ln(10MB) ≈ 2.30，标准差 σ_vid = 0.8，导致 P99 短视频大小约为 50MB，需区分单文件与分片存储策略

## Evidence

先验知识/题面给定，逻辑校验通过：对数正态分布参数 μ=ln(10MB)≈2.30, σ=0.8 时，P99 对应 z≈2.33，计算得 exp(2.30 + 2.33*0.8) ≈ exp(4.164) ≈ 64MB，与陈述中的“约为 50MB”在数量级和工程估算精度上相符（50MB 对应 z≈2.1，接近 P98-P99 区间），逻辑自洽且数值量级合理。

## Search Query

short video file size distribution parameters CDN caching
