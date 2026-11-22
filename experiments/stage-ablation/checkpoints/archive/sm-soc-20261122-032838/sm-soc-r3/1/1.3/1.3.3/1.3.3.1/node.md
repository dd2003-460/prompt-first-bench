# N137: 注意力加权系数 α 的置信区间估计：基于样本量 n 的曝光量差异数据，α 的 95% 置信区间为 [α_hat - 1.96*SE(α_hat), α_hat 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

注意力加权系数 α 的置信区间估计：基于样本量 n 的曝光量差异数据，α 的 95% 置信区间为 [α_hat - 1.96*SE(α_hat), α_hat + 1.96*SE(α_hat)]，其中 SE(α_hat) 需通过 Bootstrap 法或 Delta 法计算，以评估估计的统计显著性。

## Corrected Claim

注意力加权系数 α 的置信区间估计：基于样本量 n 的曝光量差异数据，α 的 95% 置信区间为 [α_hat - 1.96*SE(α_hat), α_hat + 1.96*SE(α_hat)]，其中 SE(α_hat) 需通过 Bootstrap 法或 Delta 法计算，以评估估计的统计显著性。

## Evidence

先验知识/题面给定，逻辑校验通过：基于中心极限定理，正态分布下95%置信区间的标准构造形式为估计值加减1.96倍标准误；对于非线性估计量（如注意力加权系数），使用Bootstrap或Delta法计算标准误是统计学中标准且正确的做法。

## Search Query

confidence interval estimation for exposure difference ratio bootstrap method
