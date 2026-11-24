# N224: 长尾区域工作点（30%用户）：距离 d=300-500km，根据 RTT=0.05*d+5，RTT=20-30ms；考虑跨网惩罚 ΔT_cross≈20ms，P

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57

## Claim

长尾区域工作点（30%用户）：距离 d=300-500km，根据 RTT=0.05*d+5，RTT=20-30ms；考虑跨网惩罚 ΔT_cross≈20ms，P99_RTT_tail ≈ 50ms，此区域是决定整体 P99 的关键瓶颈

## Corrected Claim

长尾区域工作点（30%用户）：距离 d=300-500km，根据 RTT=0.05*d+5，RTT=20-30ms；考虑跨网惩罚 ΔT_cross≈20ms，P99_RTT_tail ≈ 50ms，此区域是决定整体 P99 的关键瓶颈

## Evidence

先验知识/题面给定，逻辑校验通过：RTT计算（0.05*300+5=20ms, 0.05*500+5=30ms）与跨网惩罚叠加（20-30+20=40-50ms）符合算术逻辑，P99取上限50ms合理。
