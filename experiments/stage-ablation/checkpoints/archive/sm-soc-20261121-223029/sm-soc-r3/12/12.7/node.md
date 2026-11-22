# N377: 咨询率弹性 ε_inquiry 的对数线性模型设定：模型为 ln(C_inquiry) = α + ε_inquiry * ln(ΔP) + δ_1 * Tim

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N125, N126, N127

## Claim

咨询率弹性 ε_inquiry 的对数线性模型设定：模型为 ln(C_inquiry) = α + ε_inquiry * ln(ΔP) + δ_1 * Time_Since_Listing + δ_2 * Price_Absolute + ε，需控制挂牌时间以排除自然衰减效应；报告 ε_inquiry 的估计值、标准误及 95% 置信区间，并检验模型残差的自相关性（Durbin-Watson 统计量在 1.5-2.5 之间）以确保估计有效性。

## Corrected Claim

咨询率弹性 ε_inquiry 的对数线性模型设定：模型为 ln(C_inquiry) = α + ε_inquiry * ln(ΔP) + δ_1 * Time_Since_Listing + δ_2 * Price_Absolute + ε，需控制挂牌时间以排除自然衰减效应；报告 ε_inquiry 的估计值、标准误及 95% 置信区间，并检验模型残差的自相关性（Durbin-Watson 统计量在 1.5-2.5 之间）以确保估计有效性。

## Evidence

先验知识/题面给定，逻辑校验通过
