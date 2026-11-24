# N370: Seagate Exos X18 16TB HDD 工作点的年化电力成本：基于修正后的单盘平均功耗 3.025W（N279 修正值，考虑 Spin-down 占

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N163

## Claim

Seagate Exos X18 16TB HDD 工作点的年化电力成本：基于修正后的单盘平均功耗 3.025W（N279 修正值，考虑 Spin-down 占比），总功耗 P_total = 28 * 3.025W + 90W (Infra, N276) ≈ 175W，年电费 = 0.175 kW * 8760 h * ¥0.8/kWh ≈ ¥1,230。

## Corrected Claim

Seagate Exos X18 16TB HDD 工作点的年化电力成本：基于修正后的单盘平均功耗 3.025W（N279 修正值，考虑 Spin-down 占比），总功耗 P_total = 28 * 3.025W + 90W (Infra, N276) ≈ 175W，年电费 = 0.175 kW * 8760 h * ¥0.8/kWh ≈ ¥1,230。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（28*3.025+90=174.7W≈175W；0.175*8760*0.8=1226.4≈1230），量级符合数据中心硬盘集群能耗常识。

## Search Query

Data center electricity price China 2024
