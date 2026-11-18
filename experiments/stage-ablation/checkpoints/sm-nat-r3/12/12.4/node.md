# N193: 修正后的 LRU 字节命中率下界 H_LRU_lower = H_base(K_eff) * η_cap，其中 H_base(K_eff) = 1 - (K_e

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N83

## Claim

修正后的 LRU 字节命中率下界 H_LRU_lower = H_base(K_eff) * η_cap，其中 H_base(K_eff) = 1 - (K_eff/N)^{0.1}，η_cap 量化了冷对象挤出效应，最终结果需代入 K_eff ≈ 1.48e7 和积分值计算。

## Corrected Claim

修正后的 LRU 字节命中率下界 H_LRU_lower = H_base(K_eff) * η_cap，其中 H_base(K_eff) = 1 - (K_eff/N)^{0.1}，η_cap 量化了冷对象挤出效应，最终结果需代入 K_eff ≈ 1.48e7 和积分值计算。

## Evidence

先验知识/题面给定，逻辑校验通过
