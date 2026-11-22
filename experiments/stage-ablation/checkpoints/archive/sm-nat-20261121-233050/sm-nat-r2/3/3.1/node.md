# N11: LFU 稳态字节命中率上界（工作点1：理想无更新场景）：LFU 缓存前 M 个最高频对象（按频率排序），命中率 H_LFU = (Sum_{i=1}^M S_i

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N3

## Claim

LFU 稳态字节命中率上界（工作点1：理想无更新场景）：LFU 缓存前 M 个最高频对象（按频率排序），命中率 H_LFU = (Sum_{i=1}^M S_i * F_i) / (Sum_{j=1}^N S_j * F_j)，其中 M 由 Sum_{i=1}^M S_i <= 128GB 决定。

## Corrected Claim

LFU 稳态字节命中率上界（工作点1：理想无更新场景）：LFU 缓存前 M 个最高频对象（按频率排序），命中率 H_LFU = (Sum_{i=1}^M S_i * F_i) / (Sum_{j=1}^N S_j * F_j)，其中 M 由 Sum_{i=1}^M S_i <= 128GB 决定。

## Evidence

先验知识/题面给定，逻辑校验通过：LFU在稳态下缓存最高频对象，命中率定义为缓存内请求量占总请求量的比例，公式推导符合定义。

## Search Query

LFU cache hit rate steady state Pareto workload
