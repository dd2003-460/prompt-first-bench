# N63: 请求到达率λ的计算：λ = (DAU * req_per_user_per_day) / 86400 * Burst_Factor，其中DAU=5,000,00

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N11

## Claim

请求到达率λ的计算：λ = (DAU * req_per_user_per_day) / 86400 * Burst_Factor，其中DAU=5,000,000，req_per_user_per_day为每用户日均请求数（图片+短视频平台典型值20-50次），Burst_Factor为峰值突发系数（典型1.5-3.0，反映早晚高峰），计算得λ ≈ 17-87 req/s（全量）或按POP分摊。

## Corrected Claim

请求到达率λ的计算：λ = (DAU * req_per_user_per_day) / 86400 * Burst_Factor，其中DAU=5,000,000，req_per_user_per_day为每用户日均请求数（图片+短视频平台典型值20-50次），Burst_Factor为峰值突发系数（典型1.5-3.0，反映早晚高峰），计算得λ ≈ 17-87 req/s（全量）或按POP分摊。
