# N137: 计算最终有效命中率 H_eff 的折损项：结合 N70 的 P_invalid ≈ 0.2865% 和修正后的 H_original ≈ 1，H_eff ≈ 1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N56

## Claim

计算最终有效命中率 H_eff 的折损项：结合 N70 的 P_invalid ≈ 0.2865% 和修正后的 H_original ≈ 1，H_eff ≈ 1 - 0.002865 = 0.997135 (99.71%)；此折损主要源于对象更新导致的缓存失效，而非容量不足或替换策略次优。

## Corrected Claim

计算最终有效命中率 H_eff 的折损项：结合 N70 的 P_invalid ≈ 0.2865% 和修正后的 H_original ≈ 1，H_eff ≈ 1 - 0.002865 = 0.997135 (99.71%)；此折损主要源于对象更新导致的缓存失效，而非容量不足或替换策略次优。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 1 - 0.002865 = 0.997135 正确，且折损归因于对象更新导致的失效符合缓存机制逻辑。
