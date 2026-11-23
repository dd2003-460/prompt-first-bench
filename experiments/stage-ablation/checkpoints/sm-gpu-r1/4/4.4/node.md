# N19: 关键变量敏感性排序：对最终性价比排序（Ranking）进行一阶偏导分析，计算 ∂Ranking/∂P_price, ∂Ranking/∂T_throughput

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5

## Claim

关键变量敏感性排序：对最终性价比排序（Ranking）进行一阶偏导分析，计算 ∂Ranking/∂P_price, ∂Ranking/∂T_throughput, ∂Ranking/∂E_power；若某变量的偏导绝对值 > 0.5，则该变量为高敏感性变量，其不确定性将显著影响最终推荐，需在决策矩阵中单独列出该变量的±20%扰动场景。

## Corrected Claim

关键变量敏感性排序：对最终性价比排序（Ranking）进行一阶偏导分析，计算 ∂Ranking/∂P_price, ∂Ranking/∂T_throughput, ∂Ranking/∂E_power；若某变量的偏导绝对值 > 0.5，则该变量为高敏感性变量，其不确定性将显著影响最终推荐，需在决策矩阵中单独列出该变量的±20%扰动场景。

## Evidence

先验知识/题面给定，逻辑校验通过
