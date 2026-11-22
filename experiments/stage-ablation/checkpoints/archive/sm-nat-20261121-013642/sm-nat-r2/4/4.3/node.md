# N17: 动态更新惩罚因子 δ = 1 - C_steady * (1 - P_hit_cold)，其中 P_hit_cold 为陈旧对象被请求时的命中概率（若更新后内容

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

动态更新惩罚因子 δ = 1 - C_steady * (1 - P_hit_cold)，其中 P_hit_cold 为陈旧对象被请求时的命中概率（若更新后内容不同则 miss，P_hit_cold≈0 若内容完全替换）

## Corrected Claim

动态更新惩罚因子 δ = 1 - C_steady * (1 - P_hit_cold)，其中 P_hit_cold 为陈旧对象被请求时的命中概率（若更新后内容不同则 miss，P_hit_cold≈0 若内容完全替换）

## Evidence

父节点级核验未通过：不完备（子节点覆盖了P_hit_cold的边界（0和1）及一个中间示例（0.5），正交性良好且无冗余。但完备性不足：父节点定义了动态更新公式，子节点仅讨论了P_hit_cold的取值对δ的影响，未涵盖C_steady参数的物理意义、取值范围或δ在极端C_steady值下的行为，也未说明该公式适用的系统假设（如缓存策略）。）
