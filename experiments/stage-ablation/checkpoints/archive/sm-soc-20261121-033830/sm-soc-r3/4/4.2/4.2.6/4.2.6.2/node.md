# N235: 成交概率对价格变化的响应系数 β：定义 P(Sale|P_new) ≈ P(Sale|P_old) * (1 + β * (ΔP/P_old))，其中 β 为负

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N75

## Claim

成交概率对价格变化的响应系数 β：定义 P(Sale|P_new) ≈ P(Sale|P_old) * (1 + β * (ΔP/P_old))，其中 β 为负值（β < 0），其绝对值大小决定了降价带来的销量提升能否覆盖佣金率变化带来的利润损失；β 需基于历史交易数据回归估计，通常与价格弹性系数 η 正相关。

## Corrected Claim

成交概率对价格变化的响应系数 β：定义 P(Sale|P_new) ≈ P(Sale|P_old) * (1 + β * (ΔP/P_old))，其中 β 为负值（β < 0），其绝对值大小决定了降价带来的销量提升能否覆盖佣金率变化带来的利润损失；β 需基于历史交易数据回归估计，通常与价格弹性系数 η 正相关。

## Evidence

先验知识/题面给定，逻辑校验通过
