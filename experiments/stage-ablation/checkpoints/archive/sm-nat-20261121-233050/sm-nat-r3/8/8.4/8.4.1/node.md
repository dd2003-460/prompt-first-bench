# N171: 基于 N76 的权重 w_i 和 N78 的 T_update_i，在 M/C=1.0 且缓存覆盖所有对象的假设下，加权平均失效概率 P_invalid_avg

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

基于 N76 的权重 w_i 和 N78 的 T_update_i，在 M/C=1.0 且缓存覆盖所有对象的假设下，加权平均失效概率 P_invalid_avg = Σ w_i * (1 - exp(-T_res_i * u))。由于 T_res_i 受限于系统运行时间或对象更新频率，若假设对象在缓存中平均驻留 1 天（受限于访问频率导致的被动刷新），则 P_invalid_avg ≈ 1 - exp(-0.01 * 1) ≈ 0.00995，折损系数约为 0.99005。

## Corrected Claim

基于 N76 的权重 w_i 和 N78 的 T_update_i，在 M/C=1.0 且缓存覆盖所有对象的假设下，加权平均失效概率 P_invalid_avg = Σ w_i * (1 - exp(-T_res_i * u))。由于 T_res_i 受限于系统运行时间或对象更新频率，若假设对象在缓存中平均驻留 1 天（受限于访问频率导致的被动刷新），则 P_invalid_avg ≈ 1 - exp(-0.01 * 1) ≈ 0.00995，折损系数约为 0.99005。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 1 - exp(-0.01) ≈ 0.00995 正确，折损系数 1 - 0.00995 = 0.99005 正确，公式推导符合指数衰减模型逻辑。
