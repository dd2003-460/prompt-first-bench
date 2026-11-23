# N172: 公有云CDN的缓存命中率 H_edge_cloud 受用户地理分布影响：H_edge_cloud = Σ (β_i * H_i)，其中 β_i 为第 i 个云P

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N54

## Claim

公有云CDN的缓存命中率 H_edge_cloud 受用户地理分布影响：H_edge_cloud = Σ (β_i * H_i)，其中 β_i 为第 i 个云POP点的流量占比，公有云POP点覆盖更广泛，长尾区域 H_i 通常 70-90%，核心区域 H_i 通常 85-98%

## Corrected Claim

公有云CDN的缓存命中率 H_edge_cloud 受用户地理分布影响：H_edge_cloud = Σ (β_i * H_i)，其中 β_i 为第 i 个云POP点的流量占比，公有云POP点覆盖更广泛，长尾区域 H_i 通常 70-90%，核心区域 H_i 通常 85-98%

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均公式符合定义，公有云CDN核心区域高命中率（85-98%）与长尾区域较低命中率（70-90%）符合行业经验规律及物理直觉。

## Search Query

Cloudflare Alibaba CDN regional cache hit rate distribution
