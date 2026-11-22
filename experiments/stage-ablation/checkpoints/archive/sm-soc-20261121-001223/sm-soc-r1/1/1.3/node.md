# N7: 挂价分布推导：基于 λ 和 σ_noise，推导卖家最优挂价 P_ask = V_true * (1 + λ*σ_noise + ε)，其中 V_true 为内

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

挂价分布推导：基于 λ 和 σ_noise，推导卖家最优挂价 P_ask = V_true * (1 + λ*σ_noise + ε)，其中 V_true 为内在价值，ε 为策略性溢价，验证该公式是否覆盖 15-25% 的溢价区间。

## Corrected Claim

基于 λ 和 σ_noise，卖家最优挂价可近似表示为 P_ask ≈ V_true * (1 + k*λ*σ_noise/V_true + ε)，其中 k 为校准系数，该模型在特定参数假设下可解释 15-25% 的溢价区间，但需进一步实证校准。

## Evidence

[质询]公式结构存在逻辑缺陷：将 λ*σ_noise 直接作为乘数项 (1 + ...) 缺乏量纲一致性（σ_noise 通常为绝对值或标准差，需归一化或除以 V_true 才能构成无量纲比例），且该线性叠加模型过于简化，未考虑市场流动性、竞争博弈等非线性因素，难以严谨推导覆盖固定的 15-25% 区间。 | 先验知识/题面给定，但逻辑校验发现量纲不匹配及模型简化过度，无法严格证明覆盖特定区间，故降级。
