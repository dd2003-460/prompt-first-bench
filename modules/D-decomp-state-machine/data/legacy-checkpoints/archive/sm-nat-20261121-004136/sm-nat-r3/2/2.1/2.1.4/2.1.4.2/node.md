# N106: 计算负相关修正项的具体数值：代入 ρ=-0.3, sensitivity_coeff≈1.81*(1-0.944)≈0.101（假设 H_LRU_indepen

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N40

## Claim

计算负相关修正项的具体数值：代入 ρ=-0.3, sensitivity_coeff≈1.81*(1-0.944)≈0.101（假设 H_LRU_independent≈0.944 基于容量非绑定假设），得到修正因子 1 - |ρ|*sensitivity_coeff = 1 - 0.3*0.101 ≈ 0.9697，表明负相关使命中率下界降低约 3.03%。

## Corrected Claim

计算负相关修正项的具体数值：代入 ρ=-0.3, sensitivity_coeff≈1.81*(1-0.944)≈0.101（假设 H_LRU_independent≈0.944 基于容量非绑定假设），得到修正因子 1 - |ρ|*sensitivity_coeff = 1 - 0.3*0.101 ≈ 0.9697，表明负相关使命中率下界降低约 3.03%。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 1 - 0.3 * 0.101 = 0.9697 正确，相对降低幅度 (1-0.9697)/1 ≈ 3.03% 计算无误，量级合理。
