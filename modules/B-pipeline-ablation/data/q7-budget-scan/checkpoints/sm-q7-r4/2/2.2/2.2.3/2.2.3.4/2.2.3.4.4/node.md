# N548: 基于有效容量的单位 CapEx 修正：Unit_CapEx_Corrected = Total_CapEx / Total_Effective_Capacity

- **status**: verified
- **level**: L5
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N179

## Claim

基于有效容量的单位 CapEx 修正：Unit_CapEx_Corrected = Total_CapEx / Total_Effective_Capacity = 63,250 / 460 ≈ ¥137.5 / 有效TB（对比原未计 RAID 开销的 ¥127/TB，增加约 8.3%）。

## Corrected Claim

基于有效容量的单位 CapEx 修正：Unit_CapEx_Corrected = Total_CapEx / Total_Effective_Capacity = 63,250 / 460 ≈ ¥137.5 / 有效TB（对比原未计 RAID 开销的 ¥127/TB，增加约 8.3%）。

## Evidence

先验知识/题面给定，逻辑校验通过：63250/460=137.5，(137.5-127)/127≈8.27%，计算无误且符合RAID开销导致单位成本上升的逻辑。
