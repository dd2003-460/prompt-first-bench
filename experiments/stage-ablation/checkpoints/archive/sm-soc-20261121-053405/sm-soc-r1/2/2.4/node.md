# N13: 利益相关方核验逻辑：构建贝叶斯后验概率 $P(Stakeholder | Data) \propto P(Data | Stakeholder) \cdot P

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N2

## Claim

利益相关方核验逻辑：构建贝叶斯后验概率 $P(Stakeholder | Data) \propto P(Data | Stakeholder) \cdot P(Stakeholder)$，其中 $Data$ 包括高挂价率、短周期、降价无效率。通过比较三种假设下的似然比 $LR = \frac{P(Data | H_{buyer})}{P(Data | H_{seller})}$ 等，确定最可能的驱动方。

## Corrected Claim

利益相关方核验逻辑：构建贝叶斯后验概率 $P(Stakeholder | Data) \propto P(Data | Stakeholder) \cdot P(Stakeholder)$，其中 $Data$ 包括高挂价率、短周期、降价无效率。通过比较三种假设下的似然比 $LR = \frac{P(Data | H_{buyer})}{P(Data | H_{seller})}$ 等，确定最可能的驱动方。

## Evidence

先验知识/题面给定，逻辑校验通过：贝叶斯公式应用正确，似然比定义符合统计学原理，量纲与逻辑自洽。
