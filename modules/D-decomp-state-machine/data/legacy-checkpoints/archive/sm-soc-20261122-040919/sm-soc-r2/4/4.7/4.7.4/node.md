# N100: 三方后验概率归一化：P(H_i|D) = [P(D|H_i)P(H_i)] / Σ[P(D|H_j)P(H_j)]。需设定先验 P(H_platform)=0.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N24

## Claim

三方后验概率归一化：P(H_i|D) = [P(D|H_i)P(H_i)] / Σ[P(D|H_j)P(H_j)]。需设定先验 P(H_platform)=0.4, P(H_seller)=0.3, P(H_buyer)=0.3（基于 N19 调整），代入似然度计算后验。若 P(H_platform|D) > 0.6，则平台为驱动方。

## Corrected Claim

三方后验概率归一化：P(H_i|D) = [P(D|H_i)P(H_i)] / Σ[P(D|H_j)P(H_j)]。需设定先验 P(H_platform)=0.4, P(H_seller)=0.3, P(H_buyer)=0.3（基于 N19 调整），代入似然度计算后验。若 P(H_platform|D) > 0.6，则平台为驱动方。

## Evidence

先验知识/题面给定，逻辑校验通过
