# N80: 买家决策中 $P_{recent}$ 与 $P_{ask}$ 的权重分配模型：买家最终决策价 $P_{decision} = w_{recent} \times

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

买家决策中 $P_{recent}$ 与 $P_{ask}$ 的权重分配模型：买家最终决策价 $P_{decision} = w_{recent} \times P_{recent} + w_{ask} \times P_{ask}$，其中 $w_{recent} + w_{ask} = 1$；在‘近期成交’标签存在时，$w_{recent} = 0.85$，$w_{ask} = 0.15$；在无标签时，$w_{recent} = 0.6$，$w_{ask} = 0.4$；权重变化导致买家对高挂价的敏感度从0.4降至0.15，即敏感度下降62.5%。

## Corrected Claim

买家决策中 $P_{recent}$ 与 $P_{ask}$ 的权重分配模型：买家最终决策价 $P_{decision} = w_{recent} \times P_{recent} + w_{ask} \times P_{ask}$，其中 $w_{recent} + w_{ask} = 1$；在‘近期成交’标签存在时，$w_{recent} = 0.85$，$w_{ask} = 0.15$；在无标签时，$w_{recent} = 0.6$，$w_{ask} = 0.4$；权重变化导致买家对高挂价的敏感度从0.4降至0.15，即敏感度下降62.5%。

## Evidence

先验知识/题面给定，逻辑校验通过：权重和为1，敏感度变化计算 (0.4-0.15)/0.4 = 62.5% 正确，模型内部自洽。

## Search Query

buyer decision weighting recent transaction price vs asking price
