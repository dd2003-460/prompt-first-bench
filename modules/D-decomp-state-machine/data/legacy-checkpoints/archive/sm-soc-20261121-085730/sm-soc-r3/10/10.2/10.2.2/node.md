# N411: 随机偏好噪声标准差 σ_noise 的计算方法：σ_noise = sqrt(Var(P_observed) - Var(P_fundamental))，其中 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N145

## Claim

随机偏好噪声标准差 σ_noise 的计算方法：σ_noise = sqrt(Var(P_observed) - Var(P_fundamental))，其中 P_fundamental 由近期同类商品成交价的加权平均确定，权重 w_i = 1/(age_i + 1)，需排除异常值（>3σ）。

## Corrected Claim

随机偏好噪声标准差 σ_noise 的计算方法：σ_noise = sqrt(Var(P_observed) - Var(P_fundamental))，其中 P_fundamental 由近期同类商品成交价的加权平均确定，权重 w_i = 1/(age_i + 1)，需排除异常值（>3σ）。

## Evidence

先验知识/题面给定，逻辑校验通过
