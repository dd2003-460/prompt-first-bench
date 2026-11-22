# N13: 利益相关方核验逻辑：构建贝叶斯后验概率 $P(Stakeholder | Data) \propto P(Data | Stakeholder) \cdot P

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

利益相关方核验逻辑：构建贝叶斯后验概率 $P(Stakeholder | Data) \propto P(Data | Stakeholder) \cdot P(Stakeholder)$，其中 $Data$ 包括高挂价率、短周期、降价无效率。通过比较三种假设下的似然比 $LR = \frac{P(Data | H_{buyer})}{P(Data | H_{seller})}$ 等，确定最可能的驱动方。

## Corrected Claim

利益相关方核验逻辑：构建贝叶斯后验概率 $P(Stakeholder | Data) \propto P(Data | Stakeholder) \cdot P(Stakeholder)$，其中 $Data$ 包括高挂价率、短周期、降价无效率。通过比较三种假设下的似然比 $LR = \frac{P(Data | H_{buyer})}{P(Data | H_{seller})}$ 等，确定最可能的驱动方。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应贝叶斯公式的三个核心组成部分：观测噪声（影响似然函数的精度/方差）、先验概率（P(Stakeholder)）以及似然比（P(Data|Stakeholder)）的统计显著性检验。三者分别处理数据质量、背景知识和推断阈值，逻辑上相互独立且无重叠。）
