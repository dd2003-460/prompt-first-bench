# N22: Cloudflare 在全球范围内的 P99 延迟 SLA 承诺值通常为 < 100ms（核心区域）至 < 200ms（边缘区域），具体数值取决于用户到最近 P

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

Cloudflare 在全球范围内的 P99 延迟 SLA 承诺值通常为 < 100ms（核心区域）至 < 200ms（边缘区域），具体数值取决于用户到最近 POP 的距离，[时效待核]。

## Corrected Claim

Cloudflare 的官方 SLA 主要承诺 100% 可用性（Uptime），并未在通用 SLA 中明确承诺具体的 P99 延迟数值（如 <100ms 或 <200ms）。实际 P99 延迟取决于用户地理位置、网络状况及具体订阅层级，通常核心区域表现优于边缘区域，但具体数值需参考实时监测数据或特定服务条款。

## Evidence

[质询]Cloudflare 官方 SLA 主要承诺的是可用性（Uptime）而非具体的 P99 延迟数值；具体的延迟表现受网络状况、用户位置及具体服务类型影响极大，且不同层级（Free/Pro/Business/Enterprise）的服务标准不同，直接断言存在统一的 '<100ms 至 <200ms' 的 SLA 承诺值缺乏官方文档支持，属于将经验观测值或营销宣传误读为合同级 SLA 承诺。 | 来源 [1] 和 [3] 显示 Cloudflare 的 SLA 主要关注 100% Uptime 和支持服务，未提及具体的 P99 延迟数值承诺；来源 [2] 显示平均响应时间为 248ms，虽为第三方监测数据，但暗示实际延迟可能高于声称的 100-200ms 范围，且无来源直接支持该具体数值为 SLA 承诺。

## Search Query

Cloudflare P99 latency SLA global 2024

## Retrieval Sources

- {'url': 'https://www.cloudflare.com/business-sla/&rut=072aa4fd9092d66abed20a612b0dbbf7027ff325dcd2200658d00ce6146a9293', 'type': 'ddg', 'title': 'Business Service Level Agreement | Cloudflare'}
- {'url': 'https://labs.parlon.io/site/cloudflare&rut=34a08e8e9682f641a2446fc288fe4bccda19016ed03558ec83a25d99868f8a7f', 'type': 'ddg', 'title': 'Cloudflare Performance — 24hr Global Latency | Parlon Labs'}
- {'url': 'https://www.cloudflare.com/enterprise-support-sla/&rut=5d295d8b39466cec9b57d01acf91f975c754095fd690ccd8a800451fbd10defa', 'type': 'ddg', 'title': 'Enterprise Subscription Service Level Agreement | Cloudflare'}
