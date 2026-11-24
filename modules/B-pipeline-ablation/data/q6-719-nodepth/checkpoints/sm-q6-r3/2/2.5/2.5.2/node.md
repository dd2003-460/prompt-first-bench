# N82: 自建 POP 点的回源带宽峰值需求 (B_peak, Gbps) 计算为 (V_origin * Peak_Factor) / (Peak_Window_Hou

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N16

## Claim

自建 POP 点的回源带宽峰值需求 (B_peak, Gbps) 计算为 (V_origin * Peak_Factor) / (Peak_Window_Hours * 3600 * 8)，其中 Peak_Factor 为峰值系数（通常 1.5-3.0），Peak_Window_Hours 为高峰时段时长（通常 4-8 小时）。

## Corrected Claim

自建 POP 点的回源带宽峰值需求 (B_peak, Gbps) 计算为 (V_origin * Peak_Factor) / (Peak_Window_Hours * 3600 * 8)，其中 Peak_Factor 为峰值系数（通常 1.5-3.0），Peak_Window_Hours 为高峰时段时长（通常 4-8 小时）。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应公式中的三个关键变量（Peak_Factor, Peak_Window_Hours, 计算实例），彼此独立且无重叠。虽然第三个节点是前两个参数的应用示例，但在学术分解中用于验证量纲和数值合理性，具有独立的验证价值，不属于冗余。）
