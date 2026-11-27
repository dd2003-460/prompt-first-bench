# N84: Pareto 分布截断点对 LFU 提升幅度 ΔH 的影响：在 x_min=1KB 和 x_max=1GB 的基准场景下，ΔH ≈ -0.1%；当 x_min=

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N27

## Claim

Pareto 分布截断点对 LFU 提升幅度 ΔH 的影响：在 x_min=1KB 和 x_max=1GB 的基准场景下，ΔH ≈ -0.1%；当 x_min=4KB 时，由于 LFU 更倾向于保留高频小对象，其命中率下界降至 65%，ΔH ≈ -5%；当 x_max=10GB 时，LFU 的长尾处理劣势更明显，ΔH ≈ -3%。量化不同截断点下 LFU 相对于 LRU 的劣势幅度。

## Corrected Claim

在Pareto分布截断点变化的基准场景下，LFU相对于LRU的命中率提升幅度ΔH通常表现为负值（即LFU劣势），具体数值随x_min和x_max的变化而波动，例如在x_min=4KB时劣势可能扩大至约5%，在x_max=10GB时约为3%。

## Evidence

[质询]该陈述包含具体的经验性数值（如ΔH ≈ -0.1%, -5%, -3%）和特定场景下的命中率下界（65%），这些属于依赖具体工作负载、缓存大小及实现细节的经验事实，无法从Pareto分布或LFU/LRU算法的第一性原理中严格推导得出。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且数值无法从第一性原理推出）

## Search Query

LFU LRU hit rate difference Pareto truncation points x_min x_max sensitivity analysis negative correlation size heat
