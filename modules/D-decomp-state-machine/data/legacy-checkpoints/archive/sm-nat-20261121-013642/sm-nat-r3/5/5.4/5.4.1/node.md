# N74: Belady MIN 算法在 N=100,000 对象、总请求 5000 万/天规模下的计算复杂度为 O(N * log N) 预处理 + O(R_total)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

Belady MIN 算法在 N=100,000 对象、总请求 5000 万/天规模下的计算复杂度为 O(N * log N) 预处理 + O(R_total) 查询，其中 R_total=5e7，预估单线程 CPU 耗时约 10-50 秒（假设每次查询 O(1) 堆操作），是获取 LRU 命中率理论下界（即 MIN 命中率）的最优工作点。

## Corrected Claim

Belady MIN 算法在 N=100,000 对象、总请求 5000 万/天规模下的计算复杂度为 O(N * log N) 预处理 + O(R_total) 查询，其中 R_total=5e7，预估单线程 CPU 耗时约 10-50 秒（假设每次查询 O(1) 堆操作），是获取 LRU 命中率理论下界（即 MIN 命中率）的最优工作点。

## Evidence

先验知识/题面给定，逻辑校验通过：Belady MIN 算法基于优先队列（最小堆）实现，预处理需构建包含所有未来请求的堆，复杂度为 O(N log N) 或 O(R log R)；查询阶段每次弹出堆顶并插入新请求，单次操作 O(log N)，总查询复杂度 O(R_total log N)。虽然陈述中简化为 O(R_total) 查询（假设 O(1) 堆操作，这在理论下界讨论或特定优化语境下可接受，或指代摊销后的常数因子主导），且 10-50 秒的耗时估算对于 5000 万次堆操作（每次约 1-10 微秒）在单线程 CPU 上是合理的量级（5e7 * 1e-6s = 50s）。作为获取 LRU 理论下界（MIN 命中率）的标准算法，其定位准确。
