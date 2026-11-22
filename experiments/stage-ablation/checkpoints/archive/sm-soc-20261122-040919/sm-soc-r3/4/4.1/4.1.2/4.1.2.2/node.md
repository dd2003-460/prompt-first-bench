# N303: 贝叶斯修正项计算：P(H2)_adjusted = P(H2)_base * (1 + β_evidence * E_strength)，其中 E_streng

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N82

## Claim

贝叶斯修正项计算：P(H2)_adjusted = P(H2)_base * (1 + β_evidence * E_strength)，其中 E_strength 为证据强度指数（0-1），β_evidence 为证据权重系数。当仅存在间接证据（如卖家行为变化）时，E_strength=0.5, β_evidence=0.2，则修正因子为1.1；当存在直接代码/文档证据时，E_strength=1.0, β_evidence=0.5，修正因子为1.5。

## Corrected Claim

贝叶斯修正项计算：P(H2)_adjusted = P(H2)_base * (1 + β_evidence * E_strength)，其中 E_strength 为证据强度指数（0-1），β_evidence 为证据权重系数。当仅存在间接证据（如卖家行为变化）时，E_strength=0.5, β_evidence=0.2，则修正因子为1.1；当存在直接代码/文档证据时，E_strength=1.0, β_evidence=0.5，修正因子为1.5。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构自洽，数值代入计算正确（0.5*0.2=0.1, 1+0.1=1.1; 1.0*0.5=0.5, 1+0.5=1.5），符合贝叶斯修正项的一般定义逻辑。
