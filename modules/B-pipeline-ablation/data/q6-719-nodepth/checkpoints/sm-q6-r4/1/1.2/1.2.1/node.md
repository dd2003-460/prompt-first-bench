# N52: 公有云 CDN 单请求 P99 延迟的构成公式：P99_public = P99(RTT_user_edge) + P99(T_proc_edge) + P99

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

公有云 CDN 单请求 P99 延迟的构成公式：P99_public = P99(RTT_user_edge) + P99(T_proc_edge) + P99(T_transfer_edge_to_client) + (1-H_L1)*P99(T_origin_fetch)，其中 H_L1 为 L1 缓存命中率。

## Corrected Claim

公有云 CDN 单请求 P99 延迟的构成公式：P99_public = P99(RTT_user_edge) + P99(T_proc_edge) + P99(T_transfer_edge_to_client) + (1-H_L1)*P99(T_origin_fetch)，其中 H_L1 为 L1 缓存命中率。

## Evidence

父节点级核验未通过：不完备（子节点覆盖了公式中的 RTT、处理时间和回源时间，但遗漏了父节点公式中明确包含的 'P99(T_transfer_edge_to_client)'（边缘节点到客户端的数据传输时间）这一项。此外，子节点3计算回源时间时仅考虑了RTT和传输时间，未严格对应P99分布，且未考虑H_L1为0时的边界情况，但主要缺陷在于完备性缺失。）

## Search Query

CDN P99 latency breakdown RTT processing transfer cache miss penalty
