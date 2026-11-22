# N295: 偏差系数 B 的分母 P(Defective | Passive_Decrease) 需通过贝叶斯公式展开为 P(Passive | Defective) * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N95

## Claim

偏差系数 B 的分母 P(Defective | Passive_Decrease) 需通过贝叶斯公式展开为 P(Passive | Defective) * P(Defective) / P(Passive)，其中 P(Passive | Defective) 为缺陷商品卖家被动降价（如平台强制）的条件概率。

## Corrected Claim

偏差系数 B 的分母 P(Defective | Passive_Decrease) 需通过贝叶斯公式展开为 P(Passive | Defective) * P(Defective) / P(Passive)，其中 P(Passive | Defective) 为缺陷商品卖家被动降价（如平台强制）的条件概率。

## Evidence

先验知识/题面给定，逻辑校验通过：贝叶斯公式展开正确，量纲与逻辑自洽
