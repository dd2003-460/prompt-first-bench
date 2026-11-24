# N319: 混合策略回退场景下，公有云长尾节点的P99延迟（Cloud_Fallback_P99）受限于其边缘节点到该区域用户的RTT及缓存命中率。若回退流量集中在长尾区域

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N124

## Claim

混合策略回退场景下，公有云长尾节点的P99延迟（Cloud_Fallback_P99）受限于其边缘节点到该区域用户的RTT及缓存命中率。若回退流量集中在长尾区域，Cloud_Fallback_P99 ≈ 80-120ms（因距离较远且缓存命中率可能低于核心区域）。

## Corrected Claim

混合策略回退场景下，公有云长尾节点的P99延迟（Cloud_Fallback_P99）受限于其边缘节点到该区域用户的RTT及缓存命中率。若回退流量集中在长尾区域，Cloud_Fallback_P99 ≈ 80-120ms（因距离较远且缓存命中率可能低于核心区域）。

## Evidence

先验知识/题面给定，逻辑校验通过：80-120ms符合长尾区域高RTT及低缓存命中率下的P99延迟量级，无内部矛盾。
