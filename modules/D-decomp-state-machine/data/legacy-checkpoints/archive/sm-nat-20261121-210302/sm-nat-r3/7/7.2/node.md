# N76: LRU 驱逐对象的平均大小 S_LRU_evict 的估算公式：S_LRU_evict = E[S | P < P_evict]，其中 P_evict 是 LR

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

LRU 驱逐对象的平均大小 S_LRU_evict 的估算公式：S_LRU_evict = E[S | P < P_evict]，其中 P_evict 是 LRU 队列尾部对象的典型热度值，近似为热度分布的中位数或 50 分位数。

## Corrected Claim

LRU 驱逐对象的平均大小 S_LRU_evict 的估算公式：S_LRU_evict = E[S | P < P_evict]，其中 P_evict 是 LRU 队列尾部对象的典型热度值，近似为热度分布的中位数或 50 分位数。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点实质上是同一公式（Pareto逆CDF计算P_evict）在两个不同容量参数下的具体实例，存在结构性冗余；且父节点核心定义包含条件期望E[S|P<P_evict]，但子节点仅关注P_evict的数值估算，未覆盖S_LRU_evict最终如何由该阈值计算得出的完整逻辑链条。）

## Search Query

LRU eviction object size distribution
