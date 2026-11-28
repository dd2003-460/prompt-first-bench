# N238: 当某阶段样本量 n_i < 30 时，错误率估计的置信区间过宽，此时启用贝叶斯收缩估计：p_i_adjusted = (n_i * p_i_observed +

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N83

## Claim

当某阶段样本量 n_i < 30 时，错误率估计的置信区间过宽，此时启用贝叶斯收缩估计：p_i_adjusted = (n_i * p_i_observed + prior_count * p_prior) / (n_i + prior_count)，其中 prior_count=50（伪计数），p_prior 为上一周期的全局平均错误率，以防止小样本波动导致抽样比例剧烈震荡。

## Corrected Claim

当某阶段样本量 n_i < 30 时，错误率估计的置信区间过宽，此时启用贝叶斯收缩估计：p_i_adjusted = (n_i * p_i_observed + prior_count * p_prior) / (n_i + prior_count)，其中 prior_count=50（伪计数），p_prior 为上一周期的全局平均错误率，以防止小样本波动导致抽样比例剧烈震荡。

## Evidence

先验知识/题面给定，逻辑校验通过
