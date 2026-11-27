# N147: $\sigma_{\Delta}$ 的估计方法：基于历史 A/B 测试中参数变更的标准差，$\sigma_{\Delta} = \sqrt{\frac{1}{M

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

$\sigma_{\Delta}$ 的估计方法：基于历史 A/B 测试中参数变更的标准差，$\sigma_{\Delta} = \sqrt{\frac{1}{M-1} \sum_{m=1}^{M} (\Delta \theta_m - \mu_{\Delta})^2}$；若 $\sigma_{\Delta} > 0.5 \cdot \mu_{\Delta}$，则单次干预的效果预测置信区间将显著扩大，需增加重复实验次数 $K$ 使得 $\sigma_{\Delta}/\sqrt{K} < 0.1 \cdot \mu_{\Delta}$。

## Corrected Claim

$\sigma_{\Delta}$ 的估计方法：基于历史 A/B 测试中参数变更的标准差，$\sigma_{\Delta} = \sqrt{\frac{1}{M-1} \sum_{m=1}^{M} (\Delta \theta_m - \mu_{\Delta})^2}$；若 $\sigma_{\Delta} > 0.5 \cdot \mu_{\Delta}$，则单次干预的效果预测置信区间将显著扩大，需增加重复实验次数 $K$ 使得 $\sigma_{\Delta}/\sqrt{K} < 0.1 \cdot \mu_{\Delta}$。

## Evidence

先验知识/题面给定，逻辑校验通过：公式符合样本标准差定义，置信区间扩大与增加样本量K以降低标准误的逻辑符合统计学基本原理。
