# N128: C_opex_monthly 分项验证：C_opex = C_bw_monthly + C_eng_monthly + C_power_monthly + C_

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

C_opex_monthly 分项验证：C_opex = C_bw_monthly + C_eng_monthly + C_power_monthly + C_colocation_monthly；其中 C_power = P_server_avg * 24h * 30d * P_elec (¥0.8/kWh)，自建机房需额外计入机柜租赁费（¥500-1000/柜/月）。

## Corrected Claim

C_opex_monthly 分项验证：C_opex = C_bw_monthly + C_eng_monthly + C_power_monthly + C_colocation_monthly；其中 C_power = P_server_avg * 24h * 30d * P_elec (¥0.8/kWh)，自建机房需额外计入机柜租赁费（¥500-1000/柜/月）。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（子节点存在严重的维度混淆和冗余。父节点是成本公式的验证，子节点却混合了‘成本参数计算’（节点1、2）和‘特定场景下的总成本实例’（节点3、4、5）。工作点A、B、C本质上是同一组公式在不同输入参数下的计算结果，属于同一逻辑层面的不同取值，而非正交的独立概念。此外，节点3中的人力成本（C_eng）高达15万，远超带宽和电力，但在父节点描述中未体现人力成本的主导地位或具体定义，导致分解层级不一致。）

## Search Query

data center colocation cost per rack per month China average
