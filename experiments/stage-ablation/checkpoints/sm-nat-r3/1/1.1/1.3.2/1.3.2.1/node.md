# N90: 缓存对象数量上限 K_max = C_avail / S_min，代入 C_avail ≈ 115.2 GB (1.208e11 bytes) 和 S_min 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N27

## Claim

缓存对象数量上限 K_max = C_avail / S_min，代入 C_avail ≈ 115.2 GB (1.208e11 bytes) 和 S_min = 1 KB (1024 bytes)，K_max ≈ 117,959,104。

## Corrected Claim

缓存对象数量上限 K_max = C_avail / S_min，代入 C_avail ≈ 115.2 GB (1.208e11 bytes) 和 S_min = 1 KB (1024 bytes)，K_max ≈ 117,959,104。

## Evidence

先验知识/题面给定，逻辑校验通过：1.208e11 / 1024 ≈ 1.1796e8，数值量级与计算结果一致。
