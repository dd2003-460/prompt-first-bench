# N48: HDD 层 RAID-6 有效容量系数：假设 12 盘组，Usable_Factor_HDD = (12 - 2) / 12 = 83.3%，该系数应用于 40

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

HDD 层 RAID-6 有效容量系数：假设 12 盘组，Usable_Factor_HDD = (12 - 2) / 12 = 83.3%，该系数应用于 400TB 冷数据，反推所需裸 HDD 容量 = 400TB / 0.833 ≈ 480.2TB。

## Corrected Claim

HDD 层 RAID-6 有效容量系数：假设 12 盘组，Usable_Factor_HDD = (12 - 2) / 12 = 83.3%，该系数应用于 400TB 冷数据，反推所需裸 HDD 容量 = 400TB / 0.833 ≈ 480.2TB。

## Evidence

先验知识/题面给定，逻辑校验通过：RAID-6 双盘校验机制下，12 盘组有效容量系数为 (12-2)/12，数学推导及数值计算（400/0.8333... ≈ 480）均正确。
