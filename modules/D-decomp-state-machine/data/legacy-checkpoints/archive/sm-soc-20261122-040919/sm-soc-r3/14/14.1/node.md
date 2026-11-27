# N411: 卖家单位利润损失率 Δπ_seller 的计算公式：Δπ_seller = 1 - (P_1 × (1 - r)) / (P_0 × (1 - r)) = 1 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N125

## Claim

卖家单位利润损失率 Δπ_seller 的计算公式：Δπ_seller = 1 - (P_1 × (1 - r)) / (P_0 × (1 - r)) = 1 - (P_1 / P_0)。代入 P_0 = 1.2 * P_ref, P_1 = 1.05 * P_ref，计算得 Δπ_seller = 1 - (1.05 / 1.2) = 0.125 (12.5%)。

## Corrected Claim

卖家单位利润损失率 Δπ_seller 的计算公式：Δπ_seller = 1 - (P_1 × (1 - r)) / (P_0 × (1 - r)) = 1 - (P_1 / P_0)。代入 P_0 = 1.2 * P_ref, P_1 = 1.05 * P_ref，计算得 Δπ_seller = 1 - (1.05 / 1.2) = 0.125 (12.5%)。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导中 (1-r) 项正确约分，数值计算 1 - 1.05/1.2 = 1 - 0.875 = 0.125 准确无误。
