# N642: NVMe 热备硬件成本的精确计算：C_hot_standby = V_total * SSD_Price_Per_TB * Redundancy_Factor；

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N222

## Claim

NVMe 热备硬件成本的精确计算：C_hot_standby = V_total * SSD_Price_Per_TB * Redundancy_Factor；假设 500TB 数据，SSD 价格为 ¥300/TB/年，Redundancy_Factor=1.0 (1:1 镜像)，则 C_hot_standby = 500 * 300 * 1.0 = ¥150,000/年；若采用 RAID 1 双控架构，Redundancy_Factor=1.5，则 C_hot_standby = ¥225,000/年。

## Corrected Claim

NVMe 热备硬件成本的精确计算：C_hot_standby = V_total * SSD_Price_Per_TB * Redundancy_Factor；假设 500TB 数据，SSD 价格为 ¥300/TB/年，Redundancy_Factor=1.0 (1:1 镜像)，则 C_hot_standby = 500 * 300 * 1.0 = ¥150,000/年；若采用 RAID 1 双控架构，Redundancy_Factor=1.5，则 C_hot_standby = ¥225,000/年。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（500*300*1.0=150,000; 500*300*1.5=225,000），公式定义与计算过程自洽，符合成本估算的基本逻辑。
