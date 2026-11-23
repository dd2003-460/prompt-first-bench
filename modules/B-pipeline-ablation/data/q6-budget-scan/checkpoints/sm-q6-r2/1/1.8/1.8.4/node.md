# N46: 热点集中程度对命中率的影响：若前 10% 的对象贡献了 80% 的流量（帕累托法则），则仅需缓存 10% 的对象即可达到 >70% 的命中率；该比例直接决定所需

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

热点集中程度对命中率的影响：若前 10% 的对象贡献了 80% 的流量（帕累托法则），则仅需缓存 10% 的对象即可达到 >70% 的命中率；该比例直接决定所需的最小缓存容量 C_min。

## Corrected Claim

热点集中程度对命中率的影响：若前 10% 的对象贡献了 80% 的流量（帕累托法则），则仅需缓存 10% 的对象即可达到 >70% 的命中率；该比例直接决定所需的最小缓存容量 C_min。

## Evidence

先验知识/题面给定，逻辑校验通过：根据帕累托法则（80/20法则），若前10%对象贡献80%流量，缓存这10%对象理论上可覆盖80%的请求，因此命中率>70%在逻辑上成立且量级合理。

## Search Query

Pareto principle CDN cache hit rate top 10 percent objects
