# N28: LRU 字节命中率下界的解析近似公式为 H_LRU ≈ 1 - (1/C) * Σ_{i: s_i > C} (r_i * s_i / R_total)，该公式

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

LRU 字节命中率下界的解析近似公式为 H_LRU ≈ 1 - (1/C) * Σ_{i: s_i > C} (r_i * s_i / R_total)，该公式假设缓存能完美保留所有小于 C 的对象，但在重尾分布下，此下界通常过低，需引入 Belady's MIN 算法作为理论上限参照。

## Corrected Claim

LRU 字节命中率下界的解析近似公式为 H_LRU ≈ 1 - (1/C) * Σ_{i: s_i > C} (r_i * s_i / R_total)，该公式假设缓存能完美保留所有小于 C 的对象，但在重尾分布下，此下界通常过低，需引入 Belady's MIN 算法作为理论上限参照。

## Evidence

检索失败: no sources from any channel (all 5 failed)
