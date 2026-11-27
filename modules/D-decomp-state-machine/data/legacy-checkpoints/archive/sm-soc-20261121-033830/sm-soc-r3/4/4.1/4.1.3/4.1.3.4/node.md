# N213: C_migration_B (动态建议的卖家流失成本) = N_sellers * (1 - r_accept) * ΔChurn_passive * LTV_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N68

## Claim

C_migration_B (动态建议的卖家流失成本) = N_sellers * (1 - r_accept) * ΔChurn_passive * LTV_seller，其中 r_accept 为卖家采纳算法建议的价格调整比例（参考N69需估算，通常低于100%），ΔChurn_passive 为因未采纳建议导致竞争力下降而自然流失的比例，通常显著低于ΔChurn_forced

## Corrected Claim

C_migration_B (动态建议的卖家流失成本) = N_sellers * (1 - r_accept) * ΔChurn_passive * LTV_seller，其中 r_accept 为卖家采纳算法建议的价格调整比例（参考N69需估算，通常低于100%），ΔChurn_passive 为因未采纳建议导致竞争力下降而自然流失的比例，通常显著低于ΔChurn_forced

## Evidence

先验知识/题面给定，逻辑校验通过
