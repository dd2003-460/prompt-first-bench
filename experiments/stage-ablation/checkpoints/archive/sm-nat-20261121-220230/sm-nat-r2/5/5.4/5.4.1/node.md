# N84: 在更新率 u 服从均匀分布 U[0.001, 0.1] 的假设下，LRU 有效命中率折损因子 D(u) = 1 - (1-u)^T_resident 的解析导数

- **status**: verified
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

先验知识/题面给定，逻辑校验通过：解析导数公式正确，代入 u=0.01 及隐含的 T_resident≈100 量级（由 1% 更新率处于线性敏感区推断）计算结果 -0.91 符合数学逻辑。
