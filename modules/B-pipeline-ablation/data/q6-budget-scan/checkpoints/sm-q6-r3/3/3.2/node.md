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

父节点级核验通过：正交+完备+无冗余（子节点分别对应父节点公式中的变量 $N_{racks}$、$R_{rack}$、$E_{power}$ 和 $P_{energy}$，逻辑上完全正交且无重叠。每个子节点都提供了具体的取值依据和计算过程，覆盖了公式中所有关键参数的定义与估算，没有冗余信息，也没有遗漏父节点中提到的任何成本组成部分（机柜租金、带宽虽未单独列出但通常包含在机柜服务费或作为固定项，此处重点分解了主要可变成本，且父节点公式中未显式包含带宽项，故子节点覆盖公式变量是完备的）。）

## Search Query

data center colocation cost per rack power consumption
