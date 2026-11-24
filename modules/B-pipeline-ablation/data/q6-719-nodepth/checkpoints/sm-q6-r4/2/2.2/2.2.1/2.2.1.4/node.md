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

父节点级核验未通过：不完备（子节点分别关注用户感知质量（陈旧度）和运营成本（失效同步），维度正交且无冗余。但父节点明确指出了该工作点“适用于非实时内容”这一关键结论/适用边界，而两个子节点仅描述了陈旧度数值和成本数值，均未涵盖“适用性分析”或“业务场景匹配度”这一关键方面，导致信息不完备。）
