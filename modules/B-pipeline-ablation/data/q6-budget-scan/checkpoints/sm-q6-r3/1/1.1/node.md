# N7: P99延迟构成公式：L_P99 = max(T_cache_hit, T_cache_miss) 其中 T_cache_hit = RTT + T_proces

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

P99延迟构成公式：L_P99 = max(T_cache_hit, T_cache_miss) 其中 T_cache_hit = RTT + T_processing + T_queue，T_cache_miss = RTT + T_origin + T_queue，需分别建模命中与未命中路径的P99值

## Corrected Claim

P99延迟构成公式：L_P99 = max(T_cache_hit, T_cache_miss) 其中 T_cache_hit = RTT + T_processing + T_queue，T_cache_miss = RTT + T_origin + T_queue，需分别建模命中与未命中路径的P99值

## Evidence

父节点级核验未通过：不完备（子节点之间正交，分别描述了处理、队列和回源三个不同维度的延迟。但存在明显的完备性缺失：父节点公式中明确包含的 RTT（往返时延）在子节点中完全缺失，且 T_origin 通常由网络传输和源站处理两部分组成，子节点仅覆盖了源站处理部分，未覆盖回源网络传输延迟，导致无法完整重构 L_P99。）
