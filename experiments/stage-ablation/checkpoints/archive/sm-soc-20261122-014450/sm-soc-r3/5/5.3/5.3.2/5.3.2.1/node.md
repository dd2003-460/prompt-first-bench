# N294: 偏差系数 B 的分子 P(Defective | Active_Decrease) 需通过贝叶斯公式展开为 P(Active | Defective) * P(

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N95

## Claim

偏差系数 B 的分子 P(Defective | Active_Decrease) 需通过贝叶斯公式展开为 P(Active | Defective) * P(Defective) / P(Active)，其中 P(Active | Defective) 为缺陷商品卖家主动降价的条件概率。

## Corrected Claim

偏差系数 B 的分子 P(Defective | Active_Decrease) 需通过贝叶斯公式展开为 P(Active | Defective) * P(Defective) / P(Active)，其中 P(Active | Defective) 为缺陷商品卖家主动降价的条件概率。

## Evidence

先验知识/题面给定，逻辑校验通过：贝叶斯公式 P(A|B) = P(B|A)P(A)/P(B) 在此处应用正确，变量定义与公式结构自洽。
