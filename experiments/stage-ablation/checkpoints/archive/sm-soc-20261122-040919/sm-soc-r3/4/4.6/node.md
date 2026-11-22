# N23: 关键断言'挂价高15-25%但周期短'的置信度评估：需计算挂价偏差（15-25%）与成交周期缩短幅度的统计显著性。若成交周期缩短幅度为 k%，则需检验 k 是否

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

关键断言'挂价高15-25%但周期短'的置信度评估：需计算挂价偏差（15-25%）与成交周期缩短幅度的统计显著性。若成交周期缩短幅度为 k%，则需检验 k 是否显著大于0（t检验）。假设 k=10%，标准误为2%，则 t = 5，p-value < 0.001，置信度为[高]。若 k=2%，t=1，p-value > 0.05，置信度为[低]。[待核验]：具体周期缩短幅度未知。

## Corrected Claim

关键断言'挂价高15-25%但周期短'的置信度评估：需计算挂价偏差（15-25%）与成交周期缩短幅度的统计显著性。若成交周期缩短幅度为 k%，则需检验 k 是否显著大于0（t检验）。假设 k=10%，标准误为2%，则 t = 5，p-value < 0.001，置信度为[高]。若 k=2%，t=1，p-value > 0.05，置信度为[低]。[待核验]：具体周期缩短幅度未知。

## Evidence

先验知识/题面给定，逻辑校验通过：t检验公式应用正确（t=k/SE），数值计算无误（10/2=5, 2/2=1），p值与置信度对应关系符合统计学常识。

## Search Query

statistical significance t-test pricing deviation sales cycle shortening
