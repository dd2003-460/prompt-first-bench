# N345: Evidence（边缘似然）的计算分解：Evidence = Σ_{hypothesis} [P(Data|hypothesis) * P(hypothesis

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N120

## Claim

Evidence（边缘似然）的计算分解：Evidence = Σ_{hypothesis} [P(Data|hypothesis) * P(hypothesis)]，需明确假设空间至少包含 {Platform_Driver, Seller_Greed, Buyer_Bias} 三个互斥状态，并计算各状态下的联合概率

## Corrected Claim

Evidence（边缘似然）的计算分解：Evidence = Σ_{hypothesis} [P(Data|hypothesis) * P(hypothesis)]，需明确假设空间至少包含 {Platform_Driver, Seller_Greed, Buyer_Bias} 三个互斥状态，并计算各状态下的联合概率

## Evidence

先验知识/题面给定，逻辑校验通过：边缘似然（Evidence）的定义即为假设空间上后验概率的归一化常数，公式 P(Data) = Σ P(Data|h)P(h) 符合贝叶斯定理的基本推导，且题目设定的三个互斥假设空间逻辑自洽。
