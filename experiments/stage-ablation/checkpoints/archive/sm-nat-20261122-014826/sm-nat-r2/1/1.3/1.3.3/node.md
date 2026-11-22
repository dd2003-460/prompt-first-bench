# N32: 负相关对 LRU 有效容量的影响量化：由于热门对象更小，LRU 在 128GB 容量下可容纳的热门对象数量 N_fit = C / E[Size|Hot] = 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

负相关对 LRU 有效容量的影响量化：由于热门对象更小，LRU 在 128GB 容量下可容纳的热门对象数量 N_fit = C / E[Size|Hot] = 128GB / 9.9KB ≈ 13,333 个，相比无相关性假设 (128GB/11KB ≈ 12,000 个) 提升约 11% 的驻留对象数。

## Corrected Claim

负相关对 LRU 有效容量的影响量化：由于热门对象更小，LRU 在 128GB 容量下可容纳的热门对象数量 N_fit = C / E[Size|Hot] = 128GB / 9.9KB ≈ 13,333 个，相比无相关性假设 (128GB/11KB ≈ 12,000 个) 提升约 11% 的驻留对象数。

## Evidence

先验知识/题面给定，逻辑校验通过：128GB/9.9KB ≈ 13,333，128GB/11KB ≈ 12,000，(13333-12000)/12000 ≈ 11.1%，计算自洽。
