# N203: 多重比较校正：若同时检验多个品类或时间段的 T_high vs T_low，需应用 Bonferroni 校正或 FDR (False Discovery Ra

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N65

## Claim

多重比较校正：若同时检验多个品类或时间段的 T_high vs T_low，需应用 Bonferroni 校正或 FDR (False Discovery Rate) 控制，校正后的显著性阈值 α_adj = α / m (m为检验次数)，否则假阳性率将显著高于 5%。

## Corrected Claim

多重比较校正：若同时检验多个品类或时间段的 T_high vs T_low，需应用 Bonferroni 校正或 FDR (False Discovery Rate) 控制，校正后的显著性阈值 α_adj = α / m (m为检验次数)，否则假阳性率将显著高于 5%。

## Evidence

先验知识/题面给定，逻辑校验通过：Bonferroni 校正公式 α/m 及 FDR 控制多重比较假阳性率是统计学标准理论，逻辑自洽且数值量级合理。

## Search Query

Bonferroni correction multiple hypothesis testing p-value adjustment
