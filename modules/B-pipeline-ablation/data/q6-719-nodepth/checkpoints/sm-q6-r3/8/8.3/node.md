# N133: Ops_Monthly 计算：Ops_Monthly = Staff_Cost_Monthly + Tool_Cost_Monthly，对于公有云策略，Ops_

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

Ops_Monthly 计算：Ops_Monthly = Staff_Cost_Monthly + Tool_Cost_Monthly，对于公有云策略，Ops_Monthly ≈ 0（仅基础托管费）；对于自建策略，Ops_Monthly = 105k 元/月（来自 N26）；对于混合策略，Ops_Monthly = 5 POP 对应的运维成本（约 52.5k 元/月，按 5/10 比例分摊 N26 数值）。

## Corrected Claim

Ops_Monthly 计算：Ops_Monthly = Staff_Cost_Monthly + Tool_Cost_Monthly，对于公有云策略，Ops_Monthly ≈ 0（仅基础托管费）；对于自建策略，Ops_Monthly = 105k 元/月（来自 N26）；对于混合策略，Ops_Monthly = 5 POP 对应的运维成本（约 52.5k 元/月，按 5/10 比例分摊 N26 数值）。

## Evidence

父节点级核验未通过：不完备, 有冗余（父节点明确包含三种策略（公有云、自建、混合），但子节点仅覆盖前两种，缺失了‘混合策略’这一关键分支，导致完备性不足。此外，子节点本质上是同一参数 Ops_Monthly 在不同策略下的具体取值，属于参数枚举而非结构分解，存在冗余。）
