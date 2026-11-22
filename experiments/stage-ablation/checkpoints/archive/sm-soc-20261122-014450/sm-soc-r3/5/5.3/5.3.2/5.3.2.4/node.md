# N297: 修正后的真实无咨询比例 P(No_Inquiry | All_Sellers) 的下界需通过代入 P(Active) 的最大可能值（如 0.9）和 P(No_I

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N95

## Claim

修正后的真实无咨询比例 P(No_Inquiry | All_Sellers) 的下界需通过代入 P(Active) 的最大可能值（如 0.9）和 P(No_Inquiry | Passive) 的最小合理估计（如 0.4）进行蒙特卡洛模拟或解析计算，以确定置信区间的下限。

## Corrected Claim

修正后的真实无咨询比例 P(No_Inquiry | All_Sellers) 的下界需通过代入 P(Active) 的最大可能值（如 0.9）和 P(No_Inquiry | Passive) 的最小合理估计（如 0.4）进行蒙特卡洛模拟或解析计算，以确定置信区间的下限。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述描述的是基于贝叶斯定理或全概率公式进行敏感性分析/边界估计的标准方法论，代入极值参数（P(Active)最大值, P(No_Inquiry|Passive)最小值）以确定下界在逻辑和数学上是自洽且合理的。
