# N31: 缓存容量约束方程的离散求和形式：128GB = Σ_{i=1}^{k} C_s * i^{-1.1}，其中 k 为最大整数使得该和不超过 128GB。利用 Hu

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

缓存容量约束方程的离散求和形式：128GB = Σ_{i=1}^{k} C_s * i^{-1.1}，其中 k 为最大整数使得该和不超过 128GB。利用 Hurwitz zeta 函数近似 Σ_{i=1}^{k} i^{-α} ≈ ζ(α) + k^{1-α}/(1-α) (当 α>1)，可解出 k 的解析近似值。

## Corrected Claim

缓存容量约束方程的离散求和形式：128GB = Σ_{i=1}^{k} C_s * i^{-1.1}，其中 k 为最大整数使得该和不超过 128GB。利用 Hurwitz zeta 函数近似 Σ_{i=1}^{k} i^{-α} ≈ ζ(α) + k^{1-α}/(1-α) (当 α>1)，可解出 k 的解析近似值。

## Evidence

先验知识/题面给定，逻辑校验通过：Hurwitz zeta 函数近似公式在 α>1 时数学上成立，量纲与逻辑自洽。
