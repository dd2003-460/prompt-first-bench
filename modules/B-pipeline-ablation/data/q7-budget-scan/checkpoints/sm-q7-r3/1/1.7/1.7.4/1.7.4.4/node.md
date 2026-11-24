# N188: 背板与风扇功耗分摊模型：P_backplane ≈ N_disks * 0.5W（每盘背板电路），P_fan ≈ k * P_total_heat，k=0.05

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61, N62, N63

## Claim

背板与风扇功耗分摊模型：P_backplane ≈ N_disks * 0.5W（每盘背板电路），P_fan ≈ k * P_total_heat，k=0.05-0.1（风扇效率系数），对于 471 块 SSD 阵列，背板约 235W，风扇约 50-100W，合计分摊到每 TB 有效容量（900TB）约 0.3-0.4W/TB。

## Corrected Claim

背板与风扇功耗分摊模型：P_backplane ≈ N_disks * 0.5W（每盘背板电路），P_fan ≈ k * P_total_heat，k=0.05-0.1（风扇效率系数），对于 471 块 SSD 阵列，背板约 235W，风扇约 50-100W，合计分摊到每 TB 有效容量（900TB）约 0.3-0.4W/TB。

## Evidence

先验知识/题面给定，逻辑校验通过：背板功耗计算（471*0.5≈235W）准确；风扇功耗估算（基于总热耗的5-10%）符合数据中心工程惯例；总功耗除以有效容量得出的单位功耗量级（0.3-0.4 W/TB）在合理范围内，无逻辑矛盾。

## Search Query

server backplane and fan power consumption allocation per TB storage
