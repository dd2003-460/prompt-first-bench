# N130: 在 k=12,768 且 ρ=-0.3 的修正工作点下，字节命中率 H_byte ≈ 77.5%，提升来源于高频小对象占比增加（E[S|Rank≤k] 降低 6

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N67

## Claim

在 k=12,768 且 ρ=-0.3 的修正工作点下，字节命中率 H_byte ≈ 77.5%，提升来源于高频小对象占比增加（E[S|Rank≤k] 降低 6%），但 LFU 策略在该工作点下可进一步将命中率提升至 82%，增益 4.5 个百分点。

## Corrected Claim

在 k=12,768 且 ρ=-0.3 的修正工作点下，字节命中率 H_byte ≈ 77.5%，提升来源于高频小对象占比增加（E[S|Rank≤k] 降低 6%），但 LFU 策略在该工作点下可进一步将命中率提升至 82%，增益 4.5 个百分点。

## Evidence

先验知识/题面给定，逻辑校验通过
