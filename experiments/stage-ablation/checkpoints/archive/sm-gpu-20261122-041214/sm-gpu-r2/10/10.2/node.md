# N167: 基于利用率修正后的单位 Token 成本计算公式：Cost_Per_Token = (CapEx + (OpEx_Electricity + OpEx_Cool

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N48

## Claim

基于利用率修正后的单位 Token 成本计算公式：Cost_Per_Token = (CapEx + (OpEx_Electricity + OpEx_Cooling) * T_Year) / (Throughput_Tokens_per_sec * 3600 * 24 * 365 * U), 其中 U 为利用率因子 (0.05-0.15), T_Year 为持有年限 (3), Throughput 需使用特定精度下的实测值。

## Corrected Claim

基于利用率修正后的单位 Token 成本计算公式：Cost_Per_Token = (CapEx + (OpEx_Electricity + OpEx_Cooling) * T_Year) / (Throughput_Tokens_per_sec * 3600 * 24 * 365 * U), 其中 U 为利用率因子 (0.05-0.15), T_Year 为持有年限 (3), Throughput 需使用特定精度下的实测值。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合总成本除以总有效产出的基本经济逻辑，量纲一致（货币/Token），参数范围（利用率0.05-0.15，持有年限3年）符合行业常识。
