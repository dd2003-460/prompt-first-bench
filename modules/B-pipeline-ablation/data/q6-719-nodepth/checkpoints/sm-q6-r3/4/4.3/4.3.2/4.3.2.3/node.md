# N357: 缓存未命中惩罚成本 C_miss_penalty 的具体构成：C_miss_penalty = (1 - HitRate) * Q_day * (C_bandw

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N110

## Claim

缓存未命中惩罚成本 C_miss_penalty 的具体构成：C_miss_penalty = (1 - HitRate) * Q_day * (C_bandwidth_public - C_bandwidth_self) + (1 - HitRate) * Q_day * T_latency_penalty_value，其中 T_latency_penalty_value 为每毫秒超标对应的业务损失或 SLA 罚款折算值。

## Corrected Claim

缓存未命中惩罚成本 C_miss_penalty 的具体构成：C_miss_penalty = (1 - HitRate) * Q_day * (C_bandwidth_public - C_bandwidth_self) + (1 - HitRate) * Q_day * T_latency_penalty_value，其中 T_latency_penalty_value 为每毫秒超标对应的业务损失或 SLA 罚款折算值。

## Evidence

先验知识/题面给定，逻辑校验通过
