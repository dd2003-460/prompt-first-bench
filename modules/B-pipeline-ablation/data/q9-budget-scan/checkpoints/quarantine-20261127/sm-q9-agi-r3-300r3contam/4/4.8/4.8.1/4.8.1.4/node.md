# N223: 数值事实抽取正则表达式模式：针对实验数据中的数值事实，使用正则 `r'(?:value|measure|result|observed).*?(\d+\.?\d

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N74

## Claim

数值事实抽取正则表达式模式：针对实验数据中的数值事实，使用正则 `r'(?:value|measure|result|observed).*?(\d+\.?\d*)\s*(?:units)?'` 匹配，并人工校验前 10% 样本以确保提取准确率 > 95%。

## Corrected Claim

数值事实抽取正则表达式模式：针对实验数据中的数值事实，使用正则 `r'(?:value|measure|result|observed).*?(\d+\.?\d*)\s*(?:units)?'` 匹配，并人工校验前 10% 样本以确保提取准确率 > 95%。

## Evidence

先验知识/题面给定，逻辑校验通过
