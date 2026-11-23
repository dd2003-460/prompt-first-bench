# N32: 三种策略的加权P99延迟公式：P99_strategy = Σ (w_i × P99_i)，其中w_i为各区域/路径流量占比，P99_i为该路径的P99延迟；全

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N5

## Claim

三种策略的加权P99延迟公式：P99_strategy = Σ (w_i × P99_i)，其中w_i为各区域/路径流量占比，P99_i为该路径的P99延迟；全公有云：P99 = P99_cloud；全自建：P99 = P99_self；混合：P99 = 0.65×P99_self + 0.35×P99_cloud（基于N12比例）

## Corrected Claim

三种策略的加权P99延迟公式：P99_strategy = Σ (w_i × P99_i)，其中w_i为各区域/路径流量占比，P99_i为该路径的P99延迟；全公有云：P99 = P99_cloud；全自建：P99 = P99_self；混合：P99 = 0.65×P99_self + 0.35×P99_cloud（基于N12比例）

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

weighted P99 latency calculation hybrid CDN strategy
