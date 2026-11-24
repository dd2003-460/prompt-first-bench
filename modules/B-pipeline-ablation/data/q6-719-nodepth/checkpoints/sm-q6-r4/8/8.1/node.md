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

父节点级核验未通过：不完备, 有冗余（子节点仅覆盖了父节点中‘自建策略’的两种配置，缺失了‘公有云策略’（Infra_Annualized=0）和‘混合策略’（Core_Pops部分）的计算示例，导致覆盖不完备；同时，两个子节点本质上是同一公式（自建策略）在不同硬件参数下的实例化，属于参数取值的枚举，存在结构性冗余。）
