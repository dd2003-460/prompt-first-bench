# N23: 自建节点的 P99 延迟物理极限 = RTT + 处理时间，其中 RTT = 2 * (用户到节点距离 / 光速) * 传播延迟系数（光纤中光速约为 2e8 m

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

自建节点的 P99 延迟物理极限 = RTT + 处理时间，其中 RTT = 2 * (用户到节点距离 / 光速) * 传播延迟系数（光纤中光速约为 2e8 m/s），处理时间通常 < 10ms（缓存命中时）；对于 500km 距离，RTT ≈ 5ms，总 P99 延迟 ≈ 15ms。

## Corrected Claim

自建节点的 P99 延迟物理极限 = RTT + 处理时间，其中 RTT = 2 * (用户到节点距离 / 光速) * 传播延迟系数（光纤中光速约为 2e8 m/s），处理时间通常 < 10ms（缓存命中时）；对于 500km 距离，RTT ≈ 5ms，总 P99 延迟 ≈ 15ms。

## Evidence

先验知识/题面给定，逻辑校验通过：500km距离下，光纤RTT计算为 2 * 500,000m / 2e8m/s = 5ms，加上<10ms处理时间，总延迟约15ms，符合物理规律及工程常识。
