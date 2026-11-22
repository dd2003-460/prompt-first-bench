# N153: 工作点3（混合局部性，中 LRU 独占率/中字节量）：在 τ_locality = 3 天（中等局部性）下，LRU 保留的‘最近但非高频’对象占比 ≈ 15%，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

工作点3（混合局部性，中 LRU 独占率/中字节量）：在 τ_locality = 3 天（中等局部性）下，LRU 保留的‘最近但非高频’对象占比 ≈ 15%，s_avg_small ≈ 0.6 * E[size]，则 B_LRU_only ≈ 0.15 * C_cache * 0.6 * E[size]，此工作点作为线性插值基准，用于在仿真中校准 LRU 独占字节量的中间值，确保 ΔH 计算中 B_LRU_only 的连续性。

## Corrected Claim

工作点3（混合局部性，中 LRU 独占率/中字节量）：在 τ_locality = 3 天（中等局部性）下，LRU 保留的‘最近但非高频’对象占比 ≈ 15%，s_avg_small ≈ 0.6 * E[size]，则 B_LRU_only ≈ 0.15 * C_cache * 0.6 * E[size]，此工作点作为线性插值基准，用于在仿真中校准 LRU 独占字节量的中间值，确保 ΔH 计算中 B_LRU_only 的连续性。

## Evidence

先验知识/题面给定，逻辑校验通过
