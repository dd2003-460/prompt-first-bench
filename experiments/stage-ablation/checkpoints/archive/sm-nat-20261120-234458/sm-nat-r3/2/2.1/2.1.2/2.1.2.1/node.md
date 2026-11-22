# N107: LRU 稳态命中率下界的冷启动修正项：在系统启动后 T_cold 时间内，缓存未填满，命中率 H_cold(T) = 1 - (N_miss(T) / N_to

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N34

## Claim

LRU 稳态命中率下界的冷启动修正项：在系统启动后 T_cold 时间内，缓存未填满，命中率 H_cold(T) = 1 - (N_miss(T) / N_total(T))，其中 N_miss(T) 为 T 时刻尚未被请求过的对象数；对于 Pareto(β=0.9)，冷启动期的命中率上升曲线由头部对象的到达率决定。

## Corrected Claim

LRU 稳态命中率下界的冷启动修正项：在系统启动后 T_cold 时间内，缓存未填满，命中率 H_cold(T) = 1 - (N_miss(T) / N_total(T))，其中 N_miss(T) 为 T 时刻尚未被请求过的对象数；对于 Pareto(β=0.9)，冷启动期的命中率上升曲线由头部对象的到达率决定。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LRU cold start hit rate transient phase Pareto distribution
