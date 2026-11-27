# N162: 工作点1（完全替换）：P_content_match = 0，f_update = 1 - P_updated_in_cache，在 T_residence=1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N54

## Claim

工作点1（完全替换）：P_content_match = 0，f_update = 1 - P_updated_in_cache，在 T_residence=100 天时 f_update = 1 - 0.632 = 0.368，折损 63.2%

## Corrected Claim

工作点1（完全替换）：P_content_match = 0，f_update = 1 - P_updated_in_cache，在 T_residence=100 天时 f_update = 1 - 0.632 = 0.368，折损 63.2%

## Evidence

先验知识/题面给定，逻辑校验通过：基于指数衰减模型 P_updated_in_cache = 1 - e^(-T/τ)，若 T_residence=100 对应 1 个时间常数 τ，则 e^-1 ≈ 0.368，故 f_update = 1 - 0.368 = 0.632？不对，题目说 f_update = 1 - 0.632 = 0.368。这意味着 P_updated_in_cache = 0.632。通常 P_updated_in_cache 指“已更新”的概率。如果模型是 P_updated = 1 - e^(-t/τ)，当 t=τ 时，P_updated = 1 - 0.368 = 0.632。此时 f_update (未更新比例) = 1 - 0.632 = 0.368。逻辑自洽。
