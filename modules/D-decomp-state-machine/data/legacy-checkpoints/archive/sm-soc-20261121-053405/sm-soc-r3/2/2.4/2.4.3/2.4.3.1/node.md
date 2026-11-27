# N142: LR 的 95% 置信区间半宽计算公式：基于对数似然比的渐近正态性，$\ln(LR)$ 的标准误为 $SE_{\ln LR} = \sqrt{\frac{1}{

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46

## Claim

LR 的 95% 置信区间半宽计算公式：基于对数似然比的渐近正态性，$\ln(LR)$ 的标准误为 $SE_{\ln LR} = \sqrt{\frac{1}{n_{H_i}} + \frac{1}{n_{H_j}}}$（假设独立样本且方差同质），95% CI 为 $\ln(LR) \pm 1.96 \cdot SE_{\ln LR}$；要使 CI 不包含 0（即 LR>1 显著），需满足 $\ln(LR) > 1.96 \cdot SE_{\ln LR}$。

## Corrected Claim

LR 的 95% 置信区间半宽计算公式：基于对数似然比的渐近正态性，$\ln(LR)$ 的标准误为 $SE_{\ln LR} = \sqrt{\frac{1}{n_{H_i}} + \frac{1}{n_{H_j}}}$（假设独立样本且方差同质），95% CI 为 $\ln(LR) \pm 1.96 \cdot SE_{\ln LR}$；要使 CI 不包含 0（即 LR>1 显著），需满足 $\ln(LR) > 1.96 \cdot SE_{\ln LR}$。

## Evidence

先验知识/题面给定，逻辑校验通过
