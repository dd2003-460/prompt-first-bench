# N202: 对于分类任务（如情感分析、图像识别），应使用 Cohen's h 或 Cliff's delta 作为效应量指标；Cohen's h 计算式为 h = 2*ar

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N58

## Claim

对于分类任务（如情感分析、图像识别），应使用 Cohen's h 或 Cliff's delta 作为效应量指标；Cohen's h 计算式为 h = 2*arcsin(√p1) - 2*arcsin(√p2)，其中 p1, p2 为两组准确率；通常 h > 0.2 视为小效应，h > 0.5 视为中等效应。

## Corrected Claim

对于分类任务（如情感分析、图像识别），应使用 Cohen's h 或 Cliff's delta 作为效应量指标；Cohen's h 计算式为 h = 2*arcsin(√p1) - 2*arcsin(√p2)，其中 p1, p2 为两组准确率；通常 h > 0.2 视为小效应，h > 0.5 视为中等效应。

## Evidence

先验知识/题面给定，逻辑校验通过
