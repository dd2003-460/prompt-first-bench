# N11: LRU 缓存占用模型：稳态下缓存保留最近访问的 K 个对象，K 由总字节容量 C 和对象平均大小决定，K ≈ C / E[S]

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N2

## Claim

LRU 缓存占用模型：稳态下缓存保留最近访问的 K 个对象，K 由总字节容量 C 和对象平均大小决定，K ≈ C / E[S]

## Corrected Claim

LRU 缓存占用模型：稳态下缓存保留最近访问的 K 个对象，K 由总字节容量 C 和对象平均大小决定，K ≈ C / E[S]

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1提供了修正后的精确模型（基于热度排序和条件分布），子节点2提供了基准模型（忽略相关性）及其数值推导和异常分析。两者分别处理了‘精确解’与‘基准/异常诊断’，逻辑上互补且正交，共同覆盖了父节点中关于K的估算及其隐含假设（负相关效应）的关键方面，无冗余。）

## Search Query

LRU cache steady state occupancy model
