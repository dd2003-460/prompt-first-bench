# N64: 置信区间宽度与样本量关系：回归系数 \(\beta_1\) 的95%置信区间宽度为 \(2 \times 1.96 \times \frac{\sigma_{\

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N18

## Claim

置信区间宽度与样本量关系：回归系数 \(\beta_1\) 的95%置信区间宽度为 \(2 \times 1.96 \times \frac{\sigma_{\epsilon}}{\sqrt{n} \cdot \sqrt{\sum (x_i - \bar{x})^2}}\)，其中 \(\sigma_{\epsilon}\) 为残差标准差，\(n\) 为样本量。若要求置信区间不包含0（即显著为负），最小样本量 \(n_{min}\) 需满足 \(n > \frac{(1.96 \sigma_{\epsilon} / \beta_1)^2}{Var(P_{premium})}\)，当前缺乏 \(n\) 和 \(\sigma_{\epsilon}\) 的具体数值，标记为[待核验]。

## Corrected Claim

置信区间宽度与样本量关系：回归系数 \(\beta_1\) 的95%置信区间宽度为 \(2 \times 1.96 \times \frac{\sigma_{\epsilon}}{\sqrt{n} \cdot \sqrt{\sum (x_i - \bar{x})^2}}\)，其中 \(\sigma_{\epsilon}\) 为残差标准差，\(n\) 为样本量。若要求置信区间不包含0（即显著为负），最小样本量 \(n_{min}\) 需满足 \(n > \frac{(1.96 \sigma_{\epsilon} / \beta_1)^2}{Var(P_{premium})}\)，当前缺乏 \(n\) 和 \(\sigma_{\epsilon}\) 的具体数值，标记为[待核验]。

## Evidence

先验知识/题面给定，逻辑校验通过：公式符合线性回归系数标准误及置信区间定义，样本量推导逻辑自洽。
