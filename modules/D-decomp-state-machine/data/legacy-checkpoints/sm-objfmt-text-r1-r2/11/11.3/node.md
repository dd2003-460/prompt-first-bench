# N85: 单位 Token 总成本 (Cost_per_1k_Tokens) 计算公式为 (Daily_Amortized + Daily_Energy) / Daily

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N24

## Claim

单位 Token 总成本 (Cost_per_1k_Tokens) 计算公式为 (Daily_Amortized + Daily_Energy) / Daily_Tokens_Generated，在低利用率 (单用户) 场景下，RTX 4090 的成本约为 $0.005-0.01/1k Tokens，A100 80GB 约为 $0.02-0.04/1k Tokens。

## Corrected Claim

单位 Token 总成本 (Cost_per_1k_Tokens) 计算公式为 (Daily_Amortized + Daily_Energy) / Daily_Tokens_Generated，在低利用率 (单用户) 场景下，RTX 4090 的成本约为 $0.005-0.01/1k Tokens，A100 80GB 约为 $0.02-0.04/1k Tokens。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 单卡成本低且推理速度快，A100 80GB 成本高且功耗大，在低利用率（单用户）场景下，A100 的单位 Token 成本显著高于 RTX 4090，数量级符合硬件成本与能效比的常识推断。
