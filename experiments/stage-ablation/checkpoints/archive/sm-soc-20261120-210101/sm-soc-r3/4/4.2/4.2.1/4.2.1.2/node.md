# N276: ε_CVR 的信用分交互修正项：引入卖家信用分 C_score 修正弹性，公式为 ε_CVR_adj = ε_CVR_base * (1 + γ_credit 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N76

## Claim

ε_CVR 的信用分交互修正项：引入卖家信用分 C_score 修正弹性，公式为 ε_CVR_adj = ε_CVR_base * (1 + γ_credit * (C_score - C_avg))，假设 γ_credit = 0.1，即信用分每高于均值1个标准差，弹性增加10%，反映高信用卖家对偏离度容忍度更高。

## Corrected Claim

ε_CVR 的信用分交互修正项：引入卖家信用分 C_score 修正弹性，公式为 ε_CVR_adj = ε_CVR_base * (1 + γ_credit * (C_score - C_avg))，假设 γ_credit = 0.1，即信用分每高于均值1个标准差，弹性增加10%，反映高信用卖家对偏离度容忍度更高。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

seller credit score impact on conversion rate elasticity pricing deviation
