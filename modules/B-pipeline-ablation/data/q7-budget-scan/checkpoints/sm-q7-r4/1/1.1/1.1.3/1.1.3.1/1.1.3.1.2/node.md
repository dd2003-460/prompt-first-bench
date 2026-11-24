# N418: 修正后的RAID-10单位年硬件成本：基于修正后的有效容量43.2TB，年硬件折旧成本 = (Total_CapEx - Residual_Value) / D

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N139

## Claim

修正后的RAID-10单位年硬件成本：基于修正后的有效容量43.2TB，年硬件折旧成本 = (Total_CapEx - Residual_Value) / Depreciation_Years。假设12块盘总CapEx=24,000元，残值率5%（1,200元），3年直线折旧，年折旧 = (24,000 - 1,200) / 3 = 7,600元。单位年硬件成本 = 7,600元 / 43.2TB ≈ ¥175.9/TB·年。

## Corrected Claim

修正后的RAID-10单位年硬件成本：基于修正后的有效容量43.2TB，年硬件折旧成本 = (Total_CapEx - Residual_Value) / Depreciation_Years。假设12块盘总CapEx=24,000元，残值率5%（1,200元），3年直线折旧，年折旧 = (24,000 - 1,200) / 3 = 7,600元。单位年硬件成本 = 7,600元 / 43.2TB ≈ ¥175.9/TB·年。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 (24000-1200)/3=7600 及 7600/43.2≈175.9 均正确，量纲与逻辑自洽。
