# N106: 更新率 u=1%/天 对全量缓存命中率的折损量化：有效命中率 H_eff = 1 - P_stale，其中 P_stale = 1 - exp(-u * T_a

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

更新率 u=1%/天 对全量缓存命中率的折损量化：有效命中率 H_eff = 1 - P_stale，其中 P_stale = 1 - exp(-u * T_avg_lifetime)，T_avg_lifetime 为对象在缓存中的平均存活时间（等于其访问间隔），需结合 Pareto(β=0.9) 访问间隔分布计算

## Corrected Claim

更新率 u=1%/天 对全量缓存命中率的折损量化：有效命中率 H_eff = 1 - P_stale，其中 P_stale = 1 - exp(-u * T_avg_lifetime)，T_avg_lifetime 为对象在缓存中的平均存活时间（等于其访问间隔），需结合 Pareto(β=0.9) 访问间隔分布计算

## Evidence

先验知识/题面给定，逻辑校验通过：基于指数衰减模型，P_stale = 1 - exp(-u * T) 是描述固定更新率下数据陈旧概率的标准公式，H_eff = 1 - P_stale 逻辑自洽，且结合 Pareto 分布计算平均存活时间符合缓存理论常识。
