# N10: P99延迟 = RTT + 缓存未命中时的回源延迟 + 节点处理延迟，其中RTT = 2 * (用户到节点距离 / 光速) * 传播延迟系数，缓存未命中率 = 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

P99延迟 = RTT + 缓存未命中时的回源延迟 + 节点处理延迟，其中RTT = 2 * (用户到节点距离 / 光速) * 传播延迟系数，缓存未命中率 = 1 - 缓存命中率，回源延迟 = 回源RTT + 源站处理时间。

## Corrected Claim

P99延迟 = RTT + 缓存未命中时的回源延迟 + 节点处理延迟，其中RTT = 2 * (用户到节点距离 / 光速) * 传播延迟系数，缓存未命中率 = 1 - 缓存命中率，回源延迟 = 回源RTT + 源站处理时间。

## Evidence

先验知识/题面给定，逻辑校验通过
