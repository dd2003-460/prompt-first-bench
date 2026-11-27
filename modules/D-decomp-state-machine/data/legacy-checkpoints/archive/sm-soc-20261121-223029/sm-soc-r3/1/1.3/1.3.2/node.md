# N42: σ_W（偏好噪声标准差）由买家群体的收入分布方差 Var(Income) 和商品差异化程度 D_diff 共同决定，公式为 σ_W = sqrt(Var(Inc

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N8

## Claim

σ_W（偏好噪声标准差）由买家群体的收入分布方差 Var(Income) 和商品差异化程度 D_diff 共同决定，公式为 σ_W = sqrt(Var(Income) * β_income + D_diff * β_pref)，其中 β_income 和 β_pref 为敏感度系数。

## Corrected Claim

在某些异质性消费者选择模型中，偏好噪声标准差 σ_W 可被建模为收入分布方差 Var(Income) 和商品差异化程度 D_diff 的函数，例如 σ_W = sqrt(Var(Income) * β_income + D_diff * β_pref)，其中 β 为模型特定的敏感度系数。

## Evidence

[质询]该公式属于特定理论模型（如离散选择模型或异质性消费者模型）的假设性设定，并非普适的物理或经济定律。不同模型中偏好噪声的结构可能不同（例如可能包含交互项、非线性关系或独立的噪声项），且敏感度系数 β 的定义和量纲在不同文献中可能不一致，直接断言此特定公式为通用决定机制存在过度概括的风险。 | 经验事实/模型设定，逻辑自洽（量纲上若 β 为无量纲或适当归一化，sqrt(方差*系数) 结构合理），但检索无可用来源支持该特定公式的普适性，且属于特定模型假设而非第一性原理必然推论。

## Search Query

standard deviation of willingness to pay income variance product differentiation
