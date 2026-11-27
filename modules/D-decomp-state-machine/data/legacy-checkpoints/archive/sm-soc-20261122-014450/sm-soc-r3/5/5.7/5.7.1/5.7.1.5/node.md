# N335: H5(买家风险溢价系数 γ) 的先验分布设定为 N(1.0, 0.25^2)，均值 1.0 表示买家对不确定性的平均风险中性偏好，标准差 0.25 允许覆盖风险

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N106

## Claim

H5(买家风险溢价系数 γ) 的先验分布设定为 N(1.0, 0.25^2)，均值 1.0 表示买家对不确定性的平均风险中性偏好，标准差 0.25 允许覆盖风险厌恶 (γ<1) 和风险寻求 (γ>1) 的极端群体，该参数影响买家在信息不完全时的购买概率 Q_buy。

## Corrected Claim

H5(买家风险溢价系数 γ) 的先验分布设定为 N(1.0, 0.25^2)，均值 1.0 表示买家对不确定性的平均风险中性偏好，标准差 0.25 允许覆盖风险厌恶 (γ<1) 和风险寻求 (γ>1) 的极端群体，该参数影响买家在信息不完全时的购买概率 Q_buy。

## Evidence

先验知识/题面给定，逻辑校验通过：均值1.0对应风险中性符合经济学定义，标准差0.25在量级上合理覆盖风险厌恶与寻求区间，且作为模型参数设定逻辑自洽。

## Search Query

buyer risk premium coefficient distribution second hand goods purchase probability
