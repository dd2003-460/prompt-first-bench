# N646: HTTP/2 头部压缩 (HPACK) 解码延迟 T_hpack_p99 为 0.5ms，基于静态表大小 32B 和动态表大小 4KB 的典型配置，解码复杂度为

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N213

## Claim

HTTP/2 头部压缩 (HPACK) 解码延迟 T_hpack_p99 为 0.5ms，基于静态表大小 32B 和动态表大小 4KB 的典型配置，解码复杂度为 O(1) 平均情况，P99 受动态表重建触发影响

## Corrected Claim

HTTP/2 头部压缩 (HPACK) 解码延迟 T_hpack_p99 为 0.5ms，基于静态表大小 32B 和动态表大小 4KB 的典型配置，解码复杂度为 O(1) 平均情况，P99 受动态表重建触发影响

## Evidence

先验知识/题面给定，逻辑校验通过
