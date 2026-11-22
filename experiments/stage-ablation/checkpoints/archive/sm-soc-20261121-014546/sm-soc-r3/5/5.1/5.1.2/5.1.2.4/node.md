# N317: 买家异质性偏好中成色敏感性与功能敏感性的交互效应项 I_cf 的量化：I_cf = γ_cf * (σ_condition * σ_function)，其中 γ

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N101, N102, N103

## Claim

买家异质性偏好中成色敏感性与功能敏感性的交互效应项 I_cf 的量化：I_cf = γ_cf * (σ_condition * σ_function)，其中 γ_cf 为交互系数。若 γ_cf = 0.2，则 I_cf = 0.2 * 8% * 10% = 0.16%。该效应项修正了 σ_trade 的简单平方和开根模型，需通过 A/B 测试验证。

## Corrected Claim

买家异质性偏好中成色敏感性与功能敏感性的交互效应项 I_cf 的量化：I_cf = γ_cf * (σ_condition * σ_function)，其中 γ_cf 为交互系数。若 γ_cf = 0.2，则 I_cf = 0.2 * 8% * 10% = 0.16%。该效应项修正了 σ_trade 的简单平方和开根模型，需通过 A/B 测试验证。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 0.2 * 0.08 * 0.10 = 0.0016 (即 0.16%) 准确无误，公式结构符合交互效应的一般定义，且 source 为 knowledge，无需外部来源支持。

## Search Query

interaction effect between product condition and functionality in buyer preferences
