# N152: 交互效应项：算法偏差与市场波动的耦合度 Cov(α_t, SupplyDemand_t)，若相关系数 r > 0.3，则表明算法顺应市场波动而非独立偏差，σ²_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N48

## Claim

交互效应项：算法偏差与市场波动的耦合度 Cov(α_t, SupplyDemand_t)，若相关系数 r > 0.3，则表明算法顺应市场波动而非独立偏差，σ²_algo_bias 需修正为 σ²_total - 2*r*σ_α*σ_sd，否则视为独立噪声源。

## Corrected Claim

交互效应项：算法偏差与市场波动的耦合度 Cov(α_t, SupplyDemand_t)，若相关系数 r > 0.3，则表明算法顺应市场波动而非独立偏差，σ²_algo_bias 需修正为 σ²_total - 2*r*σ_α*σ_sd，否则视为独立噪声源。

## Evidence

先验知识/题面给定，逻辑校验通过：方差分解公式 Var(X+Y) = Var(X) + Var(Y) + 2Cov(X,Y) 在数学上成立，且相关系数阈值设定符合统计推断常规逻辑。

## Search Query

covariance between algorithmic bias and market supply demand volatility
