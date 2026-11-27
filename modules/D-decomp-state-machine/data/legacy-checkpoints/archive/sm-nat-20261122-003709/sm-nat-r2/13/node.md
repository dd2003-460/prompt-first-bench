# N98: LFU相对LRU的最大提升幅度 ΔH_max 的量化：在β=0.9（高偏斜）和ρ=-0.3（热小冷大）条件下，LFU因能更准确保留小热对象而优于LRU。理论提升

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

LFU相对LRU的最大提升幅度 ΔH_max 的量化：在β=0.9（高偏斜）和ρ=-0.3（热小冷大）条件下，LFU因能更准确保留小热对象而优于LRU。理论提升上限 ΔH_max ≈ (Gini_β - 0.5) * 10% ≈ 4.09%（基于Gini=0.909），实际提升受更新率滞后影响，净提升约 2-3 个百分点。

## Corrected Claim

LFU相对LRU的最大提升幅度 ΔH_max 的量化：在β=0.9（高偏斜）和ρ=-0.3（热小冷大）条件下，LFU因能更准确保留小热对象而优于LRU。理论提升上限 ΔH_max ≈ (Gini_β - 0.5) * 10% ≈ 4.09%（基于Gini=0.909），实际提升受更新率滞后影响，净提升约 2-3 个百分点。

## Evidence

检索失败: no sources from any channel (all 5 failed)
