# N207: 截断 Pareto(α=1.1, s_min=1KB, s_max=10GB) 的归一化常数 Z_size = (s_min^(1-α) - s_max^(1-

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N71

## Claim

截断 Pareto(α=1.1, s_min=1KB, s_max=10GB) 的归一化常数 Z_size = (s_min^(1-α) - s_max^(1-α)) / (α-1)，代入 α=1.1 得 Z_size = (1KB^(-0.1) - 10GB^(-0.1)) / 0.1 ≈ (0.7943 - 0.00794) / 0.1 ≈ 7.864，用于计算条件期望 E[size | s_min ≤ s ≤ s_max] = 1 / (Z_size * (α-1)) * (s_min^(1-α) - s_max^(1-α))，确保 E[size] 有限且匹配 128GB 约束。

## Corrected Claim

截断 Pareto(α=1.1, s_min=1KB, s_max=10GB) 的归一化常数 Z_size = (s_min^(1-α) - s_max^(1-α)) / (α-1)，代入 α=1.1 得 Z_size = (1KB^(-0.1) - 10GB^(-0.1)) / 0.1 ≈ (0.7943 - 0.00794) / 0.1 ≈ 7.864，用于计算条件期望 E[size | s_min ≤ s ≤ s_max] = 1 / (Z_size * (α-1)) * (s_min^(1-α) - s_max^(1-α))，确保 E[size] 有限且匹配 128GB 约束。
