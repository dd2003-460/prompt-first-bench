# N83: 若买家偏好噪声服从正态分布 N(μ, σ²)，比价效率损失率 L_compare = 1 - Φ((P_median - P_ask) / σ_pref)；当 

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N18

## Claim

若买家偏好噪声服从正态分布 N(μ, σ²)，比价效率损失率 L_compare = 1 - Φ((P_median - P_ask) / σ_pref)；当 σ_pref > 0.15 * P_median 时，L_compare > 0.4，导致买家放弃比价，该阈值是量化‘低比价效率’的关键参数。

## Corrected Claim

若买家偏好噪声服从正态分布 N(μ, σ²)，比价效率损失率 L_compare = 1 - Φ((P_median - P_ask) / σ_pref)；在特定模型假设下，当 σ_pref 超过 P_median 的某一比例（如 0.15）时，L_compare 可能显著升高（如 > 0.4），该阈值用于量化‘低比价效率’。

## Evidence

[质询]该陈述将具体的数值阈值（σ_pref > 0.15 * P_median 导致 L_compare > 0.4）作为既定事实，但这并非数学恒等式或第一性原理可推导的普适规律，而是依赖于特定市场假设或经验数据的参数设定。若缺乏具体来源支持该特定系数（0.15）和结果（0.4）的对应关系，则属于未经证实的经验性断言。 | 逻辑上公式定义自洽（L=1-Φ(...)），但具体阈值 0.15 和 0.4 的对应关系属于经验事实/模型参数，非第一性原理可推导，且无外部来源支持，故降级。
