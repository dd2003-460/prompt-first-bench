# N131: Infra_Annualized 计算：对于自建策略，Infra_Annualized = Annualized_CapEx + OpEx_Monthly × 

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N38

## Claim

Infra_Annualized 计算：对于自建策略，Infra_Annualized = Annualized_CapEx + OpEx_Monthly × 12，其中 Annualized_CapEx 由 N16 折旧公式得出；对于公有云策略，Infra_Annualized = 0（已包含在 Bandwidth_Monthly 中）；对于混合策略，Infra_Annualized = Core_Pops_Annualized_CapEx + Core_Pops_OpEx_Monthly × 12。

## Corrected Claim

Infra_Annualized 计算：对于自建策略，Infra_Annualized = Annualized_CapEx + OpEx_Monthly × 12，其中 Annualized_CapEx 由 N16 折旧公式得出；对于公有云策略，Infra_Annualized = 0（已包含在 Bandwidth_Monthly 中）；对于混合策略，Infra_Annualized = Core_Pops_Annualized_CapEx + Core_Pops_OpEx_Monthly × 12。

## Evidence

父节点级核验未通过：不完备, 有冗余（1. 正交性：两个子节点描述了不同的硬件配置（全闪存 vs 混合存储），互不重叠，正交性合格。2. 完备性：父节点明确定义了三种策略（自建、公有云、混合），但子节点仅覆盖了‘自建策略’的两个工作点，完全缺失‘公有云’和‘混合策略’的计算示例或说明，导致对父节点定义域的覆盖不完整。3. 冗余：这两个子节点本质上是同一公式（自建策略公式）在不同硬件参数下的实例化。它们并非独立的逻辑分支，而是同一参数空间（CapEx/OpEx）的采样点。在结构上，它们应被归类为‘自建策略’下的参数变体，或者合并为一个带有参数表的节点，而不是作为与‘公有云’、‘混合’并列的一级子节点。）
