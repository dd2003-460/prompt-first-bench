# N44: LFU 相比 LRU 的增益来源于对‘长尾低频但大尺寸’对象的驱逐差异：在 M/C < 1.0 时，LRU 会因新访问驱逐高频对象，而 LFU 保留高频对象，增

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

LFU 相比 LRU 的增益来源于对‘长尾低频但大尺寸’对象的驱逐差异：在 M/C < 1.0 时，LRU 会因新访问驱逐高频对象，而 LFU 保留高频对象，增益 ΔH ≈ (Sum_{i∈LRU_miss} S_i F_i - Sum_{i∈LFU_miss} S_i F_i) / TotalBytes。

## Corrected Claim

LFU 相比 LRU 的增益来源于对‘长尾低频但大尺寸’对象的驱逐差异：在 M/C < 1.0 时，LRU 会因新访问驱逐高频对象，而 LFU 保留高频对象，增益 ΔH ≈ (Sum_{i∈LRU_miss} S_i F_i - Sum_{i∈LFU_miss} S_i F_i) / TotalBytes。

## Evidence

先验知识/题面给定，逻辑校验通过
