# N47: ΔH 的上界估计：ΔH_max = H_byte_LFU - H_byte_LRU，在 β=0.9 的平缓热度分布下，LFU 与 LRU 的缓存集合差异主要来自

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N11

## Claim

ΔH 的上界估计：ΔH_max = H_byte_LFU - H_byte_LRU，在 β=0.9 的平缓热度分布下，LFU 与 LRU 的缓存集合差异主要来自低频大对象，ΔH 的上界约为 2-5 个百分点，需通过对比两种策略的缓存集合差异量化。

## Corrected Claim

ΔH 的上界估计：ΔH_max = H_byte_LFU - H_byte_LRU，在 β=0.9 的平缓热度分布下，LFU 与 LRU 的缓存集合差异主要来自低频大对象，ΔH 的上界约为 2-5 个百分点，需通过对比两种策略的缓存集合差异量化。

## Evidence

父节点级核验未通过：不完备（子节点存在严重的逻辑矛盾和概念混淆。首先，父节点定义的是ΔH的上界（ΔH_max），但子节点2却将其定义为“噪声下限”（ΔH_min），且计算逻辑（ΔH_max - 噪声）实际上是在估算实际性能或下界，而非上界，这与父节点主题不符。其次，子节点1中提到的“Top_K_freq”未定义K与缓存大小的关系，且直接假设理想状态下的命中率公式缺乏严谨性。最重要的是，父节点强调“需通过对比两种策略的缓存集合差异量化”，但两个子节点均侧重于命中率（Hit Rate）的代数估算，完全忽略了父节点核心的“集合差异量化”方法论，导致完备性缺失。）

## Search Query

LFU vs LRU hit rate difference upper bound Pareto workload
