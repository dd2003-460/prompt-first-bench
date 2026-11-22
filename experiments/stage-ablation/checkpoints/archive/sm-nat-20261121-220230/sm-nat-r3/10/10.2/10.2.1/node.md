# N289: 相关性修正项 Δρ 在 Belady MIN 近似中的积分形式：Δρ = ∫_{s∈C_min, h∈H_min} (f_{S,H}(s,h) - f_S(s)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N100

## Claim

相关性修正项 Δρ 在 Belady MIN 近似中的积分形式：Δρ = ∫_{s∈C_min, h∈H_min} (f_{S,H}(s,h) - f_S(s)f_H(h)) ds dh，需明确 C_min 和 H_min 的边界定义（即缓存容量 C 和热度阈值 h_th 对应的区域）。

## Corrected Claim

相关性修正项 Δρ 在 Belady MIN 近似中的积分形式：Δρ = ∫_{s∈C_min, h∈H_min} (f_{S,H}(s,h) - f_S(s)f_H(h)) ds dh，需明确 C_min 和 H_min 的边界定义（即缓存容量 C 和热度阈值 h_th 对应的区域）。

## Evidence

先验知识/题面给定，逻辑校验通过
