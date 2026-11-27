# N363: 净影响回归模型：建立 OLS 模型 ΔImpression_24h = β_0 + β_1 * δ_premium + β_2 * Z_quality + β_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N122

## Claim

净影响回归模型：建立 OLS 模型 ΔImpression_24h = β_0 + β_1 * δ_premium + β_2 * Z_quality + β_3 * (Seller_History_Score) + ε，需报告 β_1 的估计值及其 95% 置信区间，若 CI 不包含 0 且 β_1 > 0 则支持溢价驱动曝光假设。

## Corrected Claim

净影响回归模型：建立 OLS 模型 ΔImpression_24h = β_0 + β_1 * δ_premium + β_2 * Z_quality + β_3 * (Seller_History_Score) + ε，需报告 β_1 的估计值及其 95% 置信区间，若 CI 不包含 0 且 β_1 > 0 则支持溢价驱动曝光假设。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述描述了一个标准的OLS回归模型设定及假设检验逻辑（H0: β1=0 vs H1: β1>0），变量定义清晰，统计推断逻辑（CI不包含0且方向正确支持假设）符合统计学基本原理，无内部矛盾或量纲错误。

## Search Query

regression model premium price effect on exposure e-commerce platform
