# N556: 3.84TB NVMe SSD 方案下的基础设施功耗 P_infra_3.84TB = P_controller + P_backplane + P_fan +

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N239

## Claim

3.84TB NVMe SSD 方案下的基础设施功耗 P_infra_3.84TB = P_controller + P_backplane + P_fan + P_PDU_loss，其中 P_controller 与盘数成正比（假设 0.2W/disk），P_backplane 与盘数成正比（假设 0.1W/disk），P_fan 与总发热量成正比（假设 0.1 * P_total），P_PDU_loss 假设 5% 损耗。P_controller = 236 * 0.2 = 47.2W, P_backplane = 236 * 0.1 = 23.6W。设 P_total = P_drives + P_infra，P_fan = 0.1 * P_total，P_PDU_loss = 0.05 * P_total。P_infra = 47.2 + 23.6 + 0.1 * P_total + 0.05 * P_total = 70.8 + 0.15 * P_total。又 P_total = 3127 + P_infra = 3127 + 70.8 + 0.15 * P_total => 0.85 * P_total = 3197.8 => P_total ≈ 3762W。故 P_infra_3.84TB ≈ 3762 - 3127 = 635W

## Corrected Claim

3.84TB NVMe SSD 方案下的基础设施功耗 P_infra_3.84TB = P_controller + P_backplane + P_fan + P_PDU_loss，其中 P_controller 与盘数成正比（假设 0.2W/disk），P_backplane 与盘数成正比（假设 0.1W/disk），P_fan 与总发热量成正比（假设 0.1 * P_total），P_PDU_loss 假设 5% 损耗。P_controller = 236 * 0.2 = 47.2W, P_backplane = 236 * 0.1 = 23.6W。设 P_total = P_drives + P_infra，P_fan = 0.1 * P_total，P_PDU_loss = 0.05 * P_total。P_infra = 47.2 + 23.6 + 0.1 * P_total + 0.05 * P_total = 70.8 + 0.15 * P_total。又 P_total = 3127 + P_infra = 3127 + 70.8 + 0.15 * P_total => 0.85 * P_total = 3197.8 => P_total ≈ 3762W。故 P_infra_3.84TB ≈ 3762 - 3127 = 635W

## Evidence

先验知识/题面给定，逻辑校验通过：代数推导自洽，数值计算准确（0.85 * P_total = 3197.8 => P_total ≈ 3762.12W, P_infra ≈ 635.12W），符合物理直觉。
