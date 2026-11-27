# N283: 在标准 HTTP/CDN 架构中，'更新'导致的缓存失效（Invalidate）通常由客户端或源站发送 PURGE 请求或设置较短的 TTL 触发，而非仅依赖 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N107

## Claim

在标准 HTTP/CDN 架构中，'更新'导致的缓存失效（Invalidate）通常由客户端或源站发送 PURGE 请求或设置较短的 TTL 触发，而非仅依赖 ETag 变更；若未显式 PURGE，LRU 的'有效命中率'折损因子 D 应基于 TTL 过期率而非内容变更率计算，公式为 D = 1 - e^(-1/TTL)。

## Corrected Claim

在标准 HTTP/CDN 架构中，'更新'导致的缓存失效通常由 PURGE 请求或 TTL 过期触发。若未显式 PURGE，缓存命中率受 TTL 过期率影响，但具体折损因子 D 需根据请求到达率与 TTL 的比值（如泊松过程模型）计算，而非简单的 1 - e^(-1/TTL)。

## Evidence

[质询]公式 D = 1 - e^(-1/TTL) 存在严重的量纲错误（TTL 为时间单位，指数部分必须无量纲），且该公式并非缓存理论中的标准定义，属于非标准的经验性简化或错误推导。 | 先验知识/题面给定，逻辑校验未通过：公式量纲不一致，且缺乏标准理论支持。

## Search Query

CDN cache invalidation mechanism PURGE vs ETag change TTL expiry
