# N70: T_cache_miss_P99_self = max_i (RTT_P99(i) + RTT_origin_P99(i) + T_origin_proc_P9

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

T_cache_miss_P99_self = max_i (RTT_P99(i) + RTT_origin_P99(i) + T_origin_proc_P99 + T_origin_queue_P99)，其中RTT_origin_P99(i)为第i个POP到源站的P99 RTT，受骨干网拥塞影响

## Corrected Claim

T_cache_miss_P99_self = max_i (RTT_P99(i) + RTT_origin_P99(i) + T_origin_proc_P99 + T_origin_queue_P99)，其中RTT_origin_P99(i)为第i个POP到源站的P99 RTT，受骨干网拥塞影响

## Evidence

先验知识/题面给定，逻辑校验通过
