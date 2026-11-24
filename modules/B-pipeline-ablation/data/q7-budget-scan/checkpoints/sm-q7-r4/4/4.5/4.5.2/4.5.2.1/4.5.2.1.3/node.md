# N476: 工作点C（经济型）：接受RTO 8小时，聚合重建带宽 50GB/s，缓存命中率0.4，所需SSD缓存容量 C_cache_C = (50 * 8 * 3600)

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N210

## Claim

工作点C（经济型）：接受RTO 8小时，聚合重建带宽 50GB/s，缓存命中率0.4，所需SSD缓存容量 C_cache_C = (50 * 8 * 3600) / 0.4 = 3,600,000 GB ≈ 3.44 PB，虽然RTO较长，但因带宽需求减半，若采用大容量低速SSD，单位成本可能更低。

## Corrected Claim

工作点C（经济型）：接受RTO 8小时，聚合重建带宽 50GB/s，缓存命中率0.4，所需SSD缓存容量 C_cache_C = (50 * 8 * 3600) / 0.4 = 3,600,000 GB ≈ 3.44 PB，虽然RTO较长，但因带宽需求减半，若采用大容量低速SSD，单位成本可能更低。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 (50 * 8 * 3600) / 0.4 = 3,600,000 GB 正确，单位换算 3,600,000 / 1024 / 1024 ≈ 3.44 PB 正确，逻辑自洽。
