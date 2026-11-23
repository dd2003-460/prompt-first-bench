# N8: 网络RTT的P99值：基于用户地理分布与POP点位置，RTT_P99 = 2 * (d/c) + T_switch，其中d为平均传播距离，c为光速，T_swit

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1

## Claim

网络RTT的P99值：基于用户地理分布与POP点位置，RTT_P99 = 2 * (d/c) + T_switch，其中d为平均传播距离，c为光速，T_switch为交换机/路由器处理延迟，典型值为10-50ms（同城）/50-100ms（跨区）

## Corrected Claim

网络RTT的P99值：基于用户地理分布与POP点位置，RTT_P99 = 2 * (d/c) + T_switch，其中d为平均传播距离，c为光速，T_switch为交换机/路由器处理延迟，典型值为10-50ms（同城）/50-100ms（跨区）

## Evidence

父节点级核验通过：正交+完备+无冗余（两个子节点分别对应公式中的两个核心变量 T_switch 和 d，彼此独立且无重叠。子节点1详细分解了交换/路由延迟的构成，子节点2详细分解了传播距离的地理分布，共同覆盖了父节点公式的所有关键组成部分。未发现冗余内容，因为二者针对不同的物理量。）

## Search Query

typical RTT P99 values for CDN edge nodes by region
