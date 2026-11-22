# N222: 对象更新率 u=1%/天 对 LRU 有效命中率的衰减因子 D 可近似为 D ≈ exp(-u * T_avg_resident)，若 T_avg_reside

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

对象更新率 u=1%/天 对 LRU 有效命中率的衰减因子 D 可近似为 D ≈ exp(-u * T_avg_resident)，若 T_avg_resident 为 1 天，则 D ≈ 0.990；若 T_avg_resident 为 10 天（长尾对象），则 D ≈ 0.905，表明长尾对象因驻留时间长受更新影响更大，需通过 'cache invalidation rate update frequency hit rate decay' 查证。

## Corrected Claim

对象更新率 u=1%/天 对 LRU 有效命中率的衰减因子 D 可近似为 D ≈ exp(-u * T_avg_resident)，若 T_avg_resident 为 1 天，则 D ≈ 0.990；若 T_avg_resident 为 10 天（长尾对象），则 D ≈ 0.905，表明长尾对象因驻留时间长受更新影响更大，需通过 'cache invalidation rate update frequency hit rate decay' 查证。

## Evidence

检索失败: no sources from any channel (all 5 failed)
