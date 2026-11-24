# N295: HDD 年故障率 (AFR) 的修正因子：原始 AFR 2.25% 基于 5 年寿命和标准负载；若 HDD 处于 24/7 高负载扫描状态（温数据缓存层），实际

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N104

## Claim

HDD 年故障率 (AFR) 的修正因子：原始 AFR 2.25% 基于 5 年寿命和标准负载；若 HDD 处于 24/7 高负载扫描状态（温数据缓存层），实际 AFR 可能上升至 3.0%-3.5%（热力学磨损加速）；若处于低频访问冷存储层，AFR 可能降至 1.5%-2.0%。需根据实际负载剖面调整 AFR 参数

## Corrected Claim

HDD 年故障率 (AFR) 的修正因子：原始 AFR 2.25% 基于 5 年寿命和标准负载；若 HDD 处于 24/7 高负载扫描状态（温数据缓存层），实际 AFR 可能上升至 3.0%-3.5%（热力学磨损加速）；若处于低频访问冷存储层，AFR 可能降至 1.5%-2.0%。需根据实际负载剖面调整 AFR 参数

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

HDD annual failure rate high load vs idle workload correlation
