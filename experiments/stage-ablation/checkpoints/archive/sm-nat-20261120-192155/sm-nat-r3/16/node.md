# N155: LFU相比LRU的提升百分点 ΔH_max 在稳态Pareto负载下通常小于 0.5%，因为LRU在稳定热点分布下能迅速收敛到最优集合；LFU的优势仅在负载存在

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

LFU相比LRU的提升百分点 ΔH_max 在稳态Pareto负载下通常小于 0.5%，因为LRU在稳定热点分布下能迅速收敛到最优集合；LFU的优势仅在负载存在周期性扫描（scan）或热点剧烈漂移时显现，此时LFU通过频率计数避免冷对象污染，提升幅度可达 5-10%。

## Corrected Claim

LFU相比LRU的提升百分点 ΔH_max 在稳态Pareto负载下通常小于 0.5%，因为LRU在稳定热点分布下能迅速收敛到最优集合；LFU的优势仅在负载存在周期性扫描（scan）或热点剧烈漂移时显现，此时LFU通过频率计数避免冷对象污染，提升幅度可达 5-10%。

## Evidence

检索失败: no sources from any channel (all 5 failed)
