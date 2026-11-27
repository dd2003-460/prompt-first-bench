# N15: 更新导致的缓存失效概率 P_invalid = 1 - exp(-λ_update * τ_LRU)，其中 λ_update = 0.01/day，τ_LRU 

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

更新导致的缓存失效概率 P_invalid = 1 - exp(-λ_update * τ_LRU)，其中 λ_update = 0.01/day，τ_LRU 为对象在 LRU 缓存中的平均驻留时间（取决于缓存容量 C=128GB 与请求速率 R=50M/day 及大小分布）。

## Corrected Claim

更新导致的缓存失效概率 P_invalid = 1 - exp(-λ_update * τ_LRU)，其中 λ_update = 0.01/day，τ_LRU 为对象在 LRU 缓存中的平均驻留时间（取决于缓存容量 C=128GB 与请求速率 R=50M/day 及大小分布）。

## Evidence

父节点级核验未通过：不完备（父节点定义了包含多个变量（λ_update, τ_LRU）的公式，其中 τ_LRU 明确依赖于缓存容量、请求速率和大小分布。子节点仅提供了最终数值解，完全缺失了对关键中间变量 τ_LRU 的推导或定义过程，导致无法验证数值解的正确性，未覆盖父节点中关于 τ_LRU 依赖关系的关键方面。）
