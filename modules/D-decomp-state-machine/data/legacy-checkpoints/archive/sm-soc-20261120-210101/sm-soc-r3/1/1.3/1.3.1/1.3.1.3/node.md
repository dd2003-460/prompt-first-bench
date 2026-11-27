# N152: 下游投影2（长期搜索者）：当买家搜索历史长度 L_search 较长（L_search > 20次点击）时，买家已建立品类价格分布的先验信念，不确定性降低。假设

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N38

## Claim

下游投影2（长期搜索者）：当买家搜索历史长度 L_search 较长（L_search > 20次点击）时，买家已建立品类价格分布的先验信念，不确定性降低。假设 σ_buyer = 0.1 * P_ref。此时 ε_buyer 的分布收敛，买家决策更理性，仅当价格显著低于其保留价格时才停止搜索。这解释了为何高挂价商品在长期搜索者面前依然难以成交，因为噪声无法掩盖价格偏离信号。

## Corrected Claim

下游投影2（长期搜索者）：当买家搜索历史长度 L_search 较长（L_search > 20次点击）时，买家已建立品类价格分布的先验信念，不确定性降低。假设 σ_buyer = 0.1 * P_ref。此时 ε_buyer 的分布收敛，买家决策更理性，仅当价格显著低于其保留价格时才停止搜索。这解释了为何高挂价商品在长期搜索者面前依然难以成交，因为噪声无法掩盖价格偏离信号。

## Evidence

先验知识/题面给定，逻辑校验通过：基于搜索理论（Search Theory），随着搜索次数增加，买家对价格分布的先验信念更新，不确定性（σ）降低，导致决策阈值更精确，符合经济学直觉。

## Search Query

long search history buyer rational decision price sensitivity
