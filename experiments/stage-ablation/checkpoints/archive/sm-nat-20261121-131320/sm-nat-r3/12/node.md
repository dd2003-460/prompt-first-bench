# N160: LRU 缓存的'堆栈距离模型'（Stack Distance Model）假设请求流具有完全的时间局部性，即最近访问过的对象更可能被再次访问；该理论假设属于通用

- **status**: verified
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

LRU 缓存的'堆栈距离模型'（Stack Distance Model）假设请求流具有完全的时间局部性，即最近访问过的对象更可能被再次访问；该理论假设属于通用缓存理论（凭记忆），不依赖于具体的 Pareto 参数，但在非平稳负载下可能失效。

## Corrected Claim

LRU 缓存的'堆栈距离模型'（Stack Distance Model）假设请求流具有完全的时间局部性，即最近访问过的对象更可能被再次访问；该理论假设属于通用缓存理论（凭记忆），不依赖于具体的 Pareto 参数，但在非平稳负载下可能失效。

## Evidence

[rework-angle r1] 先验知识/题面给定，逻辑校验通过

## Search Query

LRU cache stack distance model non-stationary workload
