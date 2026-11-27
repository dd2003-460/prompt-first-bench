# N248: 工作点1（ρ=0 基准）：当 ρ=0 时，M_byte=1.0。字节命中率 H_byte_0 仅由容量约束 k_max 决定。在 Pareto(β=0.9) 下

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N92

## Claim

工作点1（ρ=0 基准）：当 ρ=0 时，M_byte=1.0。字节命中率 H_byte_0 仅由容量约束 k_max 决定。在 Pareto(β=0.9) 下，若 k_max/N = 0.5，则 H_byte_0 ≈ 1 - (0.5)^0.1 ≈ 0.933。此为无相关性假设下的基准值。

## Corrected Claim

工作点1（ρ=0 基准）：当 ρ=0 时，M_byte=1.0。字节命中率 H_byte_0 仅由容量约束 k_max 决定。在 Pareto(β=0.9) 下，若 k_max/N = 0.5，则 H_byte_0 ≈ 1 - (0.5)^0.1 ≈ 0.933。此为无相关性假设下的基准值。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布尾部概率公式应用正确，数值计算准确（1 - 0.5^0.1 ≈ 0.933），符合无相关性假设下的基准定义。
