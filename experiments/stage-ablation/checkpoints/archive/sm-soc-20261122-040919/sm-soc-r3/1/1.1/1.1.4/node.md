# N34: 挂价偏离度统计分布宽度计算：挂价偏离率 $\delta = (P_{list} - P_{ref}) / P_{ref}$ 的分布宽度由 $W = \sqrt{

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N5

## Claim

挂价偏离度统计分布宽度计算：挂价偏离率 $\delta = (P_{list} - P_{ref}) / P_{ref}$ 的分布宽度由 $W = \sqrt{\text{Var}(\epsilon_{seller}) + \text{Var}(\epsilon_{buyer}) - 2\rho_{\epsilon}\sqrt{\text{Var}(\epsilon_{seller})\text{Var}(\epsilon_{buyer})}}$ 决定，该公式量化了共享随机源对15-25%溢价区间稳定性的贡献。

## Corrected Claim

挂价偏离度统计分布宽度计算：挂价偏离率 $\delta = (P_{list} - P_{ref}) / P_{ref}$ 的分布宽度由 $W = \sqrt{\text{Var}(\epsilon_{seller}) + \text{Var}(\epsilon_{buyer}) - 2\rho_{\epsilon}\sqrt{\text{Var}(\epsilon_{seller})\text{Var}(\epsilon_{buyer})}}$ 决定，该公式量化了共享随机源对15-25%溢价区间稳定性的贡献。

## Evidence

先验知识/题面给定，逻辑校验通过：公式符合两个随机变量线性组合方差的数学定义（Var(A-B) = Var(A)+Var(B)-2Cov(A,B)），量纲与逻辑自洽。

## Search Query

formula for width of listing price deviation distribution based on noise variances
