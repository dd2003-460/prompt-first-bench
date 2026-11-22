# N235: P_market_pre 的无偏估计：在干预前，P_market_pre 应取同类商品成交价的截尾均值（Trimmed Mean, 10%），以排除极端离群值影

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N85, N86, N87

## Claim

P_market_pre 的无偏估计：在干预前，P_market_pre 应取同类商品成交价的截尾均值（Trimmed Mean, 10%），以排除极端离群值影响，其标准误 SE_pre = σ_deal / sqrt(n_pre)，其中 n_pre 为干预前样本量。

## Corrected Claim

P_market_pre 的无偏估计：在干预前，P_market_pre 应取同类商品成交价的截尾均值（Trimmed Mean, 10%），以排除极端离群值影响，其标准误 SE_pre = σ_deal / sqrt(n_pre)，其中 n_pre 为干预前样本量。

## Evidence

先验知识/题面给定，逻辑校验通过：截尾均值是处理离群值的稳健统计量，标准误公式符合中心极限定理下的标准推导，逻辑自洽且数值量级合理。

## Search Query

trimmed mean standard error calculation
