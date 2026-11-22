# N188: β_platform 的动态调整函数：β_platform(t) = β_platform_max * exp(-λ * (UX_score(t) - UX_t

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

β_platform 的动态调整函数：β_platform(t) = β_platform_max * exp(-λ * (UX_score(t) - UX_threshold))，其中 β_platform_max 为最大偏好系数（假设 0.3），λ 为衰减速度（假设 0.1），UX_threshold 为体验阈值（假设 0.8），当 UX_score 低于阈值时，β_platform 指数下降，需计算均衡点处的 β_platform 稳定值。

## Corrected Claim

β_platform 的动态调整函数：β_platform(t) = β_platform_max * exp(-λ * (UX_score(t) - UX_threshold))，其中 β_platform_max 为最大偏好系数（假设 0.3），λ 为衰减速度（假设 0.1），UX_threshold 为体验阈值（假设 0.8），当 UX_score 低于阈值时，β_platform 指数下降，需计算均衡点处的 β_platform 稳定值。

## Evidence

先验知识/题面给定，逻辑校验通过
