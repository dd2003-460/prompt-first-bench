# N209: 迁移阻力成本敏感性分析：C_migration_seller = ΔChurn_seller * LTV_seller。若 ΔChurn = 5% 且 LTV 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

迁移阻力成本敏感性分析：C_migration_seller = ΔChurn_seller * LTV_seller。若 ΔChurn = 5% 且 LTV = 10000元，则 C_migration = 500元/卖家；若 ΔChurn = 10% 且 LTV = 5000元，则 C_migration = 500元/卖家。需验证在何种 ΔChurn-LTV 组合下，C_migration 超过平台预期GMV增量的10%，从而构成干预的硬性约束。

## Corrected Claim

迁移阻力成本敏感性分析：C_migration_seller = ΔChurn_seller * LTV_seller。若 ΔChurn = 5% 且 LTV = 10000元，则 C_migration = 500元/卖家；若 ΔChurn = 10% 且 LTV = 5000元，则 C_migration = 500元/卖家。需验证在何种 ΔChurn-LTV 组合下，C_migration 超过平台预期GMV增量的10%，从而构成干预的硬性约束。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 C = ΔChurn * LTV 符合经济学中预期损失的定义；数值计算 5%*10000=500 和 10%*5000=500 准确无误；量纲（比例*货币=货币）合理。
