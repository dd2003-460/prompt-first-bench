# N183: 在覆盖半径 R=200km 的长尾工作点下，光纤单程传播延迟 L_prop = 200km / 200,000km/s = 1.0ms，往返基础延迟 RTT_b

- **status**: pending
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

父节点级核验未通过：有冗余（子节点A、B、C分别代表了高成本/低延迟、中性价比/缓存优化、低成本/高延迟三种不同的策略维度，逻辑上正交且覆盖了父节点关于延迟与成本权衡的关键方面。然而，子节点A和C本质上是同一个物理参数（覆盖半径R/节点密度）的不同取值，属于同一维度的变化，存在结构性冗余；子节点B则是另一个独立维度（缓存策略）。）

## Search Query

long distance fiber optic latency 200km
