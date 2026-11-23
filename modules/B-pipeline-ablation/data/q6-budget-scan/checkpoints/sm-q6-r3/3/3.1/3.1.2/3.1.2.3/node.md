# N267: 本场景月计费流量计算：日均下载2TB，考虑85%缓存命中率，有效回源流量=2TB*(1-0.85)=0.3TB/日，月回源流量=0.3TB*30=9TB。此9T

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N81

## Claim

本场景月计费流量计算：日均下载2TB，考虑85%缓存命中率，有效回源流量=2TB*(1-0.85)=0.3TB/日，月回源流量=0.3TB*30=9TB。此9TB流量为CDN计费对象，而非原始2TB*30=60TB

## Corrected Claim

本场景月计费流量计算：日均下载2TB，考虑85%缓存命中率，有效回源流量=2TB*(1-0.85)=0.3TB/日，月回源流量=0.3TB*30=9TB。此9TB流量为CDN计费对象，而非原始2TB*30=60TB

## Evidence

先验知识/题面给定，逻辑校验通过：2TB * (1-0.85) = 0.3TB，0.3TB * 30 = 9TB，计算无误且符合CDN计费逻辑。
