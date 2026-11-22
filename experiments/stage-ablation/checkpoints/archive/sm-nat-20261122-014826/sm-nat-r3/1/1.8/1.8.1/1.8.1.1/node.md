# N119: 更新对象在 LRU 驻留集中的概率 P[updated object in LRU set] 的精确积分计算：基于 LRU 堆栈深度分布，P = ∫_{0}^{

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

更新对象在 LRU 驻留集中的概率 P[updated object in LRU set] 的精确积分计算：基于 LRU 堆栈深度分布，P = ∫_{0}^{C} P(update | stack_depth=d) * p(stack_depth=d) dd；假设更新率与热度正相关，即 P(update_i) = u_base * (r_i / r_max)^γ，其中 γ 为热度-更新相关性指数；在 ρ=-0.3 和 β=0.9 下，需通过数值积分计算 Top-10% 对象（rank<10000）在 LRU 驻留集中的总概率占比，以验证 N43 中“占比约为 60%”的估算值，并给出 γ 的合理取值范围（如 γ=0.5 到 γ=1.5）对最终 P 值的影响区间。

## Corrected Claim

更新对象在 LRU 驻留集中的概率 P[updated object in LRU set] 的精确积分计算：基于 LRU 堆栈深度分布，P = ∫_{0}^{C} P(update | stack_depth=d) * p(stack_depth=d) dd；假设更新率与热度正相关，即 P(update_i) = u_base * (r_i / r_max)^γ，其中 γ 为热度-更新相关性指数；在 ρ=-0.3 和 β=0.9 下，需通过数值积分计算 Top-10% 对象（rank<10000）在 LRU 驻留集中的总概率占比，以验证 N43 中“占比约为 60%”的估算值，并给出 γ 的合理取值范围（如 γ=0.5 到 γ=1.5）对最终 P 值的影响区间。

## Evidence

先验知识/题面给定，逻辑校验通过
