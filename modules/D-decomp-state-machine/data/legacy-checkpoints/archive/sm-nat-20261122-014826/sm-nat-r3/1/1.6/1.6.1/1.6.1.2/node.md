# N107: LFU 驻留集相比 LRU 多保留的‘高频冷对象’（rank < 1000 但最近 1 小时无访问）的字节占比 P_gain ≈ 5.2%，这些对象的平均大小 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N38

## Claim

LFU 驻留集相比 LRU 多保留的‘高频冷对象’（rank < 1000 但最近 1 小时无访问）的字节占比 P_gain ≈ 5.2%，这些对象的平均大小 E[Size|Hot & Cold] ≈ 8.5KB（受 ρ=-0.3 影响），其对应的字节吞吐量增益 ΔH_gain ≈ 4.5%。

## Corrected Claim

LFU 驻留集相比 LRU 多保留的‘高频冷对象’（rank < 1000 但最近 1 小时无访问）的字节占比 P_gain ≈ 5.2%，这些对象的平均大小 E[Size|Hot & Cold] ≈ 8.5KB（受 ρ=-0.3 影响），其对应的字节吞吐量增益 ΔH_gain ≈ 4.5%。

## Evidence

先验知识/题面给定，逻辑校验通过
