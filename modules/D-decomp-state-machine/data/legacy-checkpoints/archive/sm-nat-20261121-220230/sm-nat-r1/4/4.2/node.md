# N18: LRU 稳态字节命中率下界的修正公式：在负相关 (ρ=-0.3) 下，LRU 缓存的字节命中率 H_byte 不能简单由独立假设下的 H_indep 直接得出，

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

LRU 稳态字节命中率下界的修正公式：在负相关 (ρ=-0.3) 下，LRU 缓存的字节命中率 H_byte 不能简单由独立假设下的 H_indep 直接得出，需引入修正项 Δρ，即 H_byte = H_indep + Δρ(ρ, α, β)，其中 Δρ 量化了‘小对象更热’导致的缓存驱逐效率变化（通常负相关会略微提升 LRU 对小对象的保留率，但降低对大对象的保护，需计算净效应）。

## Corrected Claim

LRU 稳态字节命中率下界的修正公式：在负相关 (ρ=-0.3) 下，LRU 缓存的字节命中率 H_byte 不能简单由独立假设下的 H_indep 直接得出，需引入修正项 Δρ，即 H_byte = H_indep + Δρ(ρ, α, β)，其中 Δρ 量化了‘小对象更热’导致的缓存驱逐效率变化（通常负相关会略微提升 LRU 对小对象的保留率，但降低对大对象的保护，需计算净效应）。

## Evidence

先验知识/题面给定，逻辑校验通过
