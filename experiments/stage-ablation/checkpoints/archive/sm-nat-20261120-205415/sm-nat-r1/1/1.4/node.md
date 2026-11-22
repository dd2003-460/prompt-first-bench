# N9: 缓存空间上限 C=128GB=131,072MB 相对于总数据量 100TB=102,400,000MB 的占比为 0.00128%；在 Pareto(α=1.

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

缓存空间上限 C=128GB=131,072MB 相对于总数据量 100TB=102,400,000MB 的占比为 0.00128%；在 Pareto(α=1.1) 下，缓存覆盖率（按字节）的理论上限由 ∫_0^C f(s)ds / ∫_0^∞ f(s)ds 决定，其中 f(s) 为 Pareto 密度

## Corrected Claim

缓存空间上限 C=128GB=131,072MB 相对于总数据量 100TB=102,400,000MB 的占比为 0.00128%；在 Pareto(α=1.1) 下，缓存覆盖率（按字节）的理论上限由 ∫_0^C f(s)ds / ∫_0^∞ f(s)ds 决定，其中 f(s) 为 Pareto 密度

## Evidence

先验知识/题面给定，逻辑校验通过：128GB=131,072MB，100TB=102,400,000MB，占比计算正确；Pareto分布积分定义符合数学原理
