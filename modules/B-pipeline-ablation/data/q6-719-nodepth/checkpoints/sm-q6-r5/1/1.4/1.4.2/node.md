# N48: P99 延迟放大系数 A_p99 = (L_p99_peak - L_p99_avg) / L_p99_avg，其中 L_p99_peak 为高峰时段 P99 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N10

## Claim

P99 延迟放大系数 A_p99 = (L_p99_peak - L_p99_avg) / L_p99_avg，其中 L_p99_peak 为高峰时段 P99 延迟，L_p99_avg 为日均 P99 延迟；当 W(t) > 3 时，A_p99 ≈ 0.5-1.5，取决于缓存预热状态和回源带宽余量。

## Corrected Claim

P99 延迟放大系数 A_p99 = (L_p99_peak - L_p99_avg) / L_p99_avg，其具体数值取决于系统架构、缓存策略及负载特征，无固定通用范围。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别量化了父节点中提到的两个关键依赖变量（缓存预热状态和回源带宽余量），两者在物理机制上正交（一个影响请求命中路径，一个影响回源链路拥塞），且共同覆盖了父节点中'A_p99 ≈ 0.5-1.5'这一范围的主要决定因素。虽然父节点提到了W(t)作为触发条件，但子节点直接针对A_p99的两个主要影响因子进行建模，符合分解逻辑。）

## Search Query

P99 latency amplification during peak load CDN cache miss rate increase
