# N173: 低热度对象在 LRU 缓存中占据空间但访问稀疏的量化验证：该群体对象数量占比需通过 Pareto(β=0.9) 分布中 λ_i < 50 req/day 的累积

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N59

## Claim

低热度对象在 LRU 缓存中占据空间但访问稀疏的量化验证：该群体对象数量占比需通过 Pareto(β=0.9) 分布中 λ_i < 50 req/day 的累积概率计算，预计占比约为 30%-40%；其字节流量占比需通过 Pareto(α=1.1) 大小分布在该热度区间内的积分计算，预计该区间对象平均大小大于全局均值，导致其字节命中率折损权重 w_byte 较高，需通过蒙特卡洛仿真验证 w_byte 的具体数值。

## Corrected Claim

低热度对象在 LRU 缓存中占据空间但访问稀疏的量化验证：该群体对象数量占比需通过 Pareto(β=0.9) 分布中 λ_i < 50 req/day 的累积概率计算；其字节流量占比需通过 Pareto(α=1.1) 大小分布在该热度区间内的积分计算，预计该区间对象平均大小大于全局均值，导致其字节命中率折损权重 w_byte 较高，具体数值需通过蒙特卡洛仿真验证。

## Evidence

[质询]该陈述包含具体的经验性数值预测（30%-40%占比、w_byte较高），这些数值高度依赖于具体的Pareto分布参数（β=0.9, α=1.1）及截断阈值（λ_i < 50），无法仅从第一性原理严格推导得出，属于经验事实。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且数值预测依赖具体参数设定，非纯数学推导）

## Search Query

LRU cache low popularity objects byte hit rate loss Pareto distribution simulation
