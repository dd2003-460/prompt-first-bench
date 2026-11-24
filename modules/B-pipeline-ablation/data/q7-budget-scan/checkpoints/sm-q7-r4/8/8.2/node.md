# N128: NVMe SSD 单盘平均功耗 W_drive_avg 需基于工作负载加权：W_drive_avg = W_idle * T_idle_ratio + W_ac

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N33

## Claim

NVMe SSD 单盘平均功耗 W_drive_avg 需基于工作负载加权：W_drive_avg = W_idle * T_idle_ratio + W_active * T_active_ratio。对于冷/温数据湖，假设活跃率 10%，W_idle≈2.5W, W_active≈15W，则 W_drive_avg ≈ 3.85W，远低于 N33 假设的 20W。

## Corrected Claim

NVMe SSD 单盘平均功耗 W_drive_avg 需基于工作负载加权：W_drive_avg = W_idle * T_idle_ratio + W_active * T_active_ratio。对于冷/温数据湖，假设活跃率 10%，W_idle≈2.5W, W_active≈15W，则 W_drive_avg ≈ 3.85W，远低于 N33 假设的 20W。

## Evidence

父节点级核验失败（LLM 错误）：curl rc=28 b''

## Search Query

NVMe SSD idle vs active power consumption wattage enterprise 7.68TB
