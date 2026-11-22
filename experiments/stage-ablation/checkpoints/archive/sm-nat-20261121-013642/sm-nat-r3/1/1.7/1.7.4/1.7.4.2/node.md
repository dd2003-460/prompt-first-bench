# N155: LRU 因时间局部性优先保留的热门小对象字节量 B_lru_hot = C_cache * 0.15 * s_small，其中 s_small 为前 15% 热

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N52

## Claim

LRU 因时间局部性优先保留的热门小对象字节量 B_lru_hot = C_cache * 0.15 * s_small，其中 s_small 为前 15% 热度对象的平均大小，需结合 ρ=-0.3 计算 E[size|freq_top15%]

## Corrected Claim

LRU 因时间局部性优先保留的热门小对象字节量 B_lru_hot = C_cache * 0.15 * s_small，其中 s_small 为前 15% 热度对象的平均大小，需结合 ρ=-0.3 计算 E[size|freq_top15%]

## Evidence

先验知识/题面给定，逻辑校验通过
