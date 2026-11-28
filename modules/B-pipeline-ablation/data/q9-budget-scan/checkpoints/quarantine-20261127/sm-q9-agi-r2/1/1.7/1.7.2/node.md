# N52: p<0.05 的自动执行需指定具体的统计检验类型映射表：连续变量双组比较用 Welch's t-test (df correction), 分类变量用 Chi-

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

p<0.05 的自动执行需指定具体的统计检验类型映射表：连续变量双组比较用 Welch's t-test (df correction), 分类变量用 Chi-square (contingency table), 多组比较用 ANOVA + Tukey HSD; 若样本量 n < 30 则强制切换为非参数检验 (Mann-Whitney U/Kruskal-Wallis)。

## Corrected Claim

p<0.05 的自动执行需指定具体的统计检验类型映射表：连续变量双组比较用 Welch's t-test (df correction), 分类变量用 Chi-square (contingency table), 多组比较用 ANOVA + Tukey HSD; 若样本量 n < 30 则强制切换为非参数检验 (Mann-Whitney U/Kruskal-Wallis)。

## Evidence

先验知识/题面给定，逻辑校验通过
