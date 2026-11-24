# N67: 公有云CDN（如阿里云/Cloudflare）的缓存命中率（95%+）相对于自建POP（85-90%）带来的额外回源流量成本差异，计算公式为：(1-HitRat

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

公有云CDN（如阿里云/Cloudflare）的缓存命中率（95%+）相对于自建POP（85-90%）带来的额外回源流量成本差异，计算公式为：(1-HitRate_Cloud - HitRate_Self) * TotalTraffic * UnitPrice_Source，量化存储投入不足导致的隐性带宽成本。

## Corrected Claim

公有云CDN（如阿里云/Cloudflare）的缓存命中率（95%+）相对于自建POP（85-90%）带来的额外回源流量成本差异，计算公式为：(1-HitRate_Cloud - HitRate_Self) * TotalTraffic * UnitPrice_Source，量化存储投入不足导致的隐性带宽成本。

## Evidence

先验知识/题面给定，逻辑校验通过
