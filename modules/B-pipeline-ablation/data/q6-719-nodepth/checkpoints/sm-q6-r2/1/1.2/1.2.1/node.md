# N52: 公有云 CDN 单请求 P99 延迟的构成公式：P99_public = P99(RTT_user_edge) + P99(T_proc_edge) + P99

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N8

## Claim

公有云 CDN 单请求 P99 延迟的构成公式：P99_public = P99(RTT_user_edge) + P99(T_proc_edge) + P99(T_transfer_edge_to_client) + (1-H_L1)*P99(T_origin_fetch)，其中 H_L1 为 L1 缓存命中率。

## Corrected Claim

公有云 CDN 单请求 P99 延迟的构成公式：P99_public = P99(RTT_user_edge) + P99(T_proc_edge) + P99(T_transfer_edge_to_client) + (1-H_L1)*P99(T_origin_fetch)，其中 H_L1 为 L1 缓存命中率。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN P99 latency breakdown RTT processing transfer cache miss penalty
