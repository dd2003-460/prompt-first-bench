# N64: 非均匀更新下的修正项 C_miss/C_total：若更新率与热度正相关（热对象更常更新），则 C_miss/C_total ≈ 1 + ρ_update_he

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N18

## Claim

非均匀更新下的修正项 C_miss/C_total：若更新率与热度正相关（热对象更常更新），则 C_miss/C_total ≈ 1 + ρ_update_heat * β，导致折损放大；若负相关，则折损减小。需定义 ρ_update_heat 的量化值。

## Corrected Claim

非均匀更新下的修正项 C_miss/C_total：若更新率与热度正相关（热对象更常更新），则 C_miss/C_total ≈ 1 + ρ_update_heat * β，导致折损放大；若负相关，则折损减小。需定义 ρ_update_heat 的量化值。

## Evidence

先验知识/题面给定，逻辑校验通过
