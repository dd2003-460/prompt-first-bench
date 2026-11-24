# N215: 混合架构年电力成本 C_power_hybrid = (P_ssd_watts * V_ssd_TB + P_hdd_watts * V_hdd_TB) * P

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N66

## Claim

混合架构年电力成本 C_power_hybrid = (P_ssd_watts * V_ssd_TB + P_hdd_watts * V_hdd_TB) * PUE * Price_electricity * Hours; 代入 P_ssd=0.7W/TB, P_hdd=0.4W/TB, PUE=1.4, Price=0.8, Hours=8760, 计算得出具体金额

## Corrected Claim

混合架构年电力成本 C_power_hybrid = (P_ssd_watts * V_ssd_TB + P_hdd_watts * V_hdd_TB) * PUE * Price_electricity * Hours; 代入 P_ssd=0.7W/TB, P_hdd=0.4W/TB, PUE=1.4, Price=0.8, Hours=8760, 计算得出具体金额

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：前两个子节点分别独立计算SSD和HDD层的成本（互不重叠），第三个子节点负责汇总并对比。虽然前两个子节点的计算结构相似（都是 容量*功耗*时间*PUE*价格），但它们针对不同的硬件层级（SSD vs HDD）和不同的参数值，属于公式在不同分量上的应用，而非同一参数的冗余列举，因此不构成冗余。所有关键步骤（分项计算、汇总、对比验证）均已覆盖。）

## Search Query

hybrid SSD HDD power consumption calculation per TB
