# N29: 回源策略对 P99 的影响：Cache-Aside 模式下，未命中请求的回源延迟 L_origin = L_origin_base + L_backhaul。若

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

回源策略对 P99 的影响：Cache-Aside 模式下，未命中请求的回源延迟 L_origin = L_origin_base + L_backhaul。若自建 POP 回源中心机房，L_backhaul_self ≈ 20-50 ms；若公有云 CDN 回源，L_backhaul_cloud ≈ 10-30 ms（同区域优化）。P99 受未命中率 (1-H) 放大：L_P99 ≈ H*L_cache + (1-H)*L_origin。

## Corrected Claim

回源策略对 P99 的影响：Cache-Aside 模式下，未命中请求的回源延迟 L_origin = L_origin_base + L_backhaul。若自建 POP 回源中心机房，L_backhaul_self ≈ 20-50 ms；若公有云 CDN 回源，L_backhaul_cloud ≈ 10-30 ms（同区域优化）。P99 受未命中率 (1-H) 放大：L_P99 ≈ H*L_cache + (1-H)*L_origin。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN origin fetch latency impact on p99 tail latency
