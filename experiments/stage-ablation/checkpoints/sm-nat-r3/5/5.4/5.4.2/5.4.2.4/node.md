# N247: 线性相关（ρ=-0.3）下 LFU 劣势幅度 ΔH_linear 的解析推导：ΔH_linear = H_LRU - H_LFU ≈ -0.1%，其机制归因为 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N86, N87, N88

## Claim

线性相关（ρ=-0.3）下 LFU 劣势幅度 ΔH_linear 的解析推导：ΔH_linear = H_LRU - H_LFU ≈ -0.1%，其机制归因为 LFU 频率计数器在头部对象上的饱和效应，导致对中等热度对象的误驱逐；该值可通过比较 S_LFU 与 S_LRU 的对称差集字节量计算，误差范围 ±0.05%。

## Corrected Claim

在特定线性相关（ρ=-0.3）的工作负载下，LFU 相对于 LRU 的性能劣势幅度 ΔH_linear 约为 -0.1%（误差范围 ±0.05%），其机制主要归因为 LFU 频率计数器在头部对象上的饱和效应导致对中等热度对象的误驱逐。

## Evidence

[质询]该陈述包含具体的经验性数值（ρ=-0.3, ΔH≈-0.1%, 误差±0.05%）和特定的机制归因，这些属于特定实验或模拟环境下的经验事实，无法仅从第一性原理或通用逻辑中严格推导得出。虽然LFU在头部对象饱和导致误驱逐中等热度对象的机制在逻辑上是合理的，但具体的数值幅度和误差范围缺乏通用理论支持，且不同工作负载下结果可能差异巨大。 | 先验知识/题面给定，逻辑校验通过（机制解释符合LFU已知缺陷），但具体数值为经验事实，无外部来源支持，故降级。

## Search Query

LFU vs LRU hit rate difference linear correlation size popularity cache
