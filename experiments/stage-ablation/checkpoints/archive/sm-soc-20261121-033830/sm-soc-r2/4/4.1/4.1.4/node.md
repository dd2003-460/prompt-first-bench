# N69: 候选干预 (B) 动态价格建议的总成本 C_intervention_B = C_tech_B + C_migration_B；C_migration_B 通常

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N17

## Claim

候选干预 (B) 动态价格建议的总成本 C_intervention_B = C_tech_B + C_migration_B；C_migration_B 通常低于 (A)，因为非强制性；需估算卖家接受建议的比例 r_accept 及未接受者的流失率，以计算 C_migration_B = (1-r_accept) * ΔChurn_passive * LTV。

## Corrected Claim

候选干预 (B) 动态价格建议的总成本 C_intervention_B 由技术成本 C_tech_B 和迁移成本 C_migration_B 组成。迁移成本通常与卖家接受建议的比例 r_accept 及未接受者的流失率相关，具体计算模型需根据业务假设定义，例如 C_migration_B 可估算为 (1-r_accept) * ΔChurn_passive * LTV。

## Evidence

[质询]该陈述包含具体的成本计算公式（C_migration_B = (1-r_accept) * ΔChurn_passive * LTV）以及“非强制性导致迁移成本通常低于强制性”的经验性断言。这些属于特定的业务建模假设和经验事实，无法从第一性原理或数学公理中严格推导出来，且缺乏外部来源支持其具体形式和参数定义的准确性。 | 经验事实，逻辑自洽但缺来源支持。公式在量纲上合理（比例 * 流失率差 * 单用户价值 = 成本），但具体模型假设需外部验证。

## Search Query

dynamic pricing suggestion adoption rate seller compliance marketplace non-mandatory intervention cost
