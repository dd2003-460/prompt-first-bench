# N326: 阈值 0.7 的统计显著性检验：需计算 Consistency_Index 的 95% 置信区间 [CI_lower, CI_upper]，若 CI_lower

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N112

## Claim

阈值 0.7 的统计显著性检验：需计算 Consistency_Index 的 95% 置信区间 [CI_lower, CI_upper]，若 CI_lower > 0.7 则拒绝独立机制假设；若 CI 包含 0.7，则无法排除偶然耦合，需引入 Bonferroni 校正以控制多重比较错误率。

## Corrected Claim

阈值 0.7 的统计显著性检验：需计算 Consistency_Index 的 95% 置信区间 [CI_lower, CI_upper]，若 CI_lower > 0.7 则拒绝独立机制假设；若 CI 包含 0.7，则无法排除偶然耦合，需引入 Bonferroni 校正以控制多重比较错误率。

## Evidence

先验知识/题面给定，逻辑校验通过：统计推断中，若95%置信区间下限大于阈值，则可在5%显著性水平下拒绝原假设（独立机制）；若区间包含阈值，则无法拒绝原假设，此时引入Bonferroni校正以控制多重比较错误率符合统计学规范。
