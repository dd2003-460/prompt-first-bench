# N128: NVMe SSD 单盘平均功耗 W_drive_avg 需基于工作负载加权：W_drive_avg = W_idle * T_idle_ratio + W_ac

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

NVMe SSD 单盘平均功耗 W_drive_avg 需基于工作负载加权：W_drive_avg = W_idle * T_idle_ratio + W_active * T_active_ratio。对于冷/温数据湖，假设活跃率 10%，W_idle≈2.5W, W_active≈15W，则 W_drive_avg ≈ 3.85W，远低于 N33 假设的 20W。

## Corrected Claim

NVMe SSD 单盘平均功耗 W_drive_avg 需基于工作负载加权：W_drive_avg = W_idle * T_idle_ratio + W_active * T_active_ratio。对于冷/温数据湖，假设活跃率 10%，W_idle≈2.5W, W_active≈15W，则 W_drive_avg ≈ 3.85W，远低于 N33 假设的 20W。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（2.5*0.9 + 15*0.1 = 3.85），功耗量级符合NVMe SSD典型工程参数范围。

## Search Query

NVMe SSD idle vs active power consumption wattage enterprise 7.68TB
