# N127: 当 R_ws < 1 时，MissRate 下界退化为 0，此时需引入时间局部性修正项 τ = T_resident / T_cooldown，修正后 Miss

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N40

## Claim

当 R_ws < 1 时，MissRate 下界退化为 0，此时需引入时间局部性修正项 τ = T_resident / T_cooldown，修正后 MissRate ≈ max(0, 1 - 1/(R_ws * τ))

## Corrected Claim

该公式为特定场景下的经验修正项，非普适理论下界；在 R_ws < 1 时，MissRate 下界是否退化为 0 取决于具体缓存替换策略及时间局部性模型，不能简单由该公式推导。

## Evidence

[质询]该公式缺乏通用的理论推导支持，且量纲/逻辑存在疑点：当 R_ws < 1 时，1/(R_ws * τ) 可能大于 1，导致 max(0, ...) 为 0，这与“引入修正项以反映时间局部性影响”的直觉相悖（通常时间局部性应降低 miss rate，而非直接归零或产生非单调行为）；此外，τ 的定义 T_resident / T_cooldown 在标准缓存理论中无明确对应，疑似特定场景下的经验拟合公式而非普适定律。 | 先验知识/题面给定，但逻辑校验发现公式在边界条件（R_ws < 1）下的行为与常规缓存模型直觉不符，且缺乏标准理论支撑，无法确认为普适事实。
