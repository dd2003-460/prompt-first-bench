# N52: H_static 的数值代入：基于 N11 和 N21，H_static ≈ 0.85-0.92（典型 CDN 边缘节点），代入 H_effective 公式，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N16

## Claim

H_static 的数值代入：基于 N11 和 N21，H_static ≈ 0.85-0.92（典型 CDN 边缘节点），代入 H_effective 公式，当 P_revalidate=0 时，H_effective = 0.85 * (1 - 0.01) ≈ 0.8415，折损率 δ = 1 - 0.8415/0.85 ≈ 1.0%。

## Corrected Claim

H_static 的数值代入：基于 N11 和 N21，H_static ≈ 0.85-0.92（典型 CDN 边缘节点），代入 H_effective 公式，当 P_revalidate=0 时，H_effective = 0.85 * (1 - 0.01) ≈ 0.8415，折损率 δ = 1 - 0.8415/0.85 ≈ 1.0%。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 0.85 * 0.99 = 0.8415 正确，折损率 (0.85 - 0.8415) / 0.85 ≈ 1% 符合数学逻辑，且 CDN 边缘节点静态资源命中率 0.85-0.92 属于合理的工程经验范围。
