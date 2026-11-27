# N86: 工作点 A（标准更新率）：u=0.01/天, T_res=1e-8 天 → P_stale = 1 - exp(-1e-10) ≈ 1e-10；此工作点表明新鲜

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

工作点 A（标准更新率）：u=0.01/天, T_res=1e-8 天 → P_stale = 1 - exp(-1e-10) ≈ 1e-10；此工作点表明新鲜度失效对命中率折损 < 1e-9，可视为零

## Corrected Claim

工作点 A（标准更新率）：u=0.01/天, T_res=1e-8 天 → P_stale = 1 - exp(-1e-10) ≈ 1e-10；此工作点表明新鲜度失效对命中率折损 < 1e-9，可视为零

## Evidence

先验知识/题面给定，逻辑校验通过：P_stale = 1 - exp(-u*T_res) ≈ u*T_res = 0.01 * 1e-8 = 1e-10，量级与结论一致
