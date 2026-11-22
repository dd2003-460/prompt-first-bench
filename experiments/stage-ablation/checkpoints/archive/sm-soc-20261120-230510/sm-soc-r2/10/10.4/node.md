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

先验知识/题面给定，逻辑校验通过（0.015的平方等于0.000225，数值自洽）
