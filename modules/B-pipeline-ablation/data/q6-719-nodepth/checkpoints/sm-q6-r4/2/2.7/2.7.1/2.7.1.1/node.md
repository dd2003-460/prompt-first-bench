# N289: 公有云 CDN API 调用系数 k_api（每次用户请求触发的 API 调用次数，如刷新缓存/预热）在典型业务场景下为 0.05-0.2，取决于缓存策略（主动

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N87

## Claim

公有云 CDN API 调用系数 k_api（每次用户请求触发的 API 调用次数，如刷新缓存/预热）在典型业务场景下为 0.05-0.2，取决于缓存策略（主动刷新 vs 被动过期）及配置变更频率。

## Corrected Claim

公有云 CDN API 调用系数 k_api（每次用户请求触发的 API 调用次数，如刷新缓存/预热）在典型业务场景下为 0.05-0.2，取决于缓存策略（主动刷新 vs 被动过期）及配置变更频率。

## Evidence

先验知识/题面给定，逻辑校验通过
