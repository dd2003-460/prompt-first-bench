# N334: 75×3 成本矩阵中每个单元格的计算精度要求：Cost_per_1k_req 保留 2 位小数（元），P99 延迟保留 1 位小数（ms），确保在 N_win_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N106

## Claim

75×3 成本矩阵中每个单元格的计算精度要求：Cost_per_1k_req 保留 2 位小数（元），P99 延迟保留 1 位小数（ms），确保在 N_win_strategy 统计时，因精度截断导致的策略排序错误概率 <0.1%

## Corrected Claim

75×3 成本矩阵中每个单元格的计算精度要求：Cost_per_1k_req 保留 2 位小数（元），P99 延迟保留 1 位小数（ms），确保在 N_win_strategy 统计时，因精度截断导致的策略排序错误概率 <0.1%

## Evidence

先验知识/题面给定，逻辑校验通过
