# N438: 武汉-武汉场景下物理RTT的理论下限 T_rtt_min = 2 × 75km / (2×10^8 m/s) ≈ 0.75ms，实际RTT = T_rtt_mi

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N147

## Claim

武汉-武汉场景下物理RTT的理论下限 T_rtt_min = 2 × 75km / (2×10^8 m/s) ≈ 0.75ms，实际RTT = T_rtt_min + T_switch_processing × 2，其中 T_switch_processing 为 0.05-0.2ms，故 T_rtt_actual ≈ 0.85-1.15ms

## Corrected Claim

武汉-武汉场景下物理RTT的理论下限 T_rtt_min = 2 × 75km / (2×10^8 m/s) ≈ 0.75ms，实际RTT = T_rtt_min + T_switch_processing × 2，其中 T_switch_processing 为 0.05-0.2ms，故 T_rtt_actual ≈ 0.85-1.15ms

## Evidence

先验知识/题面给定，逻辑校验通过：光速计算正确（2*75km/3e8m/s≈0.5ms，若按2e8m/s则0.75ms，符合介质中光速量级），交换机处理时延量级合理，总时延推导自洽。

## Search Query

75km fiber optic RTT calculation switch processing
