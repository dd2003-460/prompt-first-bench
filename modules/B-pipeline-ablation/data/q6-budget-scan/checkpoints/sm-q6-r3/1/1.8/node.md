# N13: 不同策略下P99延迟分布特征：自建策略P99延迟方差较小（σ_self < σ_cloud），公有云策略P99延迟受长尾区域影响较大（P99_cloud > P

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

不同策略下P99延迟分布特征：自建策略P99延迟方差较小（σ_self < σ_cloud），公有云策略P99延迟受长尾区域影响较大（P99_cloud > P99_self），混合策略P99延迟 = max(P99_self_core, P99_cloud_tail)

## Corrected Claim

不同策略下P99延迟分布特征：自建策略P99延迟方差较小（σ_self < σ_cloud），公有云策略P99延迟受长尾区域影响较大（P99_cloud > P99_self），混合策略P99延迟通常介于自建与公有云之间，具体取决于流量分配比例和负载特征。

## Evidence

父节点级核验未通过：不完备（子节点仅覆盖了父节点中‘自建策略’和‘公有云策略’的延迟构成，完全缺失了父节点明确提及的‘混合策略’（P99_delay = max(P99_self_core, P99_cloud_tail)）的分解与定义，导致内容不完备。）
