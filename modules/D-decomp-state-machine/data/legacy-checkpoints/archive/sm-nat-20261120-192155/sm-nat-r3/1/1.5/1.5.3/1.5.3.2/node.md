# N92: C_s 在命中率比值中的消去证明：H = (C_r * C_s * Σ_{i∈C} i^{-2.0}) / (C_r * C_s * Σ_{i∈U} i^{-2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

C_s 在命中率比值中的消去证明：H = (C_r * C_s * Σ_{i∈C} i^{-2.0}) / (C_r * C_s * Σ_{i∈U} i^{-2.0}) = Σ_{i∈C} i^{-2.0} / Σ_{i∈U} i^{-2.0}，因此 C_s 不影响 H 的数值，但 C_s 决定了缓存容量约束方程 128GB = C_s * Σ_{i=1}^k i^{-1.1} 中 k 的具体数值，进而影响 H 的输入参数 k。

## Corrected Claim

C_s 在命中率比值中的消去证明：H = (C_r * C_s * Σ_{i∈C} i^{-2.0}) / (C_r * C_s * Σ_{i∈U} i^{-2.0}) = Σ_{i∈C} i^{-2.0} / Σ_{i∈U} i^{-2.0}，因此 C_s 不影响 H 的数值，但 C_s 决定了缓存容量约束方程 128GB = C_s * Σ_{i=1}^k i^{-1.1} 中 k 的具体数值，进而影响 H 的输入参数 k。

## Evidence

先验知识/题面给定，逻辑校验通过：代数上分子分母同乘常数 C_s 确实消去，且 C_s 作为容量约束中的系数必然影响解出的 k 值，进而影响求和项，逻辑自洽。
