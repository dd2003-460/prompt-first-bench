# N30: 对象更新率 1%/天 对 LRU 命中率的影响因子 f_update 可通过公式 f_update = 1 - (U_rate * T_residence) 估

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

对象更新率 1%/天 对 LRU 命中率的影响因子 f_update 可通过公式 f_update = 1 - (U_rate * T_residence) 估算，其中 T_residence 为对象在缓存中的平均停留时间，若 T_residence < 100 天，则折损小于 1%，可忽略不计；否则需线性扣除。

## Corrected Claim

对象更新率 1%/天 对 LRU 命中率的影响因子 f_update 可通过公式 f_update = 1 - (U_rate * T_residence) 估算，其中 T_residence 为对象在缓存中的平均停留时间，若 T_residence < 100 天，则折损小于 1%，可忽略不计；否则需线性扣除。

## Evidence

检索失败: no sources from any channel (all 5 failed)
