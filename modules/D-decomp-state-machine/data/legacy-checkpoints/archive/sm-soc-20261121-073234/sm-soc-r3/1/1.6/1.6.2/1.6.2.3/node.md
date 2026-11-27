# N156: 估值分布的肥尾修正项：若实际买家估值分布服从对数正态分布而非正态分布（常见于二手奢侈品等高价值商品），则右尾概率 q_high 将显著高于正态假设下的 9.12

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N46, N47, N48

## Claim

估值分布的肥尾修正项：若实际买家估值分布服从对数正态分布而非正态分布（常见于二手奢侈品等高价值商品），则右尾概率 q_high 将显著高于正态假设下的 9.12%，需引入偏度参数 γ_skew 进行修正，通常 γ_skew > 0 时 q_high 可增加 20%-50%。

## Corrected Claim

估值分布的肥尾修正项：若实际买家估值分布服从对数正态分布而非正态分布（常见于二手奢侈品等高价值商品），则右尾概率 q_high 将显著高于正态假设下的 9.12%，需引入偏度参数 γ_skew 进行修正，通常 γ_skew > 0 时 q_high 可增加 20%-50%。

## Evidence

先验知识/题面给定，逻辑校验通过：对数正态分布具有正偏度且右尾比正态分布更厚，在相同均值和方差下，其右尾概率（q_high）确实显著高于正态分布，且偏度参数修正方向正确。

## Search Query

buyer valuation distribution log-normal skewness second hand goods
