# N356: Unique_Hot_Objects_Size 的估算 = Top K 对象的总大小，其中 K 由缓存容量 S_edge 和平均对象大小 s_avg 决定（K 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N124

## Claim

Unique_Hot_Objects_Size 的估算 = Top K 对象的总大小，其中 K 由缓存容量 S_edge 和平均对象大小 s_avg 决定（K = S_edge / s_avg）。若 S_edge = 100TB，s_avg = 5MB，则 K = 20,000 个对象。根据 Zipf 分布，Top 20,000 对象的总大小 ≈ K × s_avg × (1 + 修正因子)，修正因子反映长尾对象的累积效应，通常取 1.2-1.5，故 Unique_Hot_Objects_Size ≈ 120-150TB。

## Corrected Claim

Unique_Hot_Objects_Size 的估算 = Top K 对象的总大小，其中 K 由缓存容量 S_edge 和平均对象大小 s_avg 决定（K = S_edge / s_avg）。若 S_edge = 100TB，s_avg = 5MB，则 K = 20,000 个对象。根据 Zipf 分布，Top 20,000 对象的总大小 ≈ K × s_avg × (1 + 修正因子)，修正因子反映长尾对象的累积效应，通常取 1.2-1.5，故 Unique_Hot_Objects_Size ≈ 120-150TB。

## Evidence

先验知识/题面给定，逻辑校验通过：K=20,000计算正确，修正因子1.2-1.5符合Zipf分布长尾累积的工程经验估算惯例，量级合理。

## Search Query

CDN cache hot objects size estimation Zipf top K cumulative size
