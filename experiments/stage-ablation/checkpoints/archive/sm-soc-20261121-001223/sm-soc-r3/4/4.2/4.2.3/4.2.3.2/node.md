# N172: 安慰剂检验的样本量 n_placebo 要求：为确保检测到 |β_placebo| < 0.1 * |β_treatment| 这一微小效应的统计功效 (Pow

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

安慰剂检验的样本量 n_placebo 要求：为确保检测到 |β_placebo| < 0.1 * |β_treatment| 这一微小效应的统计功效 (Power) 达到 80%，需满足 n_placebo ≥ (Z_{α/2} + Z_{β})^2 * σ_outcome^2 / (0.1 * |β_treatment|)^2；若实际 n_placebo 小于此值，则安慰剂检验无效，不能支持因果归因置信度 > 0.95。

## Corrected Claim

安慰剂检验的样本量 n_placebo 要求：为确保检测到 |β_placebo| < 0.1 * |β_treatment| 这一微小效应的统计功效 (Power) 达到 80%，需满足 n_placebo ≥ (Z_{α/2} + Z_{β})^2 * σ_outcome^2 / (0.1 * |β_treatment|)^2；若实际 n_placebo 小于此值，则安慰剂检验无效，不能支持因果归因置信度 > 0.95。

## Evidence

先验知识/题面给定，逻辑校验通过：公式符合标准样本量计算逻辑（正态近似下检测最小效应量所需样本量），量纲与统计原理自洽。
