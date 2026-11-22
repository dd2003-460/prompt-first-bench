# N64: 使用 Clayton Copula 建模 S 和 H 的联合分布，参数 θ 需满足 Corr(S, H) = -0.3。由于 Clayton Copula 仅能

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N17

## Claim

使用 Clayton Copula 建模 S 和 H 的联合分布，参数 θ 需满足 Corr(S, H) = -0.3。由于 Clayton Copula 仅能表示正相关（θ > 0 时 Corr > 0），无法直接建模负相关，因此必须改用 Gumbel 或 Frank Copula，或采用反 Clayton 变换，具体 θ 值需通过数值求解 Corr(S, H; θ) = -0.3 获得，预计 θ ≈ -0.5 至 -0.8 范围。

## Corrected Claim

使用 Clayton Copula 建模 S 和 H 的联合分布，参数 θ 需满足 Corr(S, H) = -0.3。由于 Clayton Copula 仅能表示正相关（θ > 0 时 Corr > 0），无法直接建模负相关，因此必须改用 Frank Copula（θ < 0）或采用反 Clayton 变换（如使用 1-S 或 1-H 的边际分布）。若使用 Frank Copula，具体 θ 值需通过数值求解 Corr(S, H; θ) = -0.3 获得，预计 θ 约为 -2.5 至 -3.0 范围（具体值取决于精确求解）。

## Evidence

[质询]Gumbel Copula 同样仅能表示正相关（θ > 0 时 Corr > 0），无法直接建模负相关；Frank Copula 虽可表示负相关，但 θ ≈ -0.5 至 -0.8 的数值范围对于 Frank Copula 而言通常对应极弱的相关性（接近 0），远达不到 -0.3 的强度，且该数值范围并非通过标准数值求解得出的典型结果，存在严重的参数量级错误。 | 逻辑校验失败：Gumbel Copula 数学性质决定其只能生成正相关，建议改用 Gumbel 建模负相关在逻辑上自相矛盾；Frank Copula 在 θ ∈ [-0.5, -0.8] 区间内的相关系数远小于 -0.3（通常接近 0），数值量级不合理。

## Search Query

Clayton Copula negative correlation parameter theta value
