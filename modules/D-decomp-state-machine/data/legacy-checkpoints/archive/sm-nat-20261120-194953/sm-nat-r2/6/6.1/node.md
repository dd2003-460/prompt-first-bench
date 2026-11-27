# N69: LRU在突发流量下的驱逐代价量化为：当突发请求集中在尾部 $10\%$ 冷对象时，LRU驱逐头部 $K_{evict}$ 个热点对象导致的瞬时命中率损失 $\D

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

LRU在突发流量下的驱逐代价量化为：当突发请求集中在尾部 $10\%$ 冷对象时，LRU驱逐头部 $K_{evict}$ 个热点对象导致的瞬时命中率损失 $\Delta H_{burst} = \sum_{j \in Evicted} R_j S_j / TotalBytes$，其中 $K_{evict}$ 取决于突发窗口大小

## Corrected Claim

LRU在突发流量下的驱逐代价量化为：当突发请求集中在尾部 $10\%$ 冷对象时，LRU驱逐头部 $K_{evict}$ 个热点对象导致的瞬时命中率损失 $\Delta H_{burst} = \sum_{j \in Evicted} R_j S_j / TotalBytes$，其中 $K_{evict}$ 取决于突发窗口大小

## Evidence

先验知识/题面给定，逻辑校验通过
