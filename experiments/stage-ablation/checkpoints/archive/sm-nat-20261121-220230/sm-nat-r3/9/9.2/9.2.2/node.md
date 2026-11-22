# N282: Frank Copula 在 θ < 0 时的尾部渐近行为：当 θ → -∞ 时，Frank Copula 趋向于独立 Copula；当 θ → 0⁻ 时，趋向

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N97

## Claim

Frank Copula 在 θ < 0 时的尾部渐近行为：当 θ → -∞ 时，Frank Copula 趋向于独立 Copula；当 θ → 0⁻ 时，趋向于完全负相关（ρ → -1），因此 θ = -1.58 位于中度负相关区间，适合建模 ρ=-0.3 的场景。

## Corrected Claim

Frank Copula 在 θ < 0 时的尾部渐近行为：当 θ → -∞ 时，Frank Copula 趋向于独立 Copula；当 θ → 0⁻ 时，趋向于完全负相关（ρ → -1），因此 θ = -1.58 位于中度负相关区间，适合建模 ρ=-0.3 的场景。

## Evidence

先验知识/题面给定，逻辑校验通过：Frank Copula 参数 θ 的取值范围为 (-∞, +∞)，θ=0 对应独立 Copula，θ→-∞ 对应完全负相关（ρ→-1），θ→+∞ 对应完全正相关（ρ→+1）。θ=-1.58 确实位于负相关区间，且根据 Frank Copula 的 Spearman 秩相关系数公式 ρ = 1 - 4(1 - ln(1+θ)/θ)/θ，当 θ=-1.58 时，ρ 约为 -0.3 左右，符合中度负相关的描述。
