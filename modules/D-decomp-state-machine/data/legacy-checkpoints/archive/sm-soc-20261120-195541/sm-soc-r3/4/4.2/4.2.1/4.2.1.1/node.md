# N134: 成交周期 T_deal 的生存分析修正：由于存在删失数据（未成交商品），需使用 Kaplan-Meier 估计器或 Cox 比例风险模型替代简单均值，以准确计算

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46

## Claim

成交周期 T_deal 的生存分析修正：由于存在删失数据（未成交商品），需使用 Kaplan-Meier 估计器或 Cox 比例风险模型替代简单均值，以准确计算与价格偏差的相关性，避免右删失导致的偏差。

## Corrected Claim

成交周期 T_deal 的生存分析修正：由于存在删失数据（未成交商品），需使用 Kaplan-Meier 估计器或 Cox 比例风险模型替代简单均值，以准确计算与价格偏差的相关性，避免右删失导致的偏差。

## Evidence

先验知识/题面给定，逻辑校验通过：生存分析（KM/Cox）是处理右删失数据（未成交商品）的标准统计方法，用于避免均值估计偏差，符合统计学原理。
