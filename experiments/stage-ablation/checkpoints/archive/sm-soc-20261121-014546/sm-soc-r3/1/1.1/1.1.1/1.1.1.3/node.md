# N128: 噪声 ε_seller 的分布形态检验：若 ε_seller 服从正态分布 N(0, σ_seller^2)，则其偏度 Skewness ≈ 0，峰度 Kurt

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N34, N35, N36

## Claim

噪声 ε_seller 的分布形态检验：若 ε_seller 服从正态分布 N(0, σ_seller^2)，则其偏度 Skewness ≈ 0，峰度 Kurtosis ≈ 3；若存在损失厌恶导致的右偏，则 Skewness > 0，需通过 Jarque-Bera 检验判断分布假设是否成立。

## Corrected Claim

噪声 ε_seller 的分布形态检验：若 ε_seller 服从正态分布 N(0, σ_seller^2)，则其偏度 Skewness ≈ 0，峰度 Kurtosis ≈ 3；若存在损失厌恶导致的右偏，则 Skewness > 0，需通过 Jarque-Bera 检验判断分布假设是否成立。

## Evidence

逻辑推导成立，来源未直接覆盖

## Search Query

distributional test of price setting noise skewness kurtosis jarque bera
