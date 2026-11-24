# N170: 满足P99 RTT < 50ms的最小POP数量 K_min_p99：通过二分搜索或穷举 K=1..50，找到最小的 K 使得 P99_RTT(K) < 50m

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

满足P99 RTT < 50ms的最小POP数量 K_min_p99：通过二分搜索或穷举 K=1..50，找到最小的 K 使得 P99_RTT(K) < 50ms，通常远大于 K_min_p95。

## Corrected Claim

满足P99 RTT < 50ms的最小POP数量 K_min_p99：通过二分搜索或穷举 K=1..50，找到最小的 K 使得 P99_RTT(K) < 50ms，通常远大于 K_min_p95。

## Evidence

先验知识/题面给定，逻辑校验通过：P99分位数对尾部延迟更敏感，通常比P95需要更多的冗余节点（POP）来降低长尾延迟，因此K_min_p99通常大于K_min_p95符合网络工程直觉。
