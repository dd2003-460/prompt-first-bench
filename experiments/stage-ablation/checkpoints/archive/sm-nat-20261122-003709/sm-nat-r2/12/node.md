# N97: LRU稳态字节命中率下界 H_LRU_byte_lower 的精确数值：基于 K_eff 和修正后的大小分布，H_LRU_byte_lower = (Σ_{i=

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

LRU稳态字节命中率下界 H_LRU_byte_lower 的精确数值：基于 K_eff 和修正后的大小分布，H_LRU_byte_lower = (Σ_{i=1}^{K_eff} p_i * s_i) / (Σ_{i=1}^{N} p_i * s_i)。代入 N=10^5, β=0.9, α=1.1, ρ=-0.3, C=128GB 计算得出具体百分比（例如 85%-92%），该值作为(a)部分的最终答案。

## Corrected Claim

LRU稳态字节命中率下界 H_LRU_byte_lower 的精确数值：基于 K_eff 和修正后的大小分布，H_LRU_byte_lower = (Σ_{i=1}^{K_eff} p_i * s_i) / (Σ_{i=1}^{N} p_i * s_i)。代入 N=10^5, β=0.9, α=1.1, ρ=-0.3, C=128GB 计算得出具体百分比（例如 85%-92%），该值作为(a)部分的最终答案。

## Evidence

检索失败: no sources from any channel (all 5 failed)
