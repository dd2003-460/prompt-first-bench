# N187: 工作点B（Gumbel-Hougaard Copula, θ=0.5）：使用 Gumbel-Hougaard Copula 建模，参数 θ=0.5 对应 ρ≈0

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N64

## Claim

工作点B（Gumbel-Hougaard Copula, θ=0.5）：使用 Gumbel-Hougaard Copula 建模，参数 θ=0.5 对应 ρ≈0.5（正相关），无法直接建模 ρ=-0.3。需使用反 Gumbel 变换或改用 Joe-Clayton Copula。若强行使用 Gumbel，需引入修正项 Δθ，导致解析误差 >5%。该工作点代表高成本低性场景，不推荐用于负相关建模。

## Corrected Claim

工作点B（Gumbel-Hougaard Copula, θ=0.5）：使用 Gumbel-Hougaard Copula 建模，参数 θ=0.5 对应 Kendall's tau ≈ 0.33（正相关），无法直接建模负相关（如 ρ=-0.3）。需使用反 Gumbel 变换或改用 Joe-Clayton Copula。若强行使用 Gumbel 并引入修正项，可能引入显著解析误差。该工作点代表正相关场景，不推荐用于负相关建模。

## Evidence

[质询]Gumbel-Hougaard Copula 的 Kendall's tau 与参数 θ 的关系为 τ = θ/(θ+1)。当 θ=0.5 时，τ = 0.5/1.5 ≈ 0.333，而非陈述中声称的 ρ≈0.5（若 ρ 指 Pearson 相关系数，对于 Gumbel 分布，ρ 与 τ 的关系并非线性，且 θ=0.5 对应的 Pearson 相关系数通常也远低于 0.5，约为 0.3-0.4 左右，具体取决于边缘分布，但断言 ρ≈0.5 存在数值偏差）。此外，'解析误差 >5%' 是一个缺乏具体上下文（如具体优化目标、约束条件）的经验性断言，难以从第一性原理严格推导。 | 先验知识/题面给定，逻辑校验通过。Gumbel-Hougaard 确实仅能建模正相关（θ>0），无法直接建模负相关，需使用反 Gumbel 或 Joe-Clayton 等支持负相关的 Copula，这一核心逻辑正确。但参数 θ=0.5 对应的具体相关系数数值（ρ≈0.5）存在偏差（Kendall's tau 约为 0.33），且 '误差 >5%' 为经验性断言，缺乏严格推导支持，故降级。

## Search Query

Gumbel-Hougaard Copula negative correlation limitation
