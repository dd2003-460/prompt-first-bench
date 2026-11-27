# N22: 对象更新率 u=1%/天 导致的命中率折损系数 D 可通过 Markov 链稳态概率计算：D = 1 / (1 + u * T_avg_resident)，其中

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

对象更新率 u=1%/天 导致的命中率折损系数 D 可通过 Markov 链稳态概率计算：D = 1 / (1 + u * T_avg_resident)，其中 T_avg_resident 是对象在 LRU 队列中的平均平均驻留时间（秒）。

## Corrected Claim

对象更新率 u=1%/天 导致的命中率折损系数 D 可通过 Markov 链稳态概率计算：D = 1 / (1 + u * T_avg_resident)，其中 T_avg_resident 是对象在 LRU 队列中的平均平均驻留时间（秒）。

## Evidence

检索失败: no sources from any channel (all 5 failed)
