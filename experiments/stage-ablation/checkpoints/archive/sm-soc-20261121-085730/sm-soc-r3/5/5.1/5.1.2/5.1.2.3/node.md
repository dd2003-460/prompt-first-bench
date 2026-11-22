# N315: 模型复杂度 c_model 的阈值判据：若 c_model < 0.5，表明行为经济学模型的额外复杂度未带来足够的似然提升，应退化为基准模型；若 c_model

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N106

## Claim

模型复杂度 c_model 的阈值判据：若 c_model < 0.5，表明行为经济学模型的额外复杂度未带来足够的似然提升，应退化为基准模型；若 c_model > 0.8，表明模型过拟合风险高，需引入 L1/L2 正则化项，正则化系数 λ 应通过交叉验证（Cross-Validation）最小化预测误差确定。

## Corrected Claim

模型复杂度 c_model 的阈值判据：若 c_model < 0.5，表明行为经济学模型的额外复杂度未带来足够的似然提升，应退化为基准模型；若 c_model > 0.8，表明模型过拟合风险高，需引入 L1/L2 正则化项，正则化系数 λ 应通过交叉验证（Cross-Validation）最小化预测误差确定。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

model complexity threshold overfitting regularization AIC cross validation
