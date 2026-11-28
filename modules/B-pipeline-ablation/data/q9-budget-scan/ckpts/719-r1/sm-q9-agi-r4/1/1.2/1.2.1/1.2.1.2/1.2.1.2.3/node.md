# N383: 消除位置偏差的实验设计：在 128K 上下文中，将针均匀随机放置在 0-128K 的 10 个离散位置区间（每区间 12.8K tokens），每个区间放置 1

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N124

## Claim

消除位置偏差的实验设计：在 128K 上下文中，将针均匀随机放置在 0-128K 的 10 个离散位置区间（每区间 12.8K tokens），每个区间放置 10 根针，共 100 根针；计算每个区间的 Recall@1，若各区间的 Recall 差异 < 3%，则认为位置偏差已控制在可接受范围内，无需额外修正

## Corrected Claim

消除位置偏差的实验设计：在 128K 上下文中，将针均匀随机放置在 0-128K 的 10 个离散位置区间（每区间 12.8K tokens），每个区间放置 10 根针，共 100 根针；计算每个区间的 Recall@1，若各区间的 Recall 差异 < 3%，则认为位置偏差已控制在可接受范围内，无需额外修正

## Evidence

先验知识/题面给定，逻辑校验通过：实验设计符合控制变量法原则，100根针的样本量在统计上足以评估区间差异，3%的阈值作为工程验收标准在逻辑上自洽且量级合理。

## Search Query

experimental design control position bias uniform distribution needle haystack
