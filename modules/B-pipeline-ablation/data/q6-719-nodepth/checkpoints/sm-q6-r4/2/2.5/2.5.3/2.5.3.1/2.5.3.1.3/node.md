# N614: 在 N_pop=10 基线下，新增 1 个 POP 点使平均覆盖半径从 R_avg(10) 缩小至 R_avg(11) ≈ R_avg(10) * sqrt(1

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N202

## Claim

在 N_pop=10 基线下，新增 1 个 POP 点使平均覆盖半径从 R_avg(10) 缩小至 R_avg(11) ≈ R_avg(10) * sqrt(10/11)，对应传播延迟降低 ΔL_prop ≈ (R_avg(10) - R_avg(11)) / 200,000 km/s，若 R_avg(10) ≈ 400 km，则 ΔL_prop ≈ 0.19 ms，远小于 N202 声称的 8-12 ms，说明延迟降低主要源于缓存命中率提升而非传播延迟

## Corrected Claim

在 N_pop=10 基线下，新增 1 个 POP 点使平均覆盖半径从 R_avg(10) 缩小至 R_avg(11) ≈ R_avg(10) * sqrt(10/11)，对应传播延迟降低 ΔL_prop ≈ (R_avg(10) - R_avg(11)) / 200,000 km/s，若 R_avg(10) ≈ 400 km，则 ΔL_prop ≈ 0.19 ms，远小于 N202 声称的 8-12 ms，说明延迟降低主要源于缓存命中率提升而非传播延迟

## Evidence

先验知识/题面给定，逻辑校验通过：几何覆盖半径与面积成反比，半径比值为 sqrt(10/11)；数值计算 400*(1-sqrt(10/11))/200000 ≈ 0.00019s = 0.19ms，量级与逻辑均自洽。

## Search Query

CDN cache hit rate improvement additional POP latency reduction
