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

父节点级核验未通过：不完备, 有冗余（子节点仅覆盖了自建和公有云两种策略，遗漏了父节点中明确提到的‘混合策略’（Hybrid Strategy）及其P99延迟构成逻辑；此外，两个子节点的公式结构高度相似，仅参数不同，存在结构性冗余。）
