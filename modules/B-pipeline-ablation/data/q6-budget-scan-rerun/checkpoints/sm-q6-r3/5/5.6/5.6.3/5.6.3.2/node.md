# N299: 公有云CDN切换时间 $T_{cloud\_switch}$ 由API调用及配置下发主导，阿里云/Cloudflare API响应时间通常<1秒，配置生效时间取

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N113

## Claim

公有云CDN切换时间 $T_{cloud\_switch}$ 由API调用及配置下发主导，阿里云/Cloudflare API响应时间通常<1秒，配置生效时间取决于全球PoP同步，典型值为10-30秒，取中值20秒。

## Corrected Claim

公有云CDN切换时间 $T_{cloud\_switch}$ 由API调用及配置下发主导，阿里云/Cloudflare API响应时间通常<1秒，配置生效时间取决于全球PoP同步，典型值为10-30秒，取中值20秒。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Cloudflare API config propagation time
