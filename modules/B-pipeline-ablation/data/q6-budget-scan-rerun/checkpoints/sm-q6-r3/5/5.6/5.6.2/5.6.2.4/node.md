# N296: 客户端DNS缓存过期时间 $T_{dns\_cache}$ 取决于TTL设置，自建POP通常设置TTL=300秒（5分钟）以平衡切换速度与缓存效率；若用户本地D

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N112

## Claim

客户端DNS缓存过期时间 $T_{dns\_cache}$ 取决于TTL设置，自建POP通常设置TTL=300秒（5分钟）以平衡切换速度与缓存效率；若用户本地DNS缓存未过期，切换生效需等待TTL剩余时间，平均等待时间为TTL/2=150秒。

## Corrected Claim

客户端DNS缓存过期时间 $T_{dns\_cache}$ 取决于TTL设置，自建POP通常设置TTL=300秒（5分钟）以平衡切换速度与缓存效率；若用户本地DNS缓存未过期，切换生效需等待TTL剩余时间，平均等待时间为TTL/2=150秒。

## Evidence

先验知识/题面给定，逻辑校验通过：TTL=300s是自建DNS常见配置，平均等待时间TTL/2符合均匀分布假设下的数学推导。

## Search Query

DNS TTL typical value CDN edge cache
