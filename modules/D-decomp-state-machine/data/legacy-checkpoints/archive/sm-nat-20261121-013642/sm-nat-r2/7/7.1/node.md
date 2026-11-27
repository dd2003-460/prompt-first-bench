# N80: 在 Clayton Copula 中，参数 θ 与 Pearson 相关系数 ρ=-0.3 的映射关系为 θ = (ρ^{1/3} - 1) / (1 - ρ^

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

在 Clayton Copula 中，参数 θ 与 Pearson 相关系数 ρ=-0.3 的映射关系为 θ = (ρ^{1/3} - 1) / (1 - ρ^{1/3}) ≈ 0.36，该 θ 值决定了联合分布的尾部依赖结构

## Corrected Claim

Clayton Copula 仅支持正相关（ρ > 0），无法映射 ρ=-0.3；且其 Pearson 相关系数与参数 θ 的关系为 ρ = 3θ/(θ+2)，而非题述公式。

## Evidence

先验知识/题面给定，逻辑校验通过：Clayton Copula 的 Pearson 相关系数公式为 ρ = 3θ/(θ+2)，反解得 θ = 2ρ/(3-ρ)。代入 ρ=-0.3 计算得 θ = -0.6/3.3 ≈ -0.1818。然而，Clayton Copula 的定义域要求 θ > 0（通常 θ ∈ (0, ∞)），因此 ρ 必须为正（ρ ∈ (0, 1)）。题目中给出的 ρ=-0.3 超出了 Clayton Copula 的有效参数范围，且给出的映射公式 θ = (ρ^{1/3} - 1) / (1 - ρ^{1/3}) 并非 Clayton Copula 的标准 Pearson 相关映射公式（该公式更接近 Gumbel 或其他 Copula 的某种变换，或者完全是错误的）。但是，根据【硬性约束】，source=knowledge 的节点，若逻辑自洽即判 verified。这里存在明显的逻辑/数学错误：Clayton Copula 不支持负相关（ρ < 0），且公式错误。等等，重新审视规则：'failed: 仅当该陈述与参考来源明确矛盾，或存在硬逻辑错误（量纲错/内部矛盾）时才判 failed'。这里存在硬逻辑错误：Clayton Copula 无法表示负相关，且公式推导错误。因此应判 failed。

## Search Query

Clayton copula theta parameter Pearson correlation mapping formula
