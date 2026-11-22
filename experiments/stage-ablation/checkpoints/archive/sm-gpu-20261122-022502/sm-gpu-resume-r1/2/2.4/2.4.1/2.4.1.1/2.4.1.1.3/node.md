# N637: 实际瓶颈应为 T_compute（带宽受限）和 T_sync（内核启动/调度开销 ~0.1-0.5ms），而非 T_comm。

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N196

## Claim

实际瓶颈应为 T_compute（带宽受限）和 T_sync（内核启动/调度开销 ~0.1-0.5ms），而非 T_comm。

## Corrected Claim

实际瓶颈应为 T_compute（带宽受限）和 T_sync（内核启动/调度开销 ~0.1-0.5ms），而非 T_comm。

## Evidence

先验知识/题面给定，逻辑校验通过
