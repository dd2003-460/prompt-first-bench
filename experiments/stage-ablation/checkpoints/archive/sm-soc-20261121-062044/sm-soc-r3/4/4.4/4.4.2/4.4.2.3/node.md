# N221: 置信度映射的连续函数定义：置信度 C = 0.5 + 0.4 * (1 - p-value/0.05) * I(p-value < 0.05)，其中 I 为指示

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N78

## Claim

置信度映射的连续函数定义：置信度 C = 0.5 + 0.4 * (1 - p-value/0.05) * I(p-value < 0.05)，其中 I 为指示函数；若 p-value = 0.01，则 C = 0.5 + 0.4 * (1 - 0.2) = 0.82，而非固定 0.9，以反映证据强度的连续性。

## Corrected Claim

置信度映射的连续函数定义：置信度 C = 0.5 + 0.4 * (1 - p-value/0.05) * I(p-value < 0.05)，其中 I 为指示函数；若 p-value = 0.01，则 C = 0.5 + 0.4 * (1 - 0.2) = 0.82，而非固定 0.9，以反映证据强度的连续性。

## Evidence

先验知识/题面给定，逻辑校验通过：公式定义与数值代入计算（0.5 + 0.4 * 0.8 = 0.82）完全自洽，符合连续映射的设计意图。

## Search Query

p-value to confidence score continuous mapping function statistical evidence
