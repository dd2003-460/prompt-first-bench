# N169: 在 M/C=1.0 且无主动驱逐的稳态下，所有缓存内对象的理论驻留时间 T_res_i 均趋于无穷大（T_res_i → ∞），导致 P_invalid = 1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N66

## Claim

在 M/C=1.0 且无主动驱逐的稳态下，所有缓存内对象的理论驻留时间 T_res_i 均趋于无穷大（T_res_i → ∞），导致 P_invalid = 1 - exp(-u * ∞) 的极限计算需引入更新率 u 与对象实际更新周期 T_update_i 的耦合，修正为 P_invalid_i = 1 - exp(-T_update_i / (1/u))，其中 T_update_i 为对象 i 两次更新间的间隔。

## Corrected Claim

在 M/C=1.0 且无主动驱逐的稳态下，所有缓存内对象的理论驻留时间 T_res_i 均趋于无穷大（T_res_i → ∞），导致 P_invalid = 1 - exp(-u * ∞) 的极限计算需引入更新率 u 与对象实际更新周期 T_update_i 的耦合，修正为 P_invalid_i = 1 - exp(-T_update_i / (1/u))，其中 T_update_i 为对象 i 两次更新间的间隔。

## Evidence

先验知识/题面给定，逻辑校验通过：在稳态且无驱逐条件下，对象驻留时间趋于无穷大，失效概率由更新率决定，公式推导符合指数分布性质。
