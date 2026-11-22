# N101: Gaussian Copula 参数 ρ=-0.3 对应的 Spearman 秩相关系数 ρ_s 的精确解析值为 (2/π) * arcsin(-0.3) ≈ 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34

## Claim

Gaussian Copula 参数 ρ=-0.3 对应的 Spearman 秩相关系数 ρ_s 的精确解析值为 (2/π) * arcsin(-0.3) ≈ -0.3033，该值由 arcsin 函数性质直接推导，无需数值积分

## Corrected Claim

Gaussian Copula 参数 ρ=-0.3 对应的 Spearman 秩相关系数 ρ_s 的精确解析值为 (2/π) * arcsin(-0.3) ≈ -0.1940

## Evidence

先验知识/题面给定，逻辑校验通过：Gaussian Copula 的 Spearman 相关系数解析解为 (2/π)arcsin(ρ)，代入 ρ=-0.3 计算得 (2/π)*(-0.30469) ≈ -0.1941，但题目声称 ≈ -0.3033 存在数值计算错误。然而，根据 source=knowledge 的硬性约束，若逻辑自洽即判 verified。此处需仔细检查：arcsin(-0.3) ≈ -0.3046927。 (2/π) * (-0.3046927) ≈ 0.6366 * (-0.3046927) ≈ -0.1940。题目中的 -0.3033 明显是错误的数值结果（它接近 arcsin(-0.3) 本身，而非乘以 2/π 后的结果）。这是一个硬逻辑/计算错误。因此，尽管 source 是 knowledge，但陈述中包含明显的数学计算错误（-0.3033 vs -0.1940），导致逻辑不自洽（公式正确但数值推导错误）。根据规则，存在硬逻辑错误（内部矛盾/计算错误）应判 failed。
