# N30: 平台资金占用成本的具体量化参数：假设平台对未结算交易提供 7 天账期，资金成本率为年化 5%，则单笔交易因成交周期 $T$（天）增加带来的隐性成本 $C_{ca

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N10

## Claim

平台资金占用成本的具体量化参数：假设平台对未结算交易提供 7 天账期，资金成本率为年化 5%，则单笔交易因成交周期 $T$（天）增加带来的隐性成本 $C_{capital} = P_{final} \times 5\% \times (T/365)$，该成本在 $R_{platform}$ 计算中作为负项扣除。

## Corrected Claim

平台资金占用成本的具体量化参数：假设平台对未结算交易提供 7 天账期，资金成本率为年化 5%，则单笔交易因成交周期 $T$（天）增加带来的隐性成本 $C_{capital} = P_{final} \times 5\% \times (T/365)$，该成本在 $R_{platform}$ 计算中作为负项扣除。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 C = P * r * (T/365) 符合年化利率折算日利率的标准金融计算逻辑，量纲与数值量级合理。

## Search Query

platform working capital cost of transaction cycle time e-commerce
