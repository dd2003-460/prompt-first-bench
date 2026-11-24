# N174: 对象大小分布对缓存命中率的影响机制：大对象（>10MB）占用缓存空间但请求频率低，导致空间命中率（Space Hit Rate）低于请求命中率（Request 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

对象大小分布对缓存命中率的影响机制：大对象（>10MB）占用缓存空间但请求频率低，导致空间命中率（Space Hit Rate）低于请求命中率（Request Hit Rate），需引入对象大小加权因子 w_size 修正 N129 公式

## Corrected Claim

对象大小分布对缓存命中率的影响机制：大对象（>10MB）占用缓存空间但请求频率低，导致空间命中率（Space Hit Rate）低于请求命中率（Request Hit Rate），需引入对象大小加权因子 w_size 修正 N129 公式

## Evidence

先验知识/题面给定，逻辑校验通过：大对象低频访问导致空间占用与请求频率不匹配，空间命中率低于请求命中率符合缓存基本原理，引入加权因子修正公式逻辑自洽。

## Search Query

cache hit rate vs object size distribution CDN
