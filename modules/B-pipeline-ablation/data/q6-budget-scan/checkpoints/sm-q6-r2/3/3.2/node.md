# N15: 机房租赁及电力成本 $C_{colo}$ 包括机柜租金、带宽接入费及电费：$C_{colo} = N_{racks} \times (R_{rack} + E_

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

机房租赁及电力成本 $C_{colo}$ 包括机柜租金、带宽接入费及电费：$C_{colo} = N_{racks} \times (R_{rack} + E_{power} \times P_{energy})$，其中 $R_{rack}$ 为每机柜月租金（约 5000-10000 元/月），$E_{power}$ 为每机柜功耗（约 5-10 kW），$P_{energy}$ 为电价（约 0.6-0.8 元/kWh）。

## Corrected Claim

机房租赁及电力成本 $C_{colo}$ 包括机柜租金、带宽接入费及电费：$C_{colo} = N_{racks} \times (R_{rack} + E_{power} \times P_{energy})$，其中 $R_{rack}$ 为每机柜月租金（约 5000-10000 元/月），$E_{power}$ 为每机柜功耗（约 5-10 kW），$P_{energy}$ 为电价（约 0.6-0.8 元/kWh）。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应公式中的四个独立变量（N_racks, R_rack, E_power, P_energy），彼此正交且无重复。虽然 R_rack 和 E_power 的取值受地区影响，但作为不同物理量（租金 vs 功耗）的处理是合理的，且 E_power 的计算逻辑清晰，未与 R_rack 混淆。所有关键参数均已覆盖。）

## Search Query

data center colocation cost per rack power consumption
