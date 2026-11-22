# N211: C_migration_A (卖家流失迁移成本) = N_sellers_affected * (1 - r_compliance) * ΔChurn_forc

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N68

## Claim

C_migration_A (卖家流失迁移成本) = N_sellers_affected * (1 - r_compliance) * ΔChurn_forced * LTV_seller，其中 r_compliance 为卖家在价格被强制截断后的合规率（预计接近100%，因为无选择权），ΔChurn_forced 为因价格限制直接退出的卖家比例，LTV_seller 为卖家平均生命周期价值

## Corrected Claim

C_migration_A (卖家流失迁移成本) = N_sellers_affected * (1 - r_compliance) * ΔChurn_forced * LTV_seller，其中 r_compliance 为卖家在价格被强制截断后的合规率（预计接近100%，因为无选择权），ΔChurn_forced 为因价格限制直接退出的卖家比例，LTV_seller 为卖家平均生命周期价值

## Evidence

先验知识/题面给定，逻辑校验通过
