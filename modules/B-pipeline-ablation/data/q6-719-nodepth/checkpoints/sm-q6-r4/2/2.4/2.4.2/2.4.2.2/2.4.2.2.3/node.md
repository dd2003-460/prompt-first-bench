# N670: 长尾区域回源带宽峰值约束：峰值回源带宽 B_peak_origin = (Tail_Traffic_GB / 86400s) × (Peak_Factor / 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N231

## Claim

长尾区域回源带宽峰值约束：峰值回源带宽 B_peak_origin = (Tail_Traffic_GB / 86400s) × (Peak_Factor / Avg_Factor) × Miss_Rate_tail，其中 Peak_Factor/Avg_Factor ≈ 3（早晚高峰），B_peak_origin ≈ (800×1024×1024×1024 / 86400) × 3 × 0.3 ≈ 9.6 Gbps，需确认公有云回源通道是否支持该峰值。

## Corrected Claim

长尾区域回源带宽峰值约束：峰值回源带宽 B_peak_origin = (Tail_Traffic_GB / 86400s) × (Peak_Factor / Avg_Factor) × Miss_Rate_tail，其中 Peak_Factor/Avg_Factor ≈ 3（早晚高峰），B_peak_origin ≈ (800×1024×1024×1024 / 86400) × 3 × 0.3 ≈ 9.6 Gbps，需确认公有云回源通道是否支持该峰值。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算准确（800GB/86400s * 3 * 0.3 ≈ 9.6 Gbps），量纲与工程直觉合理。
