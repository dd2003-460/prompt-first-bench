# N521: 核心区域P99延迟 P99_core = RTT_core + T_proc + H_miss_core * (RTT_origin + T_transfer)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N172

## Claim

核心区域P99延迟 P99_core = RTT_core + T_proc + H_miss_core * (RTT_origin + T_transfer)，其中RTT_core为核心区域到POP的RTT，H_miss_core为核心区域缓存未命中率，需代入具体数值计算。

## Corrected Claim

核心区域P99延迟 P99_core = RTT_core + T_proc + H_miss_core * (RTT_origin + T_transfer)，其中RTT_core为核心区域到POP的RTT，H_miss_core为核心区域缓存未命中率，需代入具体数值计算。

## Evidence

先验知识/题面给定，逻辑校验通过
