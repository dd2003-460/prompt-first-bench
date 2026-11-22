# N264: 倾向得分（Propensity Score）模型设定：P(Reduce=1 | X) = Logit(β0 + β1*V_remain + β2*Time_He

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N90

## Claim

倾向得分（Propensity Score）模型设定：P(Reduce=1 | X) = Logit(β0 + β1*V_remain + β2*Time_Held + β3*Price_History)；需计算每个样本的倾向得分 e(X)，并检查得分分布的重叠区域（Overlap Region），若重叠区域 < 50% 则 PSM 不可行，需改用 IPW。

## Corrected Claim

倾向得分（Propensity Score）模型设定：P(Reduce=1 | X) = Logit(β0 + β1*V_remain + β2*Time_Held + β3*Price_History)；需计算每个样本的倾向得分 e(X)，并检查得分分布的重叠区域（Overlap Region），若重叠区域 < 50% 则 PSM 不可行，需改用 IPW。

## Evidence

先验知识/题面给定，逻辑校验通过
