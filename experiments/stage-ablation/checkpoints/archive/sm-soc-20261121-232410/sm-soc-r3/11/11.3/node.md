# N232: 因果推断稳健性的敏感性分析：若引入未观测混淆变量（如卖家信用分），其解释力 R²_confounder = 0.15，则调整后的因果置信度 Confidence

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N89

## Claim

因果推断稳健性的敏感性分析：若引入未观测混淆变量（如卖家信用分），其解释力 R²_confounder = 0.15，则调整后的因果置信度 Confidence_adj = 0.475 * (1 - R²_confounder) = 0.404；这表明即使排除噪声，遗漏变量偏误仍会将置信度进一步降低至 0.40 以下，低于 0.5 的可信阈值。

## Corrected Claim

因果推断稳健性的敏感性分析：若引入未观测混淆变量（如卖家信用分），其解释力 R²_confounder = 0.15，则调整后的因果置信度 Confidence_adj = 0.475 * (1 - R²_confounder) = 0.404；这表明即使排除噪声，遗漏变量偏误仍会将置信度进一步降低至 0.40 以下，低于 0.5 的可信阈值。

## Evidence

先验知识/题面给定，逻辑校验通过：0.475 * (1 - 0.15) = 0.475 * 0.85 = 0.40375 ≈ 0.404，且 0.404 < 0.5，数值计算与逻辑推导均正确。
