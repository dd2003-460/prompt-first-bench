# N15: 动态更新导致的缓存失效概率 P_invalid 由更新率 u=1%/天、对象平均存活时间 T_life 和 LRU 驱逐延迟决定，具体表达式为 P_invali

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

动态更新导致的缓存失效概率 P_invalid 由更新率 u=1%/天、对象平均存活时间 T_life 和 LRU 驱逐延迟决定，具体表达式为 P_invalid ≈ 1 - exp(-u * T_life / T_LRU_avg)，其中 T_LRU_avg 是对象在 LRU 队列中的平均驻留时间，需通过工作负载的访问间隔分布计算。

## Corrected Claim

动态更新导致的缓存失效概率 P_invalid 由更新率 u=1%/天、对象平均存活时间 T_life 和 LRU 驱逐延迟决定，具体表达式为 P_invalid ≈ 1 - exp(-u * T_life / T_LRU_avg)，其中 T_LRU_avg 是对象在 LRU 队列中的平均驻留时间，需通过工作负载的访问间隔分布计算。

## Evidence

父节点级核验未通过：不完备（子节点仅覆盖了 M/C=1.0 这一特定极限情况，未涵盖父节点中提到的通用情况（即 T_LRU_avg 为有限值时如何根据访问间隔分布计算），也未明确说明 T_LRU_avg 与 T_life 的一般关系，导致对父节点“具体表达式”及“需通过工作负载计算”这一核心要求的覆盖不完整。）
