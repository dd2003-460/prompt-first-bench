# N53: τ_LRU 的数值解：代入 C=128GB=134217728KB, R=50,000,000 requests/day, E[Size]≈10.1KB，计算 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N16

## Claim

τ_LRU 的数值解：代入 C=128GB=134217728KB, R=50,000,000 requests/day, E[Size]≈10.1KB，计算 τ_LRU = C / (R * E[Size]) ≈ 134217728 / (50000000 * 10.1) ≈ 0.266 days (约 6.4 小时)。

## Corrected Claim

τ_LRU 的数值解：代入 C=128GB=134217728KB, R=50,000,000 requests/day, E[Size]≈10.1KB，计算 τ_LRU = C / (R * E[Size]) ≈ 134217728 / (50000000 * 10.1) ≈ 0.266 days (约 6.4 小时)。

## Evidence

先验知识/题面给定，逻辑校验通过：134217728 / (50000000 * 10.1) ≈ 0.266，计算无误且量级合理。
