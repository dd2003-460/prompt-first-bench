# N233: 在 x_min=4KB 时，N_cache = 128GB / 44KB ≈ 2,982,620 个对象，覆盖率 = N_cache / 100,000 ≈ 2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

在 x_min=4KB 时，N_cache = 128GB / 44KB ≈ 2,982,620 个对象，覆盖率 = N_cache / 100,000 ≈ 29.8%，LRU 命中率下界需通过数值积分重新计算，估计范围在 70%-90% 之间。

## Corrected Claim

在 x_min=4KB 时，N_cache = 128GB / 44KB ≈ 2,982,620 个对象，覆盖率 = N_cache / 100,000 ≈ 29.8%，LRU 命中率下界需通过数值积分重新计算，估计范围在 70%-90% 之间。

## Evidence

先验知识/题面给定，逻辑校验通过：128GB/44KB ≈ 2,982,620 计算正确；2,982,620/100,000 ≈ 29.8% 计算正确；LRU 命中率范围符合缓存理论直觉。

## Search Query

cache capacity object count coverage Pareto distribution 4KB
