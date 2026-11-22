# N42: 均值投影：买家期望效用均值 E[U_buyer] = v_base - p_listed + k×(v_base - p_market_avg)，其中 k=0.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N8

## Claim

均值投影：买家期望效用均值 E[U_buyer] = v_base - p_listed + k×(v_base - p_market_avg)，其中 k=0.6 为搜索成本降低系数，v_base 为买家保留价格，p_listed 为挂价，p_market_avg 为市场均价；该均值在 σ²_noise 变化时保持恒定，因为 k 和 v_base 不随噪声方差改变

## Corrected Claim

均值投影：买家期望效用均值 E[U_buyer] = v_base - p_listed + k×(v_base - p_market_avg)，其中 k=0.6 为搜索成本降低系数，v_base 为买家保留价格，p_listed 为挂价，p_market_avg 为市场均价；该均值在 σ²_noise 变化时保持恒定，因为 k 和 v_base 不随噪声方差改变

## Evidence

先验知识/题面给定，逻辑校验通过：公式中不包含 σ²_noise 变量，且 k 和 v_base 被定义为常数，因此均值在数学上确实不随噪声方差变化。
