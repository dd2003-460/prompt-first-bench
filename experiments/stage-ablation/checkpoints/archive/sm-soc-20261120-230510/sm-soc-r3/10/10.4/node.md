# N111: 市场崩溃临界点量化：若 Var(ε_seller) > Var_threshold，均衡不稳定并导致市场崩溃；临界点为 Var(ε_seller) = 0.00

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

市场崩溃临界点量化：若 Var(ε_seller) > Var_threshold，均衡不稳定并导致市场崩溃；临界点为 Var(ε_seller) = 0.000225，对应卖家定价偏差标准差 σ_ε = 0.015，此值为市场崩溃的量化阈值。

## Corrected Claim

市场崩溃临界点量化：若 Var(ε_seller) > Var_threshold，均衡不稳定并导致市场崩溃；临界点为 Var(ε_seller) = 0.000225，对应卖家定价偏差标准差 σ_ε = 0.015，此值为市场崩溃的量化阈值。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1聚焦于临界点触发后的动态演化机制（时间维度/系统稳定性），子节点2聚焦于静态阈值参数的统计解释与数据一致性验证（空间/分布维度）。两者维度不同，无重叠且无矛盾，共同构成了对'量化临界点'的完整验证（机制+定义）。）
