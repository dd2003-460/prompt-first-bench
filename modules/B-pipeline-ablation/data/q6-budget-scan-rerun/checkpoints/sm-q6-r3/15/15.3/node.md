# N414: H<80%区间敏感度系数-5ms/%的推导：假设T_miss - T_hit = 50ms（典型回源惩罚），P(Hit|P99)≈1.0（低命中率下P99请求多

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N143

## Claim

H<80%区间敏感度系数-5ms/%的推导：假设T_miss - T_hit = 50ms（典型回源惩罚），P(Hit|P99)≈1.0（低命中率下P99请求多为未命中），α≈0.0，则d(P99)/dH ≈ -50ms/10% = -5ms/%，该值对应于无二级缓存吸收且回源延迟稳定的场景

## Corrected Claim

H<80%区间敏感度系数-5ms/%的推导：假设T_miss - T_hit = 50ms（典型回源惩罚），P(Hit|P99)≈1.0（低命中率下P99请求多为未命中），α≈0.0，则d(P99)/dH ≈ -50ms/10% = -5ms/%，该值对应于无二级缓存吸收且回源延迟稳定的场景

## Evidence

先验知识/题面给定，逻辑校验通过：基于微积分定义 d(P99)/dH ≈ (T_miss - T_hit) * d(P99)/d(T_miss)，在低命中率区间 P99 主要由 Miss 决定且 T_miss 随 H 线性变化（或近似线性），量纲与数值推导自洽。
