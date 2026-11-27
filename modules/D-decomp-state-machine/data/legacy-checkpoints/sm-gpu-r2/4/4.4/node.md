# N19: 关键变量敏感性排序：对最终性价比排序（Ranking）进行一阶偏导分析，计算 ∂Ranking/∂P_price, ∂Ranking/∂T_throughput

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4, N5

## Claim

关键变量敏感性排序：对最终性价比排序（Ranking）进行一阶偏导分析，计算 ∂Ranking/∂P_price, ∂Ranking/∂T_throughput, ∂Ranking/∂E_power；若某变量的偏导绝对值 > 0.5，则该变量为高敏感性变量，其不确定性将显著影响最终推荐，需在决策矩阵中单独列出该变量的±20%扰动场景。

## Corrected Claim

关键变量敏感性排序：对最终性价比排序（Ranking）进行一阶偏导分析，计算 ∂Ranking/∂P_price, ∂Ranking/∂T_throughput, ∂Ranking/∂E_power；若某变量的偏导绝对值 > 0.5，则该变量为高敏感性变量，其不确定性将显著影响最终推荐，需在决策矩阵中单独列出该变量的±20%扰动场景。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：节点1提供理论推导（解析式），节点2提供具体实例验证（判定阈值），节点3提供决策应用（扰动场景重计算）。三者分别对应‘如何计算’、‘如何判定’、‘如何应用’，无内容重复或矛盾，且完整覆盖了父节点关于导数分析、敏感性判定及扰动场景的要求。）
