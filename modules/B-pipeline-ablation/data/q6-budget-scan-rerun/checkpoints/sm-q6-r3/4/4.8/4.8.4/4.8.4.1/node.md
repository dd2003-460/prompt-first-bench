# N332: 帕累托前沿的数值化判定矩阵：构建 3x3 矩阵比较 (P99_Cloud, Cost_Cloud), (P99_Self, Cost_Self), (P99_H

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N128

## Claim

帕累托前沿的数值化判定矩阵：构建 3x3 矩阵比较 (P99_Cloud, Cost_Cloud), (P99_Self, Cost_Self), (P99_Hybrid, Cost_Hybrid)，若 P99_Hybrid ≤ P99_Cloud 且 Cost_Hybrid < Cost_Cloud，则混合优于公有云；若 P99_Self > 200ms 且 Cost_Self < Cost_Cloud，则自建仅在成本敏感且延迟容忍度高时最优

## Corrected Claim

帕累托前沿的数值化判定矩阵：构建 3x3 矩阵比较 (P99_Cloud, Cost_Cloud), (P99_Self, Cost_Self), (P99_Hybrid, Cost_Hybrid)，若 P99_Hybrid ≤ P99_Cloud 且 Cost_Hybrid < Cost_Cloud，则混合优于公有云；若 P99_Self > 200ms 且 Cost_Self < Cost_Cloud，则自建仅在成本敏感且延迟容忍度高时最优

## Evidence

先验知识/题面给定，逻辑校验通过
