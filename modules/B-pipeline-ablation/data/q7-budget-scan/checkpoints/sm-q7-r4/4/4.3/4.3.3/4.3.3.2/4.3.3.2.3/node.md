# N734: 修正后的重建时间公式：T_rebuild_actual = T_nominal * (1 + Penalty_Thermal)，其中Penalty_Therma

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N256, N257, N258

## Claim

修正后的重建时间公式：T_rebuild_actual = T_nominal * (1 + Penalty_Thermal)，其中Penalty_Thermal取决于散热设计。若散热不足导致频繁触发节流，Penalty可达0.5-1.0（即时间翻倍），而非固定的0.15 (1/0.9 - 1)。需根据具体硬件散热规格确定Penalty系数。

## Corrected Claim

修正后的重建时间公式：T_rebuild_actual = T_nominal * (1 + Penalty_Thermal)，其中Penalty_Thermal取决于散热设计。若散热不足导致频繁触发节流，Penalty可达0.5-1.0（即时间翻倍），而非固定的0.15 (1/0.9 - 1)。需根据具体硬件散热规格确定Penalty系数。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

NVMe rebuild time impact thermal throttling penalty factor calculation
