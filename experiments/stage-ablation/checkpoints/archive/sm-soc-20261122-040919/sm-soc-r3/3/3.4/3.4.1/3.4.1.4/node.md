# N287: GMV 波动率 σ²_GMV 的联合方差公式：σ²_GMV = M₀² * [Var(β_p * ΔPremium) + Var(β_s * ΔT) + 2*C

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N77

## Claim

GMV 波动率 σ²_GMV 的联合方差公式：σ²_GMV = M₀² * [Var(β_p * ΔPremium) + Var(β_s * ΔT) + 2*Cov(β_p * ΔPremium, β_s * ΔT)]，其中 Cov 项需基于 β_p 和 β_s 的联合分布估计。[待核验]：需模拟或回归确定协方差项。

## Corrected Claim

GMV 波动率 σ²_GMV 的联合方差公式：σ²_GMV = M₀² * [Var(β_p * ΔPremium) + Var(β_s * ΔT) + 2*Cov(β_p * ΔPremium, β_s * ΔT)]，其中 Cov 项需基于 β_p 和 β_s 的联合分布估计。[待核验]：需模拟或回归确定协方差项。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

GMV volatility variance decomposition price quantity cross term

## Retrieval Sources

- {'url': 'https://crunchspark.com/marketplace-financial-modelling-gmv.html&rut=e2c4abe5820405e7b91c24b08e17c0beea1132c694304dc5d18a04c8f0ccd654', 'type': 'ddg', 'title': 'Financial Modelling for Marketplace Businesses: GMV, Take Rate and Unit ...'}
- {'url': 'https://inversionistasangeles.com/marketplace-business-model/&rut=7a50107897299787db301582e3e73a8f3bb7c987ea576d3ee57177a8e8067661', 'type': 'ddg', 'title': 'Marketplace Business Model Explained (GMV vs. Revenue Example)'}
- {'url': 'https://revenuemap.app/blog/marketplace-business-model&rut=f476e74823cf764f052e93d13a5890bf93acc6e88b4c285896b060f19e897dda', 'type': 'ddg', 'title': 'Marketplace Financial Model: Take Rates, GMV Projections, and Liquidity ...'}
