# N40: 负相关修正后的命中率 H_LRU_correlated 的量化公式：H_LRU_correlated = H_LRU_independent * (1 - |ρ

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N9, N10, N11

## Claim

负相关修正后的命中率 H_LRU_correlated 的量化公式：H_LRU_correlated = H_LRU_independent * (1 - |ρ| * sensitivity_coeff)，其中 sensitivity_coeff 需通过微分 dH/dρ 在 ρ=0 处评估，量化为 sensitivity_coeff = (1-β) * ln(K_max/N) / (1 + ρ * correction_factor)。

## Corrected Claim

负相关修正后的命中率 H_LRU_correlated 通常通过引入相关系数 ρ 对独立假设下的命中率 H_LRU_independent 进行修正，具体修正系数需根据工作负载特性通过实验或特定模型推导确定，而非简单的线性乘积公式。

## Evidence

父节点级核验未通过：不完备（子节点之间正交，分别处理系数定义修正和数值计算。但不完备：父节点公式包含 sensitivity_coeff 中的 ln(K_max/N) 和 correction_factor 项，而子节点1将其完全替换为基于大小变异系数的新公式，未解释 K_max、N 或 correction_factor 的去向或关系，导致公式结构断裂；子节点2仅依赖子节点1的数值，未覆盖父节点中其他未定义变量的处理。）
