# N20: 字节命中率与请求命中率的转换系数：问题要求‘字节命中率’，但H_LRU ≈ 0.587通常指请求命中率（Request Hit Rate），字节命中率 H_by

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

字节命中率与请求命中率的转换系数：问题要求‘字节命中率’，但H_LRU ≈ 0.587通常指请求命中率（Request Hit Rate），字节命中率 H_bytes = H_req * (E[S_hit] / E[S_miss])，由于热门对象较小（ρ=-0.3），E[S_hit] < E[S_miss]，需计算该比值以修正最终的字节命中率数值。

## Corrected Claim

字节命中率与请求命中率的转换系数：问题要求‘字节命中率’，但H_LRU ≈ 0.587通常指请求命中率（Request Hit Rate），字节命中率 H_bytes = H_req * (E[S_hit] / E[S_miss])，由于热门对象较小（ρ=-0.3），E[S_hit] < E[S_miss]，需计算该比值以修正最终的字节命中率数值。

## Evidence

先验知识/题面给定，逻辑校验通过：字节命中率与请求命中率的转换公式 H_bytes = H_req * (E[S_hit] / E[S_miss]) 符合定义，且基于热门对象较小（ρ=-0.3）推断 E[S_hit] < E[S_miss] 的逻辑自洽。

## Search Query

byte hit rate vs request hit rate conversion cache size correlation
