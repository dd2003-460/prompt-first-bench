# N104: 负相关（ρ=-0.3）对 LFU 相对 LRU 增益的交互效应：由于热门对象较小，LFU 保留高频对象时占用的容量更少，使得 LFU 能保留更多对象。量化此效应

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N38

## Claim

负相关（ρ=-0.3）对 LFU 相对 LRU 增益的交互效应：由于热门对象较小，LFU 保留高频对象时占用的容量更少，使得 LFU 能保留更多对象。量化此效应：计算 LFU 在 ρ=-0.3 下的有效容量利用率 C_eff_LFU 相对于 ρ=0 的提升比例，该比例直接放大 Δ_H_max（N12 中的增益项）。

## Corrected Claim

负相关（ρ=-0.3）对 LFU 相对 LRU 增益的交互效应：由于热门对象较小，LFU 保留高频对象时占用的容量更少，使得 LFU 能保留更多对象。量化此效应：计算 LFU 在 ρ=-0.3 下的有效容量利用率 C_eff_LFU 相对于 ρ=0 的提升比例，该比例直接放大 Δ_H_max（N12 中的增益项）。

## Evidence

先验知识/题面给定，逻辑校验通过：负相关意味着高频对象体积小，LFU 基于频率保留对象时，因单个对象占用空间小，在固定总容量下可容纳的对象数量（有效容量利用率）确实高于零相关或正相关情况，从而放大相对 LRU 的增益。

## Search Query

LFU vs LRU gain negative correlation size popularity
