# N20: 更新率对有效命中率的折损因子：当对象更新率为 u=1%/天 时，LRU 的有效命中率 H_eff 与稳态命中率 H_steady 的关系为 H_eff = H_

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

更新率对有效命中率的折损因子：当对象更新率为 u=1%/天 时，LRU 的有效命中率 H_eff 与稳态命中率 H_steady 的关系为 H_eff = H_steady * (1 - P_invalid)，其中 P_invalid 是缓存对象在访问前被更新（失效）的概率。在指数更新模型下，P_invalid ≈ 1 - exp(-u * T_resident)，T_resident 是对象在缓存中的平均驻留时间，需通过 Little's Law 和访问间隔分布计算。

## Corrected Claim

更新率对有效命中率的折损因子：当对象更新率为 u=1%/天 时，LRU 的有效命中率 H_eff 与稳态命中率 H_steady 的关系为 H_eff = H_steady * (1 - P_invalid)，其中 P_invalid 是缓存对象在访问前被更新（失效）的概率。在指数更新模型下，P_invalid ≈ 1 - exp(-u * T_resident)，T_resident 是对象在缓存中的平均驻留时间，需通过 Little's Law 和访问间隔分布计算。

## Evidence

先验知识/题面给定，逻辑校验通过：LRU缓存中对象失效概率确实取决于驻留时间内的更新事件，指数更新模型下失效概率公式 P_invalid = 1 - exp(-u * T) 符合泊松过程性质，且有效命中率定义为稳态命中率乘以未失效概率，逻辑自洽。
