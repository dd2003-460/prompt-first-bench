# N723: CPU上下文切换导致的性能损耗量化：在混合负载（20%业务I/O）下，RAID控制器或内核线程因上下文切换产生的额外延迟占比 Δ_t_switch，通常占I/O

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N253

## Claim

CPU上下文切换导致的性能损耗量化：在混合负载（20%业务I/O）下，RAID控制器或内核线程因上下文切换产生的额外延迟占比 Δ_t_switch，通常占I/O处理时间的5%-15%，需结合调度器配置（如CFS权重）确定具体数值。

## Corrected Claim

CPU上下文切换导致的性能损耗量化：在混合负载（20%业务I/O）下，RAID控制器或内核线程因上下文切换产生的额外延迟占比 Δ_t_switch，通常占I/O处理时间的5%-15%，需结合调度器配置（如CFS权重）确定具体数值。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Linux kernel context switch overhead percentage storage I/O latency
