# N173: LRU 时间局部性失效概率 P[hot but cold] 的量化定义：在泊松到达假设下，对于热度排名 r 的对象，其最近一次访问间隔 T 服从指数分布 Exp

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N62

## Claim

LRU 时间局部性失效概率 P[hot but cold] 的量化定义：在泊松到达假设下，对于热度排名 r 的对象，其最近一次访问间隔 T 服从指数分布 Exp(λ_r)。对象被误判为“冷”的条件是 T > T_threshold，其中 T_threshold 是 LRU 驱逐边界对应的平均访问间隔。P[hot but cold] = ∫_{T_threshold}^{∞} λ_r * exp(-λ_r * T) dT = exp(-λ_r * T_threshold)。需计算 T_threshold 的具体数值（基于 LRU 堆栈深度分布的尾部延迟）以代入计算。

## Corrected Claim

LRU 时间局部性失效概率 P[hot but cold] 的量化定义：在泊松到达假设下，对于热度排名 r 的对象，其最近一次访问间隔 T 服从指数分布 Exp(λ_r)。对象被误判为“冷”的条件是 T > T_threshold，其中 T_threshold 是 LRU 驱逐边界对应的平均访问间隔。P[hot but cold] = ∫_{T_threshold}^{∞} λ_r * exp(-λ_r * T) dT = exp(-λ_r * T_threshold)。需计算 T_threshold 的具体数值（基于 LRU 堆栈深度分布的尾部延迟）以代入计算。

## Evidence

先验知识/题面给定，逻辑校验通过：指数分布的生存函数推导正确，量纲一致，符合LRU缓存模型的基本数学定义。
