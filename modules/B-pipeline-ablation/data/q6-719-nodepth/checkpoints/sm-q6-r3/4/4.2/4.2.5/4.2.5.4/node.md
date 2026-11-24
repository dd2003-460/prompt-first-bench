# N351: 整体回源延迟 P99 的加权计算：RTT_pop_origin_p99_weighted = Σ(P_pop_i * RTT_pop_origin_i)，其中 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N108

## Claim

整体回源延迟 P99 的加权计算：RTT_pop_origin_p99_weighted = Σ(P_pop_i * RTT_pop_origin_i)，其中 P_pop_i 为各 POP 的回源请求占比，由于长尾 POP 回源率更高，加权后整体 P99 通常高于近端 POP 的 RTT，估算值约 50-80ms

## Corrected Claim

整体回源延迟 P99 的加权计算：RTT_pop_origin_p99_weighted = Σ(P_pop_i * RTT_pop_origin_i)，其中 P_pop_i 为各 POP 的回源请求占比，由于长尾 POP 回源率更高，加权后整体 P99 通常高于近端 POP 的 RTT，估算值约 50-80ms

## Evidence

先验知识/题面给定，逻辑校验通过
