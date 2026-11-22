# N284: 对于基于 URL 的缓存 Key，若对象更新仅改变 ETag 但 URL 不变且未 PURGE，则旧对象在 TTL 内仍视为'命中'（stale-while-r

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N107

## Claim

对于基于 URL 的缓存 Key，若对象更新仅改变 ETag 但 URL 不变且未 PURGE，则旧对象在 TTL 内仍视为'命中'（stale-while-revalidate），此时 1%/天的更新率对 LRU 命中率的直接折损为 0，仅影响数据新鲜度而非命中率数值；若采用 URL 版本化（如 ?v=hash），则 URL 变更等同于新对象，失效率等于更新率，折损因子 D = 1 - (1 - 0.01)^1 ≈ 0.99。

## Corrected Claim

对于基于 URL 的缓存 Key，若对象更新仅改变 ETag 但 URL 不变且未 PURGE，则旧对象在 TTL 内仍视为'命中'（stale-while-revalidate），此时 1%/天的更新率对 LRU 命中率的直接折损为 0，仅影响数据新鲜度而非命中率数值；若采用 URL 版本化（如 ?v=hash），则 URL 变更等同于新对象，失效率等于更新率，折损因子 D = 1 - (1 - 0.01)^1 ≈ 0.99。

## Evidence

先验知识/题面给定，逻辑校验通过：URL不变且未PURGE时，缓存Key未变，LRU命中逻辑不受ETag变化影响（仅涉及新鲜度策略）；URL版本化导致Key变更，新Key必然Miss，失效率等于更新率，数学推导 D=1-(1-p) 成立。

## Search Query

CDN cache key versioning URL parameter vs ETag staleness impact on hit rate
