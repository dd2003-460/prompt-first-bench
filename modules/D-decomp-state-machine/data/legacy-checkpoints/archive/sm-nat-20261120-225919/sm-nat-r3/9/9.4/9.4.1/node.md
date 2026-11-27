# N264: 简化估计：若假设前 k_max 个最热对象的平均大小为总体平均大小的 0.5 倍（基于 ρ=-0.3 的经验修正），则 E[S|hit] ≈ 0.5 * E[S

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N100

## Claim

简化估计：若假设前 k_max 个最热对象的平均大小为总体平均大小的 0.5 倍（基于 ρ=-0.3 的经验修正），则 E[S|hit] ≈ 0.5 * E[S|all]，该比值可直接用于 H_byte 计算。

## Corrected Claim

简化估计：若假设前 k_max 个最热对象的平均大小为总体平均大小的 0.5 倍（基于 ρ=-0.3 的经验修正），则 E[S|hit] ≈ 0.5 * E[S|all]，该比值可直接用于 H_byte 计算。

## Evidence

先验知识/题面给定，逻辑校验通过
