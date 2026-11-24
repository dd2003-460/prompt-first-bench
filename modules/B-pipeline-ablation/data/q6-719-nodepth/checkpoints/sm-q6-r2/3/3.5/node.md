# N21: 流量非线性特征：Cost(Traffic) = a × Traffic^b，其中 b > 1 表示规模不经济，b < 1 表示规模经济，b 值由具体策略和云厂商

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

流量非线性特征：Cost(Traffic) = a × Traffic^b，其中 b > 1 表示规模不经济，b < 1 表示规模经济，b 值由具体策略和云厂商定价决定 [待核验]。

## Corrected Claim

流量非线性特征：Cost(Traffic) = a × Traffic^b，其中 b > 1 表示规模不经济，b < 1 表示规模经济，b 值由具体策略和云厂商定价决定 [待核验]。

## Evidence

父节点级核验未通过：不完备（子节点分别描述了公有云、自建和混合三种不同部署模式下的成本函数特征，彼此之间场景互斥，正交性良好且无冗余。然而，父节点明确指出 b 值由“具体策略和云厂商定价”决定，子节点仅覆盖了部署模式（策略），完全缺失了“云厂商定价机制”这一关键维度（如不同厂商间的定价差异、长期协议折扣等对 a 和 b 的影响），导致覆盖不完备。）

## Search Query

CDN traffic cost nonlinearity power law
