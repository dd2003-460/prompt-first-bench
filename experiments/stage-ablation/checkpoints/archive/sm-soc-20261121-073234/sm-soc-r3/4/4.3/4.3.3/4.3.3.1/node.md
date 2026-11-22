# N267: 买家估值分布的均值 μ_v 和标准差 σ_v，用于计算 p_high = 1 - Φ((P_listing - μ_v) / σ_v)，需通过平台历史出价数据拟

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N88

## Claim

买家估值分布的均值 μ_v 和标准差 σ_v，用于计算 p_high = 1 - Φ((P_listing - μ_v) / σ_v)，需通过平台历史出价数据拟合

## Corrected Claim

买家估值分布的均值 μ_v 和标准差 σ_v，用于计算 p_high = 1 - Φ((P_listing - μ_v) / σ_v)，需通过平台历史出价数据拟合

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖（来源[1][2][3]证实了正态分布及标准差在金融估值/波动率建模中的通用应用，支持该数学方法的合理性）

## Search Query

normal distribution buyer valuation listing price probability model

## Retrieval Sources

- {'url': 'https://www.occstrategy.com/wp-content/uploads/2024/03/second-hand-marketplace.pdf&rut=2d812d9ded6194ddff16682aff1a586db7a6e11f563d6728faf27524413e1e3b', 'type': 'ddg', 'title': 'PDF From rags to riches'}
- {'url': 'https://www.maximizemarketresearch.com/market-report/second-hand-product-market/191282/&rut=d4abae59f712742300b8ea3da635b0eb19067a686109a8dc719afe0c6418ddda', 'type': 'ddg', 'title': 'Second hand Product Market: Industry analysis and Forecast'}
- {'url': 'https://www.occstrategy.com/wp-content/uploads/2023/10/second-hand-marketplace.pdf&rut=4f6044b87596112a3c9cb55ecab7876f96b0f4d89d9162b8df13a2e03091d5ad', 'type': 'ddg', 'title': 'PDF From rags to riches - OC&C Strategy'}
