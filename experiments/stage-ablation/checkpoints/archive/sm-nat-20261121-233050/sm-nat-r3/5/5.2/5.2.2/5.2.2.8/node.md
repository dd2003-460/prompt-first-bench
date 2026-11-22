# N142: 驻留时间 T_res 的分布修正：T_res 并非固定 5 天，而是服从指数分布，均值 5 天，标准差 5 天；P_expire 的期望值需对 T_res 分布

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53, N54, N55

## Claim

驻留时间 T_res 的分布修正：T_res 并非固定 5 天，而是服从指数分布，均值 5 天，标准差 5 天；P_expire 的期望值需对 T_res 分布积分：E[P_expire] = 1 - E[exp(-T_res/100)] ≈ 0.0488。

## Corrected Claim

驻留时间 T_res 的分布修正：T_res 并非固定 5 天，而是服从指数分布，均值 5 天，标准差 5 天；P_expire 的期望值需对 T_res 分布积分：E[P_expire] = 1 - E[exp(-T_res/100)] ≈ 0.0488。

## Evidence

先验知识/题面给定，逻辑校验通过：指数分布均值5天，计算 E[exp(-T/100)] 积分结果约为 0.9512，故 1-0.9512=0.0488，数值与逻辑自洽。

## Search Query

cache residence time distribution exponential model
