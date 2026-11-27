# N277: 工作点2（临界阈值/中透明）：设定 w_price = 0.5, info_0 = 1.0，则 w_interaction = 0.5。此点为模型失效边界，需引

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N94

## Claim

工作点2（临界阈值/中透明）：设定 w_price = 0.5, info_0 = 1.0，则 w_interaction = 0.5。此点为模型失效边界，需引入二阶修正项 δ = 0.1 * (info_0 - 1)^2 以评估不确定性；若 δ > 0.05，则需重新评估干预方向，否则维持帕累托最优判定。

## Corrected Claim

工作点2（临界阈值/中透明）：设定 w_price = 0.5, info_0 = 1.0，则 w_interaction = 0.5。此点为模型失效边界，需引入二阶修正项 δ = 0.1 * (info_0 - 1)^2 以评估不确定性；若 δ > 0.05，则需重新评估干预方向，否则维持帕累托最优判定。

## Evidence

先验知识/题面给定，逻辑校验通过
