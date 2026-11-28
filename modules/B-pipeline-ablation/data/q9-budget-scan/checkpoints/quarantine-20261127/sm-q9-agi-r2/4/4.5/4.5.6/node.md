# N100: 在持续运行 24 小时/天且利用率 u=1.0（满载推理）的极端情况下，月耗电量 E_month = P_peak_total * 24h * 30d = 1.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24, N25, N26

## Claim

在持续运行 24 小时/天且利用率 u=1.0（满载推理）的极端情况下，月耗电量 E_month = P_peak_total * 24h * 30d = 1.1kW * 720h = 792 kWh，对应月度电费 Cost_month = 792 * $0.15 = $118.80；若利用率为典型科研间歇负载 u=0.5，则月电费约为 $59.40。

## Corrected Claim

在持续运行 24 小时/天且利用率 u=1.0（满载推理）的极端情况下，月耗电量 E_month = P_peak_total * 24h * 30d = 1.1kW * 720h = 792 kWh，对应月度电费 Cost_month = 792 * $0.15 = $118.80；若利用率为典型科研间歇负载 u=0.5，则月电费约为 $59.40。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（1.1 * 720 = 792; 792 * 0.15 = 118.8; 118.8 * 0.5 = 59.4），量纲与物理直觉一致。
