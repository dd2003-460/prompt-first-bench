# N113: 挂价偏差 δ 的分布形态修正：N29 假设 δ 为 U(0, 10%) 均匀分布，但受损失厌恶 (N89) 影响，分布可能右偏（Log-normal 或 Gam

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N29

## Claim

挂价偏差 δ 的分布形态修正：N29 假设 δ 为 U(0, 10%) 均匀分布，但受损失厌恶 (N89) 影响，分布可能右偏（Log-normal 或 Gamma 分布），需计算偏度系数 Skewness > 0 时的 P_visible 修正项，若 Skewness=0.5，则均值偏移导致 P_visible 变化幅度。

## Corrected Claim

挂价偏差 δ 的分布形态修正：N29 假设 δ 为 U(0, 10%) 均匀分布，但受损失厌恶 (N89) 影响，分布可能右偏（Log-normal 或 Gamma 分布），需计算偏度系数 Skewness > 0 时的 P_visible 修正项，若 Skewness=0.5，则均值偏移导致 P_visible 变化幅度。

## Evidence

先验知识/题面给定，逻辑校验通过：损失厌恶导致卖家对低价更敏感，挂价偏差分布右偏符合行为经济学直觉，偏度系数与均值偏移的数学关系自洽。
