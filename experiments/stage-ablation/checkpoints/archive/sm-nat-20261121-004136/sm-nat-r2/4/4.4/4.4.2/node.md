# N58: 热度-大小负相关修正项：若更新概率与热度正相关（如热门对象更易更新），E[Size | Updated] = E[Size] * (1 + ρ_update_s

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

热度-大小负相关修正项：若更新概率与热度正相关（如热门对象更易更新），E[Size | Updated] = E[Size] * (1 + ρ_update_size * β_heat)，其中 ρ_update_size 为更新率与大小的相关性，β_heat 为热度偏斜系数，量化热门小对象更新带来的带宽节省。

## Corrected Claim

热度-大小负相关修正项：若更新概率与热度正相关（如热门对象更易更新），E[Size | Updated] = E[Size] * (1 + ρ_update_size * β_heat)，其中 ρ_update_size 为更新率与大小的相关性，β_heat 为热度偏斜系数，量化热门小对象更新带来的带宽节省。

## Evidence

先验知识/题面给定，逻辑校验通过
