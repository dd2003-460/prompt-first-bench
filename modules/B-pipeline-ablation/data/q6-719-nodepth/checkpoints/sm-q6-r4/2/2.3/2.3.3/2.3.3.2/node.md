# N183: 在覆盖半径 R=200km 的长尾工作点下，光纤单程传播延迟 L_prop = 200km / 200,000km/s = 1.0ms，往返基础延迟 RTT_b

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N58

## Claim

在覆盖半径 R=200km 的长尾工作点下，光纤单程传播延迟 L_prop = 200km / 200,000km/s = 1.0ms，往返基础延迟 RTT_base = 2 * 1.0ms + 2.5ms = 4.5ms，相比基准点增加 1.5ms 的纯物理延迟开销。

## Corrected Claim

在覆盖半径 R=200km 的长尾工作点下，光纤单程传播延迟 L_prop = 200km / 200,000km/s = 1.0ms，往返基础延迟 RTT_base = 2 * 1.0ms + 2.5ms = 4.5ms，相比基准点增加 1.5ms 的纯物理延迟开销。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应高成本/低延迟、中性价比/策略优化、低成本/高延迟三个不同的优化维度（物理拓扑密度 vs 缓存策略 vs 覆盖半径），彼此独立且互斥，覆盖了父节点中延迟构成的主要变量（传播延迟、处理/排队延迟隐含在RTT_base中、回源延迟），无逻辑矛盾或重复。）

## Search Query

long distance fiber optic latency 200km
