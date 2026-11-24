# N617: T=200ms 工作点下，自建 POP 缓存命中率 H_pop 的最低要求为 0.90，以确保 Miss 请求的回源延迟（~50ms）不会将 P99 推高超过 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N202

## Claim

T=200ms 工作点下，自建 POP 缓存命中率 H_pop 的最低要求为 0.90，以确保 Miss 请求的回源延迟（~50ms）不会将 P99 推高超过 200ms 阈值；若 H_pop < 0.90，需增加 POP 带宽冗余 20% 以补偿 Miss 峰值。

## Corrected Claim

T=200ms 工作点下，自建 POP 缓存命中率 H_pop 的最低要求为 0.90，以确保 Miss 请求的回源延迟（~50ms）不会将 P99 推高超过 200ms 阈值；若 H_pop < 0.90，需增加 POP 带宽冗余 20% 以补偿 Miss 峰值。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN cache hit rate requirement for P99 latency budget 200ms
