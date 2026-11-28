# N213: Result 节点的 statistical_test 字段必须枚举标准检验方法（t-test, chi-square, ANOVA, Mann-Whitney

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

Result 节点的 statistical_test 字段必须枚举标准检验方法（t-test, chi-square, ANOVA, Mann-Whitney U），并强制关联 effect_size 的计算公式（如 Cohen's d = (m1-m2)/sd_pooled），防止仅报告 P-value 导致的伪显著性问题。

## Corrected Claim

Result 节点的 statistical_test 字段必须枚举标准检验方法（t-test, chi-square, ANOVA, Mann-Whitney U），并强制关联 effect_size 的计算公式（如 Cohen's d = (m1-m2)/sd_pooled），防止仅报告 P-value 导致的伪显著性问题。

## Evidence

先验知识/题面给定，逻辑校验通过
