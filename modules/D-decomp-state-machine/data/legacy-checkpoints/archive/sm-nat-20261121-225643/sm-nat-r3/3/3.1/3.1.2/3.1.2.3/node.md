# N88: 工作点 C（极低更新率/长驻留）：u=1e-6/天, T_res=1e-3 天 → P_stale = 1 - exp(-1e-9) ≈ 1e-9；此工作点表明

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

工作点 C（极低更新率/长驻留）：u=1e-6/天, T_res=1e-3 天 → P_stale = 1 - exp(-1e-9) ≈ 1e-9；此工作点表明在极低更新率下，即使驻留时间延长至毫秒级，P_stale 仍可忽略，除非 T_res 达到秒级以上

## Corrected Claim

工作点 C（极低更新率/长驻留）：u=1e-6/天, T_res=1e-3 天 → P_stale = 1 - exp(-1e-9) ≈ 1e-9；此工作点表明在极低更新率下，即使驻留时间延长至毫秒级，P_stale 仍可忽略，除非 T_res 达到秒级以上

## Evidence

先验知识/题面给定，逻辑校验通过：P_stale = 1 - exp(-u*T_res) ≈ u*T_res = 1e-6 * 1e-3 = 1e-9，量级与结论一致
