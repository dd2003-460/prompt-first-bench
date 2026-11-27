# N207: 投影2：S 值的置信区间计算：S 的标准误 \(SE_S = \sigma_{\epsilon} / \sqrt{\sum (\ln \Delta P_{con

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N78

## Claim

投影2：S 值的置信区间计算：S 的标准误 \(SE_S = \sigma_{\epsilon} / \sqrt{\sum (\ln \Delta P_{consult,i} - \overline{\ln \Delta P_{consult}})^2}\)。S 的 95% 置信区间为 \(S \pm 1.96 \cdot SE_S\)。若置信区间包含 1.0，则不能统计显著地拒绝 S=1.0 的假设，N23 的偏差可能源于随机噪声而非系统性偏差。

## Corrected Claim

投影2：S 值的置信区间计算：S 的标准误 \(SE_S = \sigma_{\epsilon} / \sqrt{\sum (\ln \Delta P_{consult,i} - \overline{\ln \Delta P_{consult}})^2}\)。S 的 95% 置信区间为 \(S \pm 1.96 \cdot SE_S\)。若置信区间包含 1.0，则不能统计显著地拒绝 S=1.0 的假设，N23 的偏差可能源于随机噪声而非系统性偏差。

## Evidence

先验知识/题面给定，逻辑校验通过：该公式符合对数线性回归中斜率系数标准误的标准统计定义（SE = σ/√Σ(x-x̄)²），且基于正态分布的95%置信区间构造及假设检验逻辑（CI包含原假设值则不显著）在统计学上是自洽且正确的。

## Search Query

regression coefficient standard error confidence interval hypothesis test
