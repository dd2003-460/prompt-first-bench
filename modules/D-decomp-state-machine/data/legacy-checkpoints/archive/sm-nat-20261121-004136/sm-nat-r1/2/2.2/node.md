# N10: 工作点2（中性价比最优）：引入 ρ=-0.3 的负相关修正，计算实际可缓存的‘高频且小’对象集合大小 C_effective = C * (1 + ρ * co

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

工作点2（中性价比最优）：引入 ρ=-0.3 的负相关修正，计算实际可缓存的‘高频且小’对象集合大小 C_effective = C * (1 + ρ * correction_factor)，并据此修正命中率下界 H_LRU_correlated = H_LRU_independent * (1 - |ρ| * sensitivity_coeff)。

## Corrected Claim

工作点2（中性价比最优）：引入 ρ=-0.3 的负相关修正，计算实际可缓存的‘高频且小’对象集合大小 C_effective = C * (1 + ρ * correction_factor)，并据此修正命中率下界 H_LRU_correlated = H_LRU_independent * (1 - |ρ| * sensitivity_coeff)。

## Evidence

先验知识/题面给定，逻辑校验通过
