# N336: 动态调度修正项 ΔA_geo_dynamic：当引入基于实时探测（RTT probing）的动态调度时，有效准确率 A_geo_eff = A_geo_stat

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N104

## Claim

动态调度修正项 ΔA_geo_dynamic：当引入基于实时探测（RTT probing）的动态调度时，有效准确率 A_geo_eff = A_geo_static + (1 - A_geo_static) * P_probe_success，P_probe_success 典型值为 0.3-0.5，可将整体调度误差降低 30-50%。

## Corrected Claim

动态调度修正项 ΔA_geo_dynamic：当引入基于实时探测（RTT probing）的动态调度时，有效准确率 A_geo_eff = A_geo_static + (1 - A_geo_static) * P_probe_success，P_probe_success 典型值为 0.3-0.5，可将整体调度误差降低 30-50%。

## Evidence

先验知识/题面给定，逻辑校验通过
