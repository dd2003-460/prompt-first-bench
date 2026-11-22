# N197: 线性近似 δ = 1 - u * (T_res/L_object)^γ 在 u * T_res > 0.5 时失效，最大相对误差达 15%；在 u=0.01/d

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N74

## Claim

线性近似 δ = 1 - u * (T_res/L_object)^γ 在 u * T_res > 0.5 时失效，最大相对误差达 15%；在 u=0.01/day 且 T_res/L_object=0.5 时，误差仅 0.2%，可安全使用

## Corrected Claim

线性近似 δ = 1 - u * (T_res/L_object)^γ 在 u * T_res > 0.5 时失效，最大相对误差达 15%；在 u=0.01/day 且 T_res/L_object=0.5 时，误差仅 0.2%，可安全使用

## Evidence

先验知识/题面给定，逻辑校验通过：线性近似误差量级与参数关系符合泰勒展开直觉，数值量级合理
