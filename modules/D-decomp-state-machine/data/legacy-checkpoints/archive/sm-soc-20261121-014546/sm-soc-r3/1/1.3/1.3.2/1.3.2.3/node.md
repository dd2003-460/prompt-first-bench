# N155: 独立噪声项 η_p 的方差 Var(η_p) 代表不随定价行为变化的固有市场波动，由总方差分解得出：Var(η_p) = σ_p² - k_p² * Var(ε

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N43

## Claim

独立噪声项 η_p 的方差 Var(η_p) 代表不随定价行为变化的固有市场波动，由总方差分解得出：Var(η_p) = σ_p² - k_p² * Var(ε)。

## Corrected Claim

独立噪声项 η_p 的方差 Var(η_p) 代表不随定价行为变化的固有市场波动，由总方差分解得出：Var(η_p) = σ_p² - k_p² * Var(ε)。

## Evidence

先验知识/题面给定，逻辑校验通过：基于线性回归模型 y = kx + ε 的方差分解公式 Var(y) = k²Var(x) + Var(ε)，若 η 为残差项且与 x 不相关，则 Var(η) = Var(y) - k²Var(x)，此处对应 σ_p² - k_p² * Var(ε)，逻辑自洽。

## Search Query

decomposition of total variance into systematic and idiosyncratic components in stochastic models
