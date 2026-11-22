# N215: 共享随机源 V_true：商品真实价值 V_true 的分布参数，假设 V_true ~ N(μ_V, σ_V²)，其中 μ_V 为市场均价，σ_V 为同类商品

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N64

## Claim

共享随机源 V_true：商品真实价值 V_true 的分布参数，假设 V_true ~ N(μ_V, σ_V²)，其中 μ_V 为市场均价，σ_V 为同类商品价值离散度（通常 σ_V/μ_V ∈ [0.1, 0.2]），该随机源决定了 (V - P_ask*) 的符号和幅度。

## Corrected Claim

共享随机源 V_true：商品真实价值 V_true 的分布参数，假设 V_true ~ N(μ_V, σ_V²)，其中 μ_V 为市场均价，σ_V 为同类商品价值离散度（通常 σ_V/μ_V ∈ [0.1, 0.2]），该随机源决定了 (V - P_ask*) 的符号和幅度。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

distribution of true value in second-hand market stochastic model
