# N27: 混合策略整体 P99 延迟 = max(P99_self(x), P99_cloud(1-x))，其中 P99_self(x) ≈ 20ms（自建节点），P99

- **status**: pending
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

父节点级核验未通过：不完备（子节点存在逻辑断层和覆盖缺失。1. 父节点明确指出整体P99受限于'公有云路径'(220ms)，但三个子节点全部聚焦于'自建节点'的延迟、覆盖和带宽，完全未涉及公有云侧的延迟构成或优化，导致无法解释父节点中P99_cloud(1-x)的具体来源及为何其为瓶颈。2. 父节点公式使用 max() 逻辑，意味着整体延迟由最慢路径决定，子节点2中关于'加权后贡献'的计算（0.2 * 180ms）与 max() 逻辑在数学模型上存在冲突（max通常不直接对加权值运算，而是对分位数或路径延迟取最大），且未说明如何从子节点数据推导到父节点的最终220ms结论。）
