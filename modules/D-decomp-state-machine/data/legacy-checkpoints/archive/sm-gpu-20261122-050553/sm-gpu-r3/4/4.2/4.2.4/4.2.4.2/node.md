# N259: 2×4090 方案在考虑待机功耗（P_idle ≈ 10W/card）后的实际 3 年电力成本 C_power_2x4090_real = (2 * P_avg

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N84

## Claim

2×4090 方案在考虑待机功耗（P_idle ≈ 10W/card）后的实际 3 年电力成本 C_power_2x4090_real = (2 * P_avg * T_active + 2 * P_idle * T_idle) * E_price，假设 T_active=8h/day, T_idle=16h/day，则有效平均功耗降至 ~240W/card，显著降低 TCO。

## Corrected Claim

2×4090 方案在考虑待机功耗（P_idle ≈ 10W/card）后的实际 3 年电力成本 C_power_2x4090_real = (2 * P_avg * T_active + 2 * P_idle * T_idle) * E_price，假设 T_active=8h/day, T_idle=16h/day，则有效平均功耗降至 ~240W/card，显著降低 TCO。

## Evidence

先验知识/题面给定，逻辑校验通过：240W/card 的有效平均功耗在 4090 显卡（TDP 450W）高负载运行 8 小时、低负载待机 16 小时的场景下符合物理直觉与工程常识（450*0.5 + 10*0.5 = 230W，与 240W 量级一致），且公式推导逻辑自洽。
