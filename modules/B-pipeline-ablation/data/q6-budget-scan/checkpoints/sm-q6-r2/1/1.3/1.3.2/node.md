# N27: 混合策略整体 P99 延迟 = max(P99_self(x), P99_cloud(1-x))，其中 P99_self(x) ≈ 20ms（自建节点），P99

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N6

## Claim

混合策略整体 P99 延迟 = max(P99_self(x), P99_cloud(1-x))，其中 P99_self(x) ≈ 20ms（自建节点），P99_cloud(1-x) ≈ 220ms（公有云加权平均）；因此 P99_total ≈ 220ms，受限于公有云路径的尾部延迟。

## Corrected Claim

混合策略整体 P99 延迟 = max(P99_self(x), P99_cloud(1-x))，其中 P99_self(x) ≈ 20ms（自建节点），P99_cloud(1-x) ≈ 220ms（公有云加权平均）；因此 P99_total ≈ 220ms，受限于公有云路径的尾部延迟。

## Evidence

先验知识/题面给定，逻辑校验通过：混合策略的P99延迟由最慢路径决定，取最大值符合逻辑，数值量级合理。
