# N365: 源站缓存命中率 H_origin 在标准架构下为 0，除非部署了独立的源站加速层或全局一致性哈希；若启用源站 SSD 缓存，H_origin 可提升至 0.1-

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N113

## Claim

源站缓存命中率 H_origin 在标准架构下为 0，除非部署了独立的源站加速层或全局一致性哈希；若启用源站 SSD 缓存，H_origin 可提升至 0.1-0.3，从而将 L2 有效命中率 H_L2 从 1-Miss_L1 提升至 1-Miss_L1*(1-0.2)。

## Corrected Claim

源站缓存命中率 H_origin 在标准架构下为 0，除非部署了独立的源站加速层或全局一致性哈希；若启用源站 SSD 缓存，H_origin 可提升至 0.1-0.3，从而将 L2 有效命中率 H_L2 从 1-Miss_L1 提升至 1-Miss_L1*(1-0.2)。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

origin server cache hit rate improvement CDN architecture
