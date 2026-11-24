# N167: H_dynamic 的 frontier 工作点 1（高命中/低新鲜度）：TTL 长（24h），P_TTL_expire ≈ 2%，P_repeat ≈ 25%

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53

## Claim

H_dynamic 的 frontier 工作点 1（高命中/低新鲜度）：TTL 长（24h），P_TTL_expire ≈ 2%，P_repeat ≈ 25%。H_dynamic = 25% * (1 - 2%) = 24.5%。此工作点下，动态/长尾内容大部分命中缓存，但内容更新延迟高达 24h，适用于非实时内容。

## Corrected Claim

H_dynamic 的 frontier 工作点 1（高命中/低新鲜度）：TTL 长（24h），P_TTL_expire ≈ 2%，P_repeat ≈ 25%。H_dynamic = 25% * (1 - 2%) = 24.5%。此工作点下，动态/长尾内容大部分命中缓存，但内容更新延迟高达 24h，适用于非实时内容。

## Evidence

父节点级核验未通过：不完备（子节点分别讨论了'内容陈旧度'（用户体验/质量维度）和'失效同步成本'（运维/经济维度），两者属于不同维度，正交性良好。然而，父节点明确提到该工作点'适用于非实时内容'，这涉及适用场景或业务约束，而子节点仅描述了该工作点下的两个具体指标（P_stale 和 C_invalidate），未覆盖'适用性'或'局限性'这一关键方面，因此不完备。）
