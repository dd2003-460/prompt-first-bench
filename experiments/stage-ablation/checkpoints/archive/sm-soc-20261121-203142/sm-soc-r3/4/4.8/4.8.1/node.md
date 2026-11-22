# N83: 买家保留效用 R_buyer 的量化定义：R_buyer = E[V - P_market] - C_search_base，即买家在无摩擦市场下的期望剩余；需

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N22

## Claim

买家保留效用 R_buyer 的量化定义：R_buyer = E[V - P_market] - C_search_base，即买家在无摩擦市场下的期望剩余；需计算该值占 P_market 的比例 ρ_buyer = R_buyer/P_market 作为分母基准。

## Corrected Claim

买家保留效用 R_buyer 的量化定义：R_buyer = E[V - P_market] - C_search_base，即买家在无摩擦市场下的期望剩余；需计算该值占 P_market 的比例 ρ_buyer = R_buyer/P_market 作为分母基准。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点实质上是同一参数组合（C_search_base, E[V-P_market]）在不同取值下的计算结果，属于同一公式的实例化而非独立维度的分解；且父节点要求量化定义及比例计算，子节点仅提供了三个特定数值案例，未涵盖定义本身的逻辑结构或通用计算规则，导致完备性不足且存在结构性冗余。）

## Search Query

buyer consumer surplus baseline second-hand market
