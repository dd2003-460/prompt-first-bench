# N90: 公有云 CDN 的 P99 延迟受缓存命中率影响显著：若命中率 H < 80%，回源流量激增导致源站负载上升及回源链路拥塞，P99 延迟可能从 100ms 恶化

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N24

## Claim

公有云 CDN 的 P99 延迟受缓存命中率影响显著：若命中率 H < 80%，回源流量激增导致源站负载上升及回源链路拥塞，P99 延迟可能从 100ms 恶化至 300ms+；需确保源站扩容或优化缓存策略以满足 T < 300ms。

## Corrected Claim

公有云 CDN 的 P99 延迟受缓存命中率影响显著：若命中率 H < 80%，回源流量激增导致源站负载上升及回源链路拥塞，P99 延迟可能从 100ms 恶化至 300ms+；需确保源站扩容或优化缓存策略以满足 T < 300ms。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN cache miss impact on P99 latency origin load congestion
