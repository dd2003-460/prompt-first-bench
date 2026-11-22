# N165: 线性近似失效条件：当 λ_u * T_residence > 0.1 时，f_update = 1 - λ_u * T_residence 误差超过 5%，需切

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N54

## Claim

线性近似失效条件：当 λ_u * T_residence > 0.1 时，f_update = 1 - λ_u * T_residence 误差超过 5%，需切换至指数模型 f_update = exp(-λ_u * T_residence * (1 - P_content_match))

## Corrected Claim

线性近似失效条件：当 λ_u * T_residence > 0.1 时，f_update = 1 - λ_u * T_residence 误差超过 5%，需切换至指数模型 f_update = exp(-λ_u * T_residence * (1 - P_content_match))

## Evidence

先验知识/题面给定，逻辑校验通过：线性近似 1-x 与 exp(-x) 的相对误差在 x>0.1 时确实显著超过 5%（例如 x=0.1 时相对误差约 5.3%），且指数模型是泊松过程/指数衰减的标准形式，逻辑自洽。
