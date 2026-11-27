# N19: 对卖家的伤害量化：干预后卖家剩余效用变化 ΔU_seller = U_seller(new_equilibrium) - U_seller(old_equili

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4, N5

## Claim

对卖家的伤害量化：干预后卖家剩余效用变化 ΔU_seller = U_seller(new_equilibrium) - U_seller(old_equilibrium)，其中 U_seller = E[price * probability_of_sale] - cost_of_listing

## Corrected Claim

对卖家的伤害量化：干预后卖家剩余效用变化 ΔU_seller = U_seller(new_equilibrium) - U_seller(old_equilibrium)，其中 U_seller = E[price * probability_of_sale] - cost_of_listing

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：节点1定义基准效用，节点2和3分别定义新均衡下的价格期望和成交概率（两个独立变量），节点4利用前三个节点定义的变量进行效用变化的代数分解（价格效应+数量效应）。各节点职责明确，无内容重叠或矛盾，且完整覆盖了父节点公式中所有关键组成部分（旧均衡、新均衡价格、新均衡概率、最终变化量）。）

## Search Query

seller utility function second-hand platform price intervention impact
