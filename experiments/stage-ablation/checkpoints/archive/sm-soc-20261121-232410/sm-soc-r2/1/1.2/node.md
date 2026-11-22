# N7: 随机偏好噪声σ_noise的量化：σ_noise = sqrt(Var(P_listed | P_market))，在控制锚定效应后，剩余方差中60%来自卖家个

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N1, N2, N3

## Claim

随机偏好噪声σ_noise的量化：σ_noise = sqrt(Var(P_listed | P_market))，在控制锚定效应后，剩余方差中60%来自卖家个体风险偏好差异（β_risk ~ N(0.3, 0.1)），40%来自信息不对称导致的估值误差（ε_info ~ N(0, 0.15)）。

## Corrected Claim

随机偏好噪声σ_noise的量化：σ_noise = sqrt(Var(P_listed | P_market))。在控制锚定效应后，剩余方差主要由卖家个体风险偏好差异和信息不对称导致的估值误差两部分构成，具体比例取决于市场微观结构及卖家群体特征，通常需通过实证数据拟合确定。

## Evidence

父节点级核验未通过：不完备（子节点2和3分别验证了两个独立分布参数，彼此正交且不冗余。但父节点明确定义了σ_noise为条件标准差 sqrt(Var(P_listed | P_market))，而子节点1给出的公式基于边际方差分解，且未体现'控制锚定效应'这一关键约束条件，导致数学定义与父节点不完全对齐，存在完备性缺失。）

## Search Query

price setting noise variance decomposition risk preference information asymmetry
