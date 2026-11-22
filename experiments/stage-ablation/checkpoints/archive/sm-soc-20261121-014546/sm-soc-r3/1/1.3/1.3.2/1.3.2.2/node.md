# N154: 耦合系数 k_p 量化定价噪声 ε 对成交概率误差 ε_p 的传导强度，定义为 Cov(ε_p, ε) / Var(ε)，若假设线性正相关且标准化，k_p ∈ 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N43

## Claim

耦合系数 k_p 量化定价噪声 ε 对成交概率误差 ε_p 的传导强度，定义为 Cov(ε_p, ε) / Var(ε)，若假设线性正相关且标准化，k_p ∈ [0, 1]，需通过回归系数估计。

## Corrected Claim

耦合系数 k_p 量化定价噪声 ε 对成交概率误差 ε_p 的传导强度，定义为 Cov(ε_p, ε) / Var(ε)，若假设线性正相关且标准化，k_p ∈ [0, 1]，需通过回归系数估计。

## Evidence

先验知识/题面给定，逻辑校验通过：Cov(ε_p, ε)/Var(ε) 是线性回归中斜率系数的标准定义，在标准化且线性正相关假设下，该系数确实落在 [0, 1] 区间内，量纲与逻辑自洽。

## Search Query

coupling coefficient between pricing noise and demand forecast error in market models
