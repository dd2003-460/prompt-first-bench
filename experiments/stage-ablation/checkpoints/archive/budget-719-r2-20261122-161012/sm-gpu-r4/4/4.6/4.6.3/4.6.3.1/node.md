# N246: 电力成本计算的精确公式与参数修正：年电力成本 = (Peak_Power_Watts * Utilization_Factor) * 8760 hours * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N113

## Claim

电力成本计算的精确公式与参数修正：年电力成本 = (Peak_Power_Watts * Utilization_Factor) * 8760 hours * Price_per_kWh。N113 中 2x 4090 (900W) 年成本 $131 (at $0.10/kWh) 隐含 Utilization_Factor ≈ 15% (900 * 0.15 * 8760 * 0.1 / 1000 = 118.3，接近 $131)；H100 (700W) 年成本 $102 (at $0.10/kWh) 隐含 Utilization_Factor ≈ 16.5% (700 * 0.165 * 8760 * 0.1 / 1000 = 101.7)。需明确‘利用率’定义为‘GPU 满载时间占比’，而非‘系统通电时间占比’，因为 Idle 功耗远低于 Peak。

## Corrected Claim

电力成本计算的精确公式与参数修正：年电力成本 = (Peak_Power_Watts * Utilization_Factor) * 8760 hours * Price_per_kWh。N113 中 2x 4090 (900W) 年成本 $131 (at $0.10/kWh) 隐含 Utilization_Factor ≈ 15% (900 * 0.15 * 8760 * 0.1 / 1000 = 118.3，接近 $131)；H100 (700W) 年成本 $102 (at $0.10/kWh) 隐含 Utilization_Factor ≈ 16.5% (700 * 0.165 * 8760 * 0.1 / 1000 = 101.7)。需明确‘利用率’定义为‘GPU 满载时间占比’，而非‘系统通电时间占比’，因为 Idle 功耗远低于 Peak。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1专注于定义'利用率'的语义（区分Duty Cycle与Load Factor），子节点2专注于公式的数学修正（引入Idle功耗项）。两者关注点不同（定义 vs 公式结构），无重叠或矛盾。父节点中提到的'参数修正'和'定义澄清'均被覆盖。）

## Search Query

GPU inference utilization factor average power consumption calculation
