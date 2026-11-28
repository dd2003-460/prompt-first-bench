# N62: 设定timestamp过期策略：对于时效性强的领域（如生物医学），半衰期 T_half = 6个月，检索得分乘以衰减因子 exp(-ln2 * Δt / T_h

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

设定timestamp过期策略：对于时效性强的领域（如生物医学），半衰期 T_half = 6个月，检索得分乘以衰减因子 exp(-ln2 * Δt / T_half)；静态领域（如数学）T_half = ∞

## Corrected Claim

设定timestamp过期策略：对于时效性强的领域（如生物医学），半衰期 T_half = 6个月，检索得分乘以衰减因子 exp(-ln2 * Δt / T_half)；静态领域（如数学）T_half = ∞

## Evidence

先验知识/题面给定，逻辑校验通过：指数衰减公式 exp(-ln2 * Δt / T_half) 在 Δt=T_half 时值为 0.5，符合半衰期定义；数学领域视为静态（T_half=∞）符合常识。

## Search Query

knowledge base temporal decay half-life domain specific
