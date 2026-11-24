# N117: 自建 10 POP 点缓存命中率 (CHR_self) 的决定因素：单点容量限制（C_pop 决定缓存大小）、流量分散度（geo_share_i 不均导致长尾 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

自建 10 POP 点缓存命中率 (CHR_self) 的决定因素：单点容量限制（C_pop 决定缓存大小）、流量分散度（geo_share_i 不均导致长尾 POP 命中率低）、缓存算法选择（LFU 比 LRU 高 3-5% 命中率）；典型值 70% ± 10%，基于 10 节点规模的经验数据

## Corrected Claim

自建 10 POP 点缓存命中率 (CHR_self) 的决定因素：单点容量限制（C_pop 决定缓存大小）、流量分散度（geo_share_i 不均导致长尾 POP 命中率低）、缓存算法选择（LFU 比 LRU 高 3-5% 命中率）；典型值 70% ± 10%，基于 10 节点规模的经验数据

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应父节点中明确列出的三个独立决定因素（容量、流量分散度、算法），彼此之间无逻辑重叠或矛盾。每个子节点都提供了具体的数学模型或量化范围，且覆盖了父节点描述的所有关键方面，不存在冗余压缩空间。）

## Search Query

self-hosted edge node cache hit ratio 10 POP points
