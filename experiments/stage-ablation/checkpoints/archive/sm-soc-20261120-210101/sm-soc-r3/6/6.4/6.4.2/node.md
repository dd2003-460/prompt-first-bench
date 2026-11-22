# N360: 最小可检测效应量 (MDE) 的具体计算：MDE = 1.96 * SE(ΔE) = 1.96 * sqrt(Var(E_high)/n_high + Var(

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N106

## Claim

最小可检测效应量 (MDE) 的具体计算：MDE = 1.96 * SE(ΔE) = 1.96 * sqrt(Var(E_high)/n_high + Var(E_drop)/n_drop)。若 Var(E_high) = Var(E_drop) = 0.04（标准差=0.2），n_high = n_drop = 100，则 SE(ΔE) = sqrt(0.04/100 + 0.04/100) = 0.028，MDE = 1.96 * 0.028 = 0.055。若实际 ΔE = 0.03 < 0.055，则检验不显著，置信度降级。

## Corrected Claim

最小可检测效应量 (MDE) 的具体计算：MDE = 1.96 * SE(ΔE) = 1.96 * sqrt(Var(E_high)/n_high + Var(E_drop)/n_drop)。若 Var(E_high) = Var(E_drop) = 0.04（标准差=0.2），n_high = n_drop = 100，则 SE(ΔE) = sqrt(0.04/100 + 0.04/100) = 0.028，MDE = 1.96 * 0.028 = 0.055。若实际 ΔE = 0.03 < 0.055，则检验不显著，置信度降级。

## Evidence

先验知识/题面给定，逻辑校验通过：标准差0.2对应方差0.04，样本量100时标准误计算为sqrt(0.0004+0.0004)≈0.0283，MDE≈0.0555，数值量级与统计原理一致。

## Search Query

minimum detectable effect size calculation two-sample t-test
