# N154: 流量复用系数 h(T_deal) 的函数形式：h(T_deal) = 1 / (1 + T_deal/T_cycle)，其中 T_cycle 为平台用户平均活跃

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N46

## Claim

流量复用系数 h(T_deal) 的函数形式：h(T_deal) = 1 / (1 + T_deal/T_cycle)，其中 T_cycle 为平台用户平均活跃周期（如 7 天）；当 T_deal 远小于 T_cycle 时，h ≈ 1（流量完全复用）；当 T_deal > T_cycle 时，h < 1（流量流失），需量化 T_deal 从 7 天缩短至 3 天时 h 的提升幅度（约 14%）。

## Corrected Claim

流量复用系数 h(T_deal) 的函数形式：h(T_deal) = 1 / (1 + T_deal/T_cycle)，其中 T_cycle 为平台用户平均活跃周期（如 7 天）；当 T_deal 远小于 T_cycle 时，h ≈ 1（流量完全复用）；当 T_deal > T_cycle 时，h < 1（流量流失），需量化 T_deal 从 7 天缩短至 3 天时 h 的提升幅度（约 14%）。
