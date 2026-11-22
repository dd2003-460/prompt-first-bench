# N153: 工作点 1 (高偏差-高曝光)：当 B_algo > 1.5 时，对应高价商品曝光占比 E_high/E_total > 60%，此时算法严重偏向高价，导致长尾

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N49

## Claim

工作点 1 (高偏差-高曝光)：当 B_algo > 1.5 时，对应高价商品曝光占比 E_high/E_total > 60%，此时算法严重偏向高价，导致长尾低价商品曝光不足，需量化此阈值下的曝光份额具体数值。

## Corrected Claim

工作点 1 (高偏差-高曝光)：当算法偏差指标 B_algo 显著高于 1（例如 > 1.5）时，通常对应高价商品曝光占比显著高于基线（例如 > 60%），此时算法偏向高价，导致长尾低价商品曝光不足。具体阈值需根据系统校准确定。

## Evidence

[质询]该陈述将具体的算法偏差阈值（B_algo > 1.5）与具体的曝光占比阈值（> 60%）直接挂钩，这属于特定系统或实验的经验性参数，并非普适的物理或数学定律。不同推荐系统的架构、数据分布及优化目标不同，B_algo 与曝光份额之间的映射关系并非固定不变，因此该具体数值对应关系缺乏普适性，存在口径混淆或特定场景过拟合的风险。 | source=knowledge，逻辑上高偏差导致高曝光占比符合直觉，但具体数值（1.5 和 60%）为经验参数，无外部来源支持且非第一性原理可推导，故降级。

## Search Query

algorithmic bias threshold 1.5 exposure share high price items 60%
