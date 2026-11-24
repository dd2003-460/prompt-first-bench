# N56: 自建 10 POP 单请求 P99 延迟的构成公式：P99_self = P99(RTT_user_pop) + P99(T_proc_pop) + (1-H_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N9

## Claim

自建 10 POP 单请求 P99 延迟的构成公式：P99_self = P99(RTT_user_pop) + P99(T_proc_pop) + (1-H_pop)*P99(T_origin_fetch_self)，其中 H_pop 为自建 POP 缓存命中率。

## Corrected Claim

自建 10 POP 单请求 P99 延迟的构成公式：P99_self = P99(RTT_user_pop) + P99(T_proc_pop) + (1-H_pop)*P99(T_origin_fetch_self)，其中 H_pop 为自建 POP 缓存命中率。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Self-built POP P99 latency breakdown RTT processing cache miss
