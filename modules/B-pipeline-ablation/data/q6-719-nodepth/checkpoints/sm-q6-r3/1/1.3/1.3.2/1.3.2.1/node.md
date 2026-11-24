# N223: 核心区域工作点（70%用户）：距离 d<100km，根据 RTT=0.05*d+5，RTT<10ms；考虑跨网惩罚 ΔT_cross≈15ms，P99_RTT_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57

## Claim

核心区域工作点（70%用户）：距离 d<100km，根据 RTT=0.05*d+5，RTT<10ms；考虑跨网惩罚 ΔT_cross≈15ms，P99_RTT_core ≈ 25ms

## Corrected Claim

核心区域工作点（70%用户）：距离 d<100km，根据 RTT=0.05*d+5，RTT<10ms；考虑跨网惩罚 ΔT_cross≈15ms，P99_RTT_core ≈ 25ms

## Evidence

先验知识/题面给定，逻辑校验通过：RTT计算(0.05*100+5=10ms)与跨网惩罚叠加(10+15=25ms)符合算术逻辑，量级合理。
