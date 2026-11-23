# N267: 核心区域自建回源流量绝对值 Traffic_origin_core = 2TB * 0.8 * (1 - 0.90) = 0.16 TB/日（假设核心流量占比8

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N83

## Claim

核心区域自建回源流量绝对值 Traffic_origin_core = 2TB * 0.8 * (1 - 0.90) = 0.16 TB/日（假设核心流量占比80%，自建节点稳态缓存命中率H_self=90%），该数值直接决定自建Origin出口带宽需求。

## Corrected Claim

核心区域自建回源流量绝对值 Traffic_origin_core = 2TB * 0.8 * (1 - 0.90) = 0.16 TB/日（假设核心流量占比80%，自建节点稳态缓存命中率H_self=90%），该数值直接决定自建Origin出口带宽需求。

## Evidence

先验知识/题面给定，逻辑校验通过：2 * 0.8 * 0.1 = 0.16，计算无误，量纲一致。
