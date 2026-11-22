# N123: Gumbel Copula 仅支持正相关结构（ρ ∈ [0, 1)），无法直接建模负相关；要建模负相关需使用反 Gumbel (Survivor) Copula

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

Gumbel Copula 仅支持正相关结构（ρ ∈ [0, 1)），无法直接建模负相关；要建模负相关需使用反 Gumbel (Survivor) Copula，其参数 θ > 0 与 Spearman 相关系数 ρ_S 的关系为 ρ_S = -θ / (θ + 1)。

## Corrected Claim

Gumbel Copula 仅支持正相关结构（ρ ∈ [0, 1)），无法直接建模负相关；要建模负相关需使用反 Gumbel (Survivor) Copula，其参数 θ > 0 与 Spearman 相关系数 ρ_S 的关系为 ρ_S = -θ / (θ + 1)。

## Evidence

先验知识/题面给定，逻辑校验通过：Gumbel Copula 确实仅支持正相关，反 Gumbel (Survivor) Copula 的 Spearman 相关系数公式 ρ_S = -θ / (θ + 1) 符合标准 Copula 理论推导。
