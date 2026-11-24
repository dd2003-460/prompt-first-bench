# N40: D1 合规门判据为 P99_latency <= T，其中 T 为 P99 目标值（如 200ms），三种策略的 P99_latency 分别为 P99_pub

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

D1 合规门判据为 P99_latency <= T，其中 T 为 P99 目标值（如 200ms），三种策略的 P99_latency 分别为 P99_public、P99_self、P99_mix，只有满足 P99 <= T 的策略才进入 D2 成本排序。

## Corrected Claim

D1 合规门判据为 P99_latency <= T，其中 T 为 P99 目标值（如 200ms），三种策略的 P99_latency 分别为 P99_public、P99_self、P99_mix，只有满足 P99 <= T 的策略才进入 D2 成本排序。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述定义了合规门（D1）的筛选逻辑，即基于延迟阈值（P99 <= T）进行过滤，再进入成本排序（D2），逻辑自洽且符合常规系统评估流程。
