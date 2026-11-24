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

父节点级核验未通过：不完备, 有冗余（子节点3和4针对同一公式变量T_active_ratio给出了两个截然不同的取值（3.3% vs 25%），这违反了参数定义的单一性原则，导致公式无法直接计算，属于逻辑上的冗余与冲突；同时，父节点是求'平均值'，但子节点只提供了分场景的参数，缺少一个整合步骤（如加权平均或明确最终采用哪个值），导致未能完整推导出父节点所需的最终结果。）

## Search Query

NVMe SSD idle vs active power consumption wattage enterprise 7.68TB
