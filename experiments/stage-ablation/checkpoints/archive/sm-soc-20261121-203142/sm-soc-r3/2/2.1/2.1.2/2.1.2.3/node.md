# N153: 价格区间边界对噪声截断的影响：若 R_pref ~ N(0, σ²) 被价格区间截断（Truncated Normal），则区间 [1.15, 1.25] 内的

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N42

## Claim

价格区间边界对噪声截断的影响：若 R_pref ~ N(0, σ²) 被价格区间截断（Truncated Normal），则区间 [1.15, 1.25] 内的条件方差 Var(ε|Interval) 小于总体方差，需计算截断正态分布的条件方差公式以修正 σ_pref 的有效值，避免高估噪声幅度。

## Corrected Claim

价格区间边界对噪声截断的影响：若 R_pref ~ N(0, σ²) 被价格区间截断（Truncated Normal），则区间 [1.15, 1.25] 内的条件方差 Var(ε|Interval) 小于总体方差，需计算截断正态分布的条件方差公式以修正 σ_pref 的有效值，避免高估噪声幅度。

## Evidence

先验知识/题面给定，逻辑校验通过：截断正态分布的条件方差确实小于总体方差，这是概率论的基本性质。
