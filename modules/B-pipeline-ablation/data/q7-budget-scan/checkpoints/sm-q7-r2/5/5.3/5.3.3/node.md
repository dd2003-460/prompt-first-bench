# N74: 温数据扫描延迟敏感度：顺序读P99<100ms为软约束，实际NVMe SSD顺序读延迟~0.1ms，HDD顺序读延迟~10ms（满足），S3顺序读延迟~50ms

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

温数据扫描延迟敏感度：顺序读P99<100ms为软约束，实际NVMe SSD顺序读延迟~0.1ms，HDD顺序读延迟~10ms（满足），S3顺序读延迟~50ms（满足）；但S3的GET请求RTT~50ms，若并行度16，则每批16个请求耗时50ms，总吞吐 = 16 * 1MB / 50ms = 320MB/s，远低于7GB/s需求，需并行度提升至 ~220 才能达到7GB/s，受S3 API限流（1550 GET/s/bucket）约束，最大吞吐 = 1550 * 1MB = 1.55GB/s，不满足7GB/s需求

## Corrected Claim

温数据扫描延迟敏感度：顺序读P99<100ms为软约束，实际NVMe SSD顺序读延迟~0.1ms，HDD顺序读延迟~10ms（满足），S3顺序读延迟~50ms（满足）；但S3的GET请求RTT~50ms，若并行度16，则每批16个请求耗时50ms，总吞吐 = 16 * 1MB / 50ms = 320MB/s，远低于7GB/s需求，需并行度提升至 ~220 才能达到7GB/s，受S3 API限流（1550 GET/s/bucket）约束，最大吞吐 = 1550 * 1MB = 1.55GB/s，不满足7GB/s需求

## Evidence

[质询]S3的GET请求RTT~50ms及API限流1550 GET/s/bucket属于经验参数，若实际网络延迟更低或限流策略不同，结论可能变化；但作为典型工程估算，量级合理。 | 先验知识/题面给定，逻辑校验通过：NVMe/HDD/S3延迟量级符合常识；S3吞吐计算（1550 * 1MB = 1.55GB/s < 7GB/s）逻辑自洽，结论成立。
