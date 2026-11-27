# N100: 厚尾修正项的量化：当峰度系数 κ > 3 时，需使用广义误差分布（GED）或 t 分布修正 σ 的估计，修正后的尾部溢价概率 P(Error > 2σ) 从正态

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

厚尾修正项的量化：当峰度系数 κ > 3 时，需使用广义误差分布（GED）或 t 分布修正 σ 的估计，修正后的尾部溢价概率 P(Error > 2σ) 从正态假设下的 2.3% 上升至 5%-10%，影响高挂价策略的尾部风险计算。

## Corrected Claim

厚尾修正项的量化：当峰度系数 κ > 3 时，需使用广义误差分布（GED）或 t 分布修正 σ 的估计，修正后的尾部溢价概率 P(Error > 2σ) 从正态假设下的 2.3% 上升至 5%-10%，影响高挂价策略的尾部风险计算。

## Evidence

先验知识/题面给定，逻辑校验通过：正态分布下 P(Error > 2σ) ≈ 2.28% 符合数学事实；厚尾分布（如 t 分布或 GED）在峰度 κ > 3 时，尾部概率显著高于正态分布，5%-10% 的量级在金融与统计工程实践中是合理的经验估计，逻辑自洽且无内部矛盾。

## Search Query

leptokurtic distribution tail risk pricing error correction
