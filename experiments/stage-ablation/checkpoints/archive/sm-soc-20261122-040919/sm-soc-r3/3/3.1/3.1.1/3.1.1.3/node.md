# N240: 下游投影2：样本量 n 的最小推荐值 n_min。为确保 Var(Noise_display) < 0.02 * Var(S_old)，需满足 σ²_p / n

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N65

## Claim

下游投影2：样本量 n 的最小推荐值 n_min。为确保 Var(Noise_display) < 0.02 * Var(S_old)，需满足 σ²_p / n < 0.02 * Var(S_old)。若 σ_p / sqrt(Var(S_old)) = 1（即价格波动与信号方差同量级），则 n_min > 50。若 σ_p / sqrt(Var(S_old)) = 2，则 n_min > 200。具体 n_min 取决于市场价格的离散程度。

## Corrected Claim

下游投影2：样本量 n 的最小推荐值 n_min。为确保 Var(Noise_display) < 0.02 * Var(S_old)，需满足 σ²_p / n < 0.02 * Var(S_old)。若 σ_p / sqrt(Var(S_old)) = 1（即价格波动与信号方差同量级），则 n_min > 50。若 σ_p / sqrt(Var(S_old)) = 2，则 n_min > 200。具体 n_min 取决于市场价格的离散程度。

## Evidence

先验知识/题面给定，逻辑校验通过：不等式 σ²_p/n < 0.02 * Var(S_old) 变形为 n > (σ_p/√Var(S_old))² / 0.02。当比值为1时，n > 1/0.02 = 50；当比值为2时，n > 4/0.02 = 200。数学推导正确，量级合理。
