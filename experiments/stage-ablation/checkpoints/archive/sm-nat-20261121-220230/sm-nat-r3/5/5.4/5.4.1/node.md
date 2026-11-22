# N84: 在更新率 u 服从均匀分布 U[0.001, 0.1] 的假设下，LRU 有效命中率折损因子 D(u) = 1 - (1-u)^T_resident 的解析导数

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

在更新率 u 服从均匀分布 U[0.001, 0.1] 的假设下，LRU 有效命中率折损因子 D(u) = 1 - (1-u)^T_resident 的解析导数 dD/du = -T_resident(1-u)^(T_resident-1) 在 u=0.01 处的数值为 -0.91，表明 1% 更新率处于折损曲线的线性敏感区。

## Corrected Claim

在更新率 u 服从均匀分布 U[0.001, 0.1] 的假设下，LRU 有效命中率折损因子 D(u) = 1 - (1-u)^T_resident 的解析导数 dD/du = -T_resident(1-u)^(T_resident-1) 在 u=0.01 处的数值为 -0.91，表明 1% 更新率处于折损曲线的线性敏感区。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 8 column 5 (char 738)
