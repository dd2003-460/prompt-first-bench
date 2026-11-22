# N53: 更新导致缓存失效的稳态概率 P_stale = 1 - exp(-0.01 * T_resident)，当 T_resident=100 小时时 P_stale

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N18

## Claim

更新导致缓存失效的稳态概率 P_stale = 1 - exp(-0.01 * T_resident)，当 T_resident=100 小时时 P_stale≈0.04，当 T_resident=1000 小时时 P_stale≈0.33，此值直接决定静态命中率 H_static 的折损系数

## Corrected Claim

更新导致缓存失效的稳态概率 P_stale = 1 - exp(-0.01 * T_resident)，当 T_resident=100 小时时 P_stale≈0.04，当 T_resident=1000 小时时 P_stale≈0.33，此值直接决定静态命中率 H_static 的折损系数
