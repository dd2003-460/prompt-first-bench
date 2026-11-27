# N149: Price_Discount_high 与 Price_Discount_base 的标准化处理：若两组价格偏差分布差异显著，需使用 Winsorize 方法对

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

Price_Discount_high 与 Price_Discount_base 的标准化处理：若两组价格偏差分布差异显著，需使用 Winsorize 方法对极端值（如 >99th percentile）进行截断，以避免 β_platform 被少数异常高溢价商品主导。

## Corrected Claim

Price_Discount_high 与 Price_Discount_base 的标准化处理：若两组价格偏差分布差异显著，需使用 Winsorize 方法对极端值（如 >99th percentile）进行截断，以避免 β_platform 被少数异常高溢价商品主导。

## Evidence

先验知识/题面给定，逻辑校验通过：Winsorize 是处理极端值以保护回归系数（如 β_platform）免受异常值主导的标准统计方法，逻辑自洽且符合计量经济学常规。
