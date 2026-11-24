# N371: 总回源延迟 RTT_origin_total 的 P99 值估算：对于小文件 (s<1MB)，RTT_total ≈ RTT_L1_L2 + RTT_L2_or

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N114

## Claim

总回源延迟 RTT_origin_total 的 P99 值估算：对于小文件 (s<1MB)，RTT_total ≈ RTT_L1_L2 + RTT_L2_origin ≈ 30-80ms；对于大文件 (s>5MB)，T_transfer 主导，RTT_total 可达 1-5 秒，因此 P99 延迟主要受大文件回源比例影响，若大文件占比 10%，则 P99 延迟显著上升。

## Corrected Claim

总回源延迟 RTT_origin_total 的 P99 值估算：对于小文件 (s<1MB)，RTT_total ≈ RTT_L1_L2 + RTT_L2_origin ≈ 30-80ms；对于大文件 (s>5MB)，T_transfer 主导，RTT_total 可达 1-5 秒，因此 P99 延迟主要受大文件回源比例影响，若大文件占比 10%，则 P99 延迟显著上升。

## Evidence

先验知识/题面给定，逻辑校验通过：小文件延迟由RTT主导（30-80ms符合跨地域/跨层CDN典型值），大文件延迟由传输时间主导（1-5s符合5MB以上文件在常规带宽下的传输耗时），P99受长尾大文件影响的逻辑自洽。

## Search Query

CDN origin fetch P99 latency large file impact
