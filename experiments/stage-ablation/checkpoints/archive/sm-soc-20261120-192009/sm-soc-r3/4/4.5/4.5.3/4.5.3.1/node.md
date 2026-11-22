# N267: 修正后置信区间的计算表达式：CI_corrected = [X̄ - 1.96 * 1.2 * SE_original, X̄ + 1.96 * 1.2 * S

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N91

## Claim

修正后置信区间的计算表达式：CI_corrected = [X̄ - 1.96 * 1.2 * SE_original, X̄ + 1.96 * 1.2 * SE_original]，其中 X̄ 为样本均值，SE_original 为原始标准误；需对比该区间是否完全包含 [15%, 25%] 区间。

## Corrected Claim

修正后置信区间的计算表达式：CI_corrected = [X̄ - 1.96 * 1.2 * SE_original, X̄ + 1.96 * 1.2 * SE_original]，其中 X̄ 为样本均值，SE_original 为原始标准误；需对比该区间是否完全包含 [15%, 25%] 区间。

## Evidence

先验知识/题面给定，逻辑校验通过
