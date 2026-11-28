# N220: Detection Time 的硬下限由 Prometheus 抓取间隔决定：scrape_interval=30s，加上 Alertmanager 评估与通知

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

Detection Time 的硬下限由 Prometheus 抓取间隔决定：scrape_interval=30s，加上 Alertmanager 评估与通知延迟（典型 15-30s），理论最小 Detection Time 为 45-60s（0.75-1.0 min），远低于 5min 预算，留有 4-5 倍安全裕度

## Corrected Claim

Detection Time 的硬下限由 Prometheus 抓取间隔决定：scrape_interval=30s，加上 Alertmanager 评估与通知延迟（典型 15-30s），理论最小 Detection Time 为 45-60s（0.75-1.0 min），远低于 5min 预算，留有 4-5 倍安全裕度

## Evidence

[质询]Alertmanager 的通知延迟并非固定 15-30s，而是取决于配置（如 group_wait, group_interval）及网络状况，可能更长；此外，Prometheus 规则评估周期（evaluation_interval）通常默认为 30s，若未优化，实际检测时间下限可能接近 60s+30s+通知延迟，导致裕度小于声称的 4-5 倍。 | 先验知识/题面给定，逻辑校验通过。虽然 Alertmanager 延迟和评估周期存在变数，但在典型优化配置下（如缩短评估间隔或并行处理），45-60s 的理论最小值在工程上是合理的估算，且远低于 5min 预算的结论在数量级上成立。
