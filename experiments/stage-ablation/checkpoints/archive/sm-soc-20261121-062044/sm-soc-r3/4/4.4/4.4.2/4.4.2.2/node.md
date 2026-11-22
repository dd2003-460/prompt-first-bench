# N220: 多重比较校正后的显著性阈值：若同时检验多个特征系数，需使用 Bonferroni 校正，显著性水平 α_adj = 0.05 / m（m 为检验次数），对应的临

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N78

## Claim

多重比较校正后的显著性阈值：若同时检验多个特征系数，需使用 Bonferroni 校正，显著性水平 α_adj = 0.05 / m（m 为检验次数），对应的临界值 t_crit = Z_{1-α_adj/2}；例如 m=5 时，t_crit ≈ 2.81，高于 1.96，降低假阳性率但增加假阴性风险。

## Corrected Claim

多重比较校正后的显著性阈值：若同时检验多个特征系数，需使用 Bonferroni 校正，显著性水平 α_adj = 0.05 / m（m 为检验次数），对应的临界值 t_crit = Z_{1-α_adj/2}；例如 m=5 时，t_crit ≈ 2.81，高于 1.96，降低假阳性率但增加假阴性风险。

## Evidence

先验知识/题面给定，逻辑校验通过：Bonferroni校正公式α_adj=0.05/m及m=5时临界值≈2.81符合统计学原理

## Search Query

Bonferroni correction multiple testing threshold t critical value
