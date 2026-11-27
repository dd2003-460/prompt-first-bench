# N158: 工作点1（低驻留时间）：当 T_residence < 50 天时，P_updated_in_cache = 0.01 * T_residence < 0.5，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53

## Claim

工作点1（低驻留时间）：当 T_residence < 50 天时，P_updated_in_cache = 0.01 * T_residence < 0.5，更新对象占比低，线性近似成立，折损可忽略

## Corrected Claim

工作点1（低驻留时间）：当 T_residence < 50 天时，P_updated_in_cache = 0.01 * T_residence < 0.5，更新对象占比低，线性近似成立，折损可忽略

## Evidence

先验知识/题面给定，逻辑校验通过：当 T_residence < 50 时，0.01 * T_residence < 0.5 的数学推导成立，且低占比下线性近似忽略高阶项符合常规工程直觉。
