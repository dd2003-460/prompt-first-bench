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

父节点级核验通过：正交+完备+无冗余（子节点之间逻辑清晰且相互独立：子节点1负责验证父节点中关于P99数值的内部一致性（指出27.8MB与50MB的矛盾），子节点2和3分别针对两种不同的存储策略（单文件vs分片）建立带宽/延迟模型，子节点4探讨缓存命中率这一独立维度。四个节点覆盖了父节点提及的‘分布参数’、‘P99大小’、‘单文件策略’、‘分片策略’及‘策略区分’的所有关键方面，无重复或矛盾，且各自代表独立的建模维度，不构成冗余。）

## Search Query

short video file size distribution parameters CDN caching
