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

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：节点1定义基准，节点2和3分别量化新均衡下的价格分布和成交概率（两个独立变量），节点4提供将这两个变量结合计算最终效用变化ΔU的数学分解公式（价格效应与数量效应）。内容覆盖了从旧基准到新均衡再到最终差值计算的完整链路，无重复或矛盾。）

## Search Query

seller utility function second-hand platform price intervention impact
