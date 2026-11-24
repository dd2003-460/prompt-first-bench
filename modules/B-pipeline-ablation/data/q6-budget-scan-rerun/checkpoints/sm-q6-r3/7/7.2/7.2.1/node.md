# N368: 自建 POP 单点容量对 CHR 的约束：CHR_self = min(CHR_theoretical, C_pop / (B_total_pop / CHR_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N117

## Claim

自建 POP 单点容量对 CHR 的约束：CHR_self = min(CHR_theoretical, C_pop / (B_total_pop / CHR_target))，其中 C_pop 为单点缓存容量，B_total_pop 为单点总带宽，CHR_target 为目标命中率；若 C_pop 不足（如仅 10TB 缓存），CHR 被容量限制在 70% 以下，即使理论命中率可达 85%。

## Corrected Claim

自建 POP 单点容量对 CHR 的约束：CHR_self = min(CHR_theoretical, C_pop / (B_total_pop / CHR_target))，其中 C_pop 为单点缓存容量，B_total_pop 为单点总带宽，CHR_target 为目标命中率；若 C_pop 不足（如仅 10TB 缓存），CHR 被容量限制在 70% 以下，即使理论命中率可达 85%。

## Evidence

先验知识/题面给定，逻辑校验通过
