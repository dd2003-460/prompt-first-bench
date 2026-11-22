# N173: 质量敏感度系数 β_quality 的量化：表示质量评分每增加 1 分对 k 的边际影响，需通过回归分析 k_i = k_base * (1 + β_quali

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

质量敏感度系数 β_quality 的量化：表示质量评分每增加 1 分对 k 的边际影响，需通过回归分析 k_i = k_base * (1 + β_quality * Q_i) 获取，假设 β_quality 在 0.1-0.3 之间，具体值取决于质量评分 Q 的归一化方式（如 1-5 分制）。

## Corrected Claim

质量敏感度系数 β_quality 的量化：表示质量评分每增加 1 分对 k 的边际影响，需通过回归分析 k_i = k_base * (1 + β_quality * Q_i) 获取，假设 β_quality 在 0.1-0.3 之间，具体值取决于质量评分 Q 的归一化方式（如 1-5 分制）。

## Evidence

先验知识/题面给定，逻辑校验通过
