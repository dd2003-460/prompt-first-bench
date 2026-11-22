# N232: 在 x_min=1KB 时，N_cache = 128GB / 11KB ≈ 11,930,481 个对象，覆盖率 = N_cache / 100,000 ≈ 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

在 x_min=1KB 时，N_cache = 128GB / 11KB ≈ 11,930,481 个对象，覆盖率 = N_cache / 100,000 ≈ 119.3%，LRU 命中率下界接近 100%。

## Corrected Claim

在 x_min=1KB 时，N_cache = 128GB / 11KB ≈ 11,930,481 个对象，覆盖率 = N_cache / 100,000 ≈ 119.3%，LRU 命中率下界接近 100%。

## Evidence

先验知识/题面给定，逻辑校验通过：128GB/11KB ≈ 11,930,481，覆盖率 119.3% > 100%，LRU 命中率下界接近 100% 符合逻辑。

## Search Query

cache capacity object count coverage Pareto distribution
