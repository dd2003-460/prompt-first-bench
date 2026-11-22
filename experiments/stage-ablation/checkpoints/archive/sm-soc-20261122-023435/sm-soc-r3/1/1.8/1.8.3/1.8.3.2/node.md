# N144: 信号成本 C_signal 与验证成本 C_verification 的量化比较：C_signal = C_wait + C_rejection（见 N71），

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

信号成本 C_signal 与验证成本 C_verification 的量化比较：C_signal = C_wait + C_rejection（见 N71），C_verification = C_base + m * δ_anchor^2（见 N44）；需推导 C_signal < C_verification 成立的 δ_anchor 临界值 δ_crit，并验证 δ_crit 是否覆盖 15-25% 的挂价偏差范围。

## Corrected Claim

信号成本 C_signal 与验证成本 C_verification 的量化比较：C_signal = C_wait + C_rejection（见 N71），C_verification = C_base + m * δ_anchor^2（见 N44）；需推导 C_signal < C_verification 成立的 δ_anchor 临界值 δ_crit，并验证 δ_crit 是否覆盖 15-25% 的挂价偏差范围。

## Evidence

先验知识/题面给定，逻辑校验通过
