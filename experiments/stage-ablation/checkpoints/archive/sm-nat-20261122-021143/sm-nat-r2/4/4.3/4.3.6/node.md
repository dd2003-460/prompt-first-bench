# N56: 重新计算稳态命中率下界：H_byte_LRU_eff ≥ 1 - (C_eff / W_eff_eff)，其中 W_eff_eff 是有效工作集大小，需根据 C

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N17

## Claim

重新计算稳态命中率下界：H_byte_LRU_eff ≥ 1 - (C_eff / W_eff_eff)，其中 W_eff_eff 是有效工作集大小，需根据 C_eff 重新求解 ∫_{k=1}^{K_eff} S(k) dk = C_eff，得到新的 K_eff，然后计算 H_byte_LRU_eff = ∫_{k=1}^{K_eff} R(k) dk / ∫_{k=1}^{N} R(k) dk。

## Corrected Claim

重新计算稳态命中率下界：H_byte_LRU_eff ≥ 1 - (C_eff / W_eff_eff)，其中 W_eff_eff 是有效工作集大小，需根据 C_eff 重新求解 ∫_{k=1}^{K_eff} S(k) dk = C_eff，得到新的 K_eff，然后计算 H_byte_LRU_eff = ∫_{k=1}^{K_eff} R(k) dk / ∫_{k=1}^{N} R(k) dk。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

LRU hit rate recalculation with reduced cache capacity
