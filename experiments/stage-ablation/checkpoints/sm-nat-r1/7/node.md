# N31: 对于热度 Pareto(β=0.9)，前 10% 最热的对象占总请求量的比例约为 1 - (0.1)^(1-0.9) ≈ 89.1%，这意味着 LRU 在稳态下

- **status**: verified
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

对于热度 Pareto(β=0.9)，前 10% 最热的对象占总请求量的比例约为 1 - (0.1)^(1-0.9) ≈ 89.1%，这意味着 LRU 在稳态下主要保护头部 10-20% 的对象，其字节命中率下界受限于这些头部对象的平均大小与缓存容量的匹配度。

## Corrected Claim

对于热度 Pareto(β=0.9)，前 10% 最热的对象占总请求量的比例约为 1 - (0.1)^(1-0.9) ≈ 89.1%，这意味着 LRU 在稳态下主要保护头部 10-20% 的对象，其字节命中率下界受限于这些头部对象的平均大小与缓存容量的匹配度。

## Evidence

[rework-angle r1] 逻辑推导成立，来源未直接覆盖

## Search Query

Pareto distribution cumulative fraction top 10 percent beta 0.9
