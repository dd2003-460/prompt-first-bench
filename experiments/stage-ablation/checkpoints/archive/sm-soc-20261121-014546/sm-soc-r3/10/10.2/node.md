# N369: 市场波动率 σ_market 在定价公式 P_ask = V * (1 + w_risk * σ_market) 中的具体量化为近30天同类商品成交价的标准差除

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N122

## Claim

市场波动率 σ_market 在定价公式 P_ask = V * (1 + w_risk * σ_market) 中的具体量化为近30天同类商品成交价的标准差除以均值，即变异系数 CV = σ_price/P_avg，典型取值范围为 0.1-0.3，直接决定溢价幅度的下限。

## Corrected Claim

市场波动率 σ_market 在定价公式 P_ask = V * (1 + w_risk * σ_market) 中的具体量化为近30天同类商品成交价的标准差除以均值，即变异系数 CV = σ_price/P_avg，典型取值范围为 0.1-0.3，直接决定溢价幅度的下限。

## Evidence

先验知识/题面给定，逻辑校验通过
