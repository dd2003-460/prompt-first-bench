# N219: 在 N_cap >> N 的全量缓存场景下，LRU 稳态字节命中率 H_byte 的理论下界为 1 - (1 - (1-u)^{T_res})，其中 T_res

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在 N_cap >> N 的全量缓存场景下，LRU 稳态字节命中率 H_byte 的理论下界为 1 - (1 - (1-u)^{T_res})，其中 T_res 为对象平均驻留时间，u=0.01 为日更新率；若忽略更新，下界为 1.0（100%），需通过 'LRU cache hit rate lower bound full capacity' 查证理论极限。

## Corrected Claim

在 N_cap >> N 的全量缓存场景下，LRU 稳态字节命中率 H_byte 的理论下界为 1 - (1 - (1-u)^{T_res})，其中 T_res 为对象平均驻留时间，u=0.01 为日更新率；若忽略更新，下界为 1.0（100%），需通过 'LRU cache hit rate lower bound full capacity' 查证理论极限。

## Evidence

检索失败: no sources from any channel (all 5 failed)
