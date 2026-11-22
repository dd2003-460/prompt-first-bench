# N33: 最小热度 h_min 的量化阈值：h_min = C_h * N^{-(β-1)}，用于确定哪些对象在稳态下被 LRU 缓存（热度高于阈值的对象更可能驻留），该

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

最小热度 h_min 的量化阈值：h_min = C_h * N^{-(β-1)}，用于确定哪些对象在稳态下被 LRU 缓存（热度高于阈值的对象更可能驻留），该值直接影响有效缓存对象数 K

## Corrected Claim

最小热度 h_min 的量化阈值：h_min = C_h * N^{-(β-1)}，用于确定哪些对象在稳态下被 LRU 缓存（热度高于阈值的对象更可能驻留），该值直接影响有效缓存对象数 K

## Evidence

先验知识/题面给定，逻辑校验通过
