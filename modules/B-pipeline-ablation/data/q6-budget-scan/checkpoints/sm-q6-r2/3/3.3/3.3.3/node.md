# N107: 缓存命中率H_cache的Zipf分布解析解：H_cache ≈ 1 - (1 - α) / (α * ln(N_objects))，其中N_objects为可

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N28

## Claim

缓存命中率H_cache的Zipf分布解析解：H_cache ≈ 1 - (1 - α) / (α * ln(N_objects))，其中N_objects为可缓存对象总数（图片+短视频去重后数量），α为Zipf参数（N26指出需校准，典型视频平台α≈0.9-1.2），该公式用于从N26/N27推导具体H_cache值

## Corrected Claim

缓存命中率H_cache的Zipf分布解析解：H_cache ≈ 1 - (1 - α) / (α * ln(N_objects))，其中N_objects为可缓存对象总数（图片+短视频去重后数量），α为Zipf参数（N26指出需校准，典型视频平台α≈0.9-1.2），该公式用于从N26/N27推导具体H_cache值

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Zipf distribution cache hit rate formula
