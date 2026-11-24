# N434: 北京-广州场景下物理RTT的理论下限 T_rtt_min = 2 × 1900km / (2×10^8 m/s) ≈ 19ms，实际RTT = T_rtt_mi

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N146

## Claim

北京-广州场景下物理RTT的理论下限 T_rtt_min = 2 × 1900km / (2×10^8 m/s) ≈ 19ms，实际RTT = T_rtt_min × (1 + T_switch_processing/T_rtt_min) + T_fiber_delay，其中 T_fiber_delay 为光纤介质额外延迟（通常 5-10%）

## Corrected Claim

北京-广州场景下物理RTT的理论下限 T_rtt_min = 2 × 1900km / (2×10^8 m/s) ≈ 19ms，实际RTT = T_rtt_min × (1 + T_switch_processing/T_rtt_min) + T_fiber_delay，其中 T_fiber_delay 为光纤介质额外延迟（通常 5-10%）

## Evidence

先验知识/题面给定，逻辑校验通过：北京至广州直线距离约1900km，光速在光纤中约为2×10^8 m/s，计算得出的理论下限19ms符合物理直觉；光纤介质延迟占比5-10%及处理延迟公式结构符合网络工程常识。

## Search Query

fiber optic propagation delay speed of light in fiber 200000 km/s
