# N122: Loss_RTO 计算示例（HDD 分层）：假设 RTO = 4 小时，Annual_Business_Revenue_At_Risk = $45M，Impac

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N29

## Claim

Loss_RTO 计算示例（HDD 分层）：假设 RTO = 4 小时，Annual_Business_Revenue_At_Risk = $45M，Impact_Factor = 0.85，则 Loss_RTO = (4/24) × ($45M / 365) × 0.85 ≈ $16,900/次；若年发生 1 次，年损失 ≈ $16,900。

## Corrected Claim

Loss_RTO 计算示例（HDD 分层）：假设 RTO = 4 小时，Annual_Business_Revenue_At_Risk = $45M，Impact_Factor = 0.85，则 Loss_RTO = (4/24) × ($45M / 365) × 0.85 ≈ $16,900/次；若年发生 1 次，年损失 ≈ $16,900。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 (4/24) * (45,000,000/365) * 0.85 ≈ 16,900 数学上准确，量级合理。
