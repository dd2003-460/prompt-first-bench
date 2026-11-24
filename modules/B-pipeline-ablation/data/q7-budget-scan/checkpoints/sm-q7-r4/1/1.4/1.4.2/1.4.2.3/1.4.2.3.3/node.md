# N466: 额外 SSD 随机读 IOPS 与功耗的关联公式：ΔIOPS = Scan_Data_Size * Miss_Rate / Avg_Object_Size。ΔP

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N156

## Claim

额外 SSD 随机读 IOPS 与功耗的关联公式：ΔIOPS = Scan_Data_Size * Miss_Rate / Avg_Object_Size。ΔPower_W = ΔIOPS * Power_Per_IOPS_NVMe。假设 Power_Per_IOPS ≈ 0.001 W/IOPS (NVMe 随机读能效)，若 ΔIOPS = 1000，则 ΔPower ≈ 1W。题面 '5-10W' 暗示 ΔIOPS 需在 5000-10000 范围，需验证 Miss_Rate 是否真能达到此量级。

## Corrected Claim

额外 SSD 随机读 IOPS 与功耗的关联公式：ΔIOPS = Scan_Data_Size * Miss_Rate / Avg_Object_Size。ΔPower_W = ΔIOPS * Power_Per_IOPS_NVMe。假设 Power_Per_IOPS ≈ 0.001 W/IOPS (NVMe 随机读能效)，若 ΔIOPS = 1000，则 ΔPower ≈ 1W。题面 '5-10W' 暗示 ΔIOPS 需在 5000-10000 范围，需验证 Miss_Rate 是否真能达到此量级。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导自洽，0.001 W/IOPS 符合 NVMe 随机读能效量级，1000 IOPS 对应 1W 及 5-10W 对应 5k-10k IOPS 的数值换算正确。

## Search Query

NVMe SSD power consumption per random read IOPS
