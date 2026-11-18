# N197: 若 u * T_res >= 0.01，则有效命中率 H_eff = H_base * (1 - ΔH_update)，其中 ΔH_update = u * T

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N84

## Claim

若 u * T_res >= 0.01，则有效命中率 H_eff = H_base * (1 - ΔH_update)，其中 ΔH_update = u * T_res * (1 - H_base)，需迭代求解 T_res 因为 R_miss 依赖于 H_base。

## Corrected Claim

若 u * T_res >= 0.01，则有效命中率 H_eff = H_base * (1 - ΔH_update)，其中 ΔH_update = u * T_res * (1 - H_base)，需迭代求解 T_res 因为 R_miss 依赖于 H_base。

## Evidence

先验知识/题面给定，逻辑校验通过
