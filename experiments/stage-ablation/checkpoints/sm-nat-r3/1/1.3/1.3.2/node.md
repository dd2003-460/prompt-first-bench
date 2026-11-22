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

父节点级核验通过：正交+完备+无冗余（子节点分别针对 Gumbel 和 Frank 两种 Copula 进行独立分析，内容互不重叠（正交）；父节点核心诉求是寻找能建模负相关的替代方案，两个子节点恰好提供了这两个主要替代路径的可行性分析（完备）；两者代表不同的数学结构，非同一参数的不同取值（无冗余）。）

## Search Query

Gumbel copula negative correlation parameter theta formula
