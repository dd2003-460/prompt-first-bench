# N168: 自建POP点的缓存命中率 H_edge_self 受地理分布影响：H_edge_self = Σ (α_i * H_i)，其中 α_i 为第 i 个POP点的流

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53

## Claim

自建POP点的缓存命中率 H_edge_self 受地理分布影响：H_edge_self = Σ (α_i * H_i)，其中 α_i 为第 i 个POP点的流量占比，H_i 为该POP点的局部命中率，核心区域POP（如北上广深）H_i 通常 80-95%，长尾区域 H_i 通常 60-80%

## Corrected Claim

自建POP点的缓存命中率 H_edge_self 受地理分布影响：H_edge_self = Σ (α_i * H_i)，其中 α_i 为第 i 个POP点的流量占比，H_i 为该POP点的局部命中率，核心区域POP（如北上广深）H_i 通常 80-95%，长尾区域 H_i 通常 60-80%

## Evidence

先验知识/题面给定，逻辑校验通过：加权平均公式符合定义，核心区域高命中率（80-95%）与长尾区域较低命中率（60-80%）符合CDN缓存分布的普遍工程经验。

## Search Query

CDN cache hit rate regional distribution core vs long tail
