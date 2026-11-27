# N120: 多卡方案（如 2×RTX 4090）在并发数 > 单卡 Batch_max 时的边际 TCO 增量公式：ΔTCO_multi = (Cost_hardware_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N27

## Claim

多卡方案（如 2×RTX 4090）在并发数 > 单卡 Batch_max 时的边际 TCO 增量公式：ΔTCO_multi = (Cost_hardware_extra + Cost_cooling_extra) / 3y + (Power_consumption_multi - Power_consumption_single) * 3y * Electricity_Rate，用于量化从单卡切换到多卡的额外成本。

## Corrected Claim

多卡方案（如 2×RTX 4090）在并发数 > 单卡 Batch_max 时的边际 TCO 增量公式：ΔTCO_multi = (Cost_hardware_extra + Cost_cooling_extra) / 3y + (Power_consumption_multi - Power_consumption_single) * 3y * Electricity_Rate，用于量化从单卡切换到多卡的额外成本。

## Evidence

先验知识/题面给定，逻辑校验通过
