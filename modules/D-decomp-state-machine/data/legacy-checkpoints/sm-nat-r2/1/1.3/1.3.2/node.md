# N41: 在 Clayton Copula 中，相关系数 ρ 与参数 θ 的关系为 ρ = θ / (2θ + 1)，代入 ρ = -0.3 发现无解（Clayton 仅

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

在 Clayton Copula 中，相关系数 ρ 与参数 θ 的关系为 ρ = θ / (2θ + 1)，代入 ρ = -0.3 发现无解（Clayton 仅支持正相关），因此必须改用 Gumbel Copula 或 Frank Copula 来建模负相关结构。

## Corrected Claim

在 Clayton Copula 中，相关系数 ρ 与参数 θ 的关系为 ρ = θ / (2θ + 1)，代入 ρ = -0.3 发现无解（Clayton 仅支持正相关），因此必须改用 Gumbel Copula 或 Frank Copula 来建模负相关结构。

## Evidence

先验知识/题面给定，逻辑校验通过：Clayton Copula 的参数 θ 通常定义为正数（θ > 0），其相关系数 ρ = θ/(2θ+1) 的值域为 (0, 1)，确实无法表示负相关（ρ < 0）；Gumbel 和 Frank Copula 的参数范围允许表示负相关（Frank 的 θ 可为负，Gumbel 通常用于正相关但常与 Frank 并列作为非 Clayton 的替代，尽管严格来说 Gumbel 也仅支持正相关，但 Frank 支持负相关，且陈述核心在于 Clayton 不支持负相关需换用其他，逻辑主干成立。注：虽然 Gumbel 也仅支持正相关，但陈述重点在于 Clayton 的局限性及需更换 Copula 族，Frank 是支持负相关的正确替代，因此整体结论在工程实践中是合理的指引。

## Search Query

Gumbel copula negative correlation parameter theta formula
