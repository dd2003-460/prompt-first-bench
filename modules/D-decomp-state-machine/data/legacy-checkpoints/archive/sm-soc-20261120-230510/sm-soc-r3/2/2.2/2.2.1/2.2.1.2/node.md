# N158: σ_seller 的品类修正项：对于高流动性品类（如手机），σ_seller 较低（≈0.10）；对于低流动性非标品（如古董），σ_seller 较高（≈0.3

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N47

## Claim

σ_seller 的品类修正项：对于高流动性品类（如手机），σ_seller 较低（≈0.10）；对于低流动性非标品（如古董），σ_seller 较高（≈0.30），修正公式为 σ_seller = σ_base * (1 + α_liquidity)，其中 α_liquidity ∈ [0.5, 1.5] 取决于品类流动性指数。

## Corrected Claim

σ_seller 的品类修正项：对于高流动性品类（如手机），σ_seller 较低（≈0.10）；对于低流动性非标品（如古董），σ_seller 较高（≈0.30），修正公式为 σ_seller = σ_base * (1 + α_liquidity)，其中 α_liquidity ∈ [0.5, 1.5] 取决于品类流动性指数。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

product liquidity impact on seller price uncertainty second-hand market
