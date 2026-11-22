# N87: 工作点 B（高更新率/短驻留）：u=1/天, T_res=1e-8 天 → P_stale = 1 - exp(-1e-8) ≈ 1e-8；此工作点表明即使更新

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

工作点 B（高更新率/短驻留）：u=1/天, T_res=1e-8 天 → P_stale = 1 - exp(-1e-8) ≈ 1e-8；此工作点表明即使更新率提高 100 倍，P_stale 仍远低于 0.01，新鲜度失效仍非主导因素

## Corrected Claim

工作点 B（高更新率/短驻留）：u=1/天, T_res=1e-8 天 → P_stale = 1 - exp(-1e-8) ≈ 1e-8；此工作点表明即使更新率提高 100 倍，P_stale 仍远低于 0.01，新鲜度失效仍非主导因素

## Evidence

先验知识/题面给定，逻辑校验通过：P_stale = 1 - exp(-u*T_res) 在 u*T_res << 1 时近似为 u*T_res，即 1e-8，远小于 0.01，推导自洽。
