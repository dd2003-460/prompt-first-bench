# N142: 验证 N64 中'忽略高阶交互效应'的具体代价：在 ρ=-0.3 约束下，S 和 R 的协方差 Cov(S,R) = ρ * σ_S * σ_R。若忽略三阶交叉

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64

## Claim

验证 N64 中'忽略高阶交互效应'的具体代价：在 ρ=-0.3 约束下，S 和 R 的协方差 Cov(S,R) = ρ * σ_S * σ_R。若忽略三阶交叉项 E[S^2 R]，解析近似将高估热门大对象的权重。需计算被忽略的交叉项占比：ε_interaction = E[S^2 R]_true / (E[S^2]_approx * E[R]_approx)。若 ε_interaction > 0.1，则 N64 的 ±5% 误差边界失效。

## Corrected Claim

验证 N64 中'忽略高阶交互效应'的具体代价：在 ρ=-0.3 约束下，S 和 R 的协方差 Cov(S,R) = ρ * σ_S * σ_R。若忽略三阶交叉项 E[S^2 R]，解析近似将高估热门大对象的权重。需计算被忽略的交叉项占比：ε_interaction = E[S^2 R]_true / (E[S^2]_approx * E[R]_approx)。若 ε_interaction > 0.1，则 N64 的 ±5% 误差边界失效。

## Evidence

先验知识/题面给定，逻辑校验通过
