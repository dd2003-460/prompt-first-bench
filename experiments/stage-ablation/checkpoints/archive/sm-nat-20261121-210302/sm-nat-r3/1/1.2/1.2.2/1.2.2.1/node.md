# N105: N_cap >> N 条件下的 LRU 行为退化分析：当 N_cap >= N 时，LRU 队列永远不会驱逐任何对象（因为所有对象始终在缓存中），因此 LRU 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

N_cap >> N 条件下的 LRU 行为退化分析：当 N_cap >= N 时，LRU 队列永远不会驱逐任何对象（因为所有对象始终在缓存中），因此 LRU 等价于‘全量缓存’策略，其字节命中率下界仅受对象更新率 u 和请求大小分布影响，与替换算法无关

## Corrected Claim

N_cap >> N 条件下的 LRU 行为退化分析：当 N_cap >= N 时，LRU 队列永远不会驱逐任何对象（因为所有对象始终在缓存中），因此 LRU 等价于‘全量缓存’策略，其字节命中率下界仅受对象更新率 u 和请求大小分布影响，与替换算法无关

## Evidence

先验知识/题面给定，逻辑校验通过：当缓存容量 N_cap >= 对象总数 N 时，LRU 队列中始终容纳所有对象，不会发生驱逐，因此行为等价于全量缓存，命中率仅取决于访问模式（更新率 u 和请求分布），与替换策略无关。
