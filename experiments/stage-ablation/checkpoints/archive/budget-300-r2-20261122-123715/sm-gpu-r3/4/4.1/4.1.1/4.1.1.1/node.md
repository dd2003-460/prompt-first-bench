# N288: 性价比指标 Value 的归一化定义：Value = (Effective_Tokens_per_Second * 3600 * 24 * 365 * 3) /

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N84

## Claim

性价比指标 Value 的归一化定义：Value = (Effective_Tokens_per_Second * 3600 * 24 * 365 * 3) / TCO_3year_total。分子为 3 年总生成 Token 数，分母为 3 年总拥有成本 (硬件+电力+维护)。此指标消除了时间维度，直接反映每美元购买的计算能力。

## Corrected Claim

性价比指标 Value 的归一化定义：Value = (Effective_Tokens_per_Second * 3600 * 24 * 365 * 3) / TCO_3year_total。分子为 3 年总生成 Token 数，分母为 3 年总拥有成本 (硬件+电力+维护)。此指标消除了时间维度，直接反映每美元购买的计算能力。

## Evidence

先验知识/题面给定，逻辑校验通过：分子单位 (tokens/s * s) 为总 Token 数，分母为总成本，比值单位 tokens/cost 符合性价比定义，量纲与逻辑自洽。

## Search Query

TCO normalization formula GPU inference cost per token annualized
