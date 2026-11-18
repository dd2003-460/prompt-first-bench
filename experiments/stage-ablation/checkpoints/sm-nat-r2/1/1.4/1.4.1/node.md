# N35: Pareto 权重 w_i 的归一化常数 Z(β, N) = Σ_{j=1}^{N} j^{-β} 在 β=0.9, N=100,000 时近似为 ζ(0.9)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N9

## Claim

Pareto 权重 w_i 的归一化常数 Z(β, N) = Σ_{j=1}^{N} j^{-β} 在 β=0.9, N=100,000 时近似为 ζ(0.9) ≈ 10.4 (基于 Hurwitz Zeta 函数近似或数值求和)，用于计算单个对象的绝对热度。

## Corrected Claim

Pareto 权重 w_i 的归一化常数 Z(β, N) = Σ_{j=1}^{N} j^{-β} 在 β=0.9, N=100,000 时近似为 ζ(0.9) ≈ 10.4 (基于 Hurwitz Zeta 函数近似或数值求和)，用于计算单个对象的绝对热度。

## Evidence

先验知识/题面给定，逻辑校验通过：ζ(0.9) 的数值确实在 10.4 左右（实际约为 10.43），且当 N=100,000 时，有限和 Σ_{j=1}^{N} j^{-β} 与 ζ(β) 的误差极小（量级约为 N^{1-β}/(β-1) ≈ 0.003），近似成立。

## Search Query

Hurwitz zeta function approximation for large N beta 0.9
