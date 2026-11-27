# N107: 低风险规避工作点（如高频交易品类，k≈0.1），挂价溢价率噪声贡献项 P_markup_noise = 0.1 * σ²_pref，若 σ²_pref = 0.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

低风险规避工作点（如高频交易品类，k≈0.1），挂价溢价率噪声贡献项 P_markup_noise = 0.1 * σ²_pref，若 σ²_pref = 0.02，则 P_markup_noise ≈ 0.002，对总溢价率影响可忽略。

## Corrected Claim

低风险规避工作点（如高频交易品类，k≈0.1），挂价溢价率噪声贡献项 P_markup_noise = 0.1 * σ²_pref，若 σ²_pref = 0.02，则 P_markup_noise ≈ 0.002，对总溢价率影响可忽略。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 0.1 * 0.02 = 0.002 准确，量级合理，符合低风险工作点噪声贡献小的直觉。
